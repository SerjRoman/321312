import os
import datetime
import time

def get_day():
    return int(datetime.datetime.now().strftime('%d'))

def make_commit(day):
    os.system('git add .')
    os.system(f'git commit -m {day}')
    os.system(f'git checkout -b {day}')

main = True
index = 16
while main:
    
    make_commit(index)
    # past_day = get_day()
    index += 1
    time.sleep(10)

    # now_day = get_day()

    # if now_day > past_day:
        # make_commit(now_day)
