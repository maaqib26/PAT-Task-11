# Importing required modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Defining a class named Drag_Drop
class Drag_Drop:

    #Locators Data
    source_locator = 'draggable'
    target_locator = 'droppable'

    # Constructor of the class
    def __init__(self,url):
        self.url = url
        # Initializing the webdriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        sleep(2)

    # Method to perform drag and drop action
    def drag_and_drop(self):
        # Creating an instance of ActionChains class
        action = ActionChains(self.driver)
        # Finding the draggable element
        source = self.driver.find_element(by=By.ID,value=self.source_locator)
        # Finding the droppable element
        target = self.driver.find_element(by=By.ID,value=self.target_locator)

        # Checking if both elements are displayed
        if source.is_displayed() and target.is_displayed():
            # Checking if both elements are enabled
            if source.is_enabled() and target.is_enabled():
                # Performing the drag and drop action
                action.drag_and_drop(source,target).perform()

# Main block
if __name__=="__main__":
    # Setting the URL
    url = "https://jqueryui.com/droppable/"
    # Creating an instance of Drag_Drop class
    drag_drop_object = Drag_Drop(url)
    # Calling the drag_and_drop method
    drag_drop_object.drag_and_drop()
