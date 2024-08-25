
## cfg.StrOpt

cfg.StrOpt는 OpenStack의 oslo.config 라이브러리에서 문자열 옵션을 정의할 때 사용됩니다. 이를 사용하면 구성 파일이나 명령줄 인수를 통해 프로그램 설정을 쉽게 관리할 수 있습니다. 다음은 cfg.StrOpt를 사용하는 간단한 예제입니다.

#### 1. install
```sh
$ pip install oslo.config
```

#### 2. config file
```
[DEFAULT]
username = myuser
password = mypassword
```
#### 3. python code 
```py

from oslo_config import cfg

# 옵션 정의
opts = [
    cfg.StrOpt('username', default='admin', help='The username for logging in'),
    cfg.StrOpt('password', help='The password for logging in')
]

# ConfigOpts 인스턴스 생성
conf = cfg.ConfigOpts()
conf.register_opts(opts)

# 구성 파일 읽기
conf(default_config_files=['app.conf'])

# 명령줄 인수 분석
conf(sys.argv[1:])

# 옵션 사용
print(f"Username: {conf.username}")
print(f"Password: {conf.password}")
```


#### 4. 실행 예시 
```sh
$ python app.py --username newuser --password newpassword
```

위의 코드를 실행하면 프로그램은 명령줄 인수와 구성 파일을 읽어 설정 값을 출력합니다.

1. 명령줄 인수를 통해 전달된 값이 우선적으로 사용됩니다.
2. 구성 파일에 지정된 값은 명령줄 인수가 없는 경우 사용됩니다.
3. 기본 값은 구성 파일이나 명령줄 인수가 없는 경우 사용됩니다.
 

---

## logging

### 로그 지정 
#### 1. 기본 로그 지정 
```py
import logging

# 기본 로그 설정
logging.basicConfig(level=logging.DEBUG)

# 로그 출력
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

#### 2.  로그 포맷

```py
import logging

# 포맷 지정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 로그 출력
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```
* %(asctime)s: 로그 생성 시간
* %(name)s: 로거 이름
* %(levelname)s: 로그 레벨 이름
* %(message)s: 로그 메시지
### 3. 로그 핸들러

* logging.getLogger(__name__):
* logging.getLogger() 함수는 로거 인스턴스를 가져오거나 생성합니다.
* __name__은 현재 모듈의 이름을 나타내는 변수입니다.
* 따라서 __name__을 인수로 전달하면, 현재 모듈의 이름을 가진 로거 인스턴스를 가져오거나 생성합니다.
* 이는 모듈 별로 개별적인 로거를 사용하여 로그 메시지를 기록할 수 있게 해줍니다.

```py
import logging

# 로거 생성
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 콘솔 핸들러 생성
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 포맷터 생성 및 핸들러에 추가
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# 로거에 핸들러 추가
logger.addHandler(console_handler)

# 로그 출력
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

#### 4. openstack log
*  oslo_log 패키지 사용한다. 
*  따라서 기본 log 사용해서 디버깅하려면 이것을 좀 수정해서 사용해야 한다.  

```py
from oslo_log import log as logging

from manila import exception
from manila.i18n import _
from manila.share import driver
from manila import utils as manila_utils

# LDAP error codes
LDAP_INVALID_CREDENTIALS = 49

LOG = logging.getLogger(__name__)
```


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