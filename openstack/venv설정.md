pip3 install 명령을 사용하여 requirements.txt 파일에 명시된 패키지들을 설치하는 방법은 매우 간단합니다. requirements.txt 파일은 프로젝트에 필요한 Python 패키지들의 목록과 해당 버전 정보를 저장한 파일입니다.

#### requirements.txt 파일 예시

```
requests==2.25.1
numpy>=1.18.5
pandas==1.2.3
```


#### 가상환경 설치방법

```sh
python3 -m venv venv
source venv/bin/activate  # macOS/Linux

pip3 install --upgrade -r requirements.txt

pip3 install -r requirements.txt
pip3 list

pip3 install --upgrade -r requirements.txt
```
