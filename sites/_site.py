from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Site:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get( self.host )
