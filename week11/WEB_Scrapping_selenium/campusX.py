
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Define the driver path
driver_path = r"C:\Users\anish\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create the Service object
service = Service(executable_path=driver_path)

# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Ignore certificate and SSL errors
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

# Maximize the browser window
chrome_options.add_argument("start-maximized")

# Initialize the Chrome driver
driver = webdriver.Chrome(
    service=service,
    options=chrome_options
)

# Open the CampusX website
driver.get("https://campusx.com/")
