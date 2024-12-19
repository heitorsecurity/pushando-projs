# Python Maven Search Application

This project is a Python application that accesses mvnrepository.com to search for libraries based on a list provided in a text file.

## Project Structure

```
python-mvn-search-app
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       └── search.py    # Utility functions for web requests
├── requirements.txt      # Project dependencies
├── libraries.txt         # List of libraries to search for
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-mvn-search-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare the `libraries.txt` file with the names of the libraries you want to search for, one per line.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

The application will read the library names from `libraries.txt`, perform searches on mvnrepository.com, and display the results.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.