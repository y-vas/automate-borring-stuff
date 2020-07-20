import sys
from secret import *
run = sys.argv

if 'find_job' in run:
    from sites.linkedin import LinkedIn
    bot = LinkedIn( 'EMAIL', 'PASSWORD' )
    bot.search_jobs( 20 )

if 'get_followers' in run:
    from sites.instagram import Instagram

    bot = Instagram( NAME, PASS )
    bot.followall()

if 'likeposts' in run:
    from sites.instagram import Instagram
    bot = Instagram( 'USERNAME_INSTA' , 'PASSWORD_INSTA' )
    bot.likeposts()

if 'get_a_girlfriend' in run:
    from sites.tinder import TinderBot
    bot = TinderBot(  )
    bot.login()
