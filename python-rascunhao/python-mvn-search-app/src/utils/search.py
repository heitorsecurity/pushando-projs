def search_mvn_repository(library_name):
    import requests
    from bs4 import BeautifulSoup

    url = f"https://mvnrepository.com/search?q={library_name}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', class_='vbtn')
        return [result.text for result in results]
    else:
        return []