from selenium import webdriver
from time import sleep
from config import *
# from faker import Faker
# fk = Faker()


class InstaBot:
    def __init__(self, username, pw):
        self.username = un
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")

    def _register():
        print("")

    def _login():
        sleep( 2 )
        self.driver.find_element_by_xpath("//a[contains(text(), 'Entrar')]").click()
        sleep( 2 )
        self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(un)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep( 4 )
        self.driver.find_element_by_xpath("//button[contains(text(), 'Ahora no')]").click()
        sleep( 2 )

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep( 2 )
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep( 2 )
        scroll_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]')
        last_ht, ht = 0, 1

        while last_ht != ht:
            last_ht = ht

            sleep( 1 )
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box
            )

        links = scroll_box.find_elements_by_tag_name('a')
        names = [ name.text for name in links if name.text != '' ]

        foll = scroll_box.find_elements_by_xpath('//button[contains(text(), Seguir)]')

        for fb in foll:
            sleep(2)
            fb.click()

        return names

    def _followall(self):
        self.driver.get("https://www.instagram.com/explore/people/suggested/")
        print(self._get_names())



my_bot = InstaBot(un, pw)
# my_bot._followall()
