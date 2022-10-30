from typing import Union, Optional

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UIBasic:
    """ Родительский класс с базовыми UI методами """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def element_presence(self, element: tuple[By, str], waiting_time: int = 10,
                         driver: Optional[WebDriver] = None) -> WebElement:
        with allure.step(f'Проверить, что элемент представлен на странице - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.presence_of_element_located(locator=element))

    def all_elements_presence(self, element: tuple[By, str], waiting_time: int = 10,
                              driver: Optional[WebDriver] = None) -> list[WebElement]:
        with allure.step(f'Проверить что все элементы представлены на странице - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.presence_of_all_elements_located(locator=element))

    def element_clickable(self, element: Union[tuple[By, str], WebElement],
                          waiting_time: int = 10, driver: Optional[WebDriver] = None) -> Union[WebElement, bool]:
        with allure.step(f'Проверить что элемент на странице кликабелен - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.element_to_be_clickable(mark=element))

    def element_missing(self, element: Union[tuple[By, str], WebElement],
                        waiting_time: int = 10, driver: Optional[WebDriver] = None) -> Union[WebElement, bool]:
        with allure.step(f'Проверить что элемент пропал со страницы - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.invisibility_of_element(element=element))

    def text_in_element(self, element: tuple[By, str], text: str, waiting_time: int = 10,
                        driver: Optional[WebDriver] = None) -> bool:
        with allure.step(f'Проверить что текст внутри элемента совпадает с ожидаемым - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.text_to_be_present_in_element(locator=element, text_=text))

    def text_in_element_attribute(self, element: tuple[By, str], text: str, attribute: str,
                                  waiting_time: int = 10, driver: Optional[WebDriver] = None) -> bool:
        with allure.step(f'Проверить что текст внутри атрибута элемента совпадает с ожидаемым - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.text_to_be_present_in_element_attribute(locator=element, text_=text,
                                                                                   attribute_=attribute))

    def alert_window_presence(self, waiting_time: int = 10) -> Union[Alert, bool]:
        with allure.step(f'Проверить что сигнальное окно представлено на странице'):
            return WebDriverWait(driver=self.driver, timeout=waiting_time) \
                .until(expected_conditions.alert_is_present())
