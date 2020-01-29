from selenium import webdriver


class Site:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get( self.host )

    def _login():
        pass
