import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the list of user names
user_names = [
    "User1 Full Name",
    "User2 Full Name",
    # Add more user names here
]

# Initialize the WebDriver (you need to have the appropriate driver installed)
driver = webdriver.Chrome()  # Change to the appropriate driver for your browser

# Loop through the user names and automate the process
for user_name in user_names:
    try:
        # Navigate to the ServiceNow portal URL
        driver.get("https://bcbsaz.service-now.com/servingblue?id=sc_cat_item_guide&sys_id=4988e209dbec6450229a6165ca961910")

        # Locate the "Requested For" input field, enter the user name, and select it from the dropdown
        requested_for = driver.find_element(By.ID, "sys_display.sc_task.requested_for")
        requested_for.clear()
        requested_for.send_keys(user_name)
        time.sleep(2)  # Wait for dropdown suggestions to appear
        requested_for.send_keys(Keys.RETURN)

        # Check the checkbox (you'll need to identify the checkbox element)
        checkbox = driver.find_element(By.ID, "checkbox_id")  # Replace with the actual element identifier
        checkbox.click()

        # Click the "Next" button (you'll need to identify the button element)
        next_button = driver.find_element(By.ID, "next_button_id")  # Replace with the actual element identifier
        next_button.click()

        # Replace 'prod' with 'train' in the dropdown selection
        select_area = Select(driver.find_element(By.ID, "area_dropdown_id"))  # Replace with the actual element identifier
        select_area.select_by_visible_text("BCBSAZ - Service")

        select_environment = Select(driver.find_element(By.ID, "environment_dropdown_id"))  # Replace with the actual element identifier
        select_environment.select_by_visible_text("train")  # Replaced 'prod' with 'train'

        select_request_type = Select(driver.find_element(By.ID, "request_type_dropdown_id"))  # Replace with the actual element identifier
        select_request_type.select_by_visible_text("new user/role change")

        select_role = Select(driver.find_element(By.ID, "role_dropdown_id"))  # Replace with the actual element identifier
        select_role.select_by_visible_text("BCBSAZ - Service - Train - Servicing Rep")

        # Click "Next" and "Order Now" buttons on the page
        next_button = driver.find_element(By.ID, "next_button_id")  # Replace with the actual element identifier
        next_button.click()

        order_now_button = driver.find_element(By.ID, "order_now_button_id")  # Replace with the actual element identifier
        order_now_button.click()

        # Wait for the request to complete, or handle any further actions as needed

    except Exception as e:
        print(f"Error processing {user_name}: {str(e)}")

# Close the WebDriver when done
driver.quit()
