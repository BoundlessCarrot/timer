#!/usr/bin/env python3
import argparse
import time
from multiprocessing import Process
from playsound import playsound
from tqdm import tqdm

def timer(mins, secs):
    for i in tqdm(range(mins*60 + secs)):
        time.sleep(1)
    playsound('~/timer/beeper_alarm.wav')
    return 0

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(prog = 'timer', description='Create a timer of variable length')
    my_parser.add_argument('-m', help='Minutes to time', type=int, metavar='minutes', default=0)
    my_parser.add_argument('-s', help='Seconds to time', type=int, metavar='seconds', default=0)

    args = my_parser.parse_args()

    try:
        p = Process(target = timer, args = (args.m, args.s))
        p.start()
        p.join()
    except KeyboardInterrupt:
        print('\nTimer cancelled.')
    