import os
import datetime
import time 

def get_day():
    return int(datetime.datetime.now().strftime('%d'))

def make_commit(day):
    os.system('git add .')
    os.system(f'git commit -m {day}')
    os.system(f'git checkout -b {day}')
    os.system(f'git push origin {day}')

main = True

time_to_day = 10
day = 17
while main:
    make_commit(day)
    past_day = get_day()

    time.sleep(time_to_day)
    day += 1
    now_day = get_day()

    if now_day > past_day:
        make_commit(now_day)
