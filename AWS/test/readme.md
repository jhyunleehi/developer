**AWS CloudWatch**와 **AWS CloudTrail**은 모두 AWS에서 제공하는 모니터링 및 로깅 서비스이지만, 사용 목적과 기능이 다릅니다. 주요 차이점을 다음과 같이 비교할 수 있습니다:

### 1. **목적**
   - **CloudWatch**: AWS 리소스의 성능 모니터링 및 로그 관리를 담당합니다. 리소스 사용량, 애플리케이션 성능 및 운영 상태를 실시간으로 추적할 수 있습니다.
   - **CloudTrail**: AWS 계정에서 발생하는 API 호출과 관련된 활동을 기록하고 추적합니다. 누가, 언제, 어떤 작업을 수행했는지에 대한 로그를 남깁니다.

### 2. **기능**
   - **CloudWatch**:
     - EC2, RDS, Lambda 등 다양한 AWS 서비스의 **지표(metric)**를 수집하고 모니터링합니다.
     - **경보(Alarm)** 설정을 통해 리소스의 상태가 특정 임계치를 초과하거나 미달할 때 알림을 제공합니다.
     - **로그(Log) 관리**: 애플리케이션 로그, 시스템 로그 등을 중앙에서 수집하고 검색, 분석이 가능합니다.
   - **CloudTrail**:
     - AWS 리소스와 관련된 **API 활동 기록**을 저장합니다. 예를 들어, 어떤 사용자가 S3 버킷에서 데이터를 삭제했는지 기록합니다.
     - **보안 및 규정 준수**에 중점을 두며, 의심스러운 활동이나 비정상적인 행동을 추적할 수 있습니다.
     - 로그는 감사, 법적 요구 사항, 보안 분석에 주로 사용됩니다.

### 3. **로그**
   - **CloudWatch**: 시스템 및 애플리케이션 로그를 다룹니다. 예를 들어, EC2의 운영 체제 로그나, Lambda의 실행 로그를 수집합니다.
   - **CloudTrail**: 관리 작업 및 API 호출 기록 로그를 다룹니다. AWS 콘솔, CLI, SDK 등을 통한 작업이 모두 기록됩니다.

### 4. **사용 사례**
   - **CloudWatch**:
     - 애플리케이션 성능 모니터링 및 오류 분석
     - 시스템 리소스 사용량 추적
     - 특정 지표가 임계치를 넘을 때 경보 설정
   - **CloudTrail**:
     - AWS 계정에서 수행된 모든 활동을 감사 및 추적
     - 보안 문제 발생 시, 누가 어떤 작업을 수행했는지 확인
     - 규정 준수를 위한 API 활동 기록 저장

### 5. **요약**
   - **CloudWatch**는 **리소스 모니터링 및 성능 관리** 도구이고,
   - **CloudTrail**은 **보안 및 API 활동 추적**을 위한 도구입니다.

----

AWS Amplify는 풀스택 애플리케이션을 쉽게 개발, 배포할 수 있게 해주는 서비스로, 특히 프론트엔드와 백엔드가 모두 포함된 애플리케이션을 자동으로 배포할 때 매우 유용합니다. AWS Amplify는 여러 리소스를 자동으로 구성해주며, 이를 CloudFormation을 통해 관리할 수도 있습니다.

아래는 AWS Amplify를 이용해 자동으로 풀스택 애플리케이션을 배포하는 CloudFormation 템플릿의 예시입니다.

