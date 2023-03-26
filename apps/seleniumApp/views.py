from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_info(request):
    # Launch a new instance of the Chrome browser
    browser = webdriver.Chrome()

    # Navigate to the website you want to scrape
    # browser.get('https://radius.uz/category/1-%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B%20%D0%B8%20%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82%D1%8B')
    # Perform any actions you need to get the information you want
    # For example, you could search for an element on the page and extract its text
    # search_box = browser.find_element('search__field')
    # search_box.send_keys('A53')
    # search_box.submit()
    # result = browser.find_element('search-result')
    # info = result.text
    # Close the browser

    browser.get("http://137.184.21.40/dashboard/")
    title = browser.title
    info = browser.find_element(by=By.CLASS_NAME, value="title-1").text

    # image_src = image.get_attribute("src")

    browser.quit()

    # Render a template with the extracted information
    return render(request, 'scraped_info.html', {'title': title, 'info': info})
