import sys
import os 

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mypackag1 import module1,module2

def main():
    rtn=module1.hello()
    print(f'{rtn}')
    rtn=module2.hello()
    print(f'{rtn}')
    
if __name__ == '__main__':
    main()
    
    
#
#
# Exception has occurred: ModuleNotFoundError
# No module named 'mypackag1'
#   File "/home/jhyunlee/code/dev/python_test/p1/main_1.py", line 6, in <module>
#     from mypackag1 import module1,module2
# ModuleNotFoundError: No module named 'mypackag1'

# package를 사용는 main은  해당 package가 시작되는 point에 같은 위치에 있어야 한다. 
# ==> 다음과 같은 path를 유지해야만 Not
#    
# myfolder/
#     main.py
#     mypackag1/
#         __init__.py
#         module1.py
#         module2.py
    