### AWS Amplify 배포 예시 (CloudFormation 템플릿)
```yaml
Resources:
  AmplifyApp:
    Type: AWS::Amplify::App
    Properties:
      Name: "MyAmplifyApp"
      Repository: "https://github.com/your-repository/my-app" # GitHub 저장소 주소
      OauthToken: !Sub "${GitHubToken}"  # GitHub OAuth Token
      BuildSpec: |  # 선택 사항: 커스텀 빌드 사양 (buildspec.yml에서 설정 가능)
        version: 1
        applications:
          - frontend:
              phases:
                build:
                  commands:
                    - npm install
                    - npm run build
              artifacts:
                baseDirectory: public
                files:
                  - '**/*'
      EnvironmentVariables:
        - Name: "ENVIRONMENT"
          Value: "dev"

  AmplifyBranch:
    Type: AWS::Amplify::Branch
    Properties:
      AppId: !Ref AmplifyApp
      BranchName: "main"  # 배포할 브랜치 이름
      EnableAutoBuild: true  # 코드 푸시 시 자동 빌드 및 배포

  AmplifyBackendEnv:
    Type: AWS::Amplify::BackendEnvironment
    Properties:
      AppId: !Ref AmplifyApp
      EnvironmentName: "dev"
```

### 설명
1. **AmplifyApp**: Amplify 애플리케이션을 정의하는 리소스입니다. 이 부분에서 앱의 이름, 연결할 Git 저장소, 그리고 빌드 사양 등을 설정합니다. 저장소는 GitHub, GitLab, Bitbucket 등 다양한 소스를 지원합니다.
2. **AmplifyBranch**: Amplify 앱에 연결된 특정 브랜치를 정의하는 리소스입니다. 주로 `main` 또는 `master` 브랜치를 자동으로 빌드하고 배포하도록 설정할 수 있습니다.
3. **AmplifyBackendEnv**: Amplify 백엔드 환경을 설정하는 리소스입니다. 백엔드 서비스 (예: GraphQL API, Auth, Storage 등)를 배포할 환경을 설정할 수 있습니다.

### GitHub와 연동된 Amplify CI/CD
Amplify의 핵심 기능 중 하나는 GitHub와 같은 Git 기반 소스 컨트롤과 연동해 CI/CD 파이프라인을 자동으로 구축하는 것입니다. CloudFormation 템플릿에서 `Repository` 및 `BranchName`을 설정하여 코드가 해당 브랜치에 푸시될 때마다 자동으로 빌드와 배포가 이루어집니다.

### 전체 흐름
1. 사용자는 GitHub 리포지토리에서 코드를 업데이트하거나 커밋합니다.
2. Amplify가 해당 리포지토리와 브랜치의 변화를 감지하여 CI/CD 파이프라인을 통해 빌드 및 배포를 자동으로 처리합니다.
3. Amplify는 배포가 완료되면 사용자가 설정한 도메인 또는 기본 제공된 도메인을 통해 웹 애플리케이션을 접근할 수 있게 합니다.

### 빌드 사양 (buildspec.yml)
필요시 커스텀 빌드 사양을 템플릿에 정의할 수 있으며, `buildspec.yml` 파일을 통해 설정할 수도 있습니다. 예를 들어, 리액트(React) 앱이라면 아래와 같은 `buildspec.yml` 파일을 사용할 수 있습니다.

```yaml
version: 1
applications:
  - frontend:
      phases:
        install:
          commands:
            - npm install
        build:
          commands:
            - npm run build
      artifacts:
        baseDirectory: build
        files:
          - '**/*'
```

이러한 설정을 통해 Amplify는 풀스택 애플리케이션을 자동으로 관리하고 배포할 수 있으며, 특히 프론트엔드와 백엔드 리소스를 한 번에 통합 관리하는데 강력한 도구입니다.

---

AWS CloudFormation에서 "스택(Stack)"은 인프라 리소스들의 논리적 그룹을 의미합니다. CloudFormation 템플릿을 사용하여 여러 AWS 리소스를 정의하고 배포하는데, 이 템플릿이 실행되면 그 결과로 생성된 리소스들이 스택을 구성하게 됩니다.

