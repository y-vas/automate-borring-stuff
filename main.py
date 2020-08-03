import sys
from secret import *
run = sys.argv

if 'jobs' in run:
    from sites.linkedin import LinkedIn
    bot = LinkedIn( 'EMAIL', 'PASSWORD' )
    bot.search_jobs( 20 )

if 'insta' in run:
    from sites.instagram import Instagram
    bot = Instagram( NAME, PASS )
    bot.follow()
    bot.likes()

if 'girls' in run:
    from sites.tinder import TinderBot
    bot = TinderBot(  )
    bot.login()
