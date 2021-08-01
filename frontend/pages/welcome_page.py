from util.Element import Element


class WelcomePage:
    def __init__(self, driver):
        self.driver = driver

        self.top_toolbar_id = 'com.twitter.android:id/ocf_top_toolbar'
        self.acknowledgement_text_id = 'com.twitter.android:id/footer_text'
        self.acknowledgement_text = dict()
        self.acknowledgement_text['en'] = 'By signing up, you agree to our Terms, Privacy Policy, and Cookie Use.'
        self.login_text_id = 'com.twitter.android:id/detail_text'
        self.login_text = dict()
        self.login_text['en'] = 'Have an account already? Log in'
        self.header_section_id = 'com.twitter.android:id/linear_layout_header'
        self.header_text_id = 'com.twitter.android:id/primary_text'
        self.header_text = dict()
        self.header_text['en'] = 'See what’s happening in the world right now.'
        self.cta_section_id = 'com.twitter.android:id/linear_layout_cta_sso_buttons'
        self.cta_button_id = 'com.twitter.android:id/ocf_button'
        self.google_button_label = 'CONTINUE WITH GOOGLE'
        self.create_account_button_label = 'CREATE ACCOUNT'
        self.button_separator_id = 'com.twitter.android:id/ocf_separator'

    def verify_view(self):
        result = True

        if Element.is_displayed(self.driver, 'ID', self.header_section_id) and \
                self.driver.find_element_by_id(self.header_text_id).text == self.header_text['en']:
            print('Header section is correct')
        else:
            print('Header section is NOT correct')
            result = False
        buttons = self.driver.find_elements_by_id(self.cta_button_id)
        if len(buttons) == 2 and \
                buttons[0].text == self.google_button_label and \
                buttons[1].text == self.create_account_button_label and \
                Element.is_displayed(self.driver, 'ID', self.button_separator_id):
            print('CTA buttons shown fine')
        else:
            print('CTA buttons NOT shown fine')
            result = False
        if Element.is_displayed(self.driver, 'ID', self.acknowledgement_text_id) and \
                self.driver.find_element_by_id(self.acknowledgement_text_id).text == self.acknowledgement_text['en']:
            print('Acknowledgement text shown')
        else:
            print('Acknowledgement text NOT shown')
            result = False
        if Element.is_displayed(self.driver, 'ID', self.login_text_id) and \
                self.driver.find_element_by_id(self.login_text_id).text == self.login_text['en']:
            print('Acknowledgement text shown')
        else:
            print('Acknowledgement text NOT shown')
            result = False

        return result

    def tap_google_button(self):
        buttons = self.driver.find_elements_by_id(self.cta_button_id)
        for button in buttons:
            if button.text == self.google_button_label:
                button.click()

    def tap_create_account_button(self):
        buttons = self.driver.find_elements_by_id(self.cta_button_id)
        for button in buttons:
            if button.text == self.create_account_button_label:
                button.click()

    def tap_login_button(self):
        pass