예를 들어, 하나의 애플리케이션을 배포하기 위해 EC2 인스턴스, S3 버킷, RDS 데이터베이스 등을 필요로 할 수 있습니다. 이를 CloudFormation 템플릿으로 정의하고 배포하면 해당 리소스들이 하나의 스택으로 묶입니다. 스택을 통해 이 리소스들을 일괄적으로 관리하거나 삭제할 수 있습니다.

### 예시: 웹 애플리케이션 스택
AWS에서 간단한 웹 애플리케이션을 배포한다고 가정해 보겠습니다. CloudFormation 템플릿을 통해 아래와 같은 리소스들을 정의합니다:

1. **EC2 인스턴스** (웹 서버 역할)
2. **S3 버킷** (정적 콘텐츠 호스팅)
3. **RDS 데이터베이스** (데이터 저장소)
4. **Security Group** (네트워크 보안)

이 CloudFormation 템플릿을 실행하면 위의 리소스들이 생성되고, 하나의 스택으로 관리됩니다. 예를 들어, "WebAppStack"이라는 스택을 만들면, 이 스택에는 위의 리소스들이 포함되어 있습니다.

이를 통해 모든 리소스를 일관되게 관리하고, 스택을 삭제할 경우 포함된 리소스들도 함께 삭제됩니다.

### CloudFormation 템플릿 예시 (YAML)
```yaml
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-0abcdef1234567890
  MyS3Bucket:
    Type: AWS::S3::Bucket
  MyRDSDatabase:
    Type: AWS::RDS::DBInstance
    Properties:
      DBInstanceClass: db.t2.micro
      Engine: MySQL
      AllocatedStorage: 20
```

이 템플릿을 사용하여 스택을 배포하면 EC2 인스턴스, S3 버킷, RDS 인스턴스가 포함된 하나의 스택이 생성됩니다.
---

AWS Lambda 요청 템플릿은 주로 API Gateway와 연동할 때 사용되며, API Gateway로 들어온 요청을 Lambda 함수가 처리할 수 있는 형식으로 변환하는 역할을 합니다. 이 요청 템플릿(Request Template)은 **매핑 템플릿(Mapping Template)**이라고도 하며, **Velocity Template Language (VTL)**을 사용하여 API Gateway의 요청을 Lambda 함수로 변환하거나 가공할 수 있습니다.

### Lambda 요청 템플릿을 사용하는 이유
API Gateway는 HTTP 요청을 받아서 Lambda 함수로 전달하지만, Lambda 함수가 요구하는 형식으로 요청을 변환해야 하는 경우가 많습니다. 요청 템플릿을 사용하면 다음과 같은 상황에서 유용합니다.
- HTTP 요청의 파라미터를 가공하거나 필터링하여 Lambda로 전달
- JSON 포맷을 변경하거나 데이터를 재구성
- 특정 헤더 값이나 쿼리 파라미터를 Lambda 함수로 전달

### Lambda 요청 템플릿 구성 방법

#### 1. **API Gateway 콘솔에서 요청 템플릿 설정**
API Gateway 콘솔을 통해 요청 템플릿을 설정할 수 있습니다. 예를 들어, API Gateway에 정의된 특정 리소스의 `Method Request`에서 **Integration Request** 섹션을 설정할 수 있습니다.

#### 2. **매핑 템플릿 기본 구조**
매핑 템플릿은 VTL로 작성되며, API Gateway로 들어온 요청을 적절한 형태로 가공합니다. 예를 들어, HTTP GET 요청의 쿼리 파라미터나 POST 요청의 본문 데이터를 Lambda 함수로 전달할 수 있습니다.

### 매핑 템플릿 예시

#### GET 요청의 쿼리 파라미터를 Lambda로 전달하는 템플릿
```vtl
{
  "param1": "$input.params('param1')",
  "param2": "$input.params('param2')"
}
```

이 템플릿은 API Gateway에서 들어오는 요청의 쿼리 파라미터 `param1`, `param2`를 Lambda 함수로 전달할 JSON 객체를 생성합니다.

