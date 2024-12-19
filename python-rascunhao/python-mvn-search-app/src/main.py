import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def read_libraries(file_path):
    with open(file_path, 'r') as file:
        libraries = file.read().splitlines()
    return libraries

def search_mvn_repository(driver, library_name):
    driver.get("https://mvnrepository.com/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(library_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for the page to load
    return driver.page_source

def parse_search_results(html, library_name):
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.select('.im-title a'):
        if library_name in item.get_text(strip=True):
            return item['href']
    return None

def check_library_page(driver, url, library_name):
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    breadcrumb = soup.select_one('.breadcrumbs').get_text(strip=True)
    if library_name in breadcrumb:
        return driver.page_source
    return None

def find_version_page(html, version):
    soup = BeautifulSoup(html, 'html.parser')
    version_link = soup.find('a', text=version)
    if version_link:
        return version_link['href']
    return None

def extract_vulnerabilities(html, library, version):
    soup = BeautifulSoup(html, 'html.parser')
    vulnerabilities = []
    for vuln_section in soup.select('.vulnmsg'):
        vuln_text = vuln_section.select_one('.vuln').get_text(strip=True)
        vulnerabilities.append(vuln_text)
    return [{'library': library, 'version': version, 'vulnerabilities': vulnerabilities}]

def main():
    # Get the directory of the current file
    current_dir = os.path.dirname(__file__)

    # Construct the path to the libraries.txt file
    libraries_path = os.path.join(current_dir, '..', 'libraries.txt')

    # Read the libraries
    libraries = read_libraries(libraries_path)

    # Open the output file for writing
    output_file_path = os.path.join(current_dir, '..', 'vulnerabilities.txt')
    with open(output_file_path, 'w') as output_file:
        # Set up the Selenium WebDriver (e.g., Chrome)
        driver = webdriver.Chrome()

        try:
            # Search for each library, ignoring the ".jar" extension
            for library in libraries:
                library_name, version = library.rsplit('-', 1)
                library_name = library_name.replace('.jar', '')
                version = version.replace('.jar', '')

                search_results = search_mvn_repository(driver, library_name)
                if search_results:
                    library_link = parse_search_results(search_results, library_name)
                    if library_link:
                        library_page_url = f"https://mvnrepository.com{library_link}"
                        library_page_html = check_library_page(driver, library_page_url, library_name)
                        if library_page_html:
                            version_link = find_version_page(library_page_html, version)
                            if version_link:
                                version_page_url = f"https://mvnrepository.com{version_link}"
                                driver.get(version_page_url)
                                time.sleep(2)  # Wait for the page to load
                                vulnerabilities = extract_vulnerabilities(driver.page_source, library_name, version)
                                if vulnerabilities:
                                    for vuln in vulnerabilities:
                                        output_file.write(f"{vuln['library']},{vuln['version']},{vuln['vulnerabilities']}\n")
                                else:
                                    output_file.write(f"{library_name},{version},No vulnerabilities found\n")
                            else:
                                output_file.write(f"{library_name},{version},Version not found\n")
                        else:
                            output_file.write(f"{library_name},{version},Library page not found\n")
                    else:
                        output_file.write(f"{library_name},{version},Library not found in search results\n")
                else:
                    output_file.write(f"{library_name},{version},No search results\n")
        finally:
            driver.quit()

if __name__ == "__main__":
    main()