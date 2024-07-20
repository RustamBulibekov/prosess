import threading


import logging
import time

def run(num1, num2):
    logging.debug(f'Start')
    res = num2 * num1
    logging.debug(f'End')

    return res




logging.basicConfig(level=logging.DEBUG, filename='thread.log', filemode='a',
                    format='%(asctime)s  -  %(levelname)s -  %(threadName)s -  %(message)s')


def run_thread(func, *args):
    threads = []
    for x in range(10):

        t = threading.Thread(target=func, args=args)

        t.start()
        threads.append(t)



run_thread(run, 1,2)