#### POST 요청의 JSON 본문 데이터를 전달하는 템플릿
```vtl
{
  "body": $input.body,
  "headers": {
    "Content-Type": "$input.params('Content-Type')",
    "User-Agent": "$input.params('User-Agent')"
  }
}
```

이 템플릿은 POST 요청의 본문 데이터를 Lambda로 전달하면서, `Content-Type`과 `User-Agent` 같은 헤더 값도 함께 전달합니다.

#### 경로 변수(Path Parameter)를 Lambda로 전달하는 템플릿
```vtl
{
  "id": "$input.params('id')"
}
```

이 템플릿은 `/items/{id}`와 같은 API 요청에서 경로 변수 `id`를 추출하여 Lambda로 전달합니다.

### 3. **템플릿에서 사용할 수 있는 변수들**
- **$input.body**: 요청 본문을 그대로 전달 (JSON, XML, Form data 등)
- **$input.params()**: 요청의 모든 파라미터 (경로, 쿼리, 헤더)를 얻음
- **$input.params('paramName')**: 특정 쿼리, 헤더 또는 경로 변수의 값을 가져옴
- **$input.path('$.jsonPath')**: JSON 본문에서 특정 경로의 값을 가져옴

### 전체 템플릿 예시: 복합 데이터 가공
```vtl
{
  "method": "$context.httpMethod",
  "path": "$context.resourcePath",
  "queryStringParameters": {
    "param1": "$input.params('param1')",
    "param2": "$input.params('param2')"
  },
  "headers": {
    "Content-Type": "$input.params('Content-Type')"
  },
  "body": $input.json('$')
}
```
이 템플릿은 요청의 HTTP 메서드, 경로, 쿼리 파라미터, 헤더, 그리고 요청 본문을 가공하여 Lambda 함수로 전달합니다.

### 4. **템플릿의 활용 예**
- **쿼리 파라미터나 헤더의 값 검증 및 가공**: `$input.params()`와 같은 VTL 기능을 통해 유효성 검사를 하거나 필요한 데이터를 가공한 후 Lambda로 전달.
- **서로 다른 형식의 요청을 통일하여 Lambda에서 처리**: 요청이 XML, JSON, 또는 다른 포맷일 경우 이를 하나의 공통된 JSON 형식으로 변환.

### 결론
AWS Lambda 요청 템플릿은 API Gateway로 들어오는 다양한 형식의 요청을 Lambda 함수가 이해할 수 있는 구조로 변환하는데 매우 유용합니다. VTL을 통해 유연하게 데이터를 변환하고 가공할 수 있으며, API Gateway와 Lambda의 통합을 최적화하는 데 중요한 역할을 합니다.
---

AWS CodeBuild에서 **테스트 보고서**를 생성하기 위해서는 `buildspec.yml` 파일에서 테스트 결과를 수집하고 보고서를 출력하도록 설정해야 합니다. AWS CodeBuild는 여러 테스트 도구의 결과를 지원하며, 보고서는 **JUnit**, **NUnit**, **Cucumber** 등의 형식을 사용할 수 있습니다.

### 기본 구성 방법
`buildspec.yml` 파일의 **reports** 섹션에서 테스트 보고서의 경로와 형식을 지정합니다. 예를 들어, `JUnit` 테스트 보고서를 생성하고 CodeBuild 콘솔에서 이를 확인하려면 빌드 과정에서 테스트 결과 파일을 특정 디렉토리에 저장하고, 해당 경로를 보고서로 설정해야 합니다.

### `buildspec.yml` 파일 예시 (JUnit 테스트 보고서)

