from automation_framework.locators.textbox_locators import TextBoxPageLocators
from automation_framework.models.text_box import TextBox
from automation_framework.pages.text_box_page import TextBoxPage
from automation_framework.utils.data_generator import DataGen


class TestTextBox:
    def test_output_data_is_equal_to_input_data(self, driver):
        page = TextBoxPage(driver, TextBoxPageLocators.URL)
        page.open()
        text_box = TextBox(
            full_name=DataGen.full_name(),
            email=DataGen.email(),
            current_address=DataGen.address(),
            permanent_address=DataGen.address()
        )
        page.fill_text_box_form(text_box),
        page.submit_text_box_form()
        page.assert_output_data_is_equal_to_input_data(text_box)
