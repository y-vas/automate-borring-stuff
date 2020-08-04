from selenium import webdriver
from time import sleep, time
from faker import Faker
import random


class Core:
    drivers = ['chrome','firefox']
    cnf = {}

    def __init__(self, driver = None):
        self._driver( driver )

        if not hasattr(self, 'host'):
            self.host = 'https://www.google.com'

        self.driver.get( self.host )
        self.fk = Faker()
        self.sametask = int(time() + 15)

    def tired( self ):
        if self.sametask <= time():
            self.sametask = random.randint(
                int(   time()   ),
                int(time() + (60 * 5) )
            )
            return True

        return False

    def rd(self,ru = ''):
        now = self.driver.current_url
        new = f'{self.host}{ru}'
        if now != new:
            self.driver.get( new )
            sleep( 2 )

    def go(self,id,tp='id'):
        elem = self.driver.find_element_by_xpath(f'//*[@{tp}="{id}"]')
        self.driver.execute_script("return arguments[0].scrollIntoView();", elem)
        return elem

    def trywith(self,*args,action = None,many= False):
        for x in args:
            try:
                if many:
                    els = self.driver.find_elements_by_xpath(x)
                    if len(els) == 0:
                        raise Exception('no elements')
                    return els
                else:
                    el = self.driver.find_element_by_xpath(x)
                if action != None:
                    eval(f'el.{action}')
                return el
            except Exception as e:
                print( e )
            finally:
                pass

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
    def _driver( self, driver = None ):

        for driver in  self.drivers:
            try:
                eval( f"self.{driver}()" )
                return
            except Exception as e:
                continue

        print('No drivers installed')
        exit()

    def chrome( self ):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("mobileEmulation", { "deviceName": "Nexus 5" })
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument("--incognito")

        try:
            from webdriver_manager.chrome import ChromeDriverManager
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            return
        except Exception as e:
            print('webdriver_manager : not avaliable')

        try:
            self.driver = webdriver.Chrome( options = chrome_options )
        except Exception as e:
            print('chrome-default - not avaliable')

        try:
            self.driver = webdriver.Chrome(
                executable_path="/usr/bin/chromedriver",
                options = chrome_options
            )
        except:
            print('chrome-local - not avaliable')

        try:
            from webdrivermanager import ChromeDriverManager
            gdd = ChromeDriverManager()

            self.driver = webdriver.Chrome(
                gdd.download_and_install()[0],
                options = chrome_options
            )
        except Exception as e:
            # print(e)
            print('chrome-driver - not avaliable')

        raise

    def firefox(self):
        from webdrivermanager import GeckoDriverManager
        gdd = GeckoDriverManager()
        path = gdd.download_and_install()
        print( path )

        try:
            self.driver = webdriver.Firefox()
            return
        except:
            print('firefox - not avaliable')

        raise
