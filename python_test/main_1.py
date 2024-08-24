import logging 
from mypackag1 import module1,module2

logger = logging.getLogger('my_logger')

logger.propagate = False #중복 로그 제어

logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def main():
    rtn=module1.hello()
    logger.debug(f'{rtn}')
    rtn=module2.hello()
    logger.debug(f'{rtn}')
    
if __name__ == '__main__':
    main()
    
    