```yaml
version: 0.2

phases:
  install:
    commands:
      - echo "Installing dependencies..."
      - apt-get update -y
      - apt-get install -y openjdk-11-jdk
      - apt-get install -y maven
  build:
    commands:
      - echo "Building the project and running tests..."
      - mvn clean test  # Maven을 사용하여 테스트 실행
  post_build:
    commands:
      - echo "Build and test completed."

artifacts:
  files:
    - target/*.jar  # 빌드된 jar 파일을 artifacts로 저장

reports:
  JUnitReports:
    files:
      - target/surefire-reports/*.xml  # JUnit 테스트 결과 파일 경로
    base-directory: target  # 테스트 보고서가 있는 디렉토리
    discard-paths: yes  # 경로 정보를 무시하고 파일만 출력
```

### 설명:
1. **phases**:
   - **install**: 빌드 환경을 준비하는 단계입니다. 예를 들어, `Java` 및 `Maven`을 설치하고 있습니다.
   - **build**: 실제 빌드 및 테스트를 수행하는 단계로, `mvn clean test` 명령어로 Maven 프로젝트의 테스트를 실행합니다.
   - **post_build**: 빌드 후 처리 단계로, 여기서는 테스트 결과를 저장할 수 있습니다.

2. **artifacts**:
   - 빌드의 결과물(예: `.jar` 파일)을 지정합니다. `target` 디렉토리 아래의 모든 `.jar` 파일을 출력으로 설정합니다.

3. **reports**:
   - **JUnitReports**: `target/surefire-reports/`에 있는 JUnit 형식의 테스트 결과 XML 파일을 수집합니다.
   - **files**: JUnit 테스트 결과 파일들이 있는 경로를 지정합니다. 이 경우, `Maven`의 `Surefire` 플러그인이 생성하는 테스트 결과 파일을 지정합니다.
   - **base-directory**: 보고서를 저장하는 기준 디렉토리입니다. `target` 폴더 아래에 있는 파일을 참조합니다.
   - **discard-paths**: `yes`로 설정하면 경로 없이 파일만 표시됩니다.

### 또 다른 예시: Python 프로젝트에서 `pytest`를 사용하는 경우
만약 Python 프로젝트에서 `pytest`를 사용하여 테스트 결과를 CodeBuild에 보고하려면 다음과 같은 `buildspec.yml` 파일을 작성할 수 있습니다.

```yaml
version: 0.2

phases:
  install:
    commands:
      - echo "Installing dependencies..."
      - pip install -r requirements.txt
  build:
    commands:
      - echo "Running tests with pytest..."
      - pytest --junitxml=reports/test-report.xml  # pytest 결과를 JUnit XML 형식으로 저장

reports:
  PyTestReports:
    files:
      - reports/test-report.xml  # pytest 결과 파일 경로
    base-directory: reports
    discard-paths: yes
```

### 설명:
- **pytest**는 `--junitxml` 옵션을 사용하여 JUnit XML 형식의 테스트 결과 파일을 생성합니다.
- `reports/test-report.xml` 경로에 생성된 테스트 결과를 CodeBuild의 테스트 보고서로 수집합니다.

### 요약
1. `buildspec.yml` 파일에서 **reports** 섹션을 정의하여 테스트 결과 파일 경로를 지정합니다.
2. 테스트 도구에 따라 적절한 명령어로 테스트를 실행하고, 결과를 JUnit 형식으로 저장합니다.
3. CodeBuild는 `JUnit`, `NUnit`, `Cucumber`와 같은 다양한 테스트 형식을 지원합니다.

이 설정을 통해 AWS CodeBuild 콘솔에서 테스트 결과를 시각화하고 쉽게 확인할 수 있습니다.

---

AWS AppConfig Agent Lambda 확장은 AWS AppConfig의 구성을 Lambda 함수에서 쉽게 사용할 수 있도록 해주는 기능입니다. 이를 통해 Lambda 함수가 실행될 때마다 최신 구성을 자동으로 가져오거나 업데이트된 설정을 사용할 수 있습니다.

AWS AppConfig Agent Lambda 확장을 사용하면 애플리케이션의 설정 변경을 즉시 반영할 수 있습니다. 예를 들어, 데이터베이스 연결 정보, 피처 플래그, 환경 변수 등의 설정을 Lambda 함수 실행 시 동적으로 가져올 수 있습니다.

