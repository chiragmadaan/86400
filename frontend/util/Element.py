from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class Element:
    @staticmethod
    def is_present(driver, by, identifier):
        try:
            Element.find(driver, by, identifier)
            return True
        except (NoSuchElementException, WebDriverException) as e:
            return False

    @staticmethod
    def is_displayed(driver, by, identifier):
        try:
            return Element.find(driver, by, identifier).is_displayed()
        except (NoSuchElementException, WebDriverException) as e:
            return False

    @staticmethod
    def is_enabled(driver, by, identifier):
        try:
            return Element.find(driver, by, identifier).is_enabled()
        except (NoSuchElementException, WebDriverException) as e:
            return False

    @staticmethod
    def find(driver, by, identifier):
        if by == "ID":
            return driver.find_element_by_id(identifier)
        elif by == "xpath":
            return driver.find_element_by_xpath(identifier)
        elif by == "accessibility":
            return driver.find_element_by_accessibility_id(identifier)
        elif by == "predicate":
            return driver.find_element_by_ios_predicate(identifier)
        elif by == "classname":
            return driver.find_element_by_class_name(identifier)
        elif by == "class chain":
            return driver.find_element_by_ios_class_chain(identifier)
        else:
            return NoSuchElementException

