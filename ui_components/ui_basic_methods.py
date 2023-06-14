from typing import Optional
from typing import Union

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UIBasic:
    """ UI basic methods """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def element_presence(self, element: tuple[str, str], waiting_time: int = 10,
                         driver: Optional[WebDriver] = None) -> WebElement:
        """ Проверить, что элемент представлен на странице """
        with allure.step(f'Проверить, что элемент представлен на странице - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.presence_of_element_located(locator=element))

    def element_clickable(self, element: Union[tuple[str, str], WebElement],
                          waiting_time: int = 10, driver: Optional[WebDriver] = None) -> Union[WebElement, bool]:
        """ Проверить что элемент на странице кликабелен """
        with allure.step(f'Проверить что элемент на странице кликабелен - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.element_to_be_clickable(mark=element))

    def element_missing(self, element: Union[tuple[str, str], WebElement],
                        waiting_time: int = 10, driver: Optional[WebDriver] = None) -> Union[WebElement, bool]:
        """ Проверить что элемент пропал со страницы """
        with allure.step(f'Проверить что элемент пропал со страницы - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.invisibility_of_element(element=element))

    def alert_window_presence(self, waiting_time: int = 10) -> Union[Alert, bool]:
        """ Проверить что сигнальное окно представлено на странице """
        with allure.step('Проверить что сигнальное окно представлено на странице'):
            return WebDriverWait(driver=self.driver, timeout=waiting_time) \
                .until(expected_conditions.alert_is_present())
