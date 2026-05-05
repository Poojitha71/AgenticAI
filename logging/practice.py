import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%y-%m-%d %H:%m:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("ArithmeticAPP") 

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b} ={result}")
    return result

def subtract(a,b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a,b):
    result = a * b
    logger.debug(f"multiplyig {a} * {b} = {result}")
    return result

def division(a,b):
    try:
        result = a / b
        logger.debug(f"devision {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
    
add(10,20)
subtract(20,30)
multiply(10,2)
division(10,0)