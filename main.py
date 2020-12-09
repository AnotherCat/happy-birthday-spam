# main.py
from random import randint
from time import sleep

wait_time= 2
send_emojis= ["🥳", "😀", "🎺", "🎉", "🎊"]


def send_happy(i, time_to_wait):
    emoji_string = ""
    for a in range(0, i):
        emoji_string = emoji_string + f" {send_emojis[randint(0,len(send_emojis)- 1)]} "
    print(f"HAPPY BIRTHDAY {emoji_string}")
    sleep(wait_time)
    if time_to_wait < 0.05:
        return 0.07
    else:
        return time_to_wait * 0.9


while True:
    for multiplier in send_emojis:
        wait_time = send_happy(randint(0, 12), wait_time)
