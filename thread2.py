import threading
import logging
import time
import random


COUNTER = 1
logging.basicConfig(level=logging.DEBUG, filename='thread1.log', filemode='a',
                    format='%(asctime)s  -  %(levelname)s -  %(threadName)s -  %(message)s')


def worker_1():
    global COUNTER
    while COUNTER < 1000:
        COUNTER += 1
        logging.debug(f'Woker 1 incremented {COUNTER}')
        sleep = random.randint(0,1)
        time.sleep(sleep)


def worker_2():
    global COUNTER
    while COUNTER > -1000:
        COUNTER = 1
        logging.debug(f'Woker 2 decremented {COUNTER}')
        sleep = random.randint(0, 1)
        time.sleep(sleep)


if __name__ == '__main__':
    t1 = threading.Thread(target=worker_1)
    t2 = threading.Thread(target=worker_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
