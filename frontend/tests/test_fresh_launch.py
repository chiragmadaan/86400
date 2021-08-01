import pytest
import time
from pages.welcome_page import WelcomePage
from pages.create_account_page import CreateAccountPage


class TestLaunch:

    @pytest.mark.full_reset
    @pytest.mark.smoke
    @pytest.mark.welcome
    def test_welcome_screen(self, app_driver):

        welcome_page = WelcomePage(app_driver)
        assert welcome_page.verify_view()

    @pytest.mark.full_reset
    @pytest.mark.smoke
    @pytest.mark.create
    def test_create_account_screen(self, app_driver):

        welcome_page = WelcomePage(app_driver)
        create_account_page = CreateAccountPage(app_driver)
        welcome_page.tap_create_account_button()
        time.sleep(1)
        assert create_account_page.verify_view()

    @pytest.mark.full_reset
    @pytest.mark.smoke
    def test_navigation(self, app_driver):

        welcome_page = WelcomePage(app_driver)
        create_account_page = CreateAccountPage(app_driver)
        welcome_page.tap_create_account_button()
        time.sleep(1)
        create_account_page.tap_back_button()
        time.sleep(1)
        assert welcome_page.verify_view()
