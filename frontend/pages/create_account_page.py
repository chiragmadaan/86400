from util.Element import Element


class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver

        self.back_button_id = 'com.twitter.android:id/back_button'
        self.header_text_id = 'com.twitter.android:id/primary_text'
        self.header_text = dict()
        self.header_text['en'] = 'Create your account'
        self.form_id = 'com.twitter.android:id/form_container'
        self.name_field_id = 'com.twitter.android:id/name_field'
        self.name_field_placeholder_text = 'Name\n50 characters left'
        self.phone_or_email_field_id = 'com.twitter.android:id/phone_or_email_field'
        self.phone_or_email_field_placeholder_text = 'Phone number or email address'
        self.birthday_field_id = 'com.twitter.android:id/birthday_field'
        self.birthday_field_placeholder_text = 'Date of birth'
        self.next_button_id = 'com.twitter.android:id/cta_button'

    def verify_view(self):
        result = True

        if self.driver.find_element_by_id(self.header_text_id).text == self.header_text['en']:
            print('Header section is correct')
        else:
            print('Header section is NOT correct')
            result = False
        if Element.is_displayed(self.driver, 'ID', self.back_button_id):
            print('Back button is shown')
        else:
            print('Back button is NOT shown')
            result = False
        if Element.is_displayed(self.driver, 'ID', self.form_id) and \
                Element.is_displayed(self.driver, 'ID', self.name_field_id) and \
                self.driver.find_element_by_id(self.name_field_id).text.strip() == self.name_field_placeholder_text and \
                Element.is_displayed(self.driver, 'ID', self.phone_or_email_field_id) and \
                self.driver.find_element_by_id(self.phone_or_email_field_id).text == self.phone_or_email_field_placeholder_text and \
                Element.is_displayed(self.driver, 'ID', self.birthday_field_id) and \
                self.driver.find_element_by_id(self.birthday_field_id).text == self.birthday_field_placeholder_text:
            print('Correct form is shown')
        else:
            print('Correct form is NOT shown')
            result = False
        if Element.is_displayed(self.driver, 'ID', self.next_button_id) and not Element.is_enabled(self.driver, 'ID', self.next_button_id):
            print('Disabled next button is shown')
        else:
            print('Disabled next button is NOT shown')
            result = False

        return result

    def tap_next_button(self):
        self.driver.find_element_by_id(self.next_button_id).click()

    def enter_name(self, name=''):
        self.driver.find_element_by_id(self.name_field_id).send_keys(name)

    def enter_phone_number(self, phone_number=''):
        self.driver.find_element_by_id(self.phone_or_email_field_id).send_keys(phone_number)

    def enter_email(self, email=''):
        self.driver.find_element_by_id(self.phone_or_email_field_id).send_keys(email)

    def enter_birthday(self, dob=''):
        self.driver.find_element_by_id(self.birthday_field_id).send_keys(dob)

    def tap_back_button(self):
        self.driver.find_element_by_id(self.back_button_id).click()
