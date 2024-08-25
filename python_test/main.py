import logging 

logger = logging.getLogger('my_logger')

logger.propagate = False #중복 로그 제어

logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def add(a, b):
    logging.debug(f'{a},{b}')
    return a + b

def main():
    def test_add_1():
        c=add(1, 2)
        logging.debug(f'{c}')

    def test_add_2():
        c=add(1, 2)
        logger.debug(f'{c}')
        
    logging.debug("hello!!!!") # 이거는 안나옴
    logger.debug("hello world")
    
    test_add_1()
    test_add_2()
    
if __name__ == '__main__':
    main()