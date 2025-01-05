# User Details Scraper and Viewer

This project is a graphical user interface (GUI) application that allows users to fetch and display user details from an intranet portal. The application uses **Selenium WebDriver** to log in, scrape user data, and extract information such as name, class, gender, date of birth, mobile number, and address. The details, along with the user’s profile picture, are displayed on the GUI.

## Features

- **Fetch User Details**: Retrieve user details by entering a valid user ID.
- **Display Profile Picture**: Automatically fetch and display the user's profile picture.
- **Interactive GUI**: User-friendly interface built with **Tkinter**.
- **HTML Parsing**: Extract and display specific details from intranet profile pages.

## Prerequisites

1. Python 3.8+
2. Required Python libraries:
   - `selenium`
   - `Pillow`
   - `tkinter`
3. Google Chrome browser installed
4. ChromeDriver executable matching your Chrome browser version (place it in the project directory).
5. `password.txt` file containing the user credentials in a specific format.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/jbhargav/seleniume-webscraper-tkinter-app.git
   cd user-details-scraper
   ```

2. Install required Python packages:
   ```bash
   pip install selenium pillow
   ```

3. Place the `chromedriver.exe` file in the project directory.
4. Create a `password.txt` file and include the necessary credentials.

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Enter the **User ID** in the input field.
3. Click the **Submit** button.
4. View the retrieved details and profile picture on the GUI.

## File Structure

```
user-details-scraper/
├── app.py             # Main application file
├── chromedriver.exe   # ChromeDriver executable
├── password.txt       # File storing user credentials
├── img/               # Directory for storing fetched profile pictures
└── README.md          # Documentation
```

## Important Notes

- Ensure that `password.txt` contains valid credentials for logging into the intranet portal.
- The application assumes the presence of an internet connection to fetch data.
- Verify that `chromedriver.exe` matches your installed Chrome version. You can download it from [here](https://chromedriver.chromium.org/downloads).

## Troubleshooting

- **Invalid User ID Error**: Ensure the User ID is in the correct format (e.g., starts with a letter, followed by digits).
- **ChromeDriver Error**: If the app fails to run, confirm that the ChromeDriver version matches your Chrome browser version.
- **Password Not Found**: Double-check the format of `password.txt` and ensure user IDs and passwords are correctly stored.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## Author

Developed by Bhargav.

