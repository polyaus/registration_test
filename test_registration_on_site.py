import time

from selenium import webdriver


class TestRegistration:
    @classmethod
    def setup_class(cls):
        cls.browser = webdriver.Chrome()
        cls.input_data = [
            ('.first_block .first', "Ivan"),
            ('.first_block .second', "Petrov"),
            ('.first_block .third', "mail@mail.ru"),
            ('.second_block .first', "8922035555"),
            ('.second_block .second', "USA Alabama"),
        ]

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        for data in self.input_data:
            input_field = self.browser.find_element_by_css_selector(data[0])
            input_field.send_keys(data[1])

        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!", welcome_text
