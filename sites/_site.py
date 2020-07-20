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
    cnf = {}

    def __init__(self, driver = None):
        self._driver( driver )

        if not hasattr(self, 'host'):
            self.host = 'https://www.google.com'

        self.driver.get( self.host )
        self.fk = Faker()

    def rd(self,ru = ''):
        self.driver.get( f'{self.host}/{ru}' )

    def go(self,id,tp='id'):
        elem = self.driver.find_element_by_xpath(f'//*[@{tp}="{id}"]')
        self.driver.execute_script("return arguments[0].scrollIntoView();", elem)
        return elem

    def trywith(self,*args):
        for x in args:
            try:
                return self.driver.find_element_by_xpath(x)
            except Exception as e:
                print( e )

    def get(self,id,tp='id'):
        return self.driver.find_element_by_xpath(f'//*[@{tp}="{id}"]')

    def ex(self,id ,tp='id' ):
        elem = self.get(id,tp)
        try:
            elem.click()
        except:
            self.go(id,tp).click()

    def set(self,id,what=0,tp='id'):
        elem = self.get(id,tp=tp)
        elem.clear()

        if what not in self.cnf.keys():
            elem.send_keys(what)
        else:
            elem.send_keys(self.cnf[what])

    def sel(self,id,what,tp='id'):
        self.driver.execute_script(f"return arguments[0].selectedIndex = {what};", self.get(id,tp))

    def on(self,id,what,tp='id'):
        fake = self.fk
        try: val = eval(f'self.{what}')
        except: val = eval(f'fake.{what}()')
        self.get( id, tp ).send_keys(val)
        setattr(self, what, val)

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
            except Exception as e:
                continue
                print( e )
                
        raise

    def chrome(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("mobileEmulation", { "deviceName": "Nexus 5" })
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome( options = chrome_options )

        try:
            self.driver = webdriver.Chrome(
                executable_path="/usr/bin/chromedriver",
                options = chrome_options
            )
        except:
            print('chrome-local - not avaliable')

        try:
            self.driver = webdriver.Chrome(
                wm.chrome.ChromeDriverManager().install(),
                options = chrome_options
            )
        except:
            print('chrome-driver - not avaliable')

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
