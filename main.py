import sys, os
run = sys.argv

if 'jobs' in run:
    from sites.linkedin import LinkedIn
    bot = LinkedIn( 'EMAIL', 'PASSWORD' )
    bot.search_jobs( 20 )

if 'insta' in run:
    from sites.instagram import Instagram
    NAME = os.popen('echo $instauser').read()
    PASS = os.popen('echo $mypass2').read()
    HISTORY = ''

    bot = Instagram( NAME, PASS , HISTORY )
    bot.follow()

if 'girls' in run:
    from sites.tinder import TinderBot
    bot = TinderBot(  )
    bot.login()

print('commands ..')
print('girls','insta','jobs')
