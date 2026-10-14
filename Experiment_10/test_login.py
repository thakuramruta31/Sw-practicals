from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


LOGIN_PAGE = Path(__file__).resolve().with_name("login.html").as_uri()


@pytest.fixture
def driver():
	browser = webdriver.Chrome()
	try:
		browser.get(LOGIN_PAGE)
		yield browser
	finally:
		browser.quit()


def test_login_form_fields_and_button_are_visible(driver):
	username_field = driver.find_element(By.ID, "username")
	password_field = driver.find_element(By.ID, "password")
	login_button = driver.find_element(By.ID, "loginButton")

	assert username_field.is_displayed()
	assert password_field.is_displayed()
	assert login_button.is_displayed()


def test_login_succeeds_with_valid_credentials(driver):
	driver.find_element(By.ID, "username").send_keys("student")
	driver.find_element(By.ID, "password").send_keys("pass123")
	driver.find_element(By.ID, "loginButton").click()

	message = (By.ID, "message")
	WebDriverWait(driver, 5).until(
		EC.text_to_be_present_in_element(message, "Login successful!")
	)
	assert driver.find_element(*message).text == "Login successful!"


def test_login_fails_with_invalid_credentials(driver):
	driver.find_element(By.ID, "username").send_keys("wronguser")
	driver.find_element(By.ID, "password").send_keys("wrongpass")
	driver.find_element(By.ID, "loginButton").click()

	message = (By.ID, "message")
	WebDriverWait(driver, 5).until(
		EC.text_to_be_present_in_element(
			message, "Invalid username or password."
		)
	)
	assert (
		driver.find_element(*message).text
		== "Invalid username or password."
	)
