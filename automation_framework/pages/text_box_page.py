from automation_framework.locators.textbox_locators import TextBoxPageLocators
from automation_framework.models.text_box import TextBox
from automation_framework.pages.base_page import BasePage


class TextBoxPage(BasePage):
    def fill_text_box_form(self, data: TextBox) -> None:
        self.driver.find_element(
            *TextBoxPageLocators.INPUT_FULL_NAME).send_keys(data.full_name)
        self.driver.find_element(*TextBoxPageLocators.INPUT_EMAIL).send_keys(
            data.email)
        self.driver.find_element(
            *TextBoxPageLocators.INPUT_CURRENT_ADDRESS).send_keys(
            data.current_address)
        self.driver.find_element(
            *TextBoxPageLocators.INPUT_PERMANENT_ADDRESS).send_keys(
            data.permanent_address)

    def submit_text_box_form(self) -> None:
        submit_button = self.driver.find_element(
            *TextBoxPageLocators.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView()",
                                   submit_button)
        submit_button.click()

    def assert_output_data_is_equal_to_input_data(self,
                                                  input_data: TextBox) -> None:
        output_name = self.driver.find_element(
            *TextBoxPageLocators.OUTPUT_FULL_NAME).text.split(":")[1]
        output_email = self.driver.find_element(
            *TextBoxPageLocators.OUTPUT_EMAIL).text.split(":")[1]
        output_current_address = self.driver.find_element(
            *TextBoxPageLocators.OUTPUT_CURRENT_ADDRESS).text.split(":")[1]
        output_permanent_address = self.driver.find_element(
            *TextBoxPageLocators.OUTPUT_PERMANENT_ADDRESS).text.split(":")[1]

        assert output_name == input_data.full_name, (
            f"Wrong name! Expected {input_data.full_name!r}, "
            f"got {output_name!r}"
        )
        assert output_email == input_data.email, (
            f"Wrong email! Expected {input_data.email!r}, "
            f"got {output_email!r}"
        )
        assert output_current_address == input_data.current_address, (
            f"Wrong current_address! "
            f"Expected {input_data.current_address!r},"
            f"got {output_current_address!r}"
        )
        assert output_permanent_address == input_data.permanent_address, (
            f"Wrong permanent_address! "
            f"Expected {input_data.permanent_address!r},"
            f"got {output_permanent_address!r}"
        )
