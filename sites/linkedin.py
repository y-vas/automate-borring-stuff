from selenium import webdriver
from time import sleep
from config import *
# from faker import Faker
# fk = Faker()


class LinkedIn:
    def __init__(self, email, password):
        self.email = email
        self.passw = password

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

        self._login()


    def _login(self):
        sleep( 2 )

        self.driver.find_element_by_xpath('//input[@name="session_key"]').send_keys(self.email)
        self.driver.find_element_by_xpath('//input[@name="session_password"]').send_keys(self.passw)

        sleep( 4 )
        self.driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button').click()
        sleep( 2 )


    def search_jobs( self, many ):
        for x in range( 0, many ):
            print("jobs applied ", x)
            self._get_a_job()


    def _get_a_job(self):

        try:
            self.driver.get("https://www.linkedin.com/jobs")

            jobs = self.driver.find_element_by_xpath('//div[@data-scroll-name="jobs-you-may-be-interested-in"]')
            links = jobs.find_elements_by_xpath('//li[contains(@id,"ember")]')

            links[1].click()

            sleep( 3 )
            self.driver.find_elements_by_xpath('//*[@data-control-name="jobdetails_topcard_inapply"]')[0].click()
            sleep( 2 )
            self.driver.find_elements_by_xpath('//*[@data-control-name="submit_unify"]')[0].click()

        # sel_btn = self.driver.find_element_by_xpath('//button[contains(@id,"ember")]').click()
        # sel_btn = self.driver.find_element_by_xpath('//span[@class="artdeco-button__text"]').text
        # print(txt)

        except Exception as e:
            sleep( 2 )
            self._get_a_job()
