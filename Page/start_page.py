import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
from Page.card_page import Assert_value



class Start_page(Base):
    url = 'https://stilsoft.ru/products/kitsoz-synerget'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    cart_product = "//div[@class='product']"

    # Getters
    def get_cart_products(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, self.cart_product)))

    # Actions
    def process_cart_products(self):
        cart_products = self.get_cart_products()
        for index in range(len(cart_products)):
            cart_products = self.get_cart_products() #Получаем список элементов
            cart_products[index].click() #Кликаем на карточку товара
            assert_obj = Assert_value(self.driver) # Создаем экземпляр класса Assert_value
            assert_obj.auto_assert() # Вызываем метод auto_assert()
            self.driver.execute_script("window.history.go(-1)") # Возвращаемся на предыдущую страницу

    # METOD
    def start_assert_product(self):
        with allure.step("start_assert_product"):
            self.driver.get(self.url)
            self.clear_result_file()
            self.process_cart_products()