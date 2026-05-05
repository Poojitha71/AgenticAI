from logger import logging

def add(x,y):
    logging.debug("addition function is called")
    return x + y

logging.debug("addition function is taking place")
add(10,20)