from selenium import webdriver
from selenium.webdriver.firefox.webdriver import Options
from Page.start_page import Start_page
import allure

@allure.description("Test buy product")
def test_stilSoft_product(set_up):
    options = Options()
    options.add_argument("-private")
    driver = webdriver.Firefox(options=options)

    """Start PAGE"""
    sp = Start_page(driver)
    sp.start_assert_product()

    driver.quit()