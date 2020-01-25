import sys
from config import *


run = sys.argv


if 'find_job' in run:
    from sites.linkedin import LinkedIn
    bot = LinkedIn( EMAIL, PASSWORD )
    bot.search_jobs( 20 )

if 'get_followers' in run:
    from sites.instagram import Instagram
    bot = Instagram( USERNAME_INSTA, PASSWORD_INSTA )
    bot.followall()

if 'likeposts' in run:
    from sites.instagram import Instagram
    bot = Instagram( USERNAME_INSTA, PASSWORD_INSTA )
    bot.likeposts()
