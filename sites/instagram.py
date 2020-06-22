from time import sleep
from sites._site import Core

class Instagram(Core):
    def __init__(self, username, pw):
        self.host = "https://www.instagram.com/accounts/login/"
        self.password = pw
        self.username = username
        Core.__init__(self)

        self._login()

    def _login(self):
        sleep( 2 )
        self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep( 4 )
        self.driver.find_element_by_xpath("//button[contains(text(), 'Ahora no')]").click()
        sleep( 2 )

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

    def followall(self):
        self.driver.get("https://www.instagram.com/explore/people/suggested/")
        print(self._get_names())

    def likeposts(self):
        sleep( 5 )
        self.driver.get("https://instagram.com")
        scroll_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[2]/div[1]/div')
        foll = scroll_box.find_elements_by_xpath('//article')

        for art in foll:
            print(art)
