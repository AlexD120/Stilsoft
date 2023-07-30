import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base



class Assert_value(Base):
    # Locators
    title = "//div[@class='col-lg-12 title_page']"
    img_box = "//div[@class='images_dop_box']"
    service_life = "//li[contains(text(),'срок службы')]"

    # Getters
    def get_img_box(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.img_box)))

    def get_service_life(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.service_life)))

    def get_title(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.title)))

    # Actions
    """ Проверка на соотвествия """
    def process_assert(self):
        #получение значения срока службы
        try:
            element = self.get_service_life()
            text_service_life = element[0].text # Сохраняем текст элемента
            value_service_life = text_service_life[-7:-5] # Берем диаппазон символов в тексте
            text_assert = int(value_service_life) # Переводим значение в числовой тип данных

            #проверка соотвествия значения срока службы
            if text_assert >= 7: # проверяем что знчение больше или равно 7
                print("Срок службы - " + self.title_text + ": ", text_assert, " лет.")
            else:
                self.save_to_file(self.title_text) # Сохраняем тайтл товара
                print("Срок службы - " + self.title_text + ": ", text_assert, " лет.")
        except Exception as e:
            print("Ошибка:", e)

        #проверка наличия фото
        try:
            self.get_img_box()
            print("У товара есть фото")
        except Exception:
            print("У товара отсутствуют фото")
            self.save_to_file(self.title_text) # Сохраняем тайтл товара


    def auto_assert(self):
        with allure.step("auto_assert"):
            self.value_title()
            self.process_assert()

