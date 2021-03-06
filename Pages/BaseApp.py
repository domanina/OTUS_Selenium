from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser):
        self.browser = browser
        #self.url = "https://demo.opencart.com/admin/"

    def open(self, url):
        return self.browser.get(url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")