### AppConfig Agent Lambda 확장 설정 예시

1. **AppConfig 구성 생성**: 먼저 AWS AppConfig에서 애플리케이션 구성(Profile)을 생성해야 합니다. 여기서 피처 플래그 또는 애플리케이션 설정을 정의합니다.

2. **Lambda 확장 활성화**: Lambda 함수에 AppConfig Agent Lambda 확장을 설치하고, Lambda 함수 내에서 확장된 기능을 사용하여 AppConfig 구성(Profile)을 가져옵니다.

### 1. AWS AppConfig 구성 생성
AWS AppConfig에서 구성(Profile)을 생성하는 단계입니다. 예를 들어, `application_config`이라는 구성에 피처 플래그나 환경 변수를 설정합니다.

- **Application**: MyApp
- **Configuration Profile**: application_config
- **Environment**: dev

### 2. Lambda에서 AWS AppConfig Agent 확장 사용하기
AppConfig Agent Lambda 확장을 사용하여 Lambda 함수에서 설정 값을 가져오는 방법을 보여드리겠습니다.

#### 2.1 Lambda 함수에 AppConfig 확장 추가
AppConfig Agent Lambda 확장을 Lambda 함수에 추가하려면 Lambda 함수의 **레이어**(Layer)를 사용해야 합니다. AWS가 제공하는 AppConfig Lambda 확장 레이어 ARN은 아래와 같습니다.

- **Region**에 따라 ARN이 달라질 수 있으므로 AWS Lambda 콘솔에서 "AppConfig Lambda extension"을 검색하여 해당 레이어를 추가합니다.

#### 2.2 Lambda 함수에서 AppConfig 호출
Lambda 함수 코드에서 AppConfig 구성(Profile)을 호출하여 값을 가져오는 예시입니다.

```python
import os
import requests

def lambda_handler(event, context):
    # AppConfig Agent의 설정을 가져올 수 있는 엔드포인트
    appconfig_url = os.getenv('AWS_APPCONFIG_EXTENSION_HTTP_PORT')
    config_profile_id = "your-configuration-profile-id"
    environment_id = "your-environment-id"
    application_id = "your-application-id"
    
    # AppConfig 구성 API 호출
    url = f"http://localhost:{appconfig_url}/applications/{application_id}/environments/{environment_id}/configurations/{config_profile_id}"
    
    try:
        # HTTP GET 요청을 보내서 AppConfig 구성을 가져옴
        response = requests.get(url)
        response.raise_for_status()
        config_data = response.json()

        # 구성을 출력하거나 사용할 수 있음
        print(f"Configuration data: {config_data}")
        return {
            'statusCode': 200,
            'body': config_data
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching configuration: {e}")
        return {
            'statusCode': 500,
            'body': "Error fetching configuration"
        }
```

### 주요 구성 요소:
1. **AppConfig Agent 엔드포인트**: Lambda 환경 변수 `AWS_APPCONFIG_EXTENSION_HTTP_PORT`를 사용하여 로컬 엔드포인트에서 AppConfig 구성에 액세스할 수 있습니다.
2. **AppConfig 설정 정보**: `application_id`, `environment_id`, `configuration_profile_id`는 AppConfig에서 생성한 구성 요소에 해당하는 ID입니다.
3. **HTTP 요청**: Lambda 함수는 `requests` 라이브러리를 사용하여 AppConfig Agent로부터 최신 구성을 가져옵니다. 이 구성은 JSON 형식으로 전달되며, 함수에서 이를 처리하거나 출력할 수 있습니다.

### 3. Lambda 환경 변수 설정
Lambda 함수가 AppConfig 구성 정보를 가져올 수 있도록 환경 변수를 설정해야 합니다. Lambda 함수의 **환경 변수** 설정에서 아래 값을 추가하세요:

