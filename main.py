"""
Program - PAT-Task-11 - Drag and Drop using ActionChains
"""

# Importing required modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


# Defining a class named Drag_Drop
class Drag_Drop:
    # Locators Data
    source_locator = 'draggable'
    target_locator = 'droppable'


    # Constructor of the class
    def __init__(self, url):
        self.url = url
        # Initializing the webdriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)
            self.driver.switch_to.frame(self.driver.find_element(by=By.CLASS_NAME,value="demo-frame"))
            sleep(2)
            return True
        except:
            print("ERROR: Not able to start python automation")
            return False

    # Method to perform drag and drop action
    def drag_and_drop(self):
        try:

            # Creating an instance of ActionChains class
            action = ActionChains(self.driver)
            # Finding the draggable element
            source = self.driver.find_element(by=By.ID, value="draggable")
            # Finding the droppable element
            target = self.driver.find_element(by=By.ID, value="droppable")

            # Checking if both elements are displayed
            if source.is_displayed() and target.is_displayed():
                # Checking if both elements are enabled
                if source.is_enabled() and target.is_enabled():
                    # Performing the drag and drop action
                    action.drag_and_drop(source,target).perform()
                    dropped_text = target.text  # Get text of the dropped element
                    # Verify if the drag and drop is successful
                    expected_text = "Dropped!"
                    if dropped_text == expected_text:
                        print("Drag and drop successful!")
                    else:
                        print("Drag and drop unsuccessful!")

        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
           print("ERROR : ", e)
        finally:
           self.driver.quit()

# Main block
if __name__ == "__main__":
    # Setting the URL
    url = "https://jqueryui.com/droppable/"
    # Creating an instance of Drag_Drop class
    drag_drop_object = Drag_Drop(url)
    drag_drop_object.start_automation()
    # Calling the drag_and_drop method
    drag_drop_object.drag_and_drop()

