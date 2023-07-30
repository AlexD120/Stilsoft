import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """ Получение имени товара"""
    def value_title(self):
        title_element = self.get_title()
        self.title_text = title_element[0].text

    """МЕТОД СКРИНШОТА"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S.")  # создание даты
        name_screenshot = 'screenshot ' + now_date + '.png'  # создание имени скриншота с датой
        self.driver.save_screenshot('.\\finaleProgect\\screen\\' + name_screenshot)  # создание скриншота в определенной папке

    """МЕТОД СОХРАНЕНИЯ ИМЕН ТОВАРОВ"""
    def save_to_file(self, data):
        with open("result.txt", "a") as file:
            file.write(data + "\n")

    """МЕТОД ОЧИСТКИ RESULT.TXT"""
    def clear_result_file(self):
        with open("result.txt", "w") as file:
            file.write("")

