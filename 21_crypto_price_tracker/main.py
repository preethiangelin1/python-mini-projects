import schedule
import time
from job import job

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)