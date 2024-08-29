# Imports
import urllib.parse
import requests
import re
from selenium import webdriver as wb
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Initiate web driver
options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1200")

driver = wb.Chrome(options=options)
pdf_links = []

# Hyperparameters
NUM_PAGES = 10  # The Number of GS pages you want to scrape PDFs from
SEARCH_QUERY = "What is Generative AI?"  # Your Search Query Here


# Generate links from URL// Actual webscraping function
def update_titles_and_links_list():
    all_links = driver.find_elements(By.CLASS_NAME, 'gs_or_ggsm')
    for link in all_links:
        c = link.find_element(By.TAG_NAME, "a")
        pdf_link = c.get_attribute("href")
        if "pdf" in pdf_link:
            c_parent = c.find_element(By.XPATH, "..").find_element(By.XPATH, "..")
            c_grandparent = c_parent.find_element(By.XPATH, "..").find_element(By.XPATH, "..")
            title = c_grandparent.find_element(By.TAG_NAME, "h3")
            pdf_links.append((title.text, pdf_link))


# Generate URL by page number
def get_page_num_url(page_num: int) -> str:
    sq = urllib.parse.quote(re.sub(r'\s+', '+', SEARCH_QUERY.strip()))
    return f"https://scholar.google.com/scholar?start={(page_num - 1) * 10}&q={sq}&hl=en&as_sdt=0,21"


# Filename normalization
def make_valid_filename(input_string: str) -> str:
    illegal_chars_pattern = r'[\\/:"*?<>|]'
    return re.sub(r'\s+', '_', re.sub(illegal_chars_pattern, '_', input_string).strip())


# Download PDF to PDF folder
def download_pdf_file(title: str, url: str):
    # Request URL and get response object
    response = requests.get(url, stream=True)

    # isolate PDF filename from URL
    pdf_file_name = make_valid_filename(title)
    if response.status_code == 200:
        # Save in current working directory
        filepath = f"PDFs\\{pdf_file_name}.pdf"
        with open(filepath, 'wb') as pdf_object:
            pdf_object.write(response.content)
            print(f'{pdf_file_name} was successfully saved!')
    else:
        print(f'Uh oh! Could not download {pdf_file_name},')
        print(f'HTTP response status code: {response.status_code}')
        print(f"URL to PDF: {url}")


if __name__ == "__main__":
    print(f"Your search query is: {SEARCH_QUERY}")
    print(f"Scraping '{get_page_num_url(1)}'... ")
    for i in range(1, NUM_PAGES):
        driver.get(get_page_num_url(i))
        update_titles_and_links_list()

    print("PDF download links acquired! Downloading now...")
    for name, link in pdf_links:
        download_pdf_file(name, link)

    time.sleep(100)
    print("PDFs ready for processing!")