- `AWS_APPCONFIG_EXTENSION_HTTP_PORT`: AppConfig Agent와 통신하는 포트 (기본적으로 `2772` 사용)

### 4. AppConfig 설정을 주기적으로 가져오는 방법
Lambda 함수는 매번 실행될 때마다 AppConfig Agent를 호출하여 최신 구성을 가져올 수 있습니다. 이 방법을 사용하면 설정이 변경될 때마다 Lambda 함수에 즉시 반영할 수 있습니다.

### 요약
- AWS AppConfig Agent Lambda 확장을 사용하면 Lambda 함수가 최신 설정 값을 동적으로 가져올 수 있습니다.
- AppConfig Agent는 Lambda 함수가 실행될 때마다 HTTP API를 통해 설정 값을 가져옵니다.
- `buildspec.yml`과 환경 변수를 설정하여 AppConfig와 Lambda 간의 연동을 손쉽게 설정할 수 있습니다.

이 방법을 사용하면 빠르게 애플리케이션 설정을 변경하고, 이러한 설정을 Lambda 함수에서 동적으로 활용할 수 있습니다.
---

`AWS CodeDeploy` 에이전트를 로컬에 설치한 후, **codedeploy-local** 명령을 사용하여 배포 패키지를 검증할 수 있습니다. 이때 `--bundle-location` 옵션을 사용하여 S3 버킷에 저장된 코드 패키지를 지정할 수 있습니다. 이 방법은 실제로 배포 전에 로컬 환경에서 배포 패키지가 올바르게 구성되었는지 테스트하는 데 유용합니다.

다음은 `codedeploy-local` 명령을 사용하여 S3 버킷에서 코드 패키지를 지정하는 예시입니다.

### 예시: `codedeploy-local` 명령 사용

```bash
codedeploy-local --bundle-location s3://my-app-bucket/my-app-bundle.zip --type zip --output-dir /path/to/output/directory
```

### 각 옵션의 설명:

1. **--bundle-location**:
   - S3 버킷에 저장된 배포 패키지 경로를 지정합니다. 예시에서는 `s3://my-app-bucket/my-app-bundle.zip`에 저장된 배포 패키지를 사용합니다.
   
2. **--type**:
   - 배포 패키지의 형식을 지정합니다. `zip` 형식을 사용하고 있으며, `.tar`, `.tgz`, 또는 `.tar.gz` 형식도 가능합니다.

3. **--output-dir**:
   - 배포 결과 파일을 저장할 로컬 디렉터리를 지정합니다. 이 디렉터리에서 배포된 파일과 설치 로그를 확인할 수 있습니다.

### 필수 전제 조건:
- **AWS CLI 설치 및 구성**: AWS CLI가 설치되어 있어야 하고, S3 버킷에 접근할 수 있도록 IAM 역할 또는 자격 증명이 구성되어 있어야 합니다.
- **AWS CodeDeploy Agent 설치**: 로컬에 CodeDeploy 에이전트를 설치해야 합니다.
  
### 예시 실행 과정:
1. **S3 버킷에 배포 패키지 업로드**:
   - `my-app-bucket`이라는 S3 버킷에 `my-app-bundle.zip` 파일을 업로드합니다. 이 파일은 배포에 필요한 코드와 설정 파일을 포함합니다.

2. **로컬에서 배포 테스트**:
   - `codedeploy-local` 명령을 실행하면 지정된 S3 버킷에서 배포 패키지를 다운로드하고, 로컬 머신에 설치 및 검증 과정을 진행합니다.

3. **결과 확인**:
   - `--output-dir`에서 지정한 디렉터리에 배포된 파일을 확인할 수 있으며, 배포 시 발생한 로그도 이 디렉터리에 저장됩니다.

이 예시를 사용하면 실제 AWS CodeDeploy를 통해 배포하기 전에 로컬 환경에서 배포 패키지를 검증할 수 있습니다.

---
