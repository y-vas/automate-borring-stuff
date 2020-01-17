import sys
from config import *


run = sys.argv


if 'find_job' in run:
    from sites.linkedin import LinkedIn as lk


    bot = lk( EMAIL, PASSWORD )
    bot.search_jobs(20)
