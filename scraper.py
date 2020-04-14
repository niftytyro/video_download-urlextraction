# import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import selenium.webdriver.support.ui as ui

# start = time.time()

GET_URL = "http://savevideo.me/"

def get_urls(raw_url):
    try:
        urls = {}
        opts = ChromeOptions()
        opts.add_argument('--headless')
        opts.add_argument('--log-level=3')
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=opts)
        wait = ui.WebDriverWait(driver, 10)
        driver.get(GET_URL)
        field = driver.find_element_by_css_selector('.url_input')
        field.send_keys(raw_url)
        btn = driver.find_element_by_css_selector('.submit')
        btn.click()
        wait.until(lambda driver: driver.find_element_by_css_selector(".download_links"))
        parent_div = driver.find_element_by_css_selector(".download_links")
        containers = parent_div.find_elements_by_tag_name('p')
        for container in containers:
            a = container.find_element_by_tag_name('a')
            span = container.find_element_by_tag_name('span')
            subtitle = container.text[container.text.index(a.text)+len(a.text)+3:container.text.index(span.text)-1]
            urls[subtitle] = a.get_attribute('href')
    except:
        pass
    finally:
        driver.quit()
        return urls

url = input("Enter the url:\n")

print(get_urls(url))
# print("Time taken: \n", time.time()-start)