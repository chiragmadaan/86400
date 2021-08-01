import pytest
from appium import webdriver
from configparser import ConfigParser
import pathlib
from selenium.common.exceptions import InvalidSessionIdException
import time


def pytest_addoption(parser):
    parser.addoption("--app", action="store", default=None)
    parser.addoption("--platform", action="store", default="android")


@pytest.fixture()
def app_driver(request):
    platform = request.config.getoption("--platform")
    app_path = request.config.getoption("--app")

    parser = ConfigParser()
    parser.optionxform = str
    parser.read(pathlib.Path(__file__).parent.parent / 'config' / 'driver.ini')

    app_desired_caps = {}
    for key in parser.options(f"{platform}_capabilities"):
        app_desired_caps[key] = parser.get(f"{platform}_capabilities", key)

    if app_path:
        app_desired_caps['app'] = app_path

    app_server_url = parser.get("appium_server", 'url') + ":" + parser.get("appium_server", 'port') + parser.get("appium_server", 'extension')

    app_driver = webdriver.Remote(app_server_url, app_desired_caps)
    app_driver.implicitly_wait(2)

    yield app_driver

    try:
        app_driver.quit()
        time.sleep(2)
    except InvalidSessionIdException:
        pass


@pytest.fixture()
def app_driver_no_reset(request):
    platform = request.config.getoption("--platform")
    app_path = request.config.getoption("--app")

    parser = ConfigParser()
    parser.optionxform = str
    parser.read(pathlib.Path(__file__).parent.parent / 'config' / 'driver.ini')

    app_desired_caps = {}
    for key in parser.options(f"{platform}_capabilities"):
        app_desired_caps[key] = parser.get(f"{platform}_capabilities", key)

    if app_path:
        app_desired_caps['app'] = app_path

    app_desired_caps["noReset"] = "true"

    app_server_url = parser.get("appium_server", 'url') + ":" + parser.get("appium_server", 'port') + parser.get("appium_server", 'extension')

    app_driver = webdriver.Remote(app_server_url, app_desired_caps)
    app_driver.implicitly_wait(2)

    yield app_driver

    try:
        app_driver.quit()
        time.sleep(2)
    except InvalidSessionIdException:
        pass


@pytest.fixture()
def test_parameters(request):
    params = dict()
    params["app_path"] = request.config.getoption("--app")
    params["platform"] = request.config.getoption("--platform")
    return params
