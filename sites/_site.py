from selenium import webdriver
from time import sleep
from faker import Faker
import configparser , webdriver_manager as wm

# config = configparser.ConfigParser()
# config.read('../../.env',encoding='utf-8-sig')
# cnf = config['ENVIROMENT_VARIABLES']
# options = webdriver.ChromeOptions()
# options.add_argument('--load-extension=path/to/the/extension')

class Core:

    drivers = ['chrome','firefox']

    def __init__(self, driver = None):
        self._driver( driver )
        self.host = 'https:/www.google.com'
        self.driver.get( self.host )
        self.fk = Faker()


    def rd(self,ru):
        self.driver.get( f'http://{self.host}/{ru}' )

    def go(self,id,tp='id'):
        elem = self.driver.find_element_by_xpath(f'//*[@{tp}="{id}"]')
        self.driver.execute_script("return arguments[0].scrollIntoView();", elem)
        return elem

    def get(self,id,tp='id'):
        return self.driver.find_element_by_xpath(f'//*[@{tp}="{id}"]')

    def ex(self,id,tp='id'):
        elem = self.get(id,tp)
        try:
            elem.click()
        except:
            self.go(id,tp).click()

    def set(self,id,what=0,tp='id'):
        self.get(id,tp=tp).send_keys(cnf[what])

    def sel(self,id,what,tp='id'):
        self.driver.execute_script(f"return arguments[0].selectedIndex = {what};", self.get(id,tp))

    def on(self,id,what,tp='id'):
        fake = self.fk
        try: val = eval(f'self.{what}')
        except: val = eval(f'fake.{what}()')
        self.get( id, tp ).send_keys(val)
        setattr(self, what,val)

# Driver hanndeling
# ------------------------------------------------------------------------------

    def _driver(self, driver = None):
        check_drivers = self.drivers

        if driver is not None:
            check_drivers = [driver]

        for driver in check_drivers :
            try:
                eval(f"self.{driver}()")
                return
            except:
                continue
        raise

    def chrome(self):
        try:
            self.driver = webdriver.Chrome()
            return
        except: print('chrome - not avaliable')

        try:
            self.driver = webdriver.Chrome(
                executable_path="/usr/bin/chromedriver"
            )
            return
        except: print('chrome-local - not avaliable')

        try:
            self.driver = webdriver.Chrome(
                wm.chrome.ChromeDriverManager().install()
            )
            return
        except: print('chrome-driver - not avaliable')

    def firefox(self):
        try:
            self.driver = webdriver.Firefox()
            return
        except: print('firefox - not avaliable')

        try:
            self.driver = webdriver.Firefox(
                executable_path=wm.firefox.GeckoDriverManager().install()
            )
            return
        except: print('firefox-drivers - not avaliable')

        raise
