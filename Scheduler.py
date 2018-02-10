# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from VisitLink import *

# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='1-6', hour='0-23', minute='0-59')
scheduler.add_job(MyJob,'cron',hour = '23',minute = '00')
scheduler.start()