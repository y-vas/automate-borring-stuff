from time import sleep
from sites._site import Core
import random

class Instagram( Core ):
    def __init__(self, username, pw):
        self.host = "https://www.instagram.com/"
        self.password = pw
        self.username = username

        Core.__init__(self)
        self._login()
        # skip info
        self.trywith(
            "//button[contains(text(), 'Ahora no')]" ,
            "//button[contains(text(), 'Not Now')]"
        ).click()
        sleep( 2 )

    def _login(self):
        self.rd('accounts/login/')
        self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep( 3 )

    def suggestions(self):
        self.rd('explore/people/suggested/')

        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs )

        scroll_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]')
        links = scroll_box.find_elements_by_tag_name('a')

        names = [ name.text for name in links if name.text != '' ]
        return names

    # def search(self):
    #     names = self.suggestions()
    #     # names = ['ajuntamentberga'] + names
    #
    #     for x in names:
    #         self.rd( f'{x}/' )
    #         sleep( 0.1 )
    #         scroll_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[4]')
    #         links = scroll_box.find_elements_by_tag_name('a')
    #         if len(links) > 0:
    #             links[-1].find_elements_by_tag_name('div').click()
    #         sleep(5)
    #         break

    def follow(self):
        names = self.suggestions()

        scroll_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]')
        foll = scroll_box.find_elements_by_xpath('//button[contains(text(), Seguir)]')

        for fb , name in zip( foll, names ):
            # fb.click()
            print( name )

            if self.tired():
                break
            sleep( 2 )

        self.likes()


    def likes(self, name = "nbamemes/"):
        self.rd( name )
        article = self.driver.find_elements_by_xpath('//article')[0]
        images = article.find_elements_by_xpath('//img')

        random.shuffle( images )

        for image in images:
            try:
                parent = image.find_element_by_xpath('..').find_element_by_xpath('..')
                self.driver.execute_script('arguments[0].scrollIntoView()', image )
                parent.click()

                heart = self.driver.find_element_by_xpath('//svg[@aria-label="Me gusta"]')
                parent = heart.find_element_by_xpath('..').find_element_by_xpath('..')
                parent.click()

            finally:
                sleep(1)

            if self.tired():
                return
