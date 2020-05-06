# Objective:1) write a function that reads the binary file and returns data
# 2) measure time required

import logging
import time
#create logger
logging.basicConfig(filename= 'exceptionexample.log', level=logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of a file at 'path' and measure time required. """
    start_time = time.time()
    try:
        f = open(path, mode='rb')
        data = f.read()
        return data
    except FileNotFoundError as err: #err is a variable
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        print(dt)
        logger.info("Time required for {file} = {time}".format(file=path, time=dt))

data = read_file_timed('1.mp4')
