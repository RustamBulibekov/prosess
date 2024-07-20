import multiprocessing
import logging
import time

logging.basicConfig(level=logging.DEBUG, filename='pross.log', filemode='a',
                    format='%(asctime)s %(levelname)s %(message)s')


def run(num1, num2):

    return num1 * num2


def pross(func, *args):
    prosses = []
    for x in range(10):
        proc = multiprocessing.Process(target=func, args=args)
        proc.start()
        logging.debug(f'Start with pid {proc.pid}')
        prosses.append(proc)
    for p in prosses:
        p.join()
        logging.debug(f'End process {p.pid}')


if __name__ == '__main__':
    pross(run, 2, 3)
