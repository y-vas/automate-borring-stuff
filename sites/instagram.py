from time import sleep
from sites._site import Core
from jict import jict
import random

class Instagram( Core ):
    def __init__(self, username, pw , history = {} ):
        self.host = "https://www.instagram.com/"
        self.password = pw
        self.username = username
        self.history = jict( history )

        Core.__init__(self)
        self._login()

        self.trywith(
            "//button[contains(text(), 'Ahora no')]" ,
            "//button[contains(text(), 'Not Now')]",
            action = 'click()'
        )

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
        links = scroll_box.find_elements_by_tag_name( 'a' )

        names = [ name.text for name in links if name.text != '' ]
        return names

    def search( self,like = 'ajuntament' ):
        self.rd( '' )

        self.trywith(
            "//button[contains(text(), 'Not Now')]",
            "//button[contains(text(), 'Ahora no')]" ,
            action = 'click()'
        )

        search = self.trywith(
            '//input[@placeholder="Search"]',
            '//input[@placeholder="Busca"]',
        )

        parent = search.find_element_by_xpath( '..' )

        current = ''
        for x in like:
            current += x
            search.send_keys( x )
            sleep( 1 )

            divs = parent.find_elements_by_xpath('div')
            div = divs[-1].find_element_by_xpath('div/div')
            anchors = div.find_elements_by_tag_name('a')

            for a in anchors:
                try:
                    dive = a.find_element_by_xpath('div/div[2]')
                    name = dive.find_element_by_xpath('div/span').text
                    desc = dive.find_element_by_xpath('span').text

                    print(name)
                    print(desc)
                    print('-' * 30 )

                    if not like in desc.lower():
                        continue

                    if name not in self.history['followed']:
                        self.history['to_follow'] += [name]
                        self.history.save()

                except Exception as e:
                    print(e)
                    continue

        return self.history['to_follow']

    def follow(self):
        self.history.init('to_follow',[])
        self.history.init('followed', [])

        if len(self.history['to_follow']) < 3:
            names = self.search()
        else:
            names = self.history['to_follow']

        # names = self.suggestions()
        # scroll_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]')
        # foll = scroll_box.find_elements_by_xpath('//button[contains(text(), Seguir)]')

        for name in names:

            if name in self.history['followed']:
                continue

            self.likes( f'{name}/' )
            self.followbtn( name )

            self.history['followed'] += [name]
            self.history.save()

            sleep( 2 )

        self.follow()

    def likes( self, name = "nbamemes/" ):
        self.rd( name )
        article = self.driver.find_elements_by_xpath( '//article' )[0].find_element_by_tag_name("div")
        images = article.find_elements_by_tag_name( 'img' )
        random.shuffle( images )

        if len(images) == 0:
            print('no images for ', name )
            return

        if len( images ) > 2:
            images = images[:2]

        tired = random.randint( 1, len(images) )

        for i, image in enumerate(images):
            try:
                parent = image.find_element_by_xpath('..').find_element_by_xpath('..')
                self.driver.execute_script( 'arguments[0].scrollIntoView()' , image )
                parent.click()

                sleep( random.randint( 3, 6 ) )

                hearts = self.trywith(
                    '//*[@aria-label="Like"]',
                    '//*[@aria-label="Me gusta"]',
                    many = True
                )

                if hearts != None and len(hearts) > 0:
                    parent = hearts[0].find_element_by_xpath('..').find_element_by_xpath('..')
                    parent.click()

                sleep( 0.5 )

                close = self.trywith(
                    '//*[@aria-label="Close"]',
                    '//*[@aria-label="Cerrar"]',
                    many=True
                )[0]

                close.click()
                sleep( 0.5 )

            except Exception as e:
                print( e )
                raise
                continue
            finally:
                sleep(1)

            if i == tired:
                break

    def followbtn(self, extra ):
        foll = self.driver.find_element_by_xpath(f'//h2[contains(text(), {extra})]')
        pare = foll.find_element_by_xpath('..')
        segu = pare.find_elements_by_tag_name('button')[0]
        self.driver.execute_script('arguments[0].click()', segu )
        print('followed ' + extra )
