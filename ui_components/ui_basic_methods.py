from typing import Optional, Callable
from typing import Union

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def allure_listener(func: Callable) -> Callable:
    """ A decorator that adds a screenshot to Allure report if a test fails """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with allure.step(title='Method failed with an exception'):
                allure.attach(args[0].driver.get_screenshot_as_png(), name="Screenshot",
                              attachment_type=allure.attachment_type.PNG)
            raise e

    return wrapper


class UIBasic:
    """ UI basic methods """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def element_presence(self, element: tuple[str, str], waiting_time: int = 10,
                         driver: Optional[WebDriver] = None) -> WebElement:
        """ Check element presence """
        with allure.step(f'Check element presence - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.presence_of_element_located(locator=element))

    def element_clickable(self, element: Union[tuple[str, str], WebElement],
                          waiting_time: int = 10, driver: Optional[WebDriver] = None) -> Union[WebElement, bool]:
        """ Check element clickable """
        with allure.step(f'Check element clickable - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.element_to_be_clickable(mark=element))

    def element_missing(self, element: Union[tuple[str, str], WebElement],
                        waiting_time: int = 10, driver: Optional[WebDriver] = None) -> Union[WebElement, bool]:
        """ Check element missing """
        with allure.step(f'Check element missing - \n{element=}'):
            return WebDriverWait(driver=self.driver if not driver else driver, timeout=waiting_time) \
                .until(expected_conditions.invisibility_of_element(element=element))
