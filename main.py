import sys
from config import *


run = sys.argv


if 'find_job' in run:
    from sites.linkedin import LinkedIn
    bot = LinkedIn( EMAIL, PASSWORD )
    bot.search_jobs( 20 )
