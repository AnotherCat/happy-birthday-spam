# main.py
from random import randint
from time import sleep
from typing import Union

wait_time: Union[int, float] = 2
send_emojis = ["🥳", "😀", "🎺", "🎉", "🎊"]


def send_happy(i: int, time_to_wait: float) -> float:
    emoji_string = ""
    for a in range(0, i):
        emoji_string = emoji_string + f" {send_emojis[randint(0,len(send_emojis)- 1)]} "
    print(f"HAPPY BIRTHDAY {emoji_string}")
    sleep(wait_time)
    if time_to_wait < 0.05:
        return 0.07
    else:
        return time_to_wait * 0.9


if __name__ == "__main__":
    while True:
        for multiplier in send_emojis:
            wait_time = send_happy(randint(0, 12), wait_time)
