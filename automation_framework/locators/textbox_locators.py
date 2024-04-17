from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    URL = "https://demoqa.com/text-box"
    INPUT_FULL_NAME = (By.ID, "userName")
    INPUT_EMAIL = (By.ID, "userEmail")
    INPUT_CURRENT_ADDRESS = (By.ID, "currentAddress")
    INPUT_PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    OUTPUT_FULL_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
