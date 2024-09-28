### 질문 #1주제 1
한 회사에는 ALB(Application Load Balancer)에 HTTP API 호출을 하는 모바일 애플리케이션이 있습니다. ALB는 요청을 AWS Lambda 함수로 라우팅합니다. 사용자 하위 집합이 테스트 중인 버전을 포함하여 주어진 시간에 여러 다른 버전의 애플리케이션이 사용 중입니다. 애플리케이션 버전은 API에 대한 모든 요청과 함께 전송되는 user-agent 헤더에 정의되어 있습니다.
API에 대한 최근 일련의 변경 이후 회사는 애플리케이션에 문제가 있음을 발견했습니다. 회사는 사용 중인 애플리케이션의 각 버전에 대한 응답 코드로 각 API 작업에 대한 메트릭을 수집해야 합니다. DevOps 엔지니어는 Lambda 함수를 수정하여 API 작업 이름, user-agent 헤더의 버전 정보 및 응답 코드를 추출했습니다. DevOps 엔지니어
는 필요한 메트릭을 수집하기 위해 어떤 추가 작업 집합을 수행해야 합니까?

A. Lambda 함수를 수정하여 API 작업 이름, 응답 코드, 버전 번호를 Amazon CloudWatch Logs 로그 그룹에 로그 줄로 씁니다. 각 API 작업 이름에 대한 메트릭을 증가시키는 CloudWatch Logs 메트릭 필터를 구성합니다. 메트릭에 대한 차원으로 응답 코드와 애플리케이션 버전을 지정합니다. 가장 많이 투표된
B. Lambda 함수를 수정하여 API 작업 이름, 응답 코드 및 버전 번호를 Amazon CloudWatch Logs 로그 그룹에 로그 줄로 작성합니다. CloudWatch Logs Insights 쿼리를 구성하여 로그 줄에서 CloudWatch 메트릭을 채웁니다. 메트릭의 차원으로 응답 코드와 애플리케이션 버전을 지정합니다.
C. ALB 액세스 로그를 구성하여 Amazon CloudWatch Logs 로그 그룹에 씁니다. Lambda 함수를 수정하여 API 작업 이름, 응답 코드 및 버전 번호를 응답 메타데이터로 사용하여 ALB에 응답합니다. 각 API 작업 이름에 대한 메트릭을 증가시키는 CloudWatch Logs 메트릭 필터를 구성합니다. 메트릭의 차원으로 응답 코드와 애플리케이션 버전을 지정합니다.
D. Lambda 함수에서 AWS X-Ray 통합을 구성합니다. Lambda 함수를 수정하여 API 작업 이름, 응답 코드 및 버전 번호로 X-Ray 하위 세그먼트를 만듭니다. X-Ray 인사이트를 구성하여 각 API 작업 이름에 대한 집계된 메트릭을 추출하고 메트릭을 Amazon CloudWatch에 게시합니다. 메트릭의 차원으로 응답 코드와 애플리케이션 버전을 지정합니다.



### 질문 #2주제 1
한 회사가 고객에게 애플리케이션을 제공합니다. 이 애플리케이션에는 AWS Lambda 함수를 호출하는 Amazon API Gateway REST API가 있습니다. 초기화 시 Lambda 함수는 Amazon DynamoDB 테이블에서 대량의 데이터를 로드합니다. 데이터 로드 프로세스로 인해 8~10초의 긴 콜드 스타트 ​​시간이 발생합니다. DynamoDB 테이블에는 DynamoDB Accelerator(DAX)가 구성되어 있습니다.
고객들은 애플리케이션이 요청에 응답하는 데 간헐적으로 오랜 시간이 걸린다고 보고합니다. 이 애플리케이션은 하루 종일 수천 개의 요청을 받습니다. 하루 중간에 애플리케이션은 하루 중 다른 어느 시간보다 10배 더 많은 요청을 경험합니다. 하루가 끝나갈 무렵 애플리케이션의 요청 볼륨은 일반적인 총 요청 볼륨의 10%로 감소합니다.
DevOps 엔지니어는 하루 종일 Lambda 함수의 대기 시간을 줄여야 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Lambda 함수에서 프로비저닝된 동시성을 동시성 값 1로 구성합니다. DynamoDB 테이블에 대한 DAX 클러스터를 삭제합니다.
B. Lambda 함수에서 예약된 동시성을 동시성 값 0으로 구성합니다.
C. Lambda 함수에서 프로비저닝된 동시성을 구성합니다. Lambda 함수에서 AWS 애플리케이션 자동 확장을 프로비저닝된 동시성 값을 최소 1, 최대 100으로 설정하여 구성합니다. 가장 많이 투표된
D. Lambda 함수에서 예약된 동시성을 구성합니다. API Gateway API에서 예약된 동시성 최대값 100으로 AWS Application Auto Scaling을 구성합니다.



### 질문 #3주제 1
한 회사가 AWS CodeDeploy를 도입하여 Apache 웹서버가 있는 Java-Apache Tomcat 애플리케이션에 대한 애플리케이션 배포를 자동화하고 있습니다. 개발팀은 개념 증명으로 시작하여 개발자 환경을 위한 배포 그룹을 만들고 애플리케이션 내에서 기능 테스트를 수행했습니다. 완료 후 팀은 스테이징 및 프로덕션을 위한 추가 배포 그룹을 만듭니다.
현재 로그 수준은 Apache 설정 내에서 구성되지만 팀은 배포가 발생할 때 이 구성을 동적으로 변경하여 각 그룹에 대해 다른 애플리케이션 개정 없이 배포 그룹에 따라 다른 로그 수준 구성을 설정하려고 합니다. 각
배포 그룹에 대해 다른 스크립트 버전을 요구하지 않고도 최소한의 관리 오버헤드로 이러한 요구 사항을 충족할 수 있는 방법은 무엇입니까?

A. 배포 그룹에 따라 Amazon EC2 인스턴스에 태그를 지정합니다. 그런 다음 메타데이터 서비스와 EC2 API를 호출하여 인스턴스가 속한 배포 그룹을 식별하는 스크립트를 애플리케이션 개정판에 배치합니다. 이 정보를 사용하여 로그 수준 설정을 구성합니다. appspec.yml 파일에서 AfterInstall 라이프사이클 후크의 일부로 스크립트를 참조합니다.
B. CodeDeploy 환경 변수 DEPLOYMENT_GROUP_NAME을 사용하여 인스턴스가 속한 배포 그룹을 식별하는 스크립트를 만듭니다. 이 정보를 사용하여 로그 수준 설정을 구성합니다. appspec.yml 파일에서 BeforeInstall 라이프사이클 후크의 일부로 이 스크립트를 참조합니다. 가장 많이 투표된
C. 각 환경에 대한 CodeDeploy 사용자 지정 환경 변수를 만듭니다. 그런 다음 이 환경 변수를 확인하여 인스턴스가 속한 배포 그룹을 식별하는 스크립트를 애플리케이션 개정판에 넣습니다. 이 정보를 사용하여 로그 수준 설정을 구성합니다. appspec.yml 파일에서 ValidateService 라이프사이클 후크의 일부로 이 스크립트를 참조합니다.
D. CodeDeploy 환경 변수 DEPLOYMENT_GROUP_ID를 사용하여 인스턴스가 속한 배포 그룹을 식별하여 로그 수준 설정을 구성하는 스크립트를 만듭니다. appspec.yml 파일에서 Install lifecycle 후크의 일부로 이 스크립트를 참조합니다.



### 질문 #4주제 1
한 회사에서 개발자가 계정의 모든 Amazon Elastic Block Store(Amazon EBS) 볼륨에 태그를 지정하여 원하는 백업 빈도를 표시하도록 요구합니다. 이 요구 사항에는 백업이 필요하지 않은 EBS 볼륨이 포함됩니다. 이 회사는 원하는 백업 빈도에 해당하는 none, dally 또는 weekly 값을 갖는 Backup_Frequency라는 사용자 지정 태그를 사용합니다. 감사 결과 개발자가 가끔 EBS 볼륨에 태그를 지정하지 않는 것으로 나타났습니다.
DevOps 엔지니어는 다른 값이 지정되지 않는 한 회사에서 최소한 주 1회 백업을 수행할 수 있도록 모든 EBS 볼륨에 항상 Backup_Frequency 태그가 있는지 확인해야 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 계정에서 AWS Config를 설정합니다. Backup Frequency 태그가 적용되지 않은 모든 Amazon EC2 리소스에 대해 규정 준수 실패를 반환하는 사용자 지정 규칙을 만듭니다. 사용자 지정 AWS Systems Manager Automation 런북을 사용하여 매주 값으로 Backup_Frequency 태그를 적용하는 수정 작업을 구성합니다.
B. 계정에서 AWS Config를 설정합니다. Backup Frequency 태그가 적용되지 않은 EC2::Volume 리소스에 대한 규정 준수 실패를 반환하는 관리형 규칙을 사용합니다. 사용자 지정 AWS Systems Manager Automation 런북을 사용하여 주간 값으로 Backup_Frequency 태그를 적용하는 수정 작업을 구성합니다. 가장 많이 투표된
C. 계정에서 AWS CloudTrail을 켭니다. EBS CreateVolume 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. 사용자 지정 AWS Systems Manager Automation 런북을 구성하여 주간 값으로 Backup_Frequency 태그를 적용합니다. 런북을 규칙의 대상으로 지정합니다.
D. 계정에서 AWS CloudTrail을 켭니다. EBS CreateVolume 이벤트 또는 EBS ModifyVolume 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. 사용자 지정 AWS Systems Manager Automation 런북을 구성하여 주간 값으로 Backup_Frequency 태그를 적용합니다. 런북을 규칙의 대상으로 지정합니다.



### 질문 #5주제 1
한 회사가 애플리케이션의 데이터 저장소로 Amazon Aurora 클러스터를 사용하고 있습니다. Aurora 클러스터는 단일 DB 인스턴스로 구성되어 있습니다. 애플리케이션은 클러스터의 인스턴스 엔드포인트를 사용하여 데이터베이스에서 읽기 및 쓰기 작업을 수행합니다.
이 회사는 다가올 유지 관리 기간 동안 클러스터에 적용할 업데이트를 예약했습니다. 클러스터는 유지 관리 기간 동안 가능한 한 최소한의 중단으로 사용 가능해야 합니다.
DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 무엇을 해야 합니까?

A. Aurora 클러스터에 리더 인스턴스를 추가합니다. 쓰기 작업에 Aurora 클러스터 엔드포인트를 사용하도록 애플리케이션을 업데이트합니다. 읽기에 대한 Aurora 클러스터의 리더 엔드포인트를 업데이트합니다. 가장 많이 투표된
B. Aurora 클러스터에 리더 인스턴스를 추가합니다. 클러스터에 대한 사용자 정의 ANY 엔드포인트를 만듭니다. 읽기 및 쓰기 작업에 Aurora 클러스터의 사용자 정의 ANY 엔드포인트를 사용하도록 애플리케이션을 업데이트합니다.
C. Aurora 클러스터에서 Multi-AZ 옵션을 켭니다. 쓰기 작업에 Aurora 클러스터 엔드포인트를 사용하도록 애플리케이션을 업데이트합니다. 읽기에 Aurora 클러스터의 리더 엔드포인트를 업데이트합니다.
D. Aurora 클러스터에서 Multi-AZ 옵션을 켭니다. 클러스터에 대한 사용자 지정 ANY 엔드포인트를 만듭니다. 읽기 및 쓰기 작업에 Aurora 클러스터의 사용자 지정 ANY 엔드포인트를 사용하도록 애플리케이션을 업데이트합니다.



### 질문 #6주제 1
회사는 계정 간에 공유하는 모든 AMI를 암호화해야 합니다. DevOps 엔지니어는 암호화되지 않은 사용자 지정 AMI가 빌드된 소스 계정에 액세스할 수 있습니다. DevOps 엔지니어는 또한 Amazon EC2 Auto Scaling 그룹이 AMI에서 EC2 인스턴스를 시작할 대상 계정에 액세스할 수 있습니다. DevOps 엔지니어는 대상 계정과 AMI를 공유해야 합니다.
회사는 소스 계정에 AWS Key Management Service(AWS KMS) 키를 생성했습니다.
DevOps 엔지니어는 요구 사항을 충족하기 위해 어떤 추가 단계를 수행해야 합니까? (세 가지를 선택하세요.)

A. 소스 계정에서 암호화되지 않은 AMI를 암호화된 AMI로 복사합니다. 복사 작업에서 KMS 키를 지정합니다. 가장 많이 투표된
B. 소스 계정에서 암호화되지 않은 AMI를 암호화된 AMI로 복사합니다. 복사 작업에서 기본 Amazon Elastic Block Store(Amazon EBS) 암호화 키를 지정합니다.
C. 소스 계정에서 대상 계정의 자동 크기 조정 그룹 서비스 연결 역할에 권한을 위임하는 KMS 권한 부여를 만듭니다.
D. 소스 계정에서 키 정책을 수정하여 대상 계정에 권한 부여를 생성할 수 있는 권한을 부여합니다. 대상 계정에서 Auto Scaling 그룹 서비스 연결 역할에 권한을 위임하는 KMS 권한을 생성합니다. 가장 많이 투표된
E. 소스 계정에서 암호화되지 않은 AMI를 대상 계정과 공유합니다.
F. 소스 계정에서 암호화된 AMI를 대상 계정과 공유합니다. 가장 많이 투표된



### 질문 #7주제 1
한 회사에서 AWS CodePipeline 파이프라인을 사용하여 애플리케이션 릴리스를 자동화합니다. 일반적인 파이프라인은 빌드, 테스트, 배포의 세 단계로 구성됩니다. 이 회사는 각 단계에 대한 스크립트를 실행하기 위해 별도의 AWS CodeBuild 프로젝트를 사용했습니다. 그러나 이 회사는 이제 AWS CodeDeploy를 사용하여 파이프라인의 배포 단계를 처리하려고 합니다.
이 회사는 애플리케이션을 RPM 패키지로 패키징했으며 Amazon EC2 인스턴스 플릿에 애플리케이션을 배포해야 합니다. EC2 인스턴스는 EC2 Auto Scaling 그룹에 있으며 공통 AMI에서 시작됩니다.
이러한 요구 사항을 충족하기 위해 DevOps 엔지니어는 어떤 단계 조합을 수행해야 합니까? (두 가지를 선택하십시오.)

A. CodeDeploy 에이전트가 설치된 공통 AMI의 새 버전을 만듭니다. EC2 인스턴스의 IAM 역할을 업데이트하여 CodeDeploy에 대한 액세스를 허용합니다. 가장 많이 투표된
B. CodeDeploy 에이전트가 설치된 공통 AMI의 새 버전을 만듭니다. 애플리케이션 배포 스크립트를 포함하고 CodeDeploy에 대한 액세스 권한을 부여하는 AppSpec 파일을 만듭니다.
C. CodeDeploy에서 애플리케이션을 만듭니다. 인플레이스 배포 유형을 구성합니다. 배포 대상으로 자동 확장 그룹을 지정합니다. EC2 Image Builder를 사용하여 새 AMI를 만드는 CodePipeline 파이프라인에 단계를 추가합니다. 새로 만든 AMI를 배포하도록 CodeDeploy를 구성합니다.
D. CodeDeploy에서 애플리케이션을 만듭니다. 인플레이스 배포 유형을 구성합니다. 배포 대상으로 자동 확장 그룹을 지정합니다. CodePipeline 파이프라인을 업데이트하여 CodeDeploy 작업을 사용하여 애플리케이션을 배포합니다. 가장 많이 투표된
E. CodeDeploy에서 애플리케이션을 만듭니다. 인플레이스 배포 유형을 구성합니다. 배포 대상으로 공통 AMI에서 시작된 EC2 인스턴스를 지정합니다. CodePipeline 파이프라인을 업데이트하여 CodeDeploy 작업을 사용하여 애플리케이션을 배포합니다.



### 질문 #8주제 1
한 회사의 보안팀은 모든 외부 애플리케이션 로드 밸런서(ALB)와 Amazon API Gateway API가 AWS WAF 웹 ACL과 연결되어야 한다고 요구합니다. 이 회사에는 수백 개의 AWS 계정이 있으며, 모두 AWS Organizations의 단일 조직에 포함되어 있습니다. 이 회사는 조직에 대한 AWS Config를 구성했습니다. 감사 중에 이 회사는 AWS WAF 웹 ACL과 연결되지 않은 외부 ALB를 발견했습니다.
DevOps 엔지니어는 향후 위반을 방지하기 위해 어떤 단계 조합을 취해야 합니까? (두 가지를 선택하세요.)

A. AWS Firewall Manager를 보안 계정에 위임합니다. 가장 많이 투표된
B. Amazon GuardDuty를 보안 계정에 위임합니다.
C. AWS Firewall Manager 정책을 생성하여 새로 생성된 ALB 및 API Gateway API에 AWS WAF 웹 ACL을 연결합니다. 가장 많이 투표된
D. 새로 생성된 ALB 및 API Gateway API에 AWS WAF 웹 ACL을 연결하기 위해 Amazon GuardDuty 정책을 생성합니다.
E. AWS Config 관리 규칙을 구성하여 새로 생성된 ALB 및 API Gateway API에 AWS WAF 웹 ACL을 연결합니다.



### 질문 #9주제 1
한 회사에서는 AWS Key Management Service(AWS KMS) 키와 수동 키 로테이션을 사용하여 규정 준수 요구 사항을 충족합니다. 보안 팀은 90일 후에도 키가 로테이션되지 않은 경우 알림을 받고 싶어합니다.
어떤 솔루션이 이를 달성할까요?

A. 키가 90일 이상 지난 경우 Amazon Simple Notification Service(Amazon SNS) 주제에 게시하도록 AWS KMS를 구성합니다.
B. AWS Lambda 함수를 시작하여 AWS Trusted Advisor API를 호출하고 Amazon Simple Notification Service(Amazon SNS) 주제에 게시하도록 Amazon EventBridge 이벤트를 구성합니다.
C. 키가 90일 이상 경과한 경우 Amazon Simple Notification Service(Amazon SNS) 주제에 게시하는 AWS Config 사용자 지정 규칙을 개발합니다. 가장 많이 투표된
D. 키가 90일 이상 경과한 경우 Amazon Simple Notification Service(Amazon SNS) 주제에 게시하도록 AWS Security Hub를 구성합니다.



### 질문 #10주제 1
보안 검토에서 AWS CodeBuild 프로젝트가 인증되지 않은 요청을 사용하여 Amazon S3 버킷에서 데이터베이스 채우기 스크립트를 다운로드하고 있다는 사실이 확인되었습니다. 보안팀은 이 프로젝트에 대해 S3 버킷에 대한 인증되지 않은 요청을 허용하지 않습니다.
이 문제를 가장 안전한 방식으로 어떻게 수정할 수 있습니까?

A. CodeBuild 프로젝트 설정의 AllowedBuckets 섹션에 버킷 이름을 추가합니다. AWS CLI를 사용하여 데이터베이스 채우기 스크립트를 다운로드하도록 빌드 사양을 업데이트합니다.
B. S3 버킷 설정을 수정하여 HTTPS 기본 인증을 활성화하고 토큰을 지정합니다. 빌드 사양을 업데이트하여 cURL을 사용하여 토큰을 전달하고 데이터베이스 채우기 스크립트를 다운로드합니다.
C. 버킷 ​​정책을 사용하여 S3 버킷에서 인증되지 않은 액세스를 제거합니다. CodeBuild 프로젝트의 서비스 역할을 수정하여 Amazon S3 액세스를 포함합니다. AWS CLI를 사용하여 데이터베이스 채우기 스크립트를 다운로드합니다. 가장 많이 투표된
D. 버킷 정책을 사용하여 S3 버킷에서 인증되지 않은 액세스를 제거합니다. AWS CLI를 사용하여 IAM 액세스 키와 비밀 액세스 키를 사용하여 데이터베이스 채우기 스크립트를 다운로드합니다.



### 질문 #11주제 1
전자상거래 회사가 새로운 플랫폼을 호스팅하기 위해 AWS를 선택했습니다. 이 회사의 DevOps 팀은 AWS Control Tower 랜딩 존을 구축하기 시작했습니다. DevOps 팀은 AWS IAM Identity Center(AWS Single Sign-On) 내의 ID 저장소를 외부 ID 공급자(IdP)로 설정하고 SAML 2.0을 구성했습니다.
DevOps 팀은 최소 권한 원칙을 적용하는 강력한 권한 모델을 원합니다. 이 모델은 팀이 팀 자체 리소스만 빌드하고 관리할 수 있도록 허용해야 합니다.
이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. 필요한 권한을 포함하는 IAM 정책을 만듭니다. aws:PrincipalTag 조건 키를 포함합니다.
B. 권한 집합을 만듭니다. 필요한 권한을 포함하고 aws:PrincipalTag 조건 키를 사용하여 권한 범위를 지정하는 인라인 정책을 첨부합니다. 가장 많이 투표된
C. IdP에서 그룹을 만듭니다. 그룹에 사용자를 배치합니다. 그룹을 IAM Identity Center의 계정 및 권한 집합에 할당합니다. 가장 많이 투표된
D. IdP에서 그룹을 만듭니다. 그룹에 사용자를 배치합니다. 그룹을 OU 및 IAM 정책에 할당합니다.
E. IAM Identity Center에서 액세스 제어를 위한 속성을 활성화합니다. 사용자에게 태그를 적용합니다. 태그를 키-값 쌍으로 매핑합니다.
F. IAM Identity Center에서 액세스 제어를 위한 속성을 활성화합니다. IdP에서 속성을 키-값 쌍으로 매핑합니다. 가장 많이 투표된



### 질문 #12주제 1
전자상거래 회사에서 주문 내역 페이지에서 주문 처리 상태를 반영하는 데 지연이 발생한다는 보고를 받고 있습니다. 주문 처리 시스템은 예약된 동시성을 사용하는 AWS Lambda 함수로 구성되어 있습니다. Lambda 함수는 Amazon Simple Queue Service(Amazon SQS) 대기열에서 주문 메시지를 처리하고 처리된 주문을 Amazon DynamoDB 테이블에 삽입합니다. DynamoDB 테이블은 읽기 및 쓰기 용량에 대해 자동 확장이 활성화되어 있습니다.
DevOps 엔지니어는 이 지연을 해결하기 위해 어떤 조치를 취해야 합니까? (두 가지를 선택하세요.)

A. SQS 대기열에 대한 ApproximateAgeOfOldestMessage 메트릭을 확인합니다. Lambda 함수 동시성 제한을 늘립니다. 가장 많이 투표된
B. SQS 대기열의 ApproximateAgeOfOldestMessage 메트릭을 확인합니다. SQS 대기열에 대한 리드라이브 정책을 구성합니다.
C. SQS 대기열에 대한 NumberOfMessagesSent 메트릭을 확인합니다. SQS 대기열 가시성 시간 초과를 늘립니다.
D. DynamoDB 테이블에 대한 WriteThrottleEvents 메트릭을 확인합니다. 테이블의 스케일링 정책에 대한 최대 쓰기 용량 단위(WCU)를 늘립니다. 가장 많이 투표된
E. Lambda 함수의 Throttles 메트릭을 확인합니다. Lambda 함수 시간 초과를 늘립니다.



### 질문 #13주제 1
한 회사에는 단일 AWS 지역에서 수백 개의 Amazon EC2 인스턴스를 실행하는 단일 AWS 계정이 있습니다. 계정에서 매 시간 새로운 EC2 인스턴스가 시작되고 종료됩니다. 이 계정에는 1주일 이상 실행된 기존 EC2 인스턴스도 포함됩니다.
회사의 보안 정책에 따라 실행 중인 모든 EC2 인스턴스는 EC2 인스턴스 프로필을 사용해야 합니다. EC2 인스턴스에 인스턴스 프로필이 연결되지 않은 경우 EC2 인스턴스는 IAM 권한이 할당되지 않은 기본 인스턴스 프로필을 사용해야 합니다.
DevOps 엔지니어가 계정을 검토하고 인스턴스 프로필 없이 실행 중인 EC2 인스턴스를 발견합니다. 검토하는 동안 DevOps 엔지니어는 인스턴스 프로필 없이 새로운 EC2 인스턴스가 시작되고 있다는 사실도 관찰합니다.
어떤 솔루션에서 해당 지역의 모든 기존 및 향후 EC2 인스턴스에 인스턴스 프로필이 연결되도록 보장할까요?

A. EC2 RunInstances API 호출에 반응하는 Amazon EventBridge 규칙을 구성합니다. AWS Lambda 함수를 호출하여 기본 인스턴스 프로필을 EC2 인스턴스에 연결하도록 규칙을 구성합니다.
B. 구성 변경의 트리거 유형으로 ec2-instance-profile-attached AWS Config 관리 규칙을 구성합니다. 기본 인스턴스 프로필을 EC2 인스턴스에 연결하기 위해 AWS Systems Manager Automation 런북을 호출하는 자동 수정 작업을 구성합니다. 가장 많이 투표된
C. EC2 StartInstances API 호출에 반응하는 Amazon EventBridge 규칙을 구성합니다. AWS Systems Manager Automation 런북을 호출하여 기본 인스턴스 프로필을 EC2 인스턴스에 연결하도록 규칙을 구성합니다.
D. 구성 변경의 트리거 유형으로 iam-role-managed-policy-check AWS Config 관리 규칙을 구성합니다. 기본 인스턴스 프로필을 EC2 인스턴스에 연결하기 위해 AWS Lambda 함수를 호출하는 자동 수정 작업을 구성합니다.



### 질문 #14주제 1
DevOps 엔지니어가 AWS Lambda 함수를 사용하는 서버리스 애플리케이션에 대한 지속적인 배포 파이프라인을 구축하고 있습니다. 이 회사는 실패한 배포로 인한 고객 영향을 줄이고자 합니다. 또한 이 회사는 문제를 모니터링하고자 합니다.
어떤 배포 단계 구성이 이러한 요구 사항을 충족할까요?

A. AWS Serverless Application Model(AWS SAM) 템플릿을 사용하여 서버리스 애플리케이션을 정의합니다. AWS CodeDeploy를 사용하여 Canary10Percent15Minutes 배포 기본 설정 유형으로 Lambda 함수를 배포합니다. Amazon CloudWatch 알람을 사용하여 함수의 상태를 모니터링합니다. 가장 많이 투표된
B. AWS CloudFormation을 사용하여 새 스택 업데이트를 게시하고 모든 리소스에 Amazon CloudWatch 알람을 포함합니다. 개발자가 AWS CloudFormation 변경 세트를 확인하고 승인할 수 있도록 AWS CodePipeline 승인 작업을 설정합니다.
C. AWS CloudFormation을 사용하여 모든 스택 업데이트에 새 버전을 게시하고 모든 리소스에 Amazon CloudWatch 알람을 포함합니다. AWS::Lambda::Alias ​​리소스의 RoutingConfig 속성을 사용하여 스택 업데이트 중에 트래픽 라우팅을 업데이트합니다.
D. AWS CodeBuild를 사용하여 Lambda 함수에 테스트용 샘플 이벤트 페이로드를 추가합니다. 함수의 새 버전을 게시하고 Amazon CloudWatch 알람을 포함합니다. 프로덕션 별칭을 업데이트하여 새 버전을 가리키도록 합니다. 알람이 ALARM 상태일 때 롤백이 발생하도록 구성합니다.



### 질문 #15주제 1
애플리케이션을 실행하기 위해 DevOps 엔지니어는 퍼블릭 서브넷에서 퍼블릭 IP 주소로 Amazon EC2 인스턴스를 시작합니다. 사용자 데이터 스크립트는 애플리케이션 아티팩트를 가져와서 시작 시 인스턴스에 설치합니다. 이제 애플리케이션의 보안 분류가 변경되어 인스턴스가 인터넷에 액세스할 수 없이 실행되어야 합니다. 인스턴스가 성공적으로 시작되고 정상으로 표시되지만 애플리케이션이 설치되지 않은 것 같습니다.
다음 중 어떤 것이 새 규칙을 준수하면서 애플리케이션을 성공적으로 설치해야 합니까?

A. Elastic IP 주소가 연결된 퍼블릭 서브넷에서 인스턴스를 시작합니다. 애플리케이션이 설치되고 실행되면 나중에 Elastic IP 주소를 분리하는 스크립트를 실행합니다.
B. NAT 게이트웨이를 설정합니다. EC2 인스턴스를 프라이빗 서브넷에 배포합니다. 프라이빗 서브넷의 경로 테이블을 업데이트하여 NAT 게이트웨이를 기본 경로로 사용합니다.
C. Amazon S3 버킷에 애플리케이션 아티팩트를 게시하고 S3에 대한 VPC 엔드포인트를 만듭니다. EC2 인스턴스에 IAM 인스턴스 프로필을 할당하여 S3 버킷에서 애플리케이션 아티팩트를 읽을 수 있도록 합니다. 가장 많이 투표된
D. 애플리케이션 인스턴스에 대한 보안 그룹을 만들고 아티팩트 리포지토리로의 아웃바운드 트래픽만 허용합니다. 설치가 완료되면 보안 그룹 규칙을 제거합니다.



### 질문 #16주제 1
개발팀은 AWS CodeCommit을 사용하여 애플리케이션 코드의 버전을 제어하고 AWS CodePipeline을 사용하여 소프트웨어 배포를 조율합니다. 이 팀은 파이프라인이 코드 변경 사항을 통합하도록 원격 메인 브랜치를 트리거로 사용하기로 결정했습니다. 개발자는 코드 변경 사항을 CodeCommit 리포지토리에 푸시했지만 파이프라인이 10분이 지나도 아무런 반응이 없다는 것을 알아챘습니다.
이 문제를 해결하려면 다음 중 어떤 조치를 취해야 합니까?

A. 파이프라인을 트리거하기 위해 메인 브랜치에 대한 Amazon EventBridge 규칙이 생성되었는지 확인합니다. 가장 많이 투표된
B. CodePipeline 서비스 역할에 CodeCommit 저장소에 액세스할 수 있는 권한이 있는지 확인합니다.
C. 개발자의 IAM 역할에 CodeCommit 저장소에 푸시할 수 있는 권한이 있는지 확인합니다.
D. Amazon CloudWatch Logs의 CodeCommit 오류로 인해 파이프라인이 시작되지 않았는지 확인합니다.



### 질문 #17주제 1
한 회사의 개발자가 Amazon EC2 인스턴스를 원격 워크스테이션으로 사용합니다. 이 회사는 사용자가 EC2 보안 그룹을 만들거나 수정하여 무제한 인바운드 액세스를 허용할 수 있다는 점에 대해 우려하고 있습니다.
DevOps 엔지니어는 사용자가 무제한 보안 그룹 규칙을 만들 때 이를 감지하는 솔루션을 개발해야 합니다. 이 솔루션은 거의 실시간으로 보안 그룹 규칙의 변경 사항을 감지하고, 무제한 규칙을 제거하고, 보안 팀에 이메일 알림을 보내야 합니다. DevOps 엔지니어는 입력에서 보안 그룹 ID를 확인하고, 무제한 액세스를 허용하는 규칙을 제거하고, Amazon Simple Notification Service(Amazon SNS)를 통해 알림을 보내는 AWS Lambda 함수를 만들었습니다.
DevOps 엔지니어는 요구 사항을 충족하기 위해 다음에 무엇을 해야 합니까?

A. SNS 토픽에서 호출할 Lambda 함수를 구성합니다. SNS 토픽에 대한 AWS CloudTrail 구독을 만듭니다. 보안 그룹 수정 이벤트에 대한 구독 필터를 구성합니다.
B. Lambda 함수를 호출하기 위한 Amazon EventBridge 예약 규칙을 만듭니다. 매 시간 Lambda 함수를 실행하는 스케줄 패턴을 정의합니다.
C. 기본 이벤트 버스를 소스로 하는 Amazon EventBridge 이벤트 규칙을 만듭니다. EC2 보안 그룹 생성 및 수정 이벤트와 일치하도록 규칙의 이벤트 패턴을 정의합니다. Lambda 함수를 호출하도록 규칙을 구성합니다. 가장 많이 투표된
D. 모든 AWS 서비스의 이벤트를 구독하는 Amazon EventBridge 사용자 지정 이벤트 버스를 만듭니다. 사용자 지정 이벤트 버스에서 호출할 Lambda 함수를 구성합니다.




### 질문 #18주제 1
DevOps 엔지니어가 웹 서비스를 배포하기 위해 AWS CloudFormation 템플릿을 만들고 있습니다. 웹 서비스는 Application Load Balancer(ALB) 뒤의 프라이빗 서브넷에 있는 Amazon EC2 인스턴스에서 실행됩니다. DevOps 엔지니어는 서비스가 IPv6 주소가 있는 클라이언트의 요청을 수락할 수 있는지 확인해야 합니다.
IPv6 클라이언트가 웹 서비스에 액세스할 수 있도록 DevOps 엔지니어는 CloudFormation 템플릿으로 무엇을 해야 합니까?

A. EC2 인스턴스의 VPC와 프라이빗 서브넷에 IPv6 CIDR 블록을 추가합니다. IPv6 네트워크에 대한 경로 테이블 항목을 만들고, IPv6를 지원하는 EC2 인스턴스 유형을 사용하고, 각 EC2 인스턴스에 IPv6 주소를 할당합니다.
B. 각 EC2 인스턴스에 IPv6 Elastic IP 주소를 할당합니다. 대상 그룹을 만들고 EC2 인스턴스를 대상으로 추가합니다. ALB의 포트 443에 리스너를 만들고 대상 그룹을 ALB와 연결합니다.
C. ALB를 네트워크 로드 밸런서(NLB)로 교체합니다. NLB의 VPC와 서브넷에 IPv6 CIDR 블록을 추가하고 NLB에 IPv6 탄력적 IP 주소를 할당합니다.
D. ALB의 VPC와 서브넷에 IPv6 CIDR 블록을 추가합니다. 포트 443에 리스너를 만듭니다. 그리고 ALB에서 dualstack IP 주소 유형을 지정합니다. 대상 그룹을 만들고 EC2 인스턴스를 대상으로 추가합니다. 대상 그룹을 ALB와 연결합니다. 가장 많이 투표된



### 질문 #19주제 1
한 회사에서는 AWS Organizations와 AWS Control Tower를 사용하여 회사의 모든 AWS 계정을 관리합니다. 이 회사는 Enterprise Support 플랜을 사용합니다.
DevOps 엔지니어는 Account Factory for Terraform(AFT)을 사용하여 새 계정을 프로비저닝합니다. 새 계정이 프로비저닝되면 DevOps 엔지니어는 새 계정에 대한 지원 플랜이 Basic Support 플랜으로 설정되어 있음을 알게 됩니다. DevOps 엔지니어는 Enterprise Support 플랜으로 새 계정을 프로비저닝하는 솔루션을 구현해야 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS Config 적합성 팩을 사용하여 조직의 일부인 계정 AWS Config 규칙을 배포하고 규정을 준수하지 않는 모든 계정을 자동으로 수정합니다.
B. AWS Lambda 함수를 만들어 AWS Support에서 Enterprise Support 플랜에 계정을 추가하기 위한 티켓을 만듭니다. Lambda 함수에 support:ResolveCase 권한을 부여합니다.
C. control_tower_parameters 입력에 추가 값을 추가하여 AWSEnterpriseSupport 매개변수를 조직의 관리 계정 번호로 설정합니다.
D. AFT 배포 입력 구성에서 aft_feature_enterprise_support 기능 플래그를 True로 설정합니다. AFT를 다시 배포하고 변경 사항을 적용합니다. 가장 많이 투표된



### 질문 #20주제 1
한 회사의 DevOps 엔지니어가 AWS Systems Manager를 사용하여 유지 관리 기간 동안 유지 관리 작업을 수행합니다. 이 회사에는 AWS Health에서 알림을 받은 후 재시작이 필요한 Amazon EC2 인스턴스가 몇 개 있습니다. DevOps 엔지니어는 이러한 알림을 수정하기 위한 자동화된 솔루션을 구현해야 합니다. DevOps 엔지니어가 Amazon EventBridge 규칙을 만듭니다.
DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 EventBridge 규칙을 어떻게 구성해야 합니까?

A. EC2의 서비스인 AWS Health의 이벤트 소스와 인스턴스 유지 관리를 나타내는 이벤트 유형을 구성합니다. EC2 인스턴스를 다시 시작하려면 Systems Manager 문서를 대상으로 지정합니다. 가장 많이 투표된
B. Systems Manager의 이벤트 소스와 유지 관리 기간을 나타내는 이벤트 유형을 구성합니다. EC2 인스턴스를 다시 시작하려면 Systems Manager 문서를 대상으로 지정합니다.
C. EC2의 서비스인 AWS Health의 이벤트 소스와 인스턴스 유지 관리를 나타내는 이벤트 유형을 구성합니다. 유지 관리 기간 동안 EC2 인스턴스를 다시 시작하는 자동화 작업을 등록하는 새로 생성된 AWS Lambda 함수를 대상으로 합니다.
D. EC2의 이벤트 소스와 인스턴스 유지 관리를 나타내는 이벤트 유형을 구성합니다. 유지 관리 기간 동안 EC2 인스턴스를 다시 시작하기 위한 자동화 작업을 등록하는 새로 생성된 AWS Lambda 함수를 대상으로 합니다.



### 질문 #21주제 1
한 회사가 사내 품질 관리 애플리케이션을 모두 컨테이너화했습니다. 이 회사는 패치 및 업그레이드가 필요한 Amazon EC2 인스턴스에서 Jenkins를 실행하고 있습니다. 규정 준수 책임자는 DevOps 엔지니어에게 회사 지적 재산이 포함되어 있으므로 빌드 아티팩트를 암호화하기 시작하도록 요청했습니다.
DevOps 엔지니어는 가장 유지 관리하기 쉬운 방식으로 이를 달성하기 위해 무엇을 해야 합니까?

A. AWS Systems Manager를 사용하여 EC2 인스턴스에서 패치 및 업그레이드를 자동화하고 기본적으로 Amazon EBS 볼륨을 암호화합니다.
B. Amazon ECS 클러스터에 Jenkins를 배포하고 기본 암호화가 활성화된 Amazon S3 버킷에 빌드 아티팩트를 복사합니다.
C. AWS CodePipeline을 빌드 작업과 함께 활용하고 AWS Secrets Manager를 사용하여 아티팩트를 암호화합니다.
D. EC2 인스턴스에서 실행되는 Jenkins 인스턴스를 아티팩트 암호화와 함께 AWS CodeBuild를 사용하여 대체합니다. 가장 많이 투표된



### 질문 #22주제 1
IT 팀은 회사의 다른 사람들이 애플리케이션을 빠르고 안정적으로 배포하고 종료할 수 있도록 AWS CloudFormation 템플릿을 구축했습니다. 이 템플릿은 애플리케이션을 설치하는 사용자 데이터 스크립트와 애플리케이션이 실행되는 동안 정적 웹 페이지를 제공하는 데 사용하는 Amazon S3 버킷이 있는 Amazon EC2 인스턴스를 만듭니다.
CloudFormation 스택을 삭제하면 모든 리소스를 제거해야 합니다. 그러나 팀은 CloudFormation이 스택 삭제 중에 오류를 보고하고 스택에서 만든 S3 버킷이 삭제되지 않는다는 것을 관찰합니다. 팀
은 모든 리소스가 오류 없이 삭제되도록 가장 효율적인 방식으로 오류를 어떻게 해결할 수 있을까요?

A. S3 버킷 리소스에 DelelionPolicy 속성을 추가하고, 값에 Delete를 지정하면 스택이 삭제될 때 버킷도 제거됩니다.
B. S3 버킷과 IAM 역할을 지정하는 DependsOn 속성이 있는 AWS Lambda 함수로 사용자 지정 리소스를 추가합니다. RequestType이 Delete일 때 버킷에서 모든 객체를 삭제하는 Lambda 함수를 작성합니다. 가장 많이 투표된
C. 삭제되지 않은 리소스를 식별합니다. S3 버킷을 수동으로 비운 다음 삭제합니다.
D. EC2 및 S3 버킷 리소스를 단일 AWS OpsWorks Stacks 리소스로 교체합니다. 스택에 대한 사용자 지정 레시피를 정의하여 EC2 인스턴스와 S3 버킷을 만들고 삭제합니다.



### 질문 #23주제 1
한 회사에 eu-west-1 지역의 Amazon S3 버킷으로 구성된 AWS CodePipeline 파이프라인이 있습니다. 파이프라인은 동일한 지역에 AWS Lambda 애플리케이션을 배포합니다. 파이프라인은 AWS CodeBuild 프로젝트 빌드 작업과 AWS CloudFormation 배포 작업으로 구성됩니다.
CodeBuild 프로젝트는 aws cloudformation package AWS CLI 명령을 사용하여 Lambda 함수 코드의 .zip 파일과 CloudFormation 템플릿이 포함된 아티팩트를 빌드합니다. CloudFormation 배포 작업은 CodeBuild 프로젝트 빌드 작업의 출력 아티팩트에서 CloudFormation 템플릿을 참조합니다.
이 회사는 eu-west-1의 파이프라인을 사용하여 Lambda 애플리케이션을 us-east-1 지역에도 배포하려고 합니다. DevOps 엔지니어는 이미 CodeBuild 프로젝트를 업데이트하여 aws cloudformation package 명령을 사용하여 us-east-1에 대한 추가 출력 아티팩트를 생성했습니다.
DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 어떤 추가 단계 조합을 수행해야 합니까? (두 가지를 선택하세요.)

A. Lambda 함수 코드의 zip 파일 위치에 대한 매개변수를 포함하도록 CloudFormation 템플릿을 수정합니다. 파이프라인에서 us-east-1에 대한 새 CloudFormation 배포 작업을 만듭니다. 매개변수 재정의로 us-east-1 아티팩트 위치를 전달하도록 새 배포 작업을 구성합니다.
B. 파이프라인에서 us-east-1에 대한 새 CloudFormation 배포 작업을 만듭니다. us-east-1 출력 아티팩트의 CloudFormation 템플릿을 사용하도록 새 배포 작업을 구성합니다.
C. us-east-1에 S3 버킷을 만듭니다. CodePipeline이 읽기 및 쓰기 액세스 권한을 가질 수 있도록 S3 버킷 정책을 구성합니다. 가장 많이 투표된
D. us-east-1에 S3 버킷을 만듭니다. eu-west-1의 S3 버킷에서 us-east-1의 S3 버킷으로 S3 Cross-Region Replication(CRR)을 구성합니다.
E. 파이프라인을 수정하여 us-east-1의 S3 버킷을 아티팩트 저장소로 포함합니다. 파이프라인에서 us-east-1에 대한 새 CloudFormation 배포 작업을 만듭니다. us-east-1 출력 아티팩트의 CloudFormation 템플릿을 사용하도록 새 배포 작업을 구성합니다. 가장 많이 투표된



### 질문 #24주제 1
한 회사가 하나의 Amazon EC2 인스턴스에서 애플리케이션을 실행합니다. 애플리케이션 메타데이터는 Amazon S3에 저장되며 인스턴스가 재시작되면 검색해야 합니다. 인스턴스가 응답하지 않으면 인스턴스가 자동으로 재시작되거나 다시 시작되어야 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. StatusCheckFailed 메트릭에 대한 Amazon CloudWatch 알람을 만듭니다. 복구 작업을 사용하여 인스턴스를 중지하고 시작합니다. S3 이벤트 알림을 사용하여 인스턴스가 다시 작동하고 실행될 때 메타데이터를 인스턴스에 푸시합니다.
B. AWS OpsWorks를 구성하고 자동 복구 기능을 사용하여 인스턴스를 중지하고 시작합니다. OpsWorks의 라이프사이클 이벤트를 사용하여 Amazon S3에서 메타데이터를 가져와 인스턴스에 업데이트합니다. 가장 많이 투표된
C. EC2 자동 복구를 사용하여 장애 발생 시 인스턴스를 자동으로 중지하고 시작합니다. S3 이벤트 알림을 사용하여 인스턴스가 다시 작동하고 실행 중일 때 메타데이터를 인스턴스에 푸시합니다.
D. AWS CloudFormation을 사용하여 EC2 리소스에 대한 UserData 속성을 포함하는 EC2 인스턴스를 만듭니다. UserData에 명령을 추가하여 Amazon S3에서 애플리케이션 메타데이터를 검색합니다.



### 질문 #25주제 1
회사에 여러 AWS 계정이 있습니다. 이 회사는 AWS Toolkit for Microsoft Azure DevOps와 통합된 AWS IAM Identity Center(AWS Single Sign-On)를 사용합니다. 액세스 제어 기능의 속성은 IAM Identity Center에서 활성화됩니다.
속성 매핑 목록에는 두 개의 항목이 있습니다. department 키는 ${path:enterprise.department}에 매핑됩니다. costCenter 키는 ${path:enterprise.costCenter}에 매핑됩니다.
모든 기존 Amazon EC2 인스턴스에는 세 개의 회사 부서(d1, d2, d3)에 해당하는 department 태그가 있습니다. DevOps 엔지니어는 일치하는 속성을 기반으로 정책을 만들어야 합니다. 정책은 관리 작업을 최소화해야 하며 각 Azure AD 사용자에게 사용자의 해당 부서 이름으로 태그가 지정된 EC2 인스턴스에만 액세스 권한을 부여해야 합니다.
DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 사용자 지정 권한 정책에 어떤 조건 키를 포함해야 합니까?

"condition":{
    "StringQuals":{
        "ec2:ResourceTag/department": "$(aws:PrincipalTag/department)"
    }
}


### 질문 #26주제 1
한 회사가 AWS 계정에서 보안 감사 애플리케이션을 호스팅합니다. 감사 애플리케이션은 IAM 역할을 사용하여 다른 AWS 계정에 액세스합니다. 모든 계정은 AWS Organizations에서 동일한 조직에 있습니다.
최근 보안 감사에서 감사된 AWS 계정의 사용자가 감사 애플리케이션의 IAM 역할을 수정하거나 삭제할 수 있음이 밝혀졌습니다. 이 회사는 신뢰할 수 있는 관리자 IAM 역할이 아닌 다른 엔터티가 감사 애플리케이션의 IAM 역할을 수정하는 것을 방지해야 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 감사 애플리케이션의 IAM 역할에 대한 변경에 대한 Deny 문이 포함된 SCP를 만듭니다. 신뢰할 수 있는 관리자 IAM 역할이 변경을 수행할 수 있도록 허용하는 조건을 포함합니다. SCP를 조직의 루트에 연결합니다. 가장 많이 투표된
B. 신뢰할 수 있는 관리자 IAM 역할에 의한 감사 애플리케이션의 IAM 역할 변경에 대한 허용 명령문을 포함하는 SCP를 만듭니다. 다른 모든 IAM 주체에 의한 변경에 대한 거부 명령문을 포함합니다. 감사 애플리케이션에 IAM 역할이 있는 각 AWS 계정의 IAM 서비스에 SCP를 연결합니다.
C. 감사 애플리케이션의 IAM 역할에 대한 변경에 대한 Deny 문을 포함하는 IAM 권한 경계를 만듭니다. 신뢰할 수 있는 관리자 IAM 역할이 변경을 수행할 수 있도록 허용하는 조건을 포함합니다. 감사된 AWS 계정에 권한 경계를 연결합니다.
D. 감사 애플리케이션의 IAM 역할에 대한 변경에 대한 Deny 문을 포함하는 IAM 권한 경계를 만듭니다. 신뢰할 수 있는 관리자 IAM 역할이 변경을 수행할 수 있도록 허용하는 조건을 포함합니다. AWS 계정에서 감사 애플리케이션의 IAM 역할에 권한 경계를 연결합니다.



### 질문 #27주제 1
한 회사에 Go로 작성된 온프레미스 애플리케이션이 있습니다. DevOps 엔지니어는 애플리케이션을 AWS로 옮겨야 합니다. 회사의 개발팀은 블루/그린 배포를 활성화하고 A/B 테스트를 수행하려고 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Amazon EC2 인스턴스에 애플리케이션을 배포하고 인스턴스의 AMI를 만듭니다. AMI를 사용하여 Auto Scaling 그룹에서 사용되는 자동 스케일링 시작 구성을 만듭니다. Elastic Load Balancing을 사용하여 트래픽을 분산합니다. 애플리케이션에 변경 사항이 있으면 새 AMI가 생성되어 EC2 인스턴스 새로 고침이 시작됩니다.
B. Amazon Lightsail을 사용하여 애플리케이션을 배포합니다. 애플리케이션을 Amazon S3 버킷에 압축 형식으로 저장합니다. 이 압축 버전을 사용하여 애플리케이션의 새 버전을 Lightsail에 배포합니다. Lightsail 배포 옵션을 사용하여 배포를 관리합니다.
C. AWS CodeArtifact를 사용하여 애플리케이션 코드를 저장합니다. AWS CodeDeploy를 사용하여 애플리케이션을 Amazon EC2 인스턴스 플릿에 배포합니다. Elastic Load Balancing을 사용하여 트래픽을 EC2 인스턴스에 분산합니다. 애플리케이션을 변경할 때 CodeArtifact에 새 버전을 업로드하고 새 CodeDeploy 배포를 만듭니다.
D. AWS Elastic Beanstalk를 사용하여 애플리케이션을 호스팅합니다. Amazon S3에 애플리케이션의 압축 버전을 저장합니다. 해당 위치를 사용하여 애플리케이션의 새 버전을 배포합니다. Elastic Beanstalk를 사용하여 배포 옵션을 관리합니다. 가장 많이 투표된



### 질문 #28주제 1
개발자는 50대의 Amazon EC2 Linux 서버를 유지 관리하고 있습니다. 이 서버는 Amazon EC2 Auto Scaling 그룹의 일부이며, 부하 분산을 위해 Elastic Load Balancing도 사용합니다.
가끔 일부 애플리케이션 서버가 ELB HTTP 상태 검사에 실패한 후 종료됩니다. 개발자는 이 문제에 대한 근본 원인 분석을 수행하고 싶지만 애플리케이션 로그에 액세스하기 전에 서버가 종료됩니다.
로그 수집을 어떻게 자동화할 수 있습니까?

A. Auto Scaling 라이프사이클 후크를 사용하여 인스턴스를 Pending:Wait 상태로 만듭니다. EC2 인스턴스 종료 성공에 대한 Amazon CloudWatch 알람을 만들고 SSM Run Command 스크립트를 호출하여 로그를 수집하고 Amazon S3에 푸시하고 로그가 수집되면 라이프사이클 작업을 완료하는 AWS Lambda 함수를 트리거합니다.
B. Auto Scaling 라이프사이클 후크를 사용하여 인스턴스를 Terminating:Wait 상태로 만듭니다. EC2 Instance-terminate 라이프사이클 액션에 대한 AWS Config 규칙을 만들고 로그를 수집하고 Amazon S3에 푸시하고 로그가 수집되면 라이프사이클 액션을 완료하는 스크립트를 호출하는 단계 함수를 트리거합니다.
C. Auto Scaling 라이프사이클 후크를 사용하여 인스턴스를 Terminating:Wait 상태로 만듭니다. EC2 Instance Terminate Successful에 대한 Amazon CloudWatch 구독 필터를 만들고 로그를 수집하고 Amazon S3에 푸시하고 로그가 수집되면 라이프사이클 작업을 완료하는 스크립트를 호출하는 CloudWatch 에이전트를 트리거합니다.
D. Auto Scaling 라이프사이클 후크를 사용하여 인스턴스를 Terminating:Wait 상태로 만듭니다. EC2 Instance-terminate 라이프사이클 액션에 대한 Amazon EventBridge 규칙을 만들고 SSM Run Command 스크립트를 호출하여 로그를 수집하고 Amazon S3에 푸시하고 로그가 수집되면 라이프사이클 액션을 완료하는 AWS Lambda 함수를 트리거합니다. 가장 많이 투표된



### 질문 #29주제 1
회사에 AWS Organizations에 조직이 있습니다. 조직에는 엔터프라이즈 애플리케이션이 포함된 워크로드 계정이 포함됩니다. 회사는 운영 계정에서 사용자를 중앙에서 관리합니다. 워크로드 계정에서 사용자를 만들 수 없습니다. 회사는 최근에 운영 팀을 추가했으며 운영 팀 구성원에게 각 워크로드 계정에 대한 관리자 액세스 권한을 제공해야 합니다.
어떤 작업 조합이 이 액세스를 제공할까요? (세 가지를 선택하세요.)

A. 운영 계정에서 SysAdmin 역할을 만듭니다. AdministratorAccess 정책을 역할에 연결합니다. 신뢰 관계를 수정하여 워크로드 계정에서 sts:AssumeRole 작업을 허용합니다.
B. 각 워크로드 계정에서 SysAdmin 역할을 만듭니다. AdministratorAccess 정책을 역할에 연결합니다. 운영 계정에서 sts:AssumeRole 작업을 허용하도록 신뢰 관계를 수정합니다. 가장 많이 투표된
C. 운영 계정에서 Amazon Cognito ID 풀을 만듭니다. SysAdmin 역할을 인증된 역할로 연결합니다.
D. 운영 계정에서 각 운영 팀 구성원에 대한 IAM 사용자를 만듭니다. 가장 많이 투표된
E. 운영 계정에서 SysAdmins라는 이름의 IAM 사용자 그룹을 만듭니다. 각 워크로드 계정에서 SysAdmin 역할에 대한 sts:AssumeRole 작업을 허용하는 IAM 정책을 추가합니다. 모든 운영 팀 구성원을 그룹에 추가합니다. 가장 많이 투표된
F. 운영 계정에서 Amazon Cognito 사용자 풀을 만듭니다. 각 운영 팀원에 대해 Amazon Cognito 사용자를 만듭니다.



### 질문 #30주제 1
한 회사가 AWS Organizations의 한 조직에 여러 계정을 가지고 있습니다. 조직의 계정이 Amazon S3 버킷에서 Block Public Access 기능을 끄면 회사의 SecOps 팀은 Amazon Simple Notification Service(Amazon SNS) 알림을 받아야 합니다. DevOps 엔지니어는 AWS 계정의 운영에 영향을 미치지 않고 이 변경 사항을 구현해야 합니다. 구현은 조직의 개별 멤버 계정이 알림을 끌 수 없도록 해야 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 위임된 Amazon GuardDuty 관리자 계정이 될 계정을 지정합니다. 조직 전체의 모든 계정에 대해 GuardDuty를 켭니다. GuardDuty 관리자 계정에서 SNS 토픽을 만듭니다. SecOps 팀의 이메일 주소를 SNS 토픽에 구독합니다. 동일한 계정에서 GuardDuty 결과에 대한 이벤트 패턴과 SNS 토픽의 대상을 사용하는 Amazon EventBridge 규칙을 만듭니다.
B. SNS 토픽을 만들고 SecOps 팀의 이메일 주소를 SNS 토픽에 구독하는 AWS CloudFormation 템플릿을 만듭니다. 템플릿에 s3:PutBucketPublicAccessBlock에 대한 CloudTrail 활동의 이벤트 패턴과 SNS 토픽의 대상을 사용하는 Amazon EventBridge 규칙을 포함합니다. CloudFormation StackSets를 사용하여 조직의 모든 계정에 스택을 배포합니다.
C. 조직 전체에서 AWS Config를 켭니다. 위임된 관리자 계정에서 SNS 토픽을 만듭니다. SecOps 팀의 이메일 주소를 SNS 토픽에 구독합니다. 각 계정에서 s3-bucket-level-public-access-prohibited AWS Config 관리 규칙을 사용하고 AWS Systems Manager 문서를 사용하여 SecOps 팀에 알리기 위해 SNS 토픽에 이벤트를 게시하는 적합성 팩을 배포합니다. 가장 많이 투표된
D. 조직 전체에서 Amazon Inspector를 켭니다. Amazon Inspector 위임 관리자 계정에서 SNS 토픽을 만듭니다. SecOps 팀의 이메일 주소를 SNS 토픽에 구독합니다. 같은 계정에서 S3 버킷의 퍼블릭 네트워크 노출에 대한 이벤트 패턴을 사용하고 SecOps 팀에 알리기 위해 SNS 토픽에 이벤트를 게시하는 Amazon EventBridge 규칙을 만듭니다.



### 질문 #31주제 1
한 회사가 컨테이너 기반 애플리케이션을 Amazon EKS로 마이그레이션했고 자동화된 이메일 알림을 설정하려고 합니다. 각 이메일 주소로 전송된 알림은 EKS 구성 요소와 관련된 특정 활동을 위한 것입니다. 이 솔루션에는 Amazon SNS 토픽과 들어오는 로그 이벤트를 평가하고 올바른 SNS 토픽에 메시지를 게시하는 AWS Lambda 함수가 포함됩니다.
어떤 로깅 솔루션이 이러한 요구 사항을 지원할까요?

A. Amazon CloudWatch Logs를 활성화하여 EKS 구성 요소를 로깅합니다. Lambda를 구독 피드 대상으로 하여 각 구성 요소에 대한 CloudWatch 구독 필터를 만듭니다. 가장 많이 투표된
B. Amazon CloudWatch Logs를 활성화하여 EKS 구성 요소를 로깅합니다. Lambda를 호출하는 Amazon EventBridge 이벤트에 연결된 CloudWatch Logs Insights 쿼리를 만듭니다.
C. EKS 구성 요소에 대한 Amazon S3 로깅을 활성화합니다. Lambda를 구독 피드 대상으로 하여 각 구성 요소에 대한 Amazon CloudWatch 구독 필터를 구성합니다.
D. EKS 구성 요소에 대한 Amazon S3 로깅을 활성화합니다. AWS Lambda를 대상으로 S3 PUT Object 이벤트 알림을 구성합니다.



### 질문 #32주제 1
한 회사가 워크로드를 실행하기 위해 Amazon Elastic Container Service(Amazon ECS) 클러스터를 구현하고 있습니다. 회사 아키텍처는 클러스터에서 여러 ECS 서비스를 실행합니다. 아키텍처에는 프런트 엔드에 Application Load Balancer가 포함되어 있으며 여러 대상 그룹을 사용하여 트래픽을 라우팅합니다.
DevOps 엔지니어는 애플리케이션과 액세스 로그를 수집해야 합니다. 그런 다음 DevOps 엔지니어는 거의 실시간 분석을 위해 로그를 Amazon S3 버킷으로 보내야 합니다.
이러한 요구 사항을 충족하기 위해 DevOps 엔지니어는 어떤 단계 조합을 취해야 합니까? (세 가지를 선택하세요.)

A. AWS에서 Amazon CloudWatch Logs 컨테이너 인스턴스를 다운로드합니다. 이 인스턴스를 작업으로 구성합니다. 로깅 작업을 포함하도록 애플리케이션 서비스 정의를 업데이트합니다.
B. ECS 인스턴스에 Amazon CloudWatch Logs 에이전트를 설치합니다. ECS 작업 정의의 로깅 드라이버를 awslogs로 변경합니다. 가장 많이 투표된
C. Amazon EventBridge를 사용하여 60초마다 실행되고 Amazon CloudWatch Logs create-export-task 명령을 실행하는 AWS Lambda 함수를 예약합니다. 그런 다음 출력을 로깅 S3 버킷으로 가리킵니다.
D. ALB에서 액세스 로깅을 활성화합니다. 그런 다음 ALB를 로깅 S3 버킷으로 직접 가리킵니다. 가장 많이 투표된
E. ECS 서비스가 사용하는 대상 그룹에서 액세스 로깅을 활성화합니다. 그런 다음 로깅 S3 버킷으로 직접 로그를 보냅니다.
F. 로깅 S3 버킷의 목적지가 있는 Amazon Kinesis Data Firehose 전달 스트림을 만듭니다. 그런 다음 Kinesis Data Firehose에 대한 Amazon CloudWatch Logs 구독 필터를 만듭니다. 가장 많이 투표된



### BDF(100%)

질문 #33주제 1
전자 건강 기록을 사용하는 한 회사가 Amazon Linux 운영 체제를 사용하여 Amazon EC2 인스턴스 플릿을 실행하고 있습니다. 환자 개인 정보 보호 요구 사항의 일환으로 회사는 EC2 인스턴스에서 실행되는 운영 체제 및 애플리케이션에 대한 패치에 대한 지속적인 준수를 보장해야 합니다.
기본 및 사용자 지정 리포지토리를 사용하여 운영 체제 및 애플리케이션 패치의 배포를 자동화할 수 있는 방법은 무엇입니까?

A. AWS Systems Manager를 사용하여 사용자 정의 리포지토리를 포함한 새 패치 베이스라인을 만듭니다. run 명령을 사용하여 AWS-RunPatchBaseline 문서를 실행하여 패치를 확인하고 설치합니다. 가장 많이 투표된
B. AWS Direct Connect를 사용하여 기업 리포지토리를 통합하고 Amazon CloudWatch 예약 이벤트를 사용하여 패치를 배포한 다음 CloudWatch 대시보드를 사용하여 보고서를 만듭니다.
C. yum-config-manager를 사용하여 /etc/yum.repos.d에 사용자 정의 저장소를 추가하고 yum-config-manager-enable을 실행하여 저장소를 활성화합니다.
D. AWS Systems Manager를 사용하여 기업 리포지토리를 포함한 새로운 패치 베이스라인을 만듭니다. run 명령을 사용하여 AWS-AmazonLinuxDefaultPatchBaseline 문서를 실행하여 패치를 확인하고 설치합니다.



### 질문 #34주제 1
한 회사에서 AWS CodePipeline을 사용하여 릴리스 파이프라인을 자동화하고 있습니다. AWS CodeDeploy는 파이프라인에서 블루/그린 배포 모델을 사용하여 Amazon Elastic Container Service(Amazon ECS)에 애플리케이션을 배포하는 데 사용되고 있습니다. 이 회사는 트래픽을 전환하기 전에 그린 버전의 애플리케이션을 테스트하는 스크립트를 구현하려고 합니다. 이러한 스크립트는 5분 이내에 완료됩니다. 이러한 테스트 중에 오류가 발견되면 애플리케이션을 롤백해야 합니다.
이러한 요구 사항을 충족하는 전략은 무엇입니까?

A. 소스와 배포 단계 사이에 CodePipeline 파이프라인에 단계를 추가합니다. AWS CodeBuild를 사용하여 런타임 환경을 만들고 buildspec 파일에서 명령을 빌드하여 테스트 스크립트를 호출합니다. 오류가 발견되면 aws deploy stop-deployment 명령을 사용하여 배포를 중지합니다.
B. 소스와 배포 단계 사이에 CodePipeline 파이프라인에 단계를 추가합니다. 이 단계를 사용하여 테스트 스크립트를 실행하는 AWS Lambda 함수를 호출합니다. 오류가 발견되면 aws deploy stop-deployment 명령을 사용하여 배포를 중지합니다.
C. CodeDeploy AppSpec 파일에 hooks 섹션을 추가합니다. AfterAllowTestTraffic 라이프사이클 이벤트를 사용하여 AWS Lambda 함수를 호출하여 테스트 스크립트를 실행합니다. 오류가 발견되면 오류와 함께 Lambda 함수를 종료하여 롤백을 시작합니다. 가장 많이 투표된
D. CodeDeploy AppSpec 파일에 hooks 섹션을 추가합니다. AfterAllowTraffic 라이프사이클 이벤트를 사용하여 테스트 스크립트를 호출합니다. 오류가 발견되면 aws deploy stop-deployment CLI 명령을 사용하여 배포를 중지합니다.



### 질문 #35주제 1
한 회사가 여러 리소스에서 사용하는 Amazon S3 버킷 앞에서 파일 게이트웨이 모드로 AWS Storage Gateway를 사용합니다. 업무가 시작되는 아침에 사용자는 전날 저녁에 타사에서 처리한 객체를 볼 수 없습니다. DevOps 엔지니어가 S3 버킷을 직접 보면 데이터는 있지만 Storage Gateway에는 없습니다.
어떤 솔루션이 모든 업데이트된 타사 파일을 아침에 사용할 수 있도록 보장합니까?

A. Storage Gateway에 대한 RefreshCache 명령을 실행하기 위해 AWS Lambda 함수를 호출하도록 매일 밤 Amazon EventBridge 이벤트를 구성합니다. 가장 많이 투표된
B. AWS Transfer for SFTP를 사용하여 제3자에게 S3 버킷에 데이터를 넣도록 지시합니다.
C. 볼륨 게이트웨이 모드에서 실행되도록 Storage Gateway를 수정합니다.
D. S3 동일 지역 복제를 사용하여 S3 버킷에서 직접 변경한 모든 내용을 Storage Gateway에 복제합니다.



### 질문 #36주제 1
DevOps 엔지니어는 S3 크로스 리전 복제 기능을 사용하여 개인 버킷 정책이 있는 S3 버킷에 저장된 민감한 Amazon S3 객체를 백업해야 합니다. 객체를 다른 AWS 리전 및 계정의 대상 버킷에 복사해야 합니다.
이 복제를 활성화하려면 어떤 작업 조합을 수행해야 합니까? (세 가지를 선택하세요.)

A. 소스 계정에서 복제 IAM 역할 생성 가장 많이 투표된
B. 대상 계정에서 복제 I AM 역할을 생성합니다.
C. 소스 버킷 정책에 명령문을 추가하여 복제 IAM 역할이 개체를 복제할 수 있도록 허용합니다.
D. 복제 IAM 역할이 개체를 복제할 수 있도록 대상 버킷 정책에 명령문을 추가합니다. 가장 많이 투표된
E. 복제를 활성화하려면 소스 버킷에서 복제 규칙을 만듭니다. 가장 많이 투표된
F. 대상 버킷에서 복제 규칙을 생성하여 복제를 활성화합니다.



### 질문 #37주제 1
회사에 AWS Organizations의 조직에 속하는 여러 멤버 계정이 있습니다. 보안팀은 모든 Amazon EC2 보안 그룹과 해당 인바운드 및 아웃바운드 규칙을 검토해야 합니다. 보안팀은 조직의 관리 계정에서 AWS Lambda 함수를 사용하여 멤버 계정에서 이 정보를 프로그래밍 방식으로 검색하려고 합니다.
이러한 요구 사항을 충족하는 액세스 변경 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. 멤버 계정의 사용자가 관리 계정 IAM 역할을 맡을 수 있도록 하는 신뢰 관계를 만듭니다.
B. 관리 계정의 사용자가 멤버 계정의 IAM 역할을 맡을 수 있도록 하는 신뢰 관계를 만듭니다. 가장 많이 투표된
C. AmazonEC2ReadOnlyAccess 관리 정책에 액세스할 수 있는 각 멤버 계정에 IAM 역할을 생성합니다. 가장 많이 투표된
D. 각 구성원 계정에서 I AM 역할을 생성하여 관리 계정 IAM 역할의 ARN에 대해 sts:AssumeRole 작업을 허용합니다.
E. 멤버 계정 IAM 역할의 ARN에 대해 sts:AssumeRole 작업을 허용하는 관리 계정에서 I AM 역할을 생성합니다. 가장 많이 투표된
F. AmazonEC2ReadOnlyAccess 관리 정책에 액세스할 수 있는 관리 계정에서 IAM 역할을 생성합니다.



### 질문 #38주제 1
우주 탐사 회사가 여러 위성에서 원격 측정 데이터를 수신합니다. 소량의 데이터 패킷은 Amazon API Gateway를 통해 수신되어 Amazon Simple Queue Service(Amazon SQS) 표준 대기열에 직접 배치됩니다. 사용자 지정 애플리케이션이 대기열에 구독되어 데이터를 표준 형식으로 변환합니다.
위성에서 생성되는 데이터의 불일치로 인해 애플리케이션이 가끔 데이터를 변환할 수 없습니다. 이러한 경우 메시지는 SQS 대기열에 남아 있습니다. DevOps 엔지니어는 실패한 메시지를 보관하고 과학자가 검토하고 향후 처리할 수 있도록 제공하는 솔루션을 개발해야 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS Lambda를 구성하여 SQS 대기열을 폴링하고 Lambda 함수를 호출하여 대기열 메시지가 유효한지 확인합니다. 검증이 실패하면 유효하지 않은 데이터의 사본을 Amazon S3 버킷으로 보내 과학자가 데이터를 검토하고 수정할 수 있도록 합니다. 데이터가 수정되면 수정된 데이터로 재생 Lambda 함수를 사용하여 SQS 대기열의 메시지를 수정합니다.
B. SQS 표준 대기열을 SQS FIFO 대기열로 변환합니다. Amazon EventBridge 일정을 사용하여 10분마다 SQS 대기열을 폴링하도록 AWS Lambda를 구성합니다. Lambda 함수를 호출하여 5분보다 오래된 SentTimestamp 값이 있는 메시지를 식별하고, 데이터를 애플리케이션의 출력 위치와 동일한 위치로 푸시하고, 대기열에서 메시지를 제거합니다.
C. SQS 배달 못한 편지 대기열을 만듭니다. 최대 수신 설정을 1로 설정하고 배달 못한 편지 대기열 ARN을 새로 만든 대기열의 ARN으로 설정하는 재구동 정책을 포함하여 기존 대기열을 수정합니다. 과학자들에게 배달 못한 편지 대기열을 사용하여 유효하지 않은 데이터를 검토하도록 지시합니다. 나중에 이 데이터를 다시 처리합니다. 가장 많이 투표된
D. API Gateway를 구성하여 각 위성에 대해 명명된 다른 SQS 가상 대기열에 메시지를 보냅니다. 변환할 수 없는 모든 데이터에 대해 새 가상 대기열을 사용하도록 애플리케이션을 업데이트하고 메시지를 새 가상 대기열로 보냅니다. 과학자들에게 가상 대기열을 사용하여 유효하지 않은 데이터를 검토하도록 지시합니다. 나중에 이 데이터를 다시 처리합니다.



### 질문 #39주제 1
한 회사가 인프라 배포에 AWS CloudFormation을 사용하고자 합니다. 이 회사는 엄격한 태그 지정 및 리소스 요구 사항을 가지고 있으며 배포를 두 개의 지역으로 제한하고자 합니다. 개발자는 동일한 애플리케이션의 여러 버전을 배포해야 합니다.
어떤 솔루션이 회사 정책에 따라 리소스가 배포되도록 보장합니까?

A. AWS Trusted Advisor 검사를 생성하여 승인되지 않은 CloudFormation StackSets를 찾아 해결합니다.
B. 승인되지 않은 CloudFormation StackSets를 찾아 해결하기 위해 Cloud Formation 드리프트 감지 작업을 생성합니다.
C. 승인된 CloudFormation 템플릿을 사용하여 CloudFormation StackSets를 만듭니다.
D. 승인된 CloudFormation 템플릿을 사용하여 AWS 서비스 카탈로그 제품을 만듭니다. 가장 많이 투표된



### 질문 #40주제 1
어떤 회사에서는 내부적으로 마주하는 웹 애플리케이션이 고가용성을 요구합니다. 이 아키텍처는 Amazon EC2 웹 서버 인스턴스 하나와 업데이트 및 퍼블릭 데이터 액세스를 위한 아웃바운드 인터넷 액세스를 제공하는 NAT 인스턴스 하나로 구성됩니다.
이 회사는 고가용성을 달성하기 위해 어떤 아키텍처 조정 조합을 구현해야 합니까? (두 가지를 선택하세요.)

A. 여러 가용성 영역에 걸쳐 있는 EC2 자동 확장 그룹에 NAT 인스턴스를 추가합니다. 경로 테이블을 업데이트합니다.
B. 여러 가용성 영역에 걸쳐 추가 EC2 인스턴스를 만듭니다. 애플리케이션 로드 밸런서를 추가하여 로드를 이들 간에 분할합니다. 가장 많이 투표된
C. EC2 인스턴스 앞에 애플리케이션 로드 밸런서를 구성합니다. 호스트 장애 시 EC2 인스턴스를 복구하도록 Amazon CloudWatch 알람을 구성합니다.
D. 각 가용성 영역에서 NAT 인스턴스를 NAT 게이트웨이로 교체합니다. 경로 테이블을 업데이트합니다. 가장 많이 투표된
E. NAT 인스턴스를 여러 가용성 영역에 걸쳐 있는 NAT 게이트웨이로 교체합니다. 경로 테이블을 업데이트합니다.



### 질문 #41주제 1
DevOps 엔지니어가 AWS CodePipeline을 사용하여 애플리케이션을 빌드, 검증, 스테이징, 테스트 및 배포하기 위한 다단계 파이프라인을 구축하고 있습니다. 테스트 단계와 배포 단계 사이에 수동 승인 단계가 필요합니다. 개발팀은 거의 실시간 알림이 필요한 웹훅 지원이 있는 사용자 지정 채팅 도구를 사용합니다.
DevOps 엔지니어는 파이프라인 활동 및 채팅 도구에 게시할 승인 요청에 대한 상태 업데이트를 어떻게 구성해야 합니까?

A. CodePipeline 파이프라인 실행 상태 변경을 필터링하는 Amazon CloudWatch Logs 구독을 만듭니다. Amazon Simple Notification Service(Amazon SNS) 토픽에 구독 이벤트를 게시합니다. 채팅 웹훅 URL을 SNS 토픽에 구독하고 구독 검증을 완료합니다.
B. AWS CloudTrail 이벤트에서 호출되는 AWS Lambda 함수를 만듭니다. CodePipeline 파이프라인 실행 상태 변경 이벤트가 감지되면 이벤트 세부 정보를 채팅 웹훅 URL로 보냅니다.
C. CodePipeline 파이프라인 실행 상태 변경을 필터링하는 Amazon EventBridge 규칙을 만듭니다. Amazon Simple Notification Service(Amazon SNS) 토픽에 이벤트를 게시합니다. 채팅 웹훅 URL에 이벤트 세부 정보를 보내는 AWS Lambda 함수를 만듭니다. 함수를 SNS 토픽에 구독합니다. 가장 많이 투표된
D. 파이프라인 코드를 수정하여 각 단계의 끝에 이벤트 세부 정보를 채팅 웹훅 URL로 보냅니다. 각 파이프라인이 파이프라인 환경에 따라 다른 URL로 보낼 수 있도록 URL을 매개변수화합니다.



### 질문 #42주제 1
회사의 애플리케이션 개발팀은 Linux 기반 Amazon EC2 인스턴스를 베스천 호스트로 사용합니다. 베스천 호스트에 대한 인바운드 SSH 액세스는 연관된 보안 그룹에 정의된 대로 특정 IP 주소로 제한됩니다. 회사의 보안팀은 보안 그룹 규칙이 모든 IP 주소에서 SSH 액세스를 허용하도록 수정되면 알림을 받고 싶어합니다.
DevOps 엔지니어는 이 요구 사항을 충족하기 위해 무엇을 해야 합니까?

A. aws.cloudtrail 소스와 AuthorizeSecurityGroupIngress 이벤트 이름으로 Amazon EventBridge 규칙을 만듭니다. Amazon Simple Notification Service(Amazon SNS) 토픽을 대상으로 정의합니다.
B. Amazon GuardDuty를 활성화하고 AWS Security Hub에서 보안 그룹에 대한 결과를 확인합니다. NON_COMPLIANT 출력이 있는 GuardDuty 이벤트와 일치하는 사용자 지정 패턴으로 Amazon EventBridge 규칙을 구성합니다. Amazon Simple Notification Service(Amazon SNS) 토픽을 대상으로 정의합니다.
C. restricted-ssh 관리 규칙을 사용하여 AWS Config 규칙을 만들어 보안 그룹이 무제한 수신 SSH 트래픽을 허용하지 않는지 확인합니다. Amazon Simple Notification Service(Amazon SNS) 토픽에 메시지를 게시하도록 자동 수정을 구성합니다. 가장 많이 투표된
D. Amazon Inspector를 활성화합니다. Common Vulnerabilities and Exposures-1.1 규칙 패키지를 포함하여 배스천 호스트와 연관된 보안 그룹을 확인합니다. Amazon Inspector를 구성하여 Amazon Simple Notification Service(Amazon SNS) 토픽에 메시지를 게시합니다.



### 질문 #43주제 1
DevOps 팀은 Amazon API Gateway 엔드포인트의 백엔드 역할을 하는 온프레미스에서 실행되는 API를 관리합니다. 고객들은 높은 응답 지연에 대해 불평해 왔으며, 개발 팀은 Amazon CloudWatch의 API Gateway 지연 메트릭을 사용하여 이를 확인했습니다. 원인을 파악하기 위해 팀은 추가 지연을 발생시키지 않고 관련 데이터를 수집해야 합니다.
이를 달성하기 위해 어떤 조치를 취해야 합니까? (두 가지를 선택하세요.)

A. CloudWatch 에이전트 서버 측을 설치하고 에이전트가 관련 로그를 CloudWatch에 업로드하도록 구성합니다. 가장 많이 투표된
B. API Gateway에서 AWS X-Ray 추적을 활성화하고, 요청 세그먼트를 캡처하도록 애플리케이션을 수정하고, 각 요청 중에 해당 세그먼트를 X-Ray에 업로드합니다.
C. API Gateway에서 AWS X-Ray 추적을 활성화하고, 요청 세그먼트를 캡처하도록 애플리케이션을 수정하고, X-Ray 데몬을 사용하여 세그먼트를 X-Ray에 업로드합니다. 가장 많이 투표된
D. 온프레미스 애플리케이션을 수정하여 각 요청과 함께 로그 정보를 API Gateway로 다시 보냅니다.
E. 온프레미스 애플리케이션을 수정하여 API 서비스 요청과 관련된 통계 데이터를 계산하고 CloudWatch 메트릭에 업로드합니다.



### 질문 #44주제 1
한 회사에 MySQL 호환 Amazon Aurora Multi-AZ DB 클러스터를 데이터베이스로 사용하는 애플리케이션이 있습니다. 재해 복구 목적으로 지역 간 읽기 복제본이 생성되었습니다. DevOps 엔지니어는 복제본의 프로모션을 자동화하여 장애 발생 시 기본 데이터베이스 인스턴스가 되도록 하려고 합니다.
어떤 솔루션이 이를 달성할까요?

A. 상태 확인이 있는 대기 시간 기반 Amazon Route 53 CNAME을 구성하여 기본 및 복제본 엔드포인트를 모두 가리키도록 합니다. Amazon SNS 토픽을 AWS CloudTrail의 Amazon RDS 실패 알림에 구독하고 해당 토픽을 사용하여 복제본 인스턴스를 기본으로 승격하는 AWS Lambda 함수를 호출합니다.
B. 기본 데이터베이스 인스턴스를 가리키도록 Aurora 사용자 지정 엔드포인트를 만듭니다. 이 엔드포인트를 사용하도록 애플리케이션을 구성합니다. AWS CloudTrail을 구성하여 AWS Lambda 함수를 실행하여 복제본 인스턴스를 승격하고 사용자 지정 엔드포인트를 수정하여 새로 승격된 인스턴스를 가리키도록 합니다.
C. AWS Lambda 함수를 생성하여 애플리케이션의 AWS CloudFormation 템플릿을 수정하여 복제본을 승격하고, 템플릿을 적용하여 스택을 업데이트하고, 애플리케이션을 새로 승격된 인스턴스로 가리킵니다. 실패 이벤트가 발생한 후 이 Lambda 함수를 호출하기 위한 Amazon CloudWatch 알람을 생성합니다.
D. AWS Systems Manager Parameter Store에 Aurora 엔드포인트를 저장합니다. 데이터베이스 장애를 감지하고 AWS Lambda 함수를 실행하여 복제본 인스턴스를 홍보하고 AWS Systems Manager Parameter Store에 저장된 엔드포인트 URL을 업데이트하는 Amazon EventBridge 이벤트를 만듭니다. 데이터베이스 연결이 실패하면 Parameter Store에서 엔드포인트를 다시 로드하도록 애플리케이션을 코딩합니다. 가장 많이 투표된



### 질문 #45주제 1
한 회사가 Amazon EBS 스토리지로 백업된 Amazon EC2 인스턴스를 사용하여 스테이징 웹사이트를 호스팅합니다. 이 회사는 EC2 인스턴스에서 네트워크 연결 문제나 정전이 발생할 경우 최소한의 데이터 손실로 빠르게 복구하려고 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 최소, 최대 및 원하는 용량을 1로 설정하여 EC2 자동 확장 그룹에 인스턴스를 추가합니다.
B. EC2 인스턴스가 종료되거나 종료될 때 EBS 볼륨을 분리하기 위해 라이프사이클 후크를 사용하여 EC2 자동 확장 그룹에 인스턴스를 추가합니다.
C. StatusCheckFailed 시스템 메트릭에 대한 Amazon CloudWatch 알람을 생성하고 인스턴스를 복구하기 위한 EC2 작업을 선택합니다. 가장 많이 투표된
D. StatusCheckFailed 인스턴스 메트릭에 대한 Amazon CloudWatch 알람을 생성하고 EC2 작업을 선택하여 인스턴스를 재부팅합니다.



### 질문 #46주제 1
한 회사에서 AWS 개발 도구를 사용하여 현재 bash 배포 스크립트를 대체하려고 합니다. 이 회사는 현재 Application Load Balancer(ALB) 뒤에 있는 Amazon EC2 인스턴스 그룹에 LAMP 애플리케이션을 배포하고 있습니다. 배포 중에 회사는 커밋된 애플리케이션을 단위 테스트하고, 서비스를 중지하고 시작하고, 로드 밸런서에 인스턴스를 등록 취소하고 다시 등록하고, 파일 권한을 업데이트합니다. 이 회사는 AWS 서비스 사용으로 전환하는 동안 동일한 배포 기능을 유지하려고 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS CodeBuild를 사용하여 애플리케이션을 테스트합니다. AWS CodeDeploy의 appspec.yml 파일에서 호출한 bash 스크립트를 사용하여 서비스를 다시 시작하고 ALB에 인스턴스를 등록 해제하고 등록합니다. appspec.yml 파일을 사용하여 사용자 지정 스크립트 없이 파일 권한을 업데이트합니다.
B. AWS CodePipeline을 사용하여 AWS CodeCommit 리포지토리에서 AWS CodeDeploy로 애플리케이션을 이동합니다. CodeDeploy의 배포 그룹을 사용하여 애플리케이션을 테스트하고, AL로 인스턴스를 등록 해제하고 다시 등록하고, 서비스를 다시 시작합니다. appspec.yml 파일을 사용하여 사용자 지정 스크립트 없이 파일 권한을 업데이트합니다.
C. AWS CodePipeline을 사용하여 애플리케이션 소스 코드를 AWS CodeCommit 리포지토리에서 AWS CodeDeploy로 옮깁니다. CodeDeploy를 사용하여 애플리케이션을 테스트합니다. CodeDeploy의 appspec.yml 파일을 사용하여 서비스를 다시 시작하고 사용자 지정 스크립트 없이 권한을 업데이트합니다. AWS CodeBuild를 사용하여 ALB에서 인스턴스를 등록 취소하고 다시 등록합니다.
D. AWS CodePipeline을 사용하여 AWS CodeBuild를 트리거하여 애플리케이션을 테스트합니다. AWS CodeDeploy의 appspec.yml 파일에서 호출한 bash 스크립트를 사용하여 서비스를 다시 시작합니다. ALB에서 AWS CodeDeploy 배포 그룹의 인스턴스를 등록 해제했다가 다시 등록합니다. 사용자 지정 스크립트 없이 파일 권한을 업데이트하려면 appspec.yml 파일을 업데이트합니다. 가장 많이 투표된



### 질문 #47주제 1
한 회사가 Amazon EC2와 온프레미스 구성으로 애플리케이션을 실행합니다. DevOps 엔지니어는 두 환경에서 패치를 표준화해야 합니다. 회사 정책에 따르면 패치는 비업무 시간에만 실행해야 합니다.
이러한 요구 사항을 충족하는 작업 조합은 무엇입니까? (세 가지를 선택하세요.)

A. Systems Manager Hybrid Activations를 사용하여 물리적 머신을 AWS Systems Manager에 추가합니다. 가장 많이 투표된
B. EC2 인스턴스에 IAM 역할을 연결하여 AWS Systems Manager에서 관리할 수 있도록 합니다. 가장 많이 투표된
C. 온프레미스 머신이 AWS Systems Manager와 상호 작용할 수 있도록 IAM 액세스 키를 생성합니다.
D. AWS Systems Manager Automation 문서를 실행하여 매시간 시스템에 패치를 적용합니다.
E. Amazon EventBridge 예약된 이벤트를 사용하여 패치 창을 예약합니다.
F. AWS Systems Manager Maintenance Windows를 사용하여 패치 창을 예약합니다. 가장 많이 투표된



### 질문 #48주제 1
한 회사가 새 애플리케이션을 호스팅하기 위해 AWS를 선택했습니다. 이 회사는 다중 계정 전략을 구현해야 합니다. DevOps 엔지니어가 AWS Organizations에서 새 AWS 계정과 조직을 만듭니다. DevOps 엔지니어는 또한 조직의 OU 구조를 만들고 AWS Control Tower를 사용하여 랜딩 존을 설정합니다. DevOps
엔지니어는 사용자가 AWS Control Tower Account Factory를 통해 만든 새 계정에 대한 리소스를 자동으로 배포하는 솔루션을 구현해야 합니다. 사용자가 새 계정을 만들면 솔루션은 OU 또는 계정에 맞게 사용자 지정된 AWS CloudFormation 템플릿과 SCP를 적용하여 계정에 연결된 모든 리소스를 자동으로 배포해야 합니다. 모든 OU는 AWS Control Tower에 등록됩니다.
어떤 솔루션이 가장 자동화된 방식으로 이러한 요구 사항을 충족할까요?

A. AWS Control Tower와 함께 AWS Service Catalog를 사용합니다. AWS Service Catalog에서 포트폴리오와 제품을 만듭니다. 이러한 리소스를 프로비저닝하기 위한 세부적인 권한을 부여합니다. AWS CLI 및 JSON 문서를 사용하여 SCP를 배포합니다.
B. 필요한 템플릿을 사용하여 CloudFormation 스택 세트를 배포합니다. 자동 배포를 활성화합니다. 필요한 계정에 스택 인스턴스를 배포합니다. SCP를 배포하기 위해 조직의 관리 계정에 CloudFormation 스택 세트를 배포합니다.
C. CreateManagedAccount 이벤트를 감지하기 위한 Amazon EventBridge 규칙을 만듭니다. AWS Service Catalog를 대상으로 구성하여 모든 새 계정에 리소스를 배포합니다. AWS CLI 및 JSON 문서를 사용하여 SCP를 배포합니다.
D. AWS Control Tower(CfCT) 솔루션에 대한 사용자 지정을 배포합니다. AWS CodeCommit 리포지토리를 소스로 사용합니다. 리포지토리에서 CloudFormation 템플릿과 SCP JSON 문서를 포함하는 사용자 지정 패키지를 만듭니다. 가장 많이 투표된



### 질문 #49주제 1
미국에 본사를 둔 온라인 리테일 회사가 향후 6개월 내에 유럽과 아시아로 사업을 확장할 계획입니다. 해당 제품은 현재 Application Load Balancer 뒤의 Amazon EC2 인스턴스에서 실행됩니다. 인스턴스는 여러 가용성 영역에 걸쳐 Amazon EC2 Auto Scaling 그룹에서 실행됩니다. 모든 데이터는 Amazon Aurora 데이터베이스 인스턴스에 저장됩니다.
제품이 여러 지역에 배포되는 경우 회사는 모든 지역에 걸쳐 단일 제품 카탈로그를 원하지만 규정 준수를 위해 고객 정보와 구매 내역은 각 지역에 보관해야 합니다.
회사는 최소한의 애플리케이션 변경으로 이러한 요구 사항을 어떻게 충족해야 할까요?

A. 제품 카탈로그에는 Amazon Redshift를 사용하고 고객 정보와 구매 내역에는 Amazon DynamoDB 테이블을 사용합니다.
B. 제품 카탈로그에는 Amazon DynamoDB 글로벌 테이블을 사용하고 고객 정보와 구매에는 지역 테이블을 사용합니다.
C. 제품 카탈로그에 대한 읽기 복제본과 각 지역의 추가 로컬 Aurora 인스턴스를 사용하여 고객 정보와 구매를 관리합니다. 가장 많이 투표된
D. 제품 카탈로그에는 Aurora를 사용하고 고객 정보와 구매 내역에는 Amazon DynamoDB 글로벌 테이블을 사용합니다.




### 질문 #50주제 1
한 회사가 전 세계적으로 접근 가능한 API 스택에 잘 설계된 디자인을 구현하고 있습니다. 이 디자인은 북미와 유럽에 있는 사용자에게 높은 신뢰성과 빠른 응답 시간을 모두 보장해야 합니다.
API 스택에는 다음 세 가지 계층이 있습니다.

Amazon API Gateway -

AWS Lambda -

Amazon DynamoDB -
어떤 솔루션이 요구 사항을 충족할까요?

A. Amazon Route 53을 구성하여 건강 검사를 사용하여 북미와 유럽의 API Gateway API를 가리킵니다. 해당 지역의 Lambda 함수에 요청을 전달하도록 API를 구성합니다. Lambda 함수와 동일한 지역의 DynamoDB 테이블에서 데이터를 검색하고 업데이트하도록 Lambda 함수를 구성합니다.
B. 지연 기반 라우팅 및 상태 확인을 사용하여 북미 및 유럽의 API Gateway API를 가리키도록 Amazon Route 53을 구성합니다. 해당 지역의 Lambda 함수로 요청을 전달하도록 API를 구성합니다. DynamoDB 글로벌 테이블에서 데이터를 검색하고 업데이트하도록 Lambda 함수를 구성합니다. 가장 많이 투표된
C. Amazon Route 53을 북미의 API Gateway를 가리키도록 구성하고, 유럽에서 재해 복구 API를 만들고, 두 API를 모두 해당 지역의 Lambda 함수로 요청을 전달하도록 구성합니다. DynamoDB 글로벌 테이블에서 데이터를 검색합니다. Lambda 함수를 배포하여 5분마다 북미 API 상태를 확인합니다. 장애가 발생하면 Route 53을 업데이트하여 재해 복구 API를 가리킵니다.
D. 지연 기반 라우팅을 사용하여 북미의 API Gateway API를 가리키도록 Amazon Route 53을 구성합니다. API를 구성하여 사용자에게 가장 가까운 지역의 Lambda 함수로 요청을 전달합니다. Lambda 함수를 구성하여 DynamoDB 테이블의 데이터를 검색하고 업데이트합니다.



### 질문 #51주제 1
빠르게 성장하는 회사가 AWS 개발 환경에 대한 개발자 수요에 맞춰 확장하고자 합니다. 개발 환경은 AWS Management Console에서 수동으로 생성됩니다. 네트워킹 팀은 AWS CloudFormation을 사용하여 네트워킹 인프라를 관리하고 Amazon VPC 및 모든 서브넷에 대한 스택 출력 값을 내보냅니다. 개발 환경에는 애플리케이션 로드 밸런서, Amazon EC2 자동 확장 그룹, 보안 그룹, Amazon DynamoDB 테이블과 같은 공통 표준이 있습니다.
수요에 부응하기 위해 DevOps 엔지니어는 개발 환경 생성을 자동화하고자 합니다. 애플리케이션을 지원하는 데 필요한 인프라가 증가할 것으로 예상되므로 배포된 인프라를 쉽게 업데이트할 수 있는 방법이 있어야 합니다. CloudFormation을 사용하여 개발 환경의 템플릿을 생성합니다.
이러한 요구 사항을 충족하고 개발자에게 일관된 AWS 환경을 빠르게 제공할 수 있는 접근 방식은 무엇입니까?

A. 템플릿의 리소스 섹션에서 Fn::ImportValue 내장 함수를 사용하여 Virtual Private Cloud(VPC) 및 서브넷 값을 검색합니다. 개발 환경에 CloudFormation StackSets를 사용하고 Count 입력 매개변수를 사용하여 필요한 환경 수를 나타냅니다. UpdateStackSet 명령을 사용하여 기존 개발 환경을 업데이트합니다.
B. 중첩 스택을 사용하여 공통 인프라 구성 요소를 정의합니다. 내보낸 값에 액세스하려면 TemplateURL을 사용하여 네트워킹 팀의 템플릿을 참조합니다. Virtual Private Cloud(VPC) 및 서브넷 값을 검색하려면 루트 템플릿의 Parameters 섹션에서 Fn::ImportValue 내장 함수를 사용합니다. CreateChangeSet 및 ExecuteChangeSet 명령을 사용하여 기존 개발 환경을 업데이트합니다.
C. 중첩된 스택을 사용하여 공통 인프라 구성 요소를 정의합니다. 중첩된 스택의 리소스와 함께 Fn::ImportValue 내장 함수를 사용하여 Virtual Private Cloud(VPC) 및 서브넷 값을 검색합니다. CreateChangeSet 및 ExecuteChangeSet 명령을 사용하여 기존 개발 환경을 업데이트합니다. 가장 많이 투표된
D. 루트 템플릿의 Parameters 섹션에서 Fn::ImportValue 내장 함수를 사용하여 Virtual Private Cloud(VPC) 및 서브넷 값을 검색합니다. CloudFormation 중첩 스택에서 생성해야 하는 순서대로 개발 리소스를 정의합니다. CreateChangeSet 및 ExecuteChangeSet 명령을 사용하여 기존 개발 환경을 업데이트합니다.



### 질문 #52주제 1
한 회사가 AWS Organizations를 사용하여 여러 계정을 관리합니다. 정보 보안 정책에 따라 암호화되지 않은 모든 Amazon EBS 볼륨은 비준수로 표시해야 합니다. DevOps 엔지니어는 솔루션을 자동으로 배포하고 이 규정 준수 검사가 항상 존재하도록 해야 합니다.
어떤 솔루션이 이를 달성할까요?

A. EBS 암호화가 활성화되어 있는지 확인하기 위한 AWS Inspector 규칙을 정의하는 AWS CloudFormation 템플릿을 만듭니다. 회사 내 모든 계정과 공유된 Amazon S3 버킷에 템플릿을 저장합니다. Amazon S3의 CloudFormation 템플릿을 가리키는 계정 생성 스크립트를 업데이트합니다.
B. EBS 암호화가 활성화되어 있는지 확인하기 위한 AWS Config 조직 규칙을 만들고 AWS CLI를 사용하여 규칙을 배포합니다. 조직 전체에서 AWS Config를 중지하고 삭제하는 것을 금지하기 위한 SCP를 만들고 적용합니다. 가장 많이 투표된
C. Organizations에서 SCP를 만듭니다. 조건식을 사용하여 EBS 볼륨에서 암호화 없이 Amazon EC2 인스턴스를 시작하지 못하도록 정책을 설정합니다. 모든 AWS 계정에 SCP를 적용합니다. Amazon Athena를 사용하여 AWS CloudTrail 출력을 분석하여 ec2:RunInstances 작업을 거부하는 이벤트를 찾습니다.
D. 단일 신뢰할 수 있는 계정에서 모든 계정에 IAM 역할을 배포합니다. AWS Lambda에서 IAM 역할을 맡을 스테이지가 있는 AWS CodePipeline으로 파이프라인을 빌드하고 계정의 모든 EBS 볼륨을 나열합니다. Amazon S3에 보고서를 게시합니다.



### 질문 #53주제 1
한 회사가 여러 계정에서 모든 Amazon EC2 인스턴스에 대한 취약성 스캐닝을 수행하고 있습니다. 계정은 AWS Organizations의 조직에 있습니다. 각 계정의 VPC는 ​​공유 전송 게이트웨이에 연결되어 있습니다. VPC는 ​​중앙 이그레스 VPC를 통해 인터넷으로 트래픽을 전송합니다. 이 회사는 위임된 관리자 계정에서 Amazon Inspector를 활성화하고 모든 멤버 계정에 대한 스캐닝을 활성화했습니다.
DevOps 엔지니어는 일부 EC2 인스턴스가 Amazon Inspector의 "스캐닝 안 함" 탭에 나열되어 있음을 발견했습니다.
DevOps 엔지니어는 이 문제를 해결하기 위해 어떤 작업 조합을 취해야 합니까? (세 가지를 선택하세요.)

A. Amazon Inspector가 스캔하지 않는 EC2 인스턴스에 AWS Systems Manager Agent가 설치되어 실행 중인지 확인합니다. 가장 많이 투표된
B. AWS Systems Manager 서비스 엔드포인트로의 포트 443에서 아웃바운드 통신을 허용하는 보안 그룹과 대상 EC2 인스턴스를 연결합니다. 가장 많이 투표된
C. DevOps 엔지니어가 사용하는 IAM 역할에 inspector:StartAssessmentRun 권한을 부여합니다.
D. Amazon Inspector가 스캔하지 않는 EC2 인스턴스에 대해 EC2 Instance Connect를 구성합니다.
E. AWS Systems Manager와 통신할 수 있는 권한을 부여하는 인스턴스 프로필과 대상 EC2 인스턴스를 연결합니다. 가장 많이 투표된
F. 관리형 인스턴스 활성화를 만듭니다. 활성화 코드와 활성화 ID를 사용하여 EC2 인스턴스를 등록합니다.



### 질문 #54주제 1
개발팀은 애플리케이션의 버전 제어를 위해 AWS CodeCommit을 사용합니다. 개발팀은 CI/CD 인프라를 위해 AWS CodePipeline, AWS CodeBuild, AWS CodeDeploy를 사용합니다. CodeCommit에서 개발팀은 최근 코드베이스에서 장기 실행 테스트를 통과하지 못한 풀 리퀘스트를 병합했습니다. 개발팀은 코드베이스의 브랜치로 롤백을 수행해야 했고, 그 결과 시간과 노력이 낭비되었습니다.
DevOps 엔지니어는 CodeCommit에서 풀 리퀘스트 테스트를 자동화하여 검토자가 풀 리퀘스트 검토의 일부로 자동화된 테스트의 결과를 더 쉽게 볼 수 있도록 해야 합니다.
DevOps 엔지니어는 이 요구 사항을 충족하기 위해 무엇을 해야 합니까?

A. pullRequestStatusChanged 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. 애플리케이션에 대한 테스트를 실행하는 CodeBuild 작업이 있는 CodePipeline 파이프라인을 호출하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 프로그래밍하여 CodeBuild 배지를 풀 요청에 대한 댓글로 게시하여 개발자가 코드 검토에서 배지를 볼 수 있도록 합니다.
B. pullRequestCreated 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. 애플리케이션에 대한 테스트를 실행하는 CodeBuild 작업으로 CodePipeline 파이프라인을 호출하는 AWS Lambda 함수를 만듭니다. 테스트 결과가 완료되면 CodeBuild 테스트 결과를 pull 요청에 주석으로 게시하도록 Lambda 함수를 프로그래밍합니다.
C. pullRequestCreated 및 pullRequestSourceBranchUpdated 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. 애플리케이션에 대한 테스트를 실행하는 CodeBuild 작업이 있는 CodePipeline 파이프라인을 호출하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 프로그래밍하여 CodeBuild 배지를 풀 요청에 대한 댓글로 게시하여 개발자가 코드 검토에서 배지를 볼 수 있도록 합니다. 가장 많이 투표된
D. pullRequestStatusChanged 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. 애플리케이션에 대한 테스트를 실행하는 CodeBuild 작업이 있는 CodePipeline 파이프라인을 호출하는 AWS Lambda 함수를 만듭니다. 테스트 결과가 완료되면 CodeBuild 테스트 결과를 pull 요청에 주석으로 게시하도록 Lambda 함수를 프로그래밍합니다.



### 질문 #55주제 1
한 회사가 단일 AWS 계정의 프로덕션 VPC에 애플리케이션을 배포했습니다. 이 애플리케이션은 인기가 많고 사용량이 많습니다. 이 회사의 보안 팀은 AWS WAF와 같은 추가 보안을 애플리케이션 배포에 추가하려고 합니다. 그러나 애플리케이션의 제품 관리자는 비용에 대해 우려하고 보안 팀이 추가 보안이 필요하다는 것을 증명하지 않는 한 변경을 승인하고 싶어하지 않습니다.
보안 팀은 일부 애플리케이션 요구 사항이 거부 목록에 있는 IP 주소를 가진 사용자로부터 발생할 수 있다고 생각합니다. 보안 팀은 DevOps 엔지니어에게 거부 목록을 제공합니다. 거부 목록에 있는 IP 주소가 애플리케이션에 액세스하는 경우 보안 팀은 애플리케이션에 추가 보안이 필요하다는 것을 문서화할 수 있도록 거의 실시간으로 자동화된 알림을 받고 싶어합니다. DevOps 엔지니어는 프로덕션 VPC에 대한 VPC 흐름 로그를 만듭니다.
DevOps 엔지니어는 이러한 요구 사항을 가장 비용 효율적으로 충족하기 위해 어떤 추가 단계를 수행해야 합니까?

A. Amazon CloudWatch Logs에서 로그 그룹을 만듭니다. 허용된 트래픽을 캡처하고 로그 그룹으로 데이터를 전송하도록 VPC 흐름 로그를 구성합니다. 거부 목록에 있는 IP 주소에 대한 Amazon CloudWatch 메트릭 필터를 만듭니다. 메트릭 필터를 입력으로 사용하여 CloudWatch 알람을 만듭니다. 기간을 5분으로 설정하고 알람에 대한 데이터 포인트를 1로 설정합니다. Amazon Simple Notification Service(Amazon SNS) 토픽을 사용하여 보안 팀에 알람 알림을 보냅니다. 가장 많이 투표된
B. 로그 파일을 위한 Amazon S3 버킷을 만듭니다. 모든 트래픽을 캡처하고 데이터를 S3 버킷으로 보내도록 VPC 흐름 로그를 구성합니다. 거부 목록에 있는 IP 주소에 대해 S3 버킷의 모든 로그 파일을 반환하도록 Amazon Athena를 구성합니다. Athena에서 데이터를 수락하고 보안 팀이 액세스할 수 있는 대시보드로 데이터를 게시하도록 Amazon QuickSight를 구성합니다. 성공적인 액세스에 대한 임계값 경고 1을 만듭니다. 경고 임계값에 도달하면 가능한 한 자주 보안 팀에 자동으로 알리도록 경고를 구성합니다.
C. 로그 파일을 위한 Amazon S3 버킷을 만듭니다. 허용된 트래픽을 캡처하고 데이터를 S3 버킷으로 보내도록 VPC 흐름 로그를 구성합니다. 로그 파일을 위한 Amazon OpenSearch Service 클러스터와 도메인을 구성합니다. S3 버킷에서 로그를 검색하고, 로그를 포맷하고, 로그를 OpenSearch Service 클러스터에 로드하는 AWS Lambda 함수를 만듭니다. Lambda 함수가 5분마다 실행되도록 예약합니다. 거부 목록에 있는 IP 주소에서 액세스가 감지되면 Amazon Simple Notification Service(Amazon SNS) 주제를 통해 보안 팀에 알림을 보내도록 OpenSearch Service에서 알림과 조건을 구성합니다.
D. Amazon CloudWatch Logs에서 로그 그룹을 만듭니다. 쿼리 결과를 보관할 Amazon S3 버킷을 만듭니다. 모든 트래픽을 캡처하고 로그 그룹으로 데이터를 보내도록 VPC 흐름 로그를 구성합니다. AWS Lambda에서 Amazon Athena CloudWatch 커넥터를 배포합니다. 커넥터를 로그 그룹에 연결합니다. 거부 목록에 있는 IP 주소에서 허용된 모든 트래픽을 주기적으로 쿼리하고 결과를 S3 버킷에 저장하도록 Athena를 구성합니다. S3 버킷에 새 객체가 추가되면 Amazon Simple Notification Service(Amazon SNS) 주제를 통해 보안 팀에 자동으로 알리도록 S3 이벤트 알림을 구성합니다.



### 질문 #56주제 1
DevOps 엔지니어는 다음 단계에 따라 AWS CodePipeline을 사용하여 웹 서비스 배포를 자동화했습니다.
1. AWS CodeBuild 프로젝트는 배포 아티팩트를 컴파일하고 단위 테스트를 실행합니다.
2. AWS CodeDeploy 배포 그룹은 스테이징 환경의 Amazon EC2 인스턴스에 웹 서비스를 배포합니다.
3. CodeDeploy 배포 그룹은 프로덕션 환경의 EC2 인스턴스에 웹 서비스를 배포합니다.
품질 보증(QA) 팀은 프로덕션 환경에 배포하기 전에 빌드 아티팩트를 검사할 수 있는 권한을 요청합니다. QA 팀은 수동 테스트를 수행하기 위해 내부 침투 테스트 도구를 실행하려고 합니다. 이 도구는 REST API 호출에 의해 호출됩니다.
DevOps 엔지니어는 이 요청을 이행하기 위해 어떤 작업 조합을 취해야 합니까? (두 가지를 선택하세요.)

A. 파이프라인의 테스트 작업과 배포 작업 사이에 수동 승인 작업을 삽입합니다. 가장 많이 투표된
B. 컴파일 단계에 대한 buildspec.yml 파일을 수정하여 완료 전에 수동 승인이 필요하도록 합니다.
C. CodeDeploy 배포 그룹을 업데이트하여 진행에 수동 승인이 필요하도록 설정합니다.
D. 침투 테스트 도구에 대한 REST API를 직접 호출하도록 파이프라인을 업데이트합니다.
E. 침투 테스트 도구에 대한 REST API를 호출하는 AWS Lambda 함수를 호출하도록 파이프라인을 업데이트합니다. 가장 많이 투표된



### 질문 #57주제 1
한 회사가 AWS 리전에서 웹 애플리케이션을 호스팅하고 있습니다. 재해 복구 목적으로 두 번째 리전이 대기 리전으로 사용되고 있습니다. 재해 복구 요구 사항에 따르면 세션 데이터는 거의 실시간으로 리전 간에 복제되어야 하며 요청의 1%는 시스템 기능을 지속적으로 확인하기 위해 보조 리전으로 라우팅되어야 합니다. 또한 주 리전에서 서비스가 중단되면 트래픽은 자동으로 보조 리전으로 라우팅되어야 하며 보조 리전은 모든 트래픽을 처리할 수 있도록 확장할 수 있어야 합니다.
DevOps 엔지니어는 이러한 요구 사항을 어떻게 충족해야 합니까?

A. 두 지역 모두 AWS Elastic Beanstalk에 애플리케이션을 배포하고 세션 데이터에 Amazon DynamoDB 글로벌 테이블을 사용합니다. 건강 검진이 포함된 Amazon Route 53 가중 라우팅 정책을 사용하여 트래픽을 여러 지역에 분산합니다. 가장 많이 투표된
B. 두 지역 모두에서 Auto Scaling 그룹에서 애플리케이션을 시작하고 세션 데이터에 DynamoDB를 사용합니다. Route 53 장애 조치 라우팅 정책을 사용하여 상태 검사를 통해 트래픽을 지역 전체에 분산합니다.
C. 두 지역에서 모두 Amazon API Gateway에서 노출된 AWS Lambda에 애플리케이션을 배포하고, 세션 데이터에 대해 교차 지역 복제를 사용하여 Amazon RDS for PostgreSQL을 사용합니다. 클라이언트 측 로직을 사용하여 API Gateway를 직접 호출하는 웹 애플리케이션을 배포합니다.
D. 두 지역 모두에서 Auto Scaling 그룹에서 애플리케이션을 시작하고 세션 데이터에 DynamoDB 글로벌 테이블을 사용합니다. 지역 간에 Amazon CloudFront 가중 분포를 활성화합니다. Amazon Route 53 DNS 레코드를 CloudFront 분포로 지정합니다.



### 질문 #58주제 1
한 회사가 Amazon EC2 인스턴스에서 애플리케이션을 실행합니다. 이 회사는 일련의 AWS CloudFormation 스택을 사용하여 애플리케이션 리소스를 정의합니다. 개발자는 랩톱에서 애플리케이션을 빌드하고 테스트한 다음 빌드 출력과 CloudFormation 스택 템플릿을 Amazon S3에 업로드하여 업데이트를 수행합니다. 개발자의 동료는 개발자가 CloudFormation 스택 업데이트를 수행하고 EC2 인스턴스에 애플리케이션의 새 버전을 설치하기 전에 변경 사항을 검토합니다.
배포 프로세스는 오류가 발생하기 쉽고 개발자가 각 EC2 인스턴스를 새 애플리케이션으로 업데이트할 때 시간이 많이 걸립니다. 이 회사는 애플리케이션이나 리소스를 수정하기 전에 최종 수동 승인 단계를 유지하면서 가능한 한 많은 애플리케이션 배포 프로세스를 자동화하려고 합니다.
이 회사는 이미 애플리케이션과 CloudFormation 템플릿의 소스 코드를 AWS CodeCommit으로 옮겼습니다. 이 회사는 또한 애플리케이션을 빌드하고 테스트하기 위한 AWS CodeBuild 프로젝트를 만들었습니다.
어떤 단계 조합이 회사의 요구 사항을 충족할까요? (두 가지를 선택하세요.)

A. AWS CodeDeploy에서 애플리케이션 그룹과 배포 그룹을 만듭니다. EC2 인스턴스에 CodeDeploy 에이전트를 설치합니다. 가장 많이 투표된
B. AWS CodeDeploy에서 애플리케이션 개정판과 배포 그룹을 만듭니다. CodeDeploy에서 환경을 만듭니다. EC2 인스턴스를 CodeDeploy 환경에 등록합니다.
C. AWS CodePipeline을 사용하여 CodeBuild 작업을 호출하고, CloudFormation 업데이트를 실행하고, 수동 승인 단계를 위해 일시 ​​중지합니다. 승인 후 AWS CodeDeploy 배포를 시작합니다.
D. AWS CodePipeline을 사용하여 CodeBuild 작업을 호출하고, 각 애플리케이션 스택에 대한 CloudFormation 변경 세트를 만들고, 수동 승인 단계를 위해 일시 ​​중지합니다. 승인 후 CloudFormation 변경 세트를 실행하고 AWS CodeDeploy 배포를 시작합니다. 가장 많이 투표된
E. AWS CodePipeline을 사용하여 CodeBuild 작업을 호출하고, 각 애플리케이션 스택에 대한 CloudFormation 변경 세트를 만들고, 수동 승인 단계를 위해 일시 ​​중지합니다. 승인 후 AWS CodeDeploy 배포를 시작합니다.



### 질문 #59주제 1
DevOps 엔지니어는 Application Load Balancer(ALB) 뒤의 Amazon EC2 인스턴스에서 실행되는 웹 애플리케이션을 관리합니다. 인스턴스는 여러 가용성 영역에 걸쳐 EC2 자동 확장 그룹에서 실행됩니다. 엔지니어는 다음과 같은 배포 전략을 구현해야 합니다.
원래 플릿과 동일한 용량의 두 번째 인스턴스 플릿을 시작합니다.
두 번째 플릿이 시작되는 동안 원래 플릿을 변경하지 않고 유지합니다. 두 번째
플릿이 완전히 배포되면 트래픽을 두 번째 플릿으로 전환합니다.
전환 후 1시간 후에 원래 플릿을 자동으로 종료합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. ALB에 대한 보존 정책이 1시간으로 설정된 AWS CloudFormation 템플릿을 사용합니다. Amazon Route 53 레코드를 업데이트하여 새 ALB를 반영합니다.
B. 두 개의 AWS Elastic Beanstalk 환경을 사용하여 원래 환경에서 새 환경으로 블루/그린 배포를 수행합니다. 1시간 내에 원래 환경을 종료하는 애플리케이션 버전 수명 주기 정책을 만듭니다.
C. 블루/그린 배포 구성으로 구성된 배포 그룹과 함께 AWS CodeDeploy를 사용합니다. 1시간의 대기 기간으로 배포 그룹의 원래 인스턴스를 종료합니다 옵션을 선택합니다. 가장 많이 투표된
D. 구성을 Immutable로 설정한 AWS Elastic Beanstalk를 사용합니다. ALB의 삭제 정책을 1시간으로 설정하는 Resources 키를 사용하여 .ebextension을 만들고 애플리케이션을 배포합니다.



### 질문 #60주제 1
비디오 공유 회사가 Amazon S3에 비디오를 저장합니다. 이 회사는 비디오 액세스 요청이 갑자기 증가하는 것을 관찰했지만, 어떤 비디오가 가장 인기 있는지 알지 못합니다. 이 회사는 비디오 파일에 대한 일반적인 액세스 패턴을 파악해야 합니다. 이 패턴에는 특정 날짜에 특정 파일에 액세스하는 사용자 수와 특정 파일에 대한 풀 요청 수가 포함됩니다.
이 회사는 어떻게 하면 최소한의 노력으로 이러한 요구 사항을 충족할 수 있을까요?

A. S3 서버 액세스 로깅을 활성화합니다. 액세스 로그를 Amazon Aurora 데이터베이스로 가져옵니다. Aurora SQL 쿼리를 사용하여 액세스 패턴을 분석합니다.
B. S3 서버 액세스 로깅을 활성화합니다. Amazon Athena를 사용하여 로그 파일이 있는 외부 테이블을 만듭니다. Athena를 사용하여 액세스 패턴을 분석하는 SQL 쿼리를 만듭니다. 가장 많이 투표된
C. 모든 S3 객체 액세스 이벤트에 대해 AWS Lambda 함수를 호출합니다. Lambda 함수를 구성하여 사용자, S3 버킷, 파일 키와 같은 파일 액세스 정보를 Amazon Aurora 데이터베이스에 씁니다. Aurora SQL 쿼리를 사용하여 액세스 패턴을 분석합니다.
D. 모든 S3 객체 액세스 이벤트에 대해 Amazon CloudWatch Logs 로그 메시지를 기록합니다. 사용자, S3 버킷, 파일 키와 같은 파일 액세스 정보를 Amazon Kinesis Data Analytics for SQL 애플리케이션에 쓰도록 CloudWatch Logs 로그 스트림을 구성합니다. 슬라이딩 윈도우 분석을 수행합니다.



### 질문 #61주제 1
개발팀은 AWS CloudFormation 스택을 사용하여 애플리케이션을 배포하려고 합니다. 그러나 개발자 IAM 역할에는 AWS CloudFormation 템플릿에 지정된 리소스를 프로비저닝하는 데 필요한 권한이 없습니다. DevOps 엔지니어는 개발자가 스택을 배포할 수 있는 솔루션을 구현해야 합니다. 솔루션은 최소 권한의 원칙을 따라야 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 개발자가 필요한 리소스를 프로비저닝할 수 있는 IAM 정책을 만듭니다. 정책을 개발자 IAM 역할에 연결합니다.
B. AWS CloudFormation에 대한 전체 액세스를 허용하는 IAM 정책을 만듭니다. 정책을 개발자 IAM 역할에 연결합니다.
C. 필요한 권한이 있는 AWS CloudFormation 서비스 역할을 만듭니다. 개발자 IAM 역할에 cloudformation:* 작업을 부여합니다. 스택 배포 중에 새 서비스 역할을 사용합니다.
D. 필요한 권한이 있는 AWS CloudFormation 서비스 역할을 만듭니다. 개발자 IAM 역할에 iam:PassRole 권한을 부여합니다. 스택 배포 중에 새 서비스 역할을 사용합니다. 가장 많이 투표된



### 질문 #62주제 1
프로덕션 계정에는 수동으로 로그인한 모든 Amazon EC2 인스턴스가 24시간 이내에 종료되어야 한다는 요구 사항이 있습니다. 프로덕션 계정의 모든 애플리케이션은 Amazon CloudWatch Logs 에이전트가 구성된 Auto Scaling 그룹을 사용합니다.
이 프로세스는 어떻게 자동화할 수 있습니까?

A. AWS Step Functions 애플리케이션에 CloudWatch Logs 구독을 만듭니다. AWS Lambda 함수를 구성하여 로그인 이벤트를 생성한 EC2 인스턴스에 태그를 추가하고 인스턴스를 폐기하도록 표시합니다. Amazon EventBridge 규칙을 만들어 하루에 한 번 두 번째 Lambda 함수를 호출하여 이 태그가 있는 모든 인스턴스를 종료합니다.
B. 로그인 이벤트에 의해 호출되는 Amazon CloudWatch 알람을 만듭니다. 운영팀이 구독한 Amazon Simple Notification Service(Amazon SNS) 토픽에 알림을 보내고 24시간 이내에 EC2 인스턴스를 종료하도록 합니다.
C. 로그인 이벤트에 의해 호출되는 Amazon CloudWatch 알람을 만듭니다. Amazon Simple Queue Service(Amazon SQS) 대기열로 보내도록 알람을 구성합니다. 작업자 인스턴스 그룹을 사용하여 대기열의 메시지를 처리한 다음 Amazon EventBridge 규칙이 호출되도록 예약합니다.
D. AWS Lambda 함수에 대한 CloudWatch Logs 구독을 만듭니다. 로그인 이벤트를 생성한 EC2 인스턴스에 태그를 추가하고 인스턴스를 폐기하도록 표시하도록 함수를 구성합니다. 이 태그가 있는 모든 인스턴스를 종료하는 매일 Lambda 함수를 호출하는 Amazon EventBridge 규칙을 만듭니다. 가장 많이 투표된



### 질문 #63주제 1
한 회사가 AWS Organizations에서 조직의 모든 기능을 활성화했습니다. 조직에는 10개의 AWS 계정이 있습니다. 회사는 모든 계정에서 AWS CloudTrail을 켰습니다. 회사는 내년에 조직의 AWS 계정 수가 500개로 늘어날 것으로 예상합니다. 회사는 이러한 계정에 여러 OU를 사용할 계획입니다.
회사는 조직의 각 기존 AWS 계정에서 AWS Config를 활성화했습니다. DevOps 엔지니어는 조직에서 생성되는 모든 향후 AWS 계정에 대해 AWS Config를 자동으로 활성화하는 솔루션을 구현해야 합니다.
어떤 솔루션이 이 요구 사항을 충족할까요?

A. 조직의 관리 계정에서 CreateAccount API 호출에 반응하는 Amazon EventBridge 규칙을 만듭니다. 조직에 대한 AWS Config에 대한 신뢰할 수 있는 액세스를 가능하게 하는 AWS Lambda 함수를 호출하도록 규칙을 구성합니다.
B. 조직의 관리 계정에서 AWS Config를 활성화하기 위한 AWS CloudFormation 스택 세트를 만듭니다. Organizations를 통해 계정이 생성되면 스택 세트가 자동으로 배포되도록 구성합니다. 가장 많이 투표된
C. 조직의 관리 계정에서 적절한 AWS Config API 호출을 허용하여 AWS Config를 활성화하는 SCP를 만듭니다. SCP를 루트 수준 OU에 적용합니다.
D. 조직의 관리 계정에서 CreateAccount API 호출에 반응하는 Amazon EventBridge 규칙을 만듭니다. AWS Systems Manager Automation 런북을 호출하여 계정에 대한 AWS Config를 활성화하도록 규칙을 구성합니다.



### 질문 #64주제 1
회사에는 여러 애플리케이션이 있습니다. 회사의 여러 팀이 여러 언어와 프레임워크를 사용하여 애플리케이션을 개발했습니다. 애플리케이션은 온프레미스와 다른 운영 체제가 있는 다른 서버에서 실행됩니다. 각 팀은 자체 릴리스 프로토콜과 프로세스를 가지고 있습니다. 회사는 이러한 애플리케이션의 릴리스 및 유지 관리의 복잡성을 줄이고자 합니다.
회사는 이러한 애플리케이션을 포함한 기술 스택을 AWS로 마이그레이션하고 있습니다. 회사는 소스 코드의 중앙 제어, 일관되고 자동화된 제공 파이프라인, 기본 인프라에서 가능한 한 적은 유지 관리 작업을 원합니다.
DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 무엇을 해야 합니까?

A. 모든 애플리케이션에 대해 하나의 AWS CodeCommit 리포지토리를 만듭니다. 각 애플리케이션의 코드를 다른 브랜치에 넣습니다. 브랜치를 병합하고 AWS CodeBuild를 사용하여 애플리케이션을 빌드합니다. AWS CodeDeploy를 사용하여 애플리케이션을 하나의 중앙화된 애플리케이션 서버에 배포합니다.
B. 각 애플리케이션에 대해 AWS CodeCommit 리포지토리를 하나씩 만듭니다. AWS CodeBuild를 사용하여 한 번에 하나씩 애플리케이션을 빌드합니다. AWS CodeDeploy를 사용하여 애플리케이션을 하나의 중앙화된 애플리케이션 서버에 배포합니다.
C. 각 애플리케이션에 대해 AWS CodeCommit 리포지토리를 하나씩 만듭니다. AWS CodeBuild를 사용하여 한 번에 하나씩 애플리케이션을 빌드하고 각 서버에 대해 하나의 AMI를 만듭니다. AWS CloudFormation StackSets를 사용하여 이러한 AMI를 사용하여 Amazon EC2 플릿을 자동으로 프로비저닝하고 폐기합니다.
D. 각 애플리케이션에 대해 AWS CodeCommit 리포지토리를 하나씩 만듭니다. AWS CodeBuild를 사용하여 Amazon Elastic Container Registry(Amazon ECR)의 각 애플리케이션에 대해 Docker 이미지를 하나씩 빌드합니다. AWS CodeDeploy를 사용하여 AWS Fargate가 관리하는 인프라에서 Amazon Elastic Container Service(Amazon ECS)에 애플리케이션을 배포합니다. 가장 많이 투표된



### 질문 #65주제 1
회사의 애플리케이션은 현재 단일 AWS 지역에 배포되어 있습니다. 최근 이 회사는 다른 대륙에 새로운 사무실을 열었습니다. 새로운 사무실의 사용자는 높은 지연 시간을 경험하고 있습니다. 이 회사의 애플리케이션은 Application Load Balancer(ALB) 뒤의 Amazon EC2 인스턴스에서 실행되고 Amazon DynamoDB를 데이터베이스 계층으로 사용합니다. 인스턴스는 여러 가용성 영역에 걸쳐 EC2 자동 확장 그룹에서 실행됩니다. DevOps 엔지니어는 애플리케이션 응답 시간을 최소화하고 두 지역의 사용자 가용성을 개선하는 업무를 맡고 있습니다.
지연 시간 문제를 해결하기 위해 어떤 조치 조합을 취해야 합니까? (세 가지를 선택하세요.)

A. 지역 간 복제가 활성화된 새 지역에 새 DynamoDB 테이블을 만듭니다.
B. 새로운 ALB 및 자동 크기 조정 그룹 글로벌 리소스를 만들고 새 ALB가 트래픽을 새 자동 크기 조정 그룹으로 전달하도록 구성합니다.
C. 새 지역에 새 ALB 및 자동 크기 조정 그룹 리소스를 만들고 새 ALB가 새 자동 크기 조정 그룹으로 트래픽을 전달하도록 구성합니다. 가장 많이 투표된
D. Amazon Route 53 레코드, 상태 확인 및 지연 기반 라우팅 정책을 생성하여 ALB로 라우팅합니다. 가장 많이 투표된
E. Amazon Route 53 별칭, 상태 검사 및 장애 조치 라우팅 정책을 생성하여 ALB로 라우팅합니다.
F. DynamoDB 테이블을 글로벌 테이블로 변환합니다. 가장 많이 투표된



### 질문 #66주제 1
DevOps 엔지니어는 기존 AWS 계정 세트에 핵심 보안 제어 세트를 적용해야 합니다. 계정은 AWS Organizations의 조직에 있습니다. 개별 팀은 AdministratorAccess AWS 관리 정책을 사용하여 개별 계정을 관리합니다. 모든 계정에 대해. AWS CloudTrail 및 AWS Config는 사용 가능한 모든 AWS 지역에서 켜져 있어야 합니다. 개별 계정 관리자는 기준 리소스를 편집하거나 삭제할 수 없어야 합니다. 그러나 개별 계정 관리자는 자신의 CloudTrail 트레일 및 AWS Config 규칙을 편집하거나 삭제할 수 있어야 합니다.
어떤 솔루션이 가장 운영 효율적인 방식으로 이러한 요구 사항을 충족할까요?

A. 표준 계정 리소스를 정의하는 AWS CloudFormation 템플릿을 만듭니다. CloudFormation StackSets를 사용하여 조직의 관리 계정에서 모든 계정에 템플릿을 배포합니다. 스택 정책을 설정하여 Update:Delete 작업을 거부합니다.
B. AWS Control Tower를 활성화합니다. AWS Control Tower에 기존 계정을 등록합니다. 개별 계정 관리자에게 CloudTrail 및 AWS Config에 대한 액세스 권한을 부여합니다.
C. AWS Config 관리 계정을 지정합니다. AWS CloudFormation StackSets를 사용하여 모든 계정에서 AWS Config 레코더를 만듭니다. AWS Config 관리 계정을 사용하여 조직에 AWS Config 규칙을 배포합니다. 조직의 관리 계정에서 CloudTrail 조직 트레일을 만듭니다. SCP를 사용하여 AWS Config 레코더의 수정 또는 삭제를 거부합니다. 가장 많이 투표된
D. 표준 계정 리소스를 정의하는 AWS CloudFormation 템플릿을 만듭니다. Cloud Formation StackSets를 사용하여 조직의 관리 계정에서 모든 계정에 템플릿을 배포합니다. 주체가 조직의 관리 계정의 관리자가 아닌 한 CloudTrail 리소스 또는 AWS Config 리소스에 대한 업데이트 또는 삭제를 방지하는 SCP를 만듭니다.



### 질문 #67주제 1
한 회사가 AWS Organizations의 조직에 AWS 계정을 가지고 있습니다. AWS Config는 각 AWS 계정에서 수동으로 구성됩니다. 회사는 조직의 모든 계정에 대해 AWS Config를 중앙에서 구성하는 솔루션을 구현해야 합니다. 솔루션은 또한 중앙 계정에 대한 리소스 변경 사항을 기록해야 합니다.
DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 어떤 작업 조합을 수행해야 합니까? (두 가지를 선택하십시오.)

A. AWS Config에 대한 위임된 관리자 계정을 구성합니다. 조직에서 AWS Config에 대한 신뢰할 수 있는 액세스를 활성화합니다. 가장 많이 투표된
B. AWS Config에 대한 위임된 관리자 계정을 구성합니다. 조직의 관리 계정에서 AWS Config에 대한 서비스 연결 역할을 만듭니다.
C. AWS Config 애그리게이터를 생성하기 위해 AWS CloudFormation 템플릿을 만듭니다. 조직의 모든 계정에 템플릿을 배포하도록 CloudFormation 스택 세트를 구성합니다.
D. 조직의 관리 계정에서 AWS Config 조직 집계기를 만듭니다. 조직의 모든 AWS 계정과 모든 AWS 리전에서 데이터 수집을 구성합니다.
E. 위임된 관리자 계정에서 AWS Config 조직 집계기를 만듭니다. 조직의 모든 AWS 계정과 모든 AWS 리전에서 데이터 수집을 구성합니다. 가장 많이 투표된



### 질문 #68주제 1
한 회사가 Amazon EC2에 호스팅된 콘텐츠 공유 웹 애플리케이션을 서버리스 아키텍처로 마이그레이션하려고 합니다. 이 회사는 현재 EC2 인스턴스의 새로운 Auto Scaling 그룹과 새로운 Elastic Load Balancer를 생성한 다음 Amazon Route 53 가중치 라우팅 정책을 사용하여 트래픽을 이동하여 애플리케이션에 변경 사항을 배포하고 있습니다.
이 회사는 새로운 서버리스 애플리케이션의 경우 Amazon API Gateway와 AWS Lambda를 사용할 계획입니다. 이 회사는 새로운 애플리케이션에서 작동하도록 배포 프로세스를 업데이트해야 합니다. 또한 전체 사용자 기반에 기능을 출시하기 전에 소수의 사용자에게 새로운 기능을 테스트할 수 있는 기능을 유지해야 합니다.
어떤 배포 전략이 이러한 요구 사항을 충족할까요?

A. AWS CDK를 사용하여 API Gateway 및 Lambda 함수를 배포합니다. 코드를 변경해야 하는 경우 AWS CloudFormation 스택을 업데이트하고 새 버전의 API 및 Lambda 함수를 배포합니다. Canary 릴리스 전략에 Route 53 장애 조치 라우팅 정책을 사용합니다.
B. AWS CloudFormation을 사용하여 Lambda 함수 버전을 사용하여 API Gateway 및 Lambda 함수를 배포합니다. 코드를 변경해야 하는 경우 CloudFormation 스택을 새 Lambda 코드로 업데이트하고 Canary 릴리스 전략을 사용하여 API 버전을 업데이트합니다. 테스트가 완료되면 새 버전을 홍보합니다. 가장 많이 투표된
C. AWS Elastic Beanstalk를 사용하여 API Gateway 및 Lambda 함수를 배포합니다. 코드를 변경해야 하는 경우 API 및 Lambda 함수의 새 버전을 배포합니다. Elastic Beanstalk 블루/그린 배포를 사용하여 트래픽을 점진적으로 이동합니다.
D. AWS OpsWorks를 사용하여 서비스 계층에 API Gateway를 배포하고 사용자 지정 계층에 Lambda 함수를 배포합니다. 코드를 변경해야 하는 경우 OpsWorks를 사용하여 블루/그린 배포를 수행하고 트래픽을 점진적으로 이동합니다.



### 질문 #69주제 1
개발팀은 AWS CodeCommit, AWS CodePipeline, AWS CodeBuild를 사용하여 애플리케이션을 개발하고 배포합니다. 코드 변경 사항은 풀 리퀘스트를 통해 제출됩니다. 개발팀은 풀 리퀘스트를 검토하고 병합한 다음 파이프라인에서 애플리케이션을 빌드하고 테스트합니다.
시간이 지남에 따라 풀 리퀘스트 수가 증가했습니다. 파이프라인은 테스트 실패로 인해 자주 차단됩니다. 이러한 차단을 방지하기 위해 개발팀은 풀 리퀘스트가 병합되기 전에 각 풀 리퀘스트에서 단위 및 통합 테스트를 실행하려고 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 단위 및 통합 테스트를 실행하기 위한 CodeBuild 프로젝트를 만듭니다. CodeCommit 승인 규칙 템플릿을 만듭니다. CodeBuild 프로젝트의 성공적인 호출을 요구하도록 템플릿을 구성합니다. 프로젝트의 CodeCommit 리포지토리에 승인 규칙을 첨부합니다.
B. CodeCommit에서 pullRequestCreated 이벤트를 일치시키는 Amazon EventBridge 규칙을 만듭니다. 단위 및 통합 테스트를 실행하기 위해 CodeBuild 프로젝트를 만듭니다. CodeBuild 프로젝트를 이벤트의 CodeCommit 저장소 및 분기 정보가 있는 사용자 지정 이벤트 페이로드를 포함하는 EventBridge 규칙의 대상으로 구성합니다. 가장 많이 투표된
C. CodeCommit에서 pullRequestCreated 이벤트를 일치시키는 Amazon EventBridge 규칙을 만듭니다. 빌드가 풀 요청에서 시작되는 경우 배포 단계를 실행하지 않도록 기존 CodePipeline 파이프라인을 수정합니다. 이벤트에서 CodeCommit 리포지토리와 분기 정보를 포함하는 사용자 지정 페이로드로 파이프라인을 실행하도록 EventBridge 규칙을 구성합니다.
D. 단위 및 통합 테스트를 실행하기 위한 CodeBuild 프로젝트를 만듭니다. 풀 리퀘스트가 생성되거나 업데이트될 때 일치하는 CodeCommit 알림 규칙을 만듭니다. CodeBuild 프로젝트를 호출하도록 알림 규칙을 구성합니다.



### 질문 #70주제 1
한 회사에 Amazon EC2 인스턴스 플릿에서 실행되는 애플리케이션이 있습니다. 이 애플리케이션은 자주 재시작해야 합니다. 재시작이 필요할 때 애플리케이션 로그에 오류 메시지가 포함됩니다. 애플리케이션 로그는 Amazon CloudWatch Logs의 로그 그룹에 게시됩니다.
Amazon CloudWatch 알람은 로그에 재시작 관련 오류 메시지가 많이 포함된 경우 Amazon Simple Notification Service(Amazon SNS) 토픽을 통해 애플리케이션 엔지니어에게 알립니다. 애플리케이션 엔지니어는 SNS 토픽에서 알림을 받은 후 인스턴스에서 애플리케이션을 수동으로 재시작합니다.
DevOps 엔지니어는 인스턴스를 재시작하지 않고 인스턴스에서 애플리케이션 재시작을 자동화하는 솔루션을 구현해야 합니다.
어떤 솔루션이 이러한 요구 사항을 가장 운영 효율적인 방식으로 충족할까요?

A. 인스턴스에서 애플리케이션을 다시 시작하는 스크립트를 실행하는 AWS Systems Manager Automation 런북을 구성합니다. 런북을 호출하도록 SNS 토픽을 구성합니다.
B. 인스턴스에서 애플리케이션을 다시 시작하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 SNS 토픽의 이벤트 대상으로 구성합니다.
C. 인스턴스에서 애플리케이션을 다시 시작하는 스크립트를 실행하는 AWS Systems Manager Automation 런북을 구성합니다. 런북을 호출하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 SNS 토픽의 이벤트 대상으로 구성합니다.
D. 인스턴스에서 애플리케이션을 다시 시작하는 스크립트를 실행하는 AWS Systems Manager Automation 런북을 구성합니다. CloudWatch 알람이 ALARM 상태로 전환될 때 반응하는 Amazon EventBridge 규칙을 구성합니다. 규칙의 대상으로 런북을 지정합니다. 가장 많이 투표된



### 질문 #71주제 1
한 회사의 DevOps 엔지니어가 모든 사용자가 AWS IAM Identity Center(AWS Single Sign-On)를 사용하는 AWS 환경을 지원하고 있습니다. 이 회사는 모든 새 IAM 사용자의 자격 증명을 즉시 비활성화하고 보안 팀에 알림을 보내고 싶어합니다.
DevOps 엔지니어가 이러한 요구 사항을 충족하기 위해 취해야 할 단계의 조합은 무엇입니까? (세 가지를 선택하세요.)

A. AWS CloudTrail에서 IAM CreateUser API 호출에 반응하는 Amazon EventBridge 규칙을 생성합니다. 가장 많이 투표된
B. AWS CloudTrail에서 IAM GetLoginProfile API 호출에 반응하는 Amazon EventBridge 규칙을 만듭니다.
C. EventBridge 규칙의 대상인 AWS Lambda 함수를 만듭니다. Lambda 함수를 구성하여 모든 액세스 키를 비활성화하고 IAM 사용자와 연결된 로그인 프로필을 삭제합니다. 가장 많이 투표된
D. EventBridge 규칙의 대상인 AWS Lambda 함수를 만듭니다. IAM 사용자와 연결된 로그인 프로필을 삭제하도록 Lambda 함수를 구성합니다.
E. EventBridge 규칙의 대상인 Amazon Simple Notification Service(Amazon SNS) 토픽을 만듭니다. 보안 팀의 그룹 이메일 주소를 토픽에 구독합니다. 가장 많이 투표된
F. Lambda 함수의 대상인 Amazon Simple Queue Service(Amazon SQS) 대기열을 만듭니다. 보안 팀의 그룹 이메일 주소를 대기열에 구독합니다.



### 질문 #72주제 1
어떤 회사가 지속적인 배포 파이프라인을 설정하려고 합니다. 이 회사는 애플리케이션 코드를 비공개 GitHub 저장소에 저장합니다. 이 회사는 애플리케이션 구성 요소를 Amazon Elastic Container Service(Amazon ECS), Amazon EC2, AWS Lambda에 배포해야 합니다. 파이프라인은 수동 승인 작업을 지원해야 합니다.
어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Amazon ECS와 함께 AWS CodePipeline을 사용합니다. Amazon EC2, Lambda를 배포 공급자로 사용합니다.
B. AWS CodeDeploy를 배포 공급자로 사용하여 AWS CodePipeline을 사용합니다. 가장 많이 투표된
C. AWS Elastic Beanstalk를 배포 공급자로 사용하여 AWS CodePipeline을 사용합니다.
D. GitHub와 통합된 AWS CodeDeploy를 사용하여 애플리케이션을 배포합니다.



### 질문 #73주제 1
한 회사에는 Auto Scaling 그룹에 있는 Amazon EC2 인스턴스에서 실행되는 애플리케이션이 있습니다. 애플리케이션이 시작되면 애플리케이션은 요청을 처리하기 시작하기 전에 Amazon S3 버킷에서 데이터를 처리해야 합니다.
S3 버킷에 저장된 데이터의 크기가 커지고 있습니다. Auto Scaling 그룹이 새 인스턴스를 추가하면 이제 애플리케이션이 요청을 처리하기 전에 데이터를 다운로드하고 처리하는 데 몇 분이 걸립니다. 회사는 새 EC2 인스턴스가 요청을 처리할 준비가 되기까지 걸리는 시간을 줄여야 합니다. 애플리케이션
시작 시간을 줄이는 가장 비용 효율적인 방법은 무엇입니까?

A. Stopped 상태의 워밍된 EC2 인스턴스가 있는 Auto Scaling 그룹에 대한 워밍 풀을 구성합니다. Auto Scaling 그룹에서 autoscaling:EC2_INSTANCE_LAUNCHING 라이프사이클 후크를 구성합니다. 애플리케이션이 요청을 처리할 준비가 되면 라이프사이클 후크를 완료하도록 애플리케이션을 수정합니다. 가장 많이 투표된
B. 자동 확장 그룹의 최대 인스턴스 수를 늘립니다. 자동 확장 그룹에서 자동 확장:EC2_INSTANCE_LAUNCHING 라이프사이클 후크를 구성합니다. 애플리케이션이 요청을 처리할 준비가 되면 라이프사이클 후크를 완료하도록 애플리케이션을 수정합니다.
C. Running 상태의 워밍된 EC2 인스턴스가 있는 Auto Scaling 그룹에 대한 워밍 풀을 구성합니다. Auto Scaling 그룹에서 autoscaling:EC2_INSTANCE_LAUNCHING 라이프사이클 후크를 구성합니다. 애플리케이션이 요청을 처리할 준비가 되면 라이프사이클 후크를 완료하도록 애플리케이션을 수정합니다.
D. 자동 확장 그룹의 최대 인스턴스 수를 늘립니다. 자동 확장 그룹에서 자동 확장:EC2_INSTANCE_LAUNCHING 수명 주기 후크를 구성합니다. 애플리케이션을 수정하여 수명 주기 후크를 완료하고 애플리케이션이 요청을 처리할 준비가 되면 새 인스턴스를 대기 상태로 전환합니다.



### 질문 #74주제 1
한 회사에서 AWS CodeBuild 프로젝트를 사용하여 애플리케이션을 빌드하고 패키징하고 있습니다. 패키지는 여러 AWS 계정에 배포되기 전에 공유 Amazon S3 버킷에 복사됩니다.
buildspec.yml 파일에는 다음이 포함되어 있습니다.
```yaml
version: 0.2
phases:
    build:
        commands:
            - go build -o myapp
        post_build:
            commands:
            - aws s3 cp --acl authenticated-read myapp s3:artifacts/
```  
DevOps 엔지니어는 AWS 계정이 있는 사람은 누구나 아티팩트를 다운로드할 수 있다는 것을 알아챘습니다.
DevOps 엔지니어는 이를 막기 위해 어떤 조치를 취해야 합니까?

A. post_build 명령을 수정하여 --acl public-read를 사용하고 관련 AWS 계정에만 읽기 액세스 권한을 부여하는 버킷 정책을 구성합니다.
B. S3 버킷에 대한 기본 ACL을 구성하여 인증된 사용자 집합을 관련 AWS 계정으로만 정의하고 읽기 전용 액세스 권한을 부여합니다.
C. 관련 AWS 계정에 대한 읽기 액세스 권한을 부여하고 주체 "*"에 대한 읽기 액세스 권한을 거부하는 S3 버킷 정책을 만듭니다.
D. post_build 명령을 수정하여 --acl authenticated-read를 제거하고 관련 AWS 계정에만 읽기 액세스를 허용하는 버킷 정책을 구성합니다. 가장 많이 투표된



### 질문 #75주제 1
한 회사가 AWS에서 호스팅되는 서버리스 웹 애플리케이션을 개발했습니다. 이 애플리케이션은 Amazon S3, Amazon API Gateway, 여러 AWS Lambda 함수, Amazon RDS for MySQL 데이터베이스로 구성되어 있습니다. 이 회사는 AWS CodeCommit을 사용하여 소스 코드를 저장합니다. 소스 코드는 AWS Serverless Application Model(AWS SAM) 템플릿과 Python 코드의 조합입니다.
보안 감사 및 침투 테스트 결과, 데이터베이스 인증을 위한 사용자 이름과 비밀번호가 CodeCommit 저장소에 하드코딩되어 있음이 밝혀졌습니다. DevOps 엔지니어는 하드코딩된 비밀을 자동으로 감지하고 방지하는 솔루션을 구현해야 합니다.
이러한 요구 사항을 충족하는 가장 안전한 솔루션은 무엇입니까?

A. Amazon CodeGuru Profiler를 활성화합니다. @with_lambda_profiler()로 핸들러 함수를 장식합니다. 권장 사항 보고서를 수동으로 검토합니다. AWS Systems Manager Parameter Store에 보안 문자열로 비밀을 씁니다. SAM 템플릿과 Python 코드를 업데이트하여 Parameter Store에서 비밀을 가져옵니다.
B. CodeCommit 리포지토리를 Amazon CodeGuru Reviewer와 연결합니다. 수동으로 코드 검토를 확인하여 권장 사항을 확인합니다. 비밀을 보호하는 옵션을 선택합니다. SAM 템플릿과 Python 코드를 업데이트하여 AWS Secrets Manager에서 비밀을 가져옵니다. 가장 많이 투표된
C. Amazon CodeGuru Profiler를 활성화합니다. @with_lambda_profiler()로 핸들러 함수를 장식합니다. 권장 사항 보고서를 수동으로 검토합니다. 비밀을 보호하는 옵션을 선택합니다. SAM 템플릿과 Python 코드를 업데이트하여 AWS Secrets Manager에서 비밀을 가져옵니다.
D. CodeCommit 리포지토리를 Amazon CodeGuru Reviewer와 연결합니다. 수동으로 코드 검토를 확인하여 권장 사항을 확인합니다. AWS Systems Manager Parameter Store에 문자열로 비밀을 씁니다. SAM 템플릿과 Python 코드를 업데이트하여 Parameter Store에서 비밀을 가져옵니다.



### 질문 #76주제 1
한 회사가 Amazon S3 버킷을 사용하여 중요한 문서를 저장하고 있습니다. 이 회사는 일부 S3 버킷이 암호화되지 않았다는 것을 알게 되었습니다. 현재 이 회사의 IAM 사용자는 암호화 없이 새 S3 버킷을 만들 수 있습니다. 이 회사는 모든 S3 버킷을 암호화해야 한다는 새로운 요구 사항을 구현하고 있습니다.

DevOps 엔지니어는 모든 기존 S3 버킷과 모든 새 S3 버킷에서 서버 측 암호화가 활성화되도록 하는 솔루션을 구현해야 합니다. S3 버킷이 생성되는 즉시 새 S3 버킷에서 암호화를 활성화해야 합니다. 기본 암호화 유형은 256비트 고급 암호화 표준(AES-256)이어야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Amazon EventBridge 예약 규칙에 의해 주기적으로 호출되는 AWS Lambda 함수를 만듭니다. Lambda 함수를 프로그래밍하여 모든 현재 S3 버킷의 암호화 상태를 스캔하고 암호화 구성이 없는 모든 S3 버킷에 대해 AES-256을 기본 암호화로 설정합니다.
B. s3-bucket-server-side-encryption-enabled AWS Config 관리 규칙을 설정하고 활성화합니다. AWS-EnableS3BucketEncryption AWS Systems Manager Automation 런북을 수정 작업으로 사용하도록 규칙을 구성합니다. 기존 S3 버킷이 규정을 준수하는지 확인하기 위해 재평가 프로세스를 수동으로 실행합니다. 가장 많이 투표된
C. Amazon EventBridge 이벤트 규칙에 의해 호출되는 AWS Lambda 함수를 만듭니다. 새 S3 버킷 생성과 일치하는 이벤트 패턴으로 규칙을 정의합니다. Lambda 함수를 프로그래밍하여 EventBridge 이벤트를 구문 분석하고, 이벤트에서 S3 버킷의 구성을 확인하고, 기본 암호화로 AES-256을 설정합니다.
D. s3:x-amz-server-side-encryption 조건 키에 AES-256이 아닌 값이 있는 경우 s3:CreateBucket 작업을 거부하는 IAM 정책을 구성합니다. 회사의 모든 IAM 사용자에 대한 IAM 그룹을 만듭니다. IAM 정책을 IAM 그룹과 연결합니다.



### 질문 #77주제 1
DevOps 엔지니어는 AWS에서 실행되는 회사의 SaaS(Software as a Service) 웹 애플리케이션에 대한 지속적인 개발 전략을 설계하고 있습니다. 애플리케이션 및 보안상의 이유로 이 애플리케이션을 구독하는 사용자는 여러 애플리케이션 로드 밸런서(ALB)에 분산되어 있으며, 각각에는 전용 자동 확장 그룹과 Amazon EC2 인스턴스 플릿이 있습니다. 애플리케이션에는 빌드 단계가 필요하지 않으며, AWS CodeCommit에 커밋되면 애플리케이션은 모든 ALB, 자동 확장 그룹 및 EC2 플릿에 대한 동시 배포를 트리거해야 합니다.

어떤 아키텍처가 최소한의 구성으로 이러한 요구 사항을 충족할까요?

A. 각 ALB-Auto Scaling 그룹 쌍에 대해 생성된 고유한 AWS CodeDeploy 애플리케이션과 배포 그룹을 사용하여 애플리케이션을 병렬로 배포하는 단일 AWS CodePipeline 파이프라인을 생성합니다.
B. 단일 AWS CodeDeploy 애플리케이션과 단일 배포 그룹을 사용하여 애플리케이션을 배포하는 단일 AWS CodePipeline 파이프라인을 생성합니다.
C. 단일 AWS CodeDeploy 애플리케이션과 각 ALB-Auto Scaling 그룹 쌍에 대한 고유한 배포 그룹을 사용하여 애플리케이션을 병렬로 배포하는 단일 AWS CodePipeline 파이프라인을 생성합니다. 가장 많이 투표된
D. 동일한 ALB-Auto Scaling 그룹 쌍에 대해 생성된 AWS CodeDeploy 애플리케이션과 배포 그룹을 사용하여 애플리케이션을 배포하는 각 ALB-Auto Scaling 그룹 쌍에 대해 AWS CodePipeline 파이프라인을 생성합니다.



### 질문 #78주제 1
한 회사가 Amazon S3 버킷에서 정적 웹사이트를 호스팅하고 있습니다. 이 웹사이트는 example.com에서 고객에게 제공됩니다. 이 회사는 TTL이 1일인 Amazon Route 53 가중치 라우팅 정책을 사용합니다. 이 회사는 기존 정적 웹사이트를 동적 웹 애플리케이션으로 바꾸기로 결정했습니다. 동적 웹 애플리케이션은 Amazon EC2 인스턴스 플릿 앞에 있는 Application Load Balancer(ALB)를 사용합니다.

고객에게 프로덕션을 출시하는 날, 이 회사는 가중치가 255이고 TTL이 1시간인 ALB를 가리키는 추가 Route 53 가중치 DNS 레코드 항목을 만듭니다. 이틀 후, DevOps 엔지니어는 고객이 example.com으로 이동할 때 이전 정적 웹사이트가 가끔 표시된다는 것을 알아챘습니다. DevOps 엔지니어는

회사가 example.com에 대한 동적 콘텐츠만 제공하도록 어떻게 할 수 있을까요?

A. 정적 웹사이트 콘텐츠가 들어 있는 S3 버킷에서 이전 버전을 포함한 모든 객체를 삭제합니다.
B. S3 버킷을 가리키는 가중 DNS 레코드 항목을 업데이트합니다. 가중치 0을 적용합니다. 변경 사항을 즉시 전파하기 위해 도메인 재설정 옵션을 지정합니다.
C. ALB로 리디렉션하는 호스트 이름으로 S3 버킷에서 웹 페이지 리디렉션 요청을 구성합니다.
D. example.com 호스팅 영역에서 S3 버킷을 가리키는 가중 DNS 레코드 항목을 제거합니다. DNS 전파가 완료될 때까지 기다립니다. 가장 많이 투표된



### 질문 #79주제 1
한 회사가 테스트 프로세스를 자동화하기 위해 AWS CodePipeline을 구현하고 있습니다. 이 회사는 실행 상태가 실패할 때 알림을 받고 싶어하며 Amazon EventBridge에서 다음과 같은 사용자 지정 이벤트 패턴을 사용했습니다.

```json
{
    "source":[
        "aws.codepipeline"
    ],
    "detail-type":[
        "CodePipeline Action Execution State Change"
    ],
    "detail":{
        "state":["FAILED"],
        "type":{
            "category":["Approval"]
        }
    }
}
```


어떤 유형의 이벤트가 이 이벤트 패턴과 일치할까요?

A. 모든 파이프라인에서 배포 및 빌드 작업이 실패했습니다.
B. 모든 파이프라인에서 거부되거나 실패한 모든 승인 작업
C. 모든 파이프라인의 모든 이벤트
D. 모든 파이프라인에 대한 승인 작업



### 질문 #80주제 1
Auto Scaling 그룹의 Amazon EC2 인스턴스 집합에서 실행되는 애플리케이션은 작동하기 위해 구성 파일이 필요합니다. 인스턴스는 AWS CloudFormation으로 생성 및 유지 관리됩니다. DevOps 엔지니어는 인스턴스가 시작될 때 최신 구성 파일을 갖기를 원하며, CloudFormation 템플릿이 업데이트될 때 구성 파일의 변경 사항이 최소한의 지연으로 모든 인스턴스에 반영되기를 원합니다. 회사 정책에 따라 애플리케이션 구성 파일은 소스 제어에서 AWS 인프라 구성 파일과 함께 유지 관리되어야 합니다.

어떤 솔루션이 이를 달성할까요?

A. CloudFormation 템플릿에서 AWS Config 규칙을 추가합니다. 구성 파일 내용을 규칙의 InputParameters 속성에 넣고 Scope 속성을 EC2 Auto Scaling 그룹으로 설정합니다. AWS Systems Manager Resource Data Sync 리소스를 템플릿에 추가하여 구성 업데이트를 폴링합니다.
B. CloudFormation 템플릿에서 EC2 시작 템플릿 리소스를 추가합니다. 구성 파일 내용을 시작 템플릿에 넣습니다. 인스턴스가 시작될 때 실행되도록 cfn-init 스크립트를 구성하고 구성에 대한 업데이트를 폴링하도록 cfn-hup 스크립트를 구성합니다.
C. CloudFormation 템플릿에서 EC2 시작 템플릿 리소스를 추가합니다. 구성 파일 콘텐츠를 시작 템플릿에 넣습니다. AWS Systems Manager Resource Data Sync 리소스를 템플릿에 추가하여 구성 업데이트를 폴링합니다.
D. CloudFormation 템플릿에서 CloudFormation init 메타데이터를 추가합니다. 구성 파일 내용을 메타데이터에 넣습니다. 인스턴스가 시작될 때 실행되도록 cfn-init 스크립트를 구성하고 구성에 대한 업데이트를 폴링하도록 cfn-hup 스크립트를 구성합니다. 가장 많이 투표된



### 질문 #81주제 1
한 회사가 Amazon CloudWatch Logs에 로그를 저장하는 애플리케이션을 관리합니다. 이 회사는 로그를 Amazon S3 버킷에 보관하려고 합니다. 로그는 90일 후에 거의 액세스되지 않으며 10년 동안 보관해야 합니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 어떤 단계 조합을 취해야 합니까? (두 가지를 선택하세요.)

A. AWS Glue를 사용하여 모든 로그를 S3 버킷으로 전송하도록 CloudWatch Logs 구독 필터를 구성합니다.
B. Amazon Kinesis Data Firehose를 사용하여 모든 로그를 S3 버킷으로 스트리밍하도록 CloudWatch Logs 구독 필터를 구성합니다. 가장 많이 투표된
C. CloudWatch Logs 구독 필터를 구성하여 모든 로그를 S3 버킷으로 스트리밍합니다.
D. 90일 후에 S3 Glacier로 로그를 전환하고 3,650일 후에 로그를 만료하도록 S3 버킷 수명 주기 정책을 구성합니다. 가장 많이 투표된
E. 90일 후에 로그를 감소된 중복성으로 전환하고 3,650일 후에 로그를 만료하도록 S3 버킷 수명 주기 정책을 구성합니다.



### 질문 #82주제 1
회사에서 새로운 애플리케이션을 개발하고 있습니다. 이 애플리케이션은 컴퓨팅 계층에 AWS Lambda 함수를 사용합니다. 이 회사는 Lambda 함수의 모든 변경 사항에 카나리아 배포를 사용해야 합니다. 오류가 보고되면 자동 롤백이 발생해야 합니다.

이 회사의 DevOps 팀은 이 솔루션에 대한 코드로서의 인프라(IaC)와 CI/CD 파이프라인을 만들어야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (세 가지를 선택하세요.)

A. 애플리케이션에 대한 AWS CloudFormation 템플릿을 만듭니다. AWS::Lambda::Function 리소스 유형을 사용하여 템플릿에서 각 Lambda 함수를 정의합니다. 템플릿에서 AWS::Lambda::Version 리소스 유형을 사용하여 Lambda 함수의 버전을 포함합니다. CodeSha256 속성을 선언합니다. Lambda 함수의 최신 버전을 참조하는 AWS::Lambda::Alias ​​리소스를 구성합니다.
B. 애플리케이션에 대한 AWS Serverless Application Model(AWS SAM) 템플릿을 만듭니다. AWS::Serverless::Function 리소스 유형을 사용하여 템플릿에서 각 Lambda 함수를 정의합니다. 각 함수에 대해 AutoPublishAlias ​​속성과 DeploymentPreference 속성에 대한 구성을 포함합니다. 배포 구성 유형을 LambdaCanary10Percent10Minutes로 구성합니다. 가장 많이 투표된
C. AWS CodeCommit 리포지토리를 만듭니다. AWS CodePipeline 파이프라인을 만듭니다. 파이프라인을 시작하는 새 소스 단계에서 CodeCommit 리포지토리를 사용합니다. AWS Serverless Application Model(AWS SAM) 템플릿을 배포하기 위한 AWS CodeBuild 프로젝트를 만듭니다. 템플릿과 소스 코드를 CodeCommit 리포지토리에 업로드합니다. CodeCommit 리포지토리에서 SAM 애플리케이션을 빌드하고 배포하는 명령이 포함된 buildspec.yml 파일을 만듭니다. 가장 많이 투표된
D. AWS CodeCommit 리포지토리를 만듭니다. AWS CodePipeline 파이프라인을 만듭니다. 파이프라인을 시작하는 새 소스 단계에서 CodeCommit 리포지토리를 사용합니다. Canary10Percent10Minutes의 DeploymentPreference 유형으로 카나리아 배포를 위해 구성된 AWS CodeDeploy 배포 그룹을 만듭니다. AWS CloudFormation 템플릿과 소스 코드를 CodeCommit 리포지토리에 업로드합니다. CodeCommit 리포지토리에서 CloudFormation 템플릿을 배포하는 명령이 포함된 appspec.yml 파일을 만듭니다.
E. 모든 Lambda 함수에 대한 Amazon CloudWatch 복합 알람을 만듭니다. Lambda에 대한 평가 기간과 차원을 구성합니다. 오류가 감지되거나 데이터가 충분하지 않으면 알람이 ALARM 상태로 전환되도록 구성합니다.
F. 각 Lambda 함수에 대해 Amazon CloudWatch 알람을 만듭니다. 오류가 감지되면 알람이 ALARM 상태로 전환되도록 구성합니다. 평가 기간, 각 Lambda 함수 및 버전에 대한 차원, Errors 메트릭에서 AWS/Lambda로 네임스페이스를 구성합니다. 가장 많이 투표된



### 질문 #83주제 1
DevOps 엔지니어가 Amazon EC2 인스턴스와 연결된 AWS CodeDeploy 배포 그룹에 회사 애플리케이션의 새 버전을 배포하고 있습니다. 얼마 후 배포가 실패합니다. 엔지니어는 특정 배포 ID와 연결된 모든 이벤트가 건너뜀 상태이고 코드가 배포 그룹과 연결된 인스턴스에 배포되지 않았다는 것을 알게 됩니다.

이 실패의 타당한 이유는 무엇입니까? (두 가지를 선택하세요.)

A. 네트워크 구성으로 인해 EC2 인스턴스가 NAT 게이트웨이나 인터넷 게이트웨이를 통해 인터넷에 연결할 수 없고, CodeDeploy 엔드포인트에 접근할 수 없습니다. 가장 많이 투표된
B. 애플리케이션 배포를 트리거한 IAM 사용자에게 CodeDeploy 엔드포인트와 상호 작용할 권한이 없습니다.
C. 대상 EC2 인스턴스가 CodeDeploy 엔드포인트에 올바르게 등록되지 않았습니다.
D. 적절한 권한이 있는 인스턴스 프로필이 대상 EC2 인스턴스에 연결되지 않았습니다. 가장 많이 투표된
E. appspec.yml 파일이 애플리케이션 개정에 포함되지 않았습니다.



### 질문 #84주제 1
한 회사에서는 모든 Amazon EC2 인스턴스가 회사 보안팀에서 생성하는 AMI에서 시작되어야 한다는 가이드라인을 가지고 있습니다. 보안팀은 매달 모든 개발팀에 최신 승인된 AMI가 포함된 이메일 메시지를 보냅니다.

개발팀은 AWS CloudFormation을 사용하여 애플리케이션을 배포합니다. 개발자가 새 서비스를 시작하면 보안 부서에서 보낸 최신 AMI를 이메일에서 검색해야 합니다. DevOps 엔지니어는 보안팀이 개발팀에 AMI ID를 제공하는 데 사용하는 프로세스를 자동화하려고 합니다.

이러한 요구 사항을 충족하는 가장 확장 가능한 솔루션은 무엇입니까?

A. 보안 팀에 CloudFormation을 사용하여 AMI의 새 버전을 만들고 스택의 Outputs 섹션의 일부로 암호화된 Amazon S3 객체에 AMI ARN을 나열하도록 지시합니다. 개발자에게 크로스 스택 참조를 사용하여 암호화된 S3 객체를 로드하고 가장 최근의 AMI ARN을 가져오도록 지시합니다.
B. 보안 팀에 CloudFormation 스택을 사용하여 새로운 AMI를 빌드하고 최신 AMI ARN을 파이프라인 출력의 일부로 암호화된 Amazon S3 객체에 배치하는 AWS CodePipeline 파이프라인을 만들도록 지시합니다. 개발자에게 자체 CloudFormation 템플릿 내에서 크로스 스택 참조를 사용하여 S3 객체 위치와 최신 AMI ARN을 가져오도록 지시합니다.
C. 보안 팀에 Amazon EC2 Image Builder를 사용하여 새 AMI를 만들고 AMI ARN을 AWS Systems Manager Parameter Store에 매개변수로 배치하도록 지시합니다. 개발자에게 CloudFormation 스택에서 SSM 유형의 매개변수를 지정하여 Parameter Store에서 최신 AMI ARN을 가져오도록 지시합니다. 가장 많이 투표된
D. 보안 팀에 Amazon EC2 Image Builder를 사용하여 새 AMI를 만들고 모든 개발 팀이 알림을 받을 수 있도록 Amazon Simple Notification Service(Amazon SNS) 토픽을 만들도록 지시합니다. 개발 팀이 알림을 받으면 가장 최근의 AMI ARN으로 CloudFormation 스택을 업데이트하는 AWS Lambda 함수를 작성하도록 지시합니다.



### 질문 #85주제 1
애플리케이션은 Application Load Balancer(ALB) 뒤의 Amazon EC2 인스턴스에서 실행됩니다. DevOps 엔지니어가 AWS CodeDeploy를 사용하여 새 버전을 릴리스하고 있습니다. AllowTraffic 라이프사이클 이벤트 중에 배포가 실패하지만 배포 로그에 실패 원인이 표시되지 않습니다.

무엇 때문에 그럴까요?

A. appspec.yml 파일에 AllowTraffic 라이프사이클 후크에서 실행되는 잘못된 스크립트가 포함되어 있습니다.
B. 배포를 시작한 사용자에게 ALB와 상호 작용하는 데 필요한 권한이 없습니다.
C. ALB 대상 그룹에 지정된 상태 검사가 잘못 구성되었습니다. 가장 많이 투표된
D. ALB 대상 그룹에 속하는 EC2 인스턴스에 CodeDeploy 에이전트가 설치되지 않았습니다.



### 질문 #86주제 1
회사에 20개의 서비스 팀이 있습니다. 각 서비스 팀은 자체 마이크로서비스를 담당합니다. 각 서비스 팀은 마이크로서비스에 대해 별도의 AWS 계정과 192.168.0.0/22 ​​CIDR 블록이 있는 VPC를 사용합니다. 회사는 AWS Organizations로 AWS 계정을 관리합니다.

각 서비스 팀은 Application Load Balancer 뒤의 여러 Amazon EC2 인스턴스에서 마이크로서비스를 호스팅합니다. 마이크로서비스는 퍼블릭 인터넷을 통해 서로 통신합니다. 회사의 보안 팀은 마이크로서비스 간의 모든 통신은 프라이빗 네트워크 연결을 통해 HTTPS를 사용해야 하며 퍼블릭 인터넷을 통과할 수 없다는 새로운 지침을 발표했습니다.

DevOps 엔지니어는 이러한 의무를 충족하고 각 서비스 팀의 변경 횟수를 최소화하는 솔루션을 구현해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS Organizations에서 새 AWS 계정을 만듭니다. 이 계정에서 VPC를 만들고 AWS Resource Access Manager를 사용하여 이 VPC의 프라이빗 서브넷을 조직과 공유합니다. 서비스 팀에 공유 프라이빗 서브넷을 사용하는 새 Network Load Balancer(NLB) 및 EC2 인스턴스를 시작하도록 지시합니다. 마이크로서비스 간 통신에는 NLB DNS 이름을 사용합니다.
B. 각 마이크로서비스 VPC에 네트워크 로드 밸런서(NLB)를 만듭니다. AWS PrivateLink를 사용하여 각 AWS 계정에 NLB에 대한 VPC 엔드포인트를 만듭니다. 다른 각 AWS 계정에서 각 VPC 엔드포인트에 대한 구독을 만듭니다. 마이크로서비스 간 통신을 위해 VPC 엔드포인트 DNS 이름을 사용합니다. 가장 많이 투표된
C. 각 마이크로서비스 VPC에 네트워크 로드 밸런서(NLB)를 만듭니다. 각 마이크로서비스 VPC 간에 VPC 피어링 연결을 만듭니다. 피어링 링크를 사용하도록 각 VPC의 경로 테이블을 업데이트합니다. 마이크로서비스 간 통신에 NLB DNS 이름을 사용합니다.
D. AWS Organizations에서 새 AWS 계정을 만듭니다. 이 계정에서 전송 게이트웨이를 만들고 AWS Resource Access Manager를 사용하여 조직과 전송 게이트웨이를 공유합니다. 각 마이크로서비스 VPC에서 공유 전송 게이트웨이에 대한 전송 게이트웨이 연결을 만듭니다. 전송 게이트웨이를 사용하도록 각 VPC의 경로 테이블을 업데이트합니다. 각 마이크로서비스 VPC에서 네트워크 로드 밸런서(NLB)를 만듭니다. 마이크로서비스 간 통신에 NLB DNS 이름을 사용합니다.



### 질문 #87주제 1
Amazon EC2 인스턴스가 VPC에서 실행 중이며 제한된 Amazon S3 버킷에서 객체를 다운로드해야 합니다. DevOps 엔지니어가 객체를 다운로드하려고 하면 AccessDenied 오류가 수신됩니다.

이 오류의 가능한 원인은 무엇입니까? (두 가지를 선택하세요.)

A. S3 버킷 기본 암호화가 활성화되어 있습니다.
B. S3 버킷 정책에 오류가 있습니다. 가장 많이 투표된
C. 해당 객체가 S3 Glacier로 이동되었습니다.
D. IAM 역할 구성에 오류가 있습니다. 가장 많이 투표된
E. S3 버전 관리가 활성화되었습니다.



### 질문 #88주제 1
한 회사가 AWS를 기반으로 하는 독점적인 엔터프라이즈 인메모리 데이터 저장소에 그리드 시스템을 사용하려고 합니다. 이 시스템은 모든 Linux 기반 배포판의 여러 서버 노드에서 실행될 수 있습니다. 시스템은 노드가 추가되거나 제거될 때마다 전체 클러스터를 재구성할 수 있어야 합니다. 노드를 추가하거나 제거할 때 /etc/cluster/nodes.config 파일을 업데이트하여 해당 클러스터의 현재 노드 멤버의 IP 주소를 나열해야 합니다.

이 회사는 클러스터에 새 노드를 추가하는 작업을 자동화하려고 합니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 무엇을 할 수 있습니까?

A. AWS OpsWorks Stacks를 사용하여 해당 클러스터의 서버 노드를 계층화합니다. /etc/cluster/nodes.config 파일의 내용을 채우고 계층의 현재 멤버를 사용하여 서비스를 다시 시작하는 Chef 레시피를 만듭니다. 해당 레시피를 Configure 라이프사이클 이벤트에 할당합니다. 가장 많이 투표된
B. nodes.config 파일을 버전 제어에 넣습니다. 클러스터 노드에 대한 Amazon EC2 태그 값을 기반으로 AWS CodeDeploy 배포 구성 및 배포 그룹을 만듭니다. 클러스터에 새 노드를 추가할 때 모든 태그가 지정된 인스턴스로 파일을 업데이트하고 버전 제어에서 커밋합니다. 새 파일을 배포하고 서비스를 다시 시작합니다.
C. Amazon S3 버킷을 만들고 /etc/cluster/nodes.config 파일의 버전을 업로드합니다. 해당 S3 파일을 폴링하고 자주 다운로드하는 crontab 스크립트를 만듭니다. Monit 또는 systemd와 같은 프로세스 관리자를 사용하여 새 파일이 수정되었음을 감지하면 클러스터 서비스를 다시 시작합니다. 클러스터에 노드를 추가할 때 파일의 가장 최근 멤버를 편집합니다. 새 파일을 S3 버킷에 업로드합니다.
D. 클러스터의 현재 보안 그룹의 모든 멤버를 나열하고 클러스터에 새 인스턴스가 추가될 때마다 /etc/cluster/nodes.config 파일을 자동으로 업데이트하는 사용자 데이터 스크립트를 만듭니다.



### 질문 #89주제 1
DevOps 엔지니어가 온프레미스 데이터를 Amazon S3 버킷으로 마이그레이션해야 하는 데이터 보관 프로젝트를 진행하고 있습니다. DevOps 엔지니어는 1개월 이상 된 온프레미스 데이터를 Amazon S3에 점진적으로 보관하는 스크립트를 개발합니다. Amazon S3로 전송된 데이터는 온프레미스 위치에서 삭제됩니다. 스크립트는 S3 PutObject 작업을 사용합니다. DevOps 엔지니어는

코드 검토 중에 스크립트가 데이터가 Amazon S3에 성공적으로 복사되었는지 확인하지 않는다는 것을 알아챘습니다. DevOps 엔지니어는 스크립트를 업데이트하여 전송 중에 데이터가 손상되지 않도록 해야 합니다. 스크립트는 온프레미스 데이터가 삭제되기 전에 MD5 체크섬을 사용하여 데이터 무결성을 확인해야 합니다.

이러한 요구 사항을 충족하는 스크립트에 대한 솔루션은 무엇입니까? (두 가지를 선택하세요.)

A. 반환된 응답에서 VersionId를 확인합니다. 반환된 VersionId를 MD5 체크섬과 비교합니다.
B. Content-MD5 매개변수 내에 MD5 체크섬을 포함합니다. 작업 호출의 반환 상태를 확인하여 오류가 반환되었는지 확인합니다. 가장 많이 투표된
C. 태그 매개변수에 체크섬 다이제스트를 URL 쿼리 매개변수로 포함합니다.
D. 반환된 응답에서 ETag를 확인합니다. 반환된 ETag를 MD5 체크섬과 비교합니다. 가장 많이 투표된
E. Metadata 매개변수 내에 체크섬 다이제스트를 이름-값 쌍으로 포함합니다. 업로드 후 S3 HeadObject 작업을 사용하여 객체에서 메타데이터를 검색합니다.



### 질문 #90주제 1
한 회사는 AWS CodePipeline 파이프라인을 사용하여 일주일에 여러 번 Amazon API Gateway API에 업데이트를 배포합니다. 업데이트 프로세스의 일환으로 회사는 API Gateway 콘솔에서 API용 JavaScript SDK를 내보내고 SDK를 Amazon S3 버킷에 업로드합니다.

회사는 S3 버킷을 원본으로 사용하는 Amazon CloudFront 배포를 구성했습니다. 그런 다음 웹 클라이언트는 CloudFront 배포의 엔드포인트를 사용하여 SDK를 다운로드합니다. DevOps 엔지니어는 새 API 배포 중에 새 SDK를 자동으로 사용할 수 있도록 솔루션을 구현해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. API의 배포 단계 직후 CodePipeline 작업을 만듭니다. AWS Lambda 함수를 호출하도록 작업을 구성합니다. API Gateway에서 SDK를 다운로드하고, SDK를 S3 버킷에 업로드하고, SDK 경로에 대한 CloudFront 무효화를 생성하도록 Lambda 함수를 구성합니다. 가장 많이 투표된
B. API의 배포 단계 직후에 CodePipeline 작업을 만듭니다. API Gateway와 CodePipeline 통합을 사용하여 SDK를 Amazon S3로 내보내도록 작업을 구성합니다. Amazon S3와 CodePipeline 통합을 사용하여 SDK 경로에 대한 캐시를 무효화하는 다른 작업을 만듭니다.
C. aws.apigateway에서 UpdateStage 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. API Gateway에서 SDK를 다운로드하고, SDK를 S3 버킷에 업로드하고, CloudFront API를 호출하여 SDK 경로에 대한 무효화를 만드는 AWS Lambda 함수를 호출하도록 규칙을 구성합니다.
D. aws.apigateway에서 CreateDeployment 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. API Gateway에서 SDK를 다운로드하고, SDK를 S3 버킷에 업로드하고, S3 API를 호출하여 SDK 경로에 대한 캐시를 무효화하는 AWS Lambda 함수를 호출하도록 규칙을 구성합니다.



### 질문 #91주제 1
한 회사가 API를 통해 수신된 주문을 처리하는 AWS Lambda 함수를 개발했습니다. 이 회사는 CI/CD 파이프라인의 마지막 단계로 Lambda 함수를 배포하기 위해 AWS CodeDeploy를 사용하고 있습니다.

DevOps 엔지니어는 배포 후 몇 초 동안 주문 API에 간헐적인 오류가 발생하는 것을 발견했습니다. 조사 결과, DevOps 엔지니어는 Lambda 함수가 호출되기 전에 데이터베이스 변경 사항이 완전히 전파되지 않아 오류가 발생한 것으로 생각합니다.

DevOps 엔지니어는 이를 어떻게 극복해야 할까요?

A. AppSpec 파일에 BeforeAllowTraffic 후크를 추가하여 트래픽이 Lambda 함수의 새 버전으로 흐르기 전에 필요한 데이터베이스 변경 사항을 테스트하고 기다립니다. 가장 많이 투표된
B. Lambda 함수의 새 버전이 응답하기 전에 보류 중인 데이터베이스 변경 사항을 기다리도록 트래픽을 강제하는 AfterAllowTraffic 후크를 AppSpec 파일에 추가합니다.
C. Lambda 함수의 새 버전을 배포하기 전에 필요한 데이터베이스 변경 사항을 테스트하고 기다리는 BeforeInstall 후크를 AppSpec 파일에 추가합니다.
D. AppSpec 파일에 ValidateService 후크를 추가하여 들어오는 트래픽을 검사하고 데이터베이스와 같은 종속 서비스가 아직 준비되지 않은 경우 페이로드를 거부합니다.



### 질문 #92주제 1
한 회사에서 단일 AWS 계정을 사용하여 Amazon EC2 인스턴스에서 애플리케이션을 테스트합니다. 이 회사는 AWS 계정에서 AWS Config를 켜고 restricted-ssh AWS Config 관리 규칙을 활성화했습니다.

이 회사에는 계정의 보안 그룹이 restricted-ssh 규칙을 준수하지 않는 경우 실시간으로 사용자 지정 알림을 제공하는 자동화된 모니터링 솔루션이 필요합니다. 사용자 지정 알림에는 비준수 보안 그룹의 이름과 ID가 포함되어야 합니다.

DevOps 엔지니어가 계정에 Amazon Simple Notification Service(Amazon SNS) 토픽을 만들고 해당 토픽에 적절한 인력을 구독합니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 다음에 무엇을 해야 합니까?

A. restricted-ssh 규칙에 대한 NON_COMPLIANT의 AWS Config 평가 결과와 일치하는 Amazon EventBridge 규칙을 만듭니다. EventBridge 규칙에 대한 입력 변환기를 구성합니다. EventBridge 규칙을 구성하여 SNS 토픽에 알림을 게시합니다. 가장 많이 투표된
B. AWS Config를 구성하여 restricted-ssh 규칙에 대한 모든 평가 결과를 SNS 토픽으로 전송합니다. 알림에 NON_COMPLIANT 텍스트가 포함된 알림만 구독자에게 전송하도록 SNS 토픽에서 필터 정책을 구성합니다.
C. restricted-ssh 규칙에 대한 NON_COMPLIANT의 AWS Config 평가 결과와 일치하는 Amazon EventBridge 규칙을 만듭니다. EventBridge 규칙을 구성하여 SNS 토픽에서 AWS Systems Manager Run Command를 호출하여 알림을 사용자 지정하고 알림을 SNS 토픽에 게시합니다.
D. NON_COMPLIANT의 모든 AWS Config 평가 결과와 일치하는 Amazon EventBridge 규칙을 만듭니다. restricted-ssh 규칙에 대한 입력 변환기를 구성합니다. EventBridge 규칙을 구성하여 SNS 토픽에 알림을 게시합니다.




### 질문 #93주제 1
어떤 회사에서는 데이터와 애플리케이션에 대해 항상 2시간의 RPO와 10분의 RTO가 필요합니다. 애플리케이션은 MySQL 데이터베이스와 Amazon EC2 웹 서버를 사용합니다. 개발팀은 장애 조치 및 재해 복구를 위한 전략이 필요합니다.

어떤 배포 전략 조합이 이러한 요구 사항을 충족할까요? (두 가지를 선택하세요.)

A. 여러 지역에 걸쳐 하나의 가용성 영역에 Amazon Aurora 클러스터를 생성하여 데이터 저장소로 사용합니다. 재해 발생 시 Aurora의 자동 복구 기능을 사용합니다.
B. 두 지역에 Amazon Aurora 글로벌 데이터베이스를 데이터 저장소로 만듭니다. 장애가 발생하면 보조 지역을 애플리케이션의 기본 지역으로 승격합니다. 가장 많이 투표된
C. 여러 지역에 걸쳐 Amazon Aurora 멀티 마스터 클러스터를 데이터 저장소로 만듭니다. Network Load Balancer를 사용하여 다른 지역의 데이터베이스 트래픽을 균형 있게 조정합니다.
D. 두 지역에 애플리케이션을 설정하고 두 지역의 애플리케이션 로드 밸런서를 가리키는 Amazon Route 53 장애 조치 기반 라우팅을 사용합니다. 상태 검사를 사용하여 주어진 지역의 가용성을 확인합니다. 각 지역의 자동 확장 그룹을 사용하여 수요에 따라 용량을 조정합니다. 가장 많이 투표된
E. 두 지역에 애플리케이션을 설정하고 애플리케이션 로드 밸런서 뒤에 있는 다중 지역 자동 확장 그룹을 사용하여 수요에 따라 용량을 관리합니다. 재해 발생 시 자동 확장 그룹의 원하는 인스턴스 수를 조정하여 장애 조치 지역의 기준 용량을 늘립니다.



### 질문 #94주제 1
한 기업에 5개의 독립적인 AWS Lambda 함수로 구성된 애플리케이션이 있습니다.

DevOps 엔지니어는 AWS CodePipeline과 AWS CodeBuild를 사용하여 각 Lambda 함수를 순서대로 빌드, 테스트, 패키징 및 배포하는 CI/CD 파이프라인을 빌드했습니다. 파이프라인은 Amazon EventBridge 규칙을 사용하여 애플리케이션 소스 코드가 변경된 후 파이프라인이 가능한 한 빨리 시작되도록 합니다.

몇 달 동안 파이프라인을 사용한 후 DevOps 엔지니어는 파이프라인을 완료하는 데 너무 오래 걸린다는 것을 알아챘습니다.

DevOps 엔지니어는 파이프라인 속도를 가장 잘 개선하기 위해 무엇을 구현해야 할까요?

A. 파이프라인 내의 CodeBuild 프로젝트를 수정하여 사용 가능한 네트워크 처리량이 더 많은 컴퓨팅 유형을 사용합니다.
B. 빌드를 병렬로 실행하기 위한 대칭적 멀티프로세싱 구성을 포함하는 사용자 지정 CodeBuild 실행 환경을 만듭니다.
C. 동일한 runOrder를 지정하여 각 Lambda 함수에 대한 작업을 병렬로 실행하도록 CodePipeline 구성을 수정합니다. 가장 많이 투표된
D. 각 CodeBuild 프로젝트를 VPC 내에서 실행하도록 수정하고 전용 인스턴스를 사용하여 처리량을 늘립니다.



### 질문 #95주제 1
한 회사에서는 AWS CloudFormation 스택을 사용하여 애플리케이션에 업데이트를 배포합니다. 스택은 다양한 리소스로 구성됩니다. 리소스에는 AWS Auto Scaling 그룹, Amazon EC2 인스턴스, Application Load Balancer(ALB) 및 독립 스택을 시작하고 유지하는 데 필요한 기타 리소스가 포함됩니다. CloudFormation 스택 업데이트 외부의 애플리케이션 리소스에 대한 변경은 허용되지 않습니다.

이 회사는 최근 AWS CLI를 사용하여 애플리케이션 스택을 업데이트하려고 했습니다. 스택이 업데이트되지 않고 다음과 같은 오류 메시지가 생성되었습니다. "오류: 배포와 CloudFormation 스택 롤백이 모두 실패했습니다. 다음 리소스가 업데이트되지 않아 배포가 실패했습니다. [AutoScalingGroup]."

스택은 UPDATE_ROLLBACK_FAILED 상태로 유지됩니다.

어떤 솔루션으로 이 문제를 해결할 수 있을까요?

A. ALB에 대해 구성된 서브넷 매핑을 업데이트합니다. aws cloudformation update-stack-set AWS CLI 명령을 실행합니다.
B. 스택을 업데이트하는 데 필요한 권한을 제공하여 IAM 역할을 업데이트합니다. aws cloudformation continue-update-rollback AWS CLI 명령을 실행합니다. 가장 많이 투표된
C. 계정의 EC2 인스턴스 수에 대한 할당량 증가 요청을 제출합니다. aws cloudformation cancel-update-stack AWS CLI 명령을 실행합니다.
D. Auto Scaling 그룹 리소스를 삭제합니다. aws cloudformation rollback-stack AWS CLI 명령을 실행합니다.



### 질문 #96주제 1
한 회사가 Amazon EC2 인스턴스를 사용하는 새로운 애플리케이션을 배포하고 있습니다. 이 회사는 애플리케이션 로그와 AWS 계정 API 활동을 쿼리하는 솔루션이 필요합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Amazon CloudWatch 에이전트를 사용하여 EC2 인스턴스에서 Amazon CloudWatch Logs로 로그를 전송합니다. AWS CloudTrail을 구성하여 API 로그를 Amazon S3로 전달합니다. CloudWatch를 사용하여 두 로그 세트를 모두 쿼리합니다.
B. Amazon CloudWatch 에이전트를 사용하여 EC2 인스턴스에서 Amazon CloudWatch Logs로 로그를 전송합니다. AWS CloudTrail을 구성하여 API 로그를 CloudWatch Logs로 전달합니다. CloudWatch Logs Insights를 사용하여 두 로그 세트를 쿼리합니다. 가장 많이 투표된
C. Amazon CloudWatch 에이전트를 사용하여 EC2 인스턴스에서 Amazon Kinesis로 로그를 전송합니다. AWS CloudTrail을 구성하여 API 로그를 Kinesis로 전달합니다. Kinesis를 사용하여 데이터를 Amazon Redshift에 로드합니다. Amazon Redshift를 사용하여 두 로그 세트를 쿼리합니다.
D. Amazon CloudWatch 에이전트를 사용하여 EC2 인스턴스에서 Amazon S3로 로그를 전송합니다. AWS CloudTrail을 사용하여 API 로그를 Amazon S3로 전달합니다. Amazon Athena를 사용하여 Amazon S3에서 두 로그 세트를 쿼리합니다.



### 질문 #97주제 1
어떤 회사에서 EC2 인스턴스가 안전한지 확인하고 싶어합니다. 인스턴스에서 새로운 취약점이 발견되면 알림을 받고 싶어하고, 인스턴스의 모든 로그인 활동에 대한 감사 추적도 원합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS Systems Manager를 사용하여 EC2 인스턴스의 취약성을 감지합니다. Amazon Kinesis Agent를 설치하여 시스템 로그를 캡처하고 Amazon S3에 전달합니다.
B. AWS Systems Manager를 사용하여 EC2 인스턴스의 취약성을 감지합니다. Systems Manager Agent를 설치하여 시스템 로그를 캡처하고 CloudTrail 콘솔에서 로그인 활동을 확인합니다.
C. EC2 인스턴스의 취약성을 감지하도록 Amazon CloudWatch를 구성합니다. AWS Config 데몬을 설치하여 시스템 로그를 캡처하고 AWS Config 콘솔에서 확인합니다.
D. EC2 인스턴스의 취약성을 감지하도록 Amazon Inspector를 구성합니다. Amazon CloudWatch Agent를 설치하여 시스템 로그를 캡처하고 Amazon CloudWatch Logs를 통해 기록합니다. 가장 많이 투표된



### 질문 #98주제 1
한 회사가 Auto Scaling 그룹의 Amazon EC2 인스턴스에서 애플리케이션을 실행하고 있습니다. 최근에 EC2 인스턴스가 성공적으로 시작되지 못하게 하는 문제가 발생했고, 지원팀이 문제를 발견하는 데 몇 시간이 걸렸습니다. 지원팀은 EC2 인스턴스가 성공적으로 시작되지 않을 때마다 이메일로 알림을 받고 싶어합니다.

어떤 조치로 이를 달성할 수 있을까요?

A. 인스턴스 상태가 손상될 때마다 AWS Lambda 함수를 호출하기 위해 자동 크기 조정 그룹에 상태 검사를 추가합니다.
B. 인스턴스 시작이 실패할 때마다 Amazon SNS 주제에 알림을 보내도록 자동 크기 조정 그룹을 구성합니다. 가장 많이 투표된
C. AttachInstances 자동 확장 API 호출이 실패하면 AWS Lambda 함수를 호출하는 Amazon CloudWatch 알람을 생성합니다.
D. Amazon EC2에서 상태 확인 알람을 생성하여 상태 확인에 실패할 때마다 Amazon SNS 주제에 알림을 보냅니다.



### 질문 #99주제 1
한 회사가 AWS Organizations를 사용하여 AWS 계정을 중앙에서 관리하고 있습니다. 이 회사는 AWS CloudFormation StackSets를 사용하여 각 멤버 계정에서 AWS Config를 켰습니다. 이 회사는 AWS Config에 대한 Organizations에서 신뢰할 수 있는 액세스를 구성했고 멤버 계정을 AWS Config에 대한 위임된 관리자 계정으로 구성했습니다.

DevOps 엔지니어는 새로운 보안 정책을 구현해야 합니다. 이 정책은 모든 현재 및 미래의 AWS 멤버 계정이 중앙 계정에서 관리되는 수정 작업이 포함된 AWS Config 규칙의 공통 기준을 사용하도록 요구해야 합니다. 멤버 계정에 액세스할 수 있는 관리자가 아닌 사용자는 각 멤버 계정에 배포된 AWS Config 규칙의 공통 기준을 수정할 수 없어야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS Config 규칙과 수정 작업을 포함하는 CloudFormation 템플릿을 만듭니다. CloudFormation StackSets를 사용하여 Organizations 관리 계정에서 템플릿을 배포합니다.
B. AWS Config 규칙과 수정 작업을 포함하는 AWS Config 적합성 팩을 만듭니다. CloudFormation StackSets를 사용하여 Organizations 관리 계정에서 팩을 배포합니다.
C. AWS Config 규칙과 수정 작업을 포함하는 CloudFormation 템플릿을 만듭니다. AWS Config를 사용하여 위임된 관리자 계정에서 템플릿을 배포합니다.
D. AWS Config 규칙과 수정 조치를 포함하는 AWS Config 적합성 팩을 만듭니다. AWS Config를 사용하여 위임된 관리자 계정에서 팩을 배포합니다. 가장 많이 투표된



### 질문 #100주제 1
DevOps 엔지니어가 Amazon EC2에서 실행되는 대규모 상업용 웹사이트를 관리합니다. 이 웹사이트는 Amazon Kinesis Data Streams를 사용하여 웹 로그를 수집하고 처리합니다. DevOps 엔지니어는 Amazon EC2에서 실행되는 Kinesis 소비자 애플리케이션을 관리합니다.

데이터가 갑자기 증가하면 Kinesis 소비자 애플리케이션이 뒤처지고 Kinesis 데이터 스트림은 레코드를 처리하기 전에 레코드를 삭제합니다. DevOps 엔지니어는 스트림 처리를 개선하기 위한 솔루션을 구현해야 합니다.

어떤 솔루션이 이러한 요구 사항을 가장 높은 운영 효율성으로 충족합니까?

A. Kinesis 소비자 애플리케이션을 수정하여 로그를 Amazon S3에 내구성 있게 저장합니다. Amazon EMR을 사용하여 Amazon S3에서 직접 데이터를 처리하여 고객 통찰력을 얻습니다. 결과를 Amazon S3에 저장합니다.
B. Amazon CloudWatch GetRecords.IteratorAgeMilliseconds 메트릭을 기반으로 더 많은 EC2 인스턴스를 추가하여 Kinesis 소비자 애플리케이션을 수평적으로 확장합니다. Kinesis 데이터 스트림의 보존 기간을 늘립니다. 가장 많이 투표된
C. Kinesis 소비자 애플리케이션을 AWS Lambda 함수로 실행하도록 변환합니다. Lambda 함수가 데이터 스트림을 처리하도록 Kinesis 데이터 스트림을 이벤트 소스로 구성합니다.
D. Kinesis 데이터 스트림의 샤드 수를 늘려 전체 처리량을 늘리고, 이를 통해 소비자 애플리케이션이 데이터를 더 빠르게 처리할 수 있도록 합니다.



### 질문 #101주제 1
한 회사가 최근 AWS Organizations의 새 조직에 새 AWS Control Tower 랜딩 존을 만들었습니다. 랜딩 존은 AWS Foundations에 대한 Center for Internet Security(CIS) 벤치마크를 준수함을 입증할 수 있어야 합니다.

회사의 보안 팀은 AWS Security Hub를 사용하여 모든 계정의 준수 여부를 확인하려고 합니다. 보안 팀만 집계된 Security Hub 결과를 볼 수 있습니다. 또한 특정 사용자는 조직 내에서 자신의 계정에서 결과를 볼 수 있어야 합니다. 모든 계정은 계정을 만든 후 Security Hub에 등록해야 합니다.

이러한 요구 사항을 가장 자동화된 방식으로 충족하는 단계 조합은 무엇입니까? (세 가지를 선택하세요.)

A. 조직의 관리 계정에서 Security Hub에 대한 신뢰할 수 있는 액세스를 켭니다. AWS Control Tower를 사용하여 새 보안 계정을 만듭니다. 새 보안 계정을 Security Hub의 위임된 관리자 계정으로 구성합니다. 새 보안 계정에서 Security Hub에 AWS Foundations 표준에 대한 CIS 벤치마크를 제공합니다. 가장 많이 투표된
B. 조직의 관리 계정에서 Security Hub에 대한 신뢰할 수 있는 액세스를 켭니다. 관리 계정에서 Security Hub에 AWS Foundations 표준에 대한 CIS 벤치마크를 제공합니다.
C. 필요한 권한을 포함하는 AWS IAM Identity Center(AWS Single Sign-On) 권한 집합을 만듭니다. CreateAccountAssignment API 작업을 사용하여 보안 팀 사용자를 권한 집합 및 위임된 보안 계정과 연결합니다. 가장 많이 투표된
D. 보안 팀에 속하지 않은 사용자가 보안 허브에 액세스하는 것을 명시적으로 거부하는 SCP를 만듭니다.
E. 보안 허브에서 자동 활성화를 켭니다. 가장 많이 투표된
F. 조직의 관리 계정에서 CreateManagedAccount 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. Security Hub CreateMembers API 작업을 사용하여 Security Hub에 새 계정을 추가하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 호출하도록 EventBridge 규칙을 구성합니다.



### 질문 #102주제 1
한 회사가 AWS Organizations의 조직에 있는 AWS 계정에서 애플리케이션을 실행합니다. 이 애플리케이션은 Amazon EC2 인스턴스와 Amazon S3를 사용합니다.

이 회사는 기존 AWS 계정과 회사가 미래에 만드는 모든 AWS 계정에서 잠재적으로 손상된 EC2 인스턴스, 의심스러운 네트워크 활동, 비정상적인 API 활동을 감지하려고 합니다. 이 회사가 이러한 이벤트 중 하나를 감지하면 기존 Amazon Simple Notification Service(Amazon SNS) 주제를 사용하여 조사 및 수정을 위해 운영 지원 팀에 알림을 보내려고 합니다.

AWS 모범 사례에 따라 이러한 요구 사항을 충족하는 솔루션은 무엇입니까?

A. 조직의 관리 계정에서 AWS 계정을 Amazon GuardDuty 관리자 계정으로 구성합니다. GuardDuty 관리자 계정에서 회사의 기존 AWS 계정을 GuardDuty에 멤버로 추가합니다. GuardDuty 관리자 계정에서 GuardDuty 이벤트를 일치시키고 일치하는 이벤트를 SNS 토픽으로 전달하는 이벤트 패턴이 있는 Amazon EventBridge 규칙을 만듭니다. 가장 많이 투표된
B. 조직의 관리 계정에서 Amazon GuardDuty를 구성하여 초대를 통해 새로 생성된 AWS 계정을 추가하고 기존 AWS 계정에 초대를 보냅니다. GuardDuty 초대를 수락하고 Amazon EventBridge 규칙을 만드는 AWS CloudFormation 스택 세트를 만듭니다. GuardDuty 이벤트와 일치하고 일치하는 이벤트를 SNS 토픽으로 전달하도록 이벤트 패턴으로 규칙을 구성합니다. 조직의 모든 AWS 계정에 배포하도록 CloudFormation 스택 세트를 구성합니다.
C. 조직의 관리 계정에서 AWS CloudTrail 조직 트레일을 만듭니다. 조직의 모든 AWS 계정에서 조직 트레일을 활성화합니다. 조직의 각 계정에서 VPC Flow Logs를 활성화하는 SCP를 만듭니다. 조직에 AWS Security Hub를 구성합니다. Security Hub 이벤트를 일치시키고 일치하는 이벤트를 SNS 토픽으로 전달하는 이벤트 패턴이 있는 Amazon EventBridge 규칙을 만듭니다.
D. 조직의 관리 계정에서 AWS 계정을 AWS CloudTrail 관리자 계정으로 구성합니다. CloudTrail 관리자 계정에서 CloudTrail 조직 트레일을 만듭니다. 회사의 기존 AWS 계정을 조직 트레일에 추가합니다. 조직의 각 계정에서 VPC Flow Logs를 활성화하는 SCP를 만듭니다. 조직에 AWS Security Hub를 구성합니다. Security Hub 이벤트를 일치시키고 일치하는 이벤트를 SNS 토픽으로 전달하는 이벤트 패턴이 있는 Amazon EventBridge 규칙을 만듭니다.



### 질문 #103주제 1
한 회사의 DevOps 엔지니어가 다중 계정 환경에서 작업하고 있습니다. 이 회사는 AWS Transit Gateway를 사용하여 모든 아웃바운드 트래픽을 네트워크 운영 계정을 통해 라우팅합니다. 네트워크 운영 계정에서 모든 계정 트래픽은 트래픽이 인터넷 게이트웨이로 이동하기 전에 검사를 위해 방화벽 어플라이언스를 통과합니다.

방화벽 어플라이언스는 Amazon CloudWatch Logs에 로그를 보내고 CRITICAL, HIGH, MEDIUM, LOW 및 INFO의 이벤트 심각도를 포함합니다. 보안 팀은 CRITICAL 이벤트가 발생하면 알림을 받고 싶어합니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 무엇을 해야 합니까?

A. 방화벽 상태를 모니터링하기 위해 Amazon CloudWatch Synthetics 카나리아를 만듭니다. 방화벽이 CRITICAL 상태에 도달하거나 CRITICAL 이벤트를 기록하는 경우 CloudWatch 알람을 사용하여 Amazon Simple Notification Service(Amazon SNS) 토픽에 알림을 게시합니다. 보안 팀의 이메일 주소를 토픽에 구독합니다.
B. CRITICAL 이벤트에 대한 검색을 사용하여 Amazon CloudWatch 메트릭 필터를 만듭니다. 발견 사항에 대한 사용자 지정 메트릭을 게시합니다. 사용자 지정 메트릭을 기반으로 CloudWatch 알람을 사용하여 Amazon Simple Notification Service(Amazon SNS) 주제에 알림을 게시합니다. 보안 팀의 이메일 주소를 주제에 구독합니다. 가장 많이 투표된
C. 네트워크 운영 계정에서 Amazon GuardDuty를 활성화합니다. GuardDuty를 구성하여 흐름 로그를 모니터링합니다. CRITICAL인 GuardDuty 이벤트에서 호출되는 Amazon EventBridge 이벤트 규칙을 만듭니다. Amazon Simple Notification Service(Amazon SNS) 토픽을 대상으로 정의합니다. 보안 팀의 이메일 주소를 토픽에 구독합니다.
D. AWS Firewall Manager를 사용하여 모든 계정에 일관된 정책을 적용합니다. 중요한 Firewall Manager 이벤트에 의해 호출되는 Amazon EventBridge 이벤트 규칙을 만듭니다. Amazon Simple Notification Service(Amazon SNS) 토픽을 대상으로 정의합니다. 보안 팀의 이메일 주소를 토픽에 구독합니다.



### 질문 #104주제 1
회사는 팀으로 나뉩니다. 각 팀에는 AWS 계정이 있으며, 모든 계정은 AWS Organizations의 조직에 있습니다. 각 팀은 AWS 계정에 대한 전체 관리 권한을 유지해야 합니다. 또한 각 팀은 회사에서 사용을 승인한 AWS 서비스에만 액세스할 수 있어야 합니다. AWS 서비스는 요청 및 승인 프로세스를 통해 승인을 받아야 합니다. DevOps 엔지니어

는 이러한 요구 사항을 충족하기 위해 어떻게 계정을 구성해야 합니까?

A. AWS CloudFormation StackSets를 사용하여 각 계정에서 IAM 정책을 프로비저닝하여 제한된 AWS 서비스에 대한 액세스를 거부합니다. 각 계정에서 정책이 계정의 IAM 주체에 연결되도록 하는 AWS Config 규칙을 구성합니다.
B. AWS Control Tower를 사용하여 조직 내의 OU에 계정을 프로비저닝합니다. AWS Control Tower를 구성하여 AWS IAM Identity Center(AWS Single Sign-On)를 활성화합니다. IAM Identity Center를 구성하여 관리 액세스를 제공합니다. 제한된 AWS 서비스에 대한 사용자 역할에 대한 거부 정책을 포함합니다.
C. 조직 내의 모든 계정을 새로운 최상위 OU에 배치합니다. 제한된 AWS 서비스에 대한 액세스를 거부하는 SCP를 만듭니다. SCP를 OU에 연결합니다.
D. 승인된 AWS 서비스에만 액세스할 수 있는 SCP를 만듭니다. SCP를 조직의 루트 OU에 연결합니다. 조직의 루트 OU에서 FullAWSAccess SCP를 제거합니다. 가장 많이 투표된



### 질문 #105주제 1
DevOps 엔지니어가 AWS CloudFormation 사용자 지정 리소스를 사용하여 AD 커넥터를 설정했습니다. AWS Lambda 함수가 실행되어 AD 커넥터를 생성했지만 CloudFormation이 CREATE_IN_PROGRESS에서 CREATE_COMPLETE로 전환되지 않습니다.

이 문제를 해결하기 위해 엔지니어가 취해야 할 조치는 무엇입니까?

A. Lambda 함수 코드가 성공적으로 종료되었는지 확인하세요.
B. Lambda 함수 코드가 미리 서명된 URL에 대한 응답을 반환하는지 확인합니다. 가장 많이 투표된
C. Lambda 함수 IAM 역할에 스택 ARN에 대한 cloudformation:UpdateStack 권한이 있는지 확인하세요.
D. Lambda 함수 IAM 역할에 AWS 계정에 대한 ds:ConnectDirectory 권한이 있는지 확인하세요.




### 질문 #106주제 1
한 회사에서 소스 코드 제어를 위해 AWS CodeCommit을 사용합니다. 개발자는 다양한 기능 브랜치에 변경 사항을 적용하고 변경 사항이 프로덕션에 준비되면 해당 변경 사항을 메인 브랜치로 옮기기 위한 풀 요청을 생성합니다.

개발자는 변경 사항을 메인 브랜치에 직접 푸시할 수 없어야 합니다. 이 회사는 개발자의 IAM 역할에 AWSCodeCommitPowerUser 관리 정책을 적용했고, 이제 이 개발자는 AWS 계정의 모든 리포지토리에서 메인 브랜치에 직접 변경 사항을 푸시할 수 있습니다.

이 회사는 개발자가 메인 브랜치에 직접 변경 사항을 푸시하는 기능을 제한하기 위해 무엇을 해야 합니까?

A. GitPush 및 PutFile 작업에 대한 Deny 규칙을 포함하는 추가 정책을 만듭니다. 정책 문에 특정 리포지토리에 대한 제한을 포함하고 메인 브랜치를 참조하는 조건을 포함합니다. 가장 많이 투표된
B. IAM 정책을 제거하고 AWSCodeCommitReadOnly 관리 정책을 추가합니다. 정책 문에서 특정 리포지토리에 대한 GitPush 및 PutFile 작업에 대한 허용 규칙을 추가하고, 메인 브랜치를 참조하는 조건을 추가합니다.
C. IAM 정책을 수정합니다. 정책 문에 특정 리포지토리에 대한 GitPush 및 PutFile 작업에 대한 Deny 규칙을 포함시키고, 메인 브랜치를 참조하는 조건을 포함합니다.
D. GitPush 및 PutFile 작업에 대한 허용 규칙을 포함하는 추가 정책을 만듭니다. 기능 분기를 참조하는 조건과 함께 정책 문에 특정 저장소에 대한 제한을 포함합니다.



### 질문 #107주제 1
한 회사가 Application Load Balancer(ALB) 뒤의 Amazon EC2 인스턴스에서 실행되는 웹 애플리케이션을 관리합니다. EC2 인스턴스는 여러 가용성 영역에 걸쳐 Auto Scaling 그룹에서 실행됩니다. 이 애플리케이션은 Amazon RDS for MySQL DB 인스턴스를 사용하여 데이터를 저장합니다. 이 회사는 ALB를 가리키는 별칭 레코드로 Amazon Route 53을 구성했습니다.

새로운 회사 가이드라인은 RTO가 4시간, RPO가 15분인 지리적으로 고립된 재해 복구(DR) 사이트를 요구합니다.

어떤 DR 전략이 애플리케이션 스택을 최소한으로 변경하여 이러한 요구 사항을 충족할까요?

A. 다른 가용성 영역에서 Amazon RDS를 제외한 모든 항목의 복제 환경을 시작합니다. 새 가용성 영역에서 RDS 읽기 복제본을 만들고 새 스택이 로컬 RDS DB 인스턴스를 가리키도록 구성합니다. 상태 확인을 사용하여 장애 조치 라우팅 정책을 구성하여 새 스택을 Route 53 레코드 세트에 추가합니다.
B. 다른 AWS 지역에서 Amazon RDS를 제외한 모든 항목의 복제 환경을 시작합니다. 새 지역에서 RDS 읽기 복제본을 만들고 새 스택이 로컬 RDS DB 인스턴스를 가리키도록 구성합니다. 상태 확인을 사용하여 대기 시간 라우팅 정책을 구성하여 새 스택을 Route 53 레코드 세트에 추가합니다.
C. 다른 AWS 지역에서 Amazon RDS를 제외한 모든 것의 복제 환경을 시작합니다. 중단이 발생하는 경우 기본 지역에서 DR 지역으로 최신 RDS 스냅샷을 복사하여 복원합니다. DR 지역의 ALB를 가리키도록 Route 53 레코드 세트를 조정합니다.
D. 다른 AWS 지역에서 Amazon RDS를 제외한 모든 항목의 복제본 환경을 시작합니다. 새 지역에서 RDS 읽기 복제본을 만들고 새 환경을 구성하여 로컬 RDS DB 인스턴스를 가리킵니다. 장애 조치 라우팅 정책을 구성하기 위해 상태 확인을 사용하여 새 스택을 Route 53 레코드 세트에 추가합니다. 중단이 발생하면 읽기 복제본을 기본으로 승격합니다. 가장 많이 투표된



### 질문 #108주제 1
대기업이 AWS에 웹 애플리케이션을 배포하고 있습니다. 애플리케이션은 Application Load Balancer 뒤의 Amazon EC2 인스턴스에서 실행됩니다. 인스턴스는 여러 가용성 영역에 걸쳐 Auto Scaling 그룹에서 실행됩니다. 애플리케이션은 Amazon RDS for Oracle DB 인스턴스와 Amazon DynamoDB에 데이터를 저장합니다. 개발, 테스트 및 프로덕션을 위한 별도의 환경이 있습니다.

배포 중에 암호 자격 증명을 얻는 가장 안전하고 유연한 방법은 무엇입니까?

A. AWS Systems Manager SecureString 매개변수에서 액세스 키를 검색하여 AWS 서비스에 액세스합니다. Systems Manager SecureString 매개변수에서 데이터베이스 자격 증명을 검색합니다.
B. EC2 IAM 역할로 EC2 인스턴스를 시작하여 AWS 서비스에 액세스합니다. AWS Secrets Manager에서 데이터베이스 자격 증명을 검색합니다. 가장 많이 투표된
C. AWS Systems Manager 일반 텍스트 매개변수에서 액세스 키를 검색하여 AWS 서비스에 액세스합니다. Systems Manager SecureString 매개변수에서 데이터베이스 자격 증명을 검색합니다.
D. EC2 IAM 역할로 EC2 인스턴스를 시작하여 AWS 서비스에 액세스합니다. 애플리케이션 아티팩트와 함께 암호화된 구성 파일에 데이터베이스 비밀번호를 저장합니다.



### 질문 #109주제 1
보안팀은 회사의 AWS 계정에서 민감한 보안 문제를 감지하기 위해 AWS CloudTrail에 의존합니다. DevOps 엔지니어는 AWS 계정에서 CloudTrail이 꺼지는 것을 자동으로 수정하는 솔루션이 필요합니다.

CloudTrail 로그 전달에 대한 최소 다운타임을 보장하는 솔루션은 무엇입니까?

A. CloudTrail StopLogging 이벤트에 대한 Amazon EventBridge 규칙을 만듭니다. AWS SDK를 사용하여 StopLogging이 호출된 리소스의 ARN에서 StartLogging을 호출하는 AWS Lambda 함수를 만듭니다. Lambda 함수 ARN을 EventBridge 규칙에 대상으로 추가합니다. 가장 많이 투표된
B. AWS 관리형 CloudTrail 지원 AWS Config 규칙을 배포하고, 주기적 간격을 1시간으로 설정합니다. AWS Config 규칙 준수 변경을 위한 Amazon EventBridge 규칙을 만듭니다. AWS SDK를 사용하여 StopLogging이 호출된 리소스의 ARN에서 StartLogging을 호출하는 AWS Lambda 함수를 만듭니다. Lambda 함수 ARN을 EventBridge 규칙에 대상으로 추가합니다.
C. 5분마다 예약된 이벤트에 대한 Amazon EventBridge 규칙을 만듭니다. AWS SDK를 사용하여 AWS 계정의 CloudTrail 트레일에서 StartLogging을 호출하는 AWS Lambda 함수를 만듭니다. Lambda 함수 ARN을 EventBridge 규칙에 대상으로 추가합니다.
D. AWS SDK를 사용하여 현재 계정에서 CloudTrail을 쿼리하는 5분마다 실행되는 스크립트로 t2.nano 인스턴스를 시작합니다. CloudTrail 트레일이 비활성화된 경우 스크립트가 트레일을 다시 활성화하도록 합니다.



### 질문 #110주제 1
한 회사에서 AWS CodeArtifact를 사용하여 Python 패키지를 중앙에서 저장합니다. CodeArtifact 리포지토리는 다음 리포지토리 정책으로 구성되어 있습니다.



개발팀이 AWS Organizations의 조직에 있는 계정에서 새 프로젝트를 빌드하고 있습니다. 개발팀은 조직의 CodeArtifact 리포지토리에 이미 저장된 Python 라이브러리를 사용하려고 합니다. 개발팀은 AWS CodePipeline과 AWS CodeBuild를 사용하여 새 애플리케이션을 빌드합니다. 개발팀이 애플리케이션을 빌드하는 데 사용하는 CodeBuild 작업은 VPC에서 실행되도록 구성되어 있습니다. 규정 준수 요구 사항으로 인해 VPC에 인터넷 연결이 없습니다.

개발팀은 CodeArtifact에 대한 VPC 엔드포인트를 만들고 CodeBuild buildspec.yaml 파일을 업데이트합니다. 그러나 개발팀은 리포지토리에서 Python 라이브러리를 다운로드할 수 없습니다.

개발팀이 CodeArtifact를 사용할 수 있도록 DevOps 엔지니어는 어떤 단계 조합을 수행해야 합니까? (두 가지를 선택하세요.)

A. Amazon S3 게이트웨이 엔드포인트를 만듭니다. CodeBuild 작업을 실행 중인 서브넷에 대한 경로 테이블을 업데이트합니다. 가장 많이 투표된
B. CodeBuild 프로젝트가 사용하는 역할의 ARN을 포함하도록 저장소 정책의 Principal 명령문을 업데이트합니다.
C. AWS Resource Access Manager(AWS RAM)를 사용하여 CodeArtifact 저장소를 조직과 공유합니다.
D. CodeBuild 프로젝트가 사용하는 역할을 업데이트하여 해당 역할이 CodeArtifact 리포지토리를 사용할 수 있는 충분한 권한을 갖도록 합니다. 가장 많이 투표된
E. 조직에서 CodeArtifact에 대한 위임된 관리자로 저장소를 호스팅하는 계정을 지정합니다.



### 질문 #111주제 1
한 회사는 여러 리전 애플리케이션을 배포하기 위해 일련의 개별 Amazon CloudFormation 템플릿을 사용합니다. 이러한 템플릿은 특정 순서로 배포해야 합니다. 이 회사는 이전에 예상했던 것보다 더 많은 템플릿을 변경하고 있으며 새로운 템플릿을 보다 효율적으로 배포하려고 합니다. 또한 데이터 엔지니어링 팀에 템플릿의 모든 변경 사항을 알려야 합니다.

이 회사는 이러한 목표를 달성하기 위해 무엇을 해야 할까요?

A. 필요한 순서대로 CloudFormation 템플릿을 배포하기 위한 AWS Lambda 함수를 만듭니다. 스택 정책을 사용하여 데이터 엔지니어링 팀에 경고합니다.
B. Amazon S3에서 CloudFormation 템플릿을 호스팅합니다. Amazon S3 이벤트를 사용하여 CloudFormation 업데이트 및 Amazon SNS 알림을 직접 트리거합니다.
C. CloudFormation StackSets를 구현하고 드리프트 감지를 사용하여 데이터 엔지니어링 팀에 업데이트 알림을 트리거합니다.
D. 배포를 위해 CloudFormation 중첩 스택과 스택 세트를 활용합니다. Amazon SNS를 사용하여 데이터 엔지니어링 팀에 알립니다. 가장 많이 투표된




### 질문 #112주제 1
DevOps 엔지니어가 웹 애플리케이션을 프로비저닝하는 AWS CloudFormation 템플릿을 배포하기 위한 CI/CD 파이프라인을 구현했습니다. 웹 애플리케이션은 ALB(Application Load Balancer), 대상 그룹, Amazon Linux 2 AMI를 사용하는 시작 템플릿, Amazon EC2 인스턴스의 자동 확장 그룹, 보안 그룹, MySQL 데이터베이스용 Amazon RDS로 구성됩니다. 시작 템플릿에는 애플리케이션을 설치하고 시작하는 스크립트를 지정하는 사용자 데이터가 포함됩니다.

애플리케이션의 초기 배포는 성공적이었습니다. DevOps 엔지니어는 사용자 데이터로 애플리케이션 버전을 업데이트하기 위해 변경했습니다. CI/CD 파이프라인은 템플릿의 새 버전을 배포했습니다. 그러나 ALB의 상태 검사가 이제 실패하고 있습니다. 상태 검사에서 모든 대상이 비정상으로 표시되었습니다.

조사하는 동안 DevOps 엔지니어는 CloudFormation 스택의 상태가 UPDATE_COMPLETE임을 알아챘습니다. 하지만 DevOps 엔지니어가 EC2 인스턴스 중 하나에 연결하여 /var/log/messages를 확인하면 DevOps 엔지니어는 구성 오류로 인해 Apache 웹 서버가 성공적으로 시작되지 않았다는 것을 알게 됩니다.

DevOps 엔지니어는 사용자 데이터가 성공적으로 실행을 완료하지 못하면 CloudFormation 배포가 실패하도록 어떻게 보장할 수 있을까요?

A. cfn-signal 헬퍼 스크립트를 사용하여 CloudFormation에 성공 또는 실패를 알립니다. CloudFormation 템플릿 내에서 WaitOnResourceSignals 업데이트 정책을 사용합니다. 업데이트 정책에 대한 적절한 시간 초과를 설정합니다. 가장 많이 투표된
B. UnhealthyHostCount 메트릭에 대한 Amazon CloudWatch 알람을 만듭니다. 대상 그룹에 대한 적절한 알람 임계값을 포함합니다. CloudFormation에 성공 또는 실패를 알리는 대상으로 Amazon Simple Notification Service(Amazon SNS) 토픽을 만듭니다.
C. AWS::AutoScaling::LifecycleHook 리소스를 사용하여 Auto Scaling 그룹에 라이프사이클 후크를 만듭니다. CloudFormation에 성공 또는 실패를 알리는 대상으로 Amazon Simple Notification Service(Amazon SNS) 토픽을 만듭니다. 라이프사이클 후크에 적절한 시간 초과를 설정합니다.
D. Amazon CloudWatch 에이전트를 사용하여 cloud-init 로그를 스트리밍합니다. 적절한 호출 시간 제한이 있는 AWS Lambda 함수를 포함하는 구독 필터를 만듭니다. Lambda 함수를 구성하여 SignalResource API 작업을 사용하여 CloudFormation에 성공 또는 실패를 알립니다.




### 
질문 #113주제 1
한 회사에 여러 AWS 계정에서 실행되는 데이터 수집 애플리케이션이 있습니다. 계정은 AWS Organizations의 조직에 있습니다. 이 회사는 애플리케이션을 모니터링하고 애플리케이션에 대한 액세스를 통합해야 합니다. 현재 이 회사는 여러 Auto Scaling 그룹의 Amazon EC2 인스턴스에서 애플리케이션을 실행하고 있습니다. EC2 인스턴스는 데이터가 민감하기 때문에 인터넷에 액세스할 수 없습니다. 엔지니어는 필요한 VPC 엔드포인트를 배포했습니다. EC2 인스턴스는 애플리케이션을 위해 특별히 구축된 사용자 지정 AMI를 실행합니다.

애플리케이션을 유지 관리하고 문제를 해결하려면 시스템 관리자가 EC2 인스턴스에 로그인할 수 있어야 합니다. 이 액세스는 자동화되어야 하며 중앙에서 제어되어야 합니다. 인스턴스에 액세스할 때마다 회사의 보안 팀은 알림을 받아야 합니다.

이러한 요구 사항을 충족하는 솔루션은 무엇입니까?

A. 사용자가 EC2 인스턴스에 로그인할 때마다 보안 팀에 알림을 보내는 Amazon EventBridge 규칙을 만듭니다. EC2 Instance Connect를 사용하여 인스턴스에 로그인합니다. AWS CloudFormation을 사용하여 Auto Scaling 그룹을 배포합니다. cfn-init 헬퍼 스크립트를 사용하여 외부 액세스를 위한 적절한 VPC 경로를 배포합니다. 사용자 지정 AMI에 AWS Systems Manager Agent가 포함되도록 사용자 지정 AMI를 다시 빌드합니다.
B. 인터넷 액세스가 가능한 NAT 게이트웨이와 베스천 호스트를 배포합니다. 베스천 호스트에서 모든 EC2 인스턴스로 들어오는 트래픽을 허용하는 보안 그룹을 만듭니다. 모든 EC2 인스턴스에 AWS Systems Manager Agent를 설치합니다. Auto Scaling 그룹 라이프사이클 후크를 사용하여 액세스를 모니터링하고 감사합니다. Systems Manager Session Manager를 사용하여 인스턴스에 로그인합니다. Amazon CloudWatch Logs의 로그 그룹으로 로그를 보냅니다. 감사를 위해 Amazon S3로 데이터를 내보냅니다. S3 이벤트 알림을 사용하여 보안 팀에 알림을 보냅니다.
C. EC2 Image Builder를 사용하여 사용자 지정 AMI를 다시 빌드합니다. 이미지에 최신 버전의 AWS Systems Manager Agent를 포함합니다. 모든 EC2 인스턴스에 AmazonSSMManagedInstanceCore 역할을 연결하도록 Auto Scaling 그룹을 구성합니다. Systems Manager Session Manager를 사용하여 인스턴스에 로그인합니다. Amazon S3에 세션 세부 정보 로깅을 활성화합니다. Amazon Simple Notification Service(Amazon SNS) 주제를 통해 보안 팀에 메시지를 보내기 위해 새 파일 업로드에 대한 S3 이벤트 알림을 만듭니다. 가장 많이 투표된
D. AWS Systems Manager Automation을 사용하여 Systems Manager Agent를 사용자 지정 AMI에 빌드합니다. AWS Config를 구성하여 SCP를 루트 조직 계정에 연결하여 EC2 인스턴스가 Systems Manager에 연결할 수 있도록 합니다. Systems Manager Session Manager를 사용하여 인스턴스에 로그인합니다. Amazon S3에 세션 세부 정보 로깅을 활성화합니다. Amazon Simple Notification Service(Amazon SNS) 토픽을 통해 보안 팀에 메시지를 보내기 위해 새 파일 업로드에 대한 S3 이벤트 알림을 만듭니다.



### 질문 #114주제 1
한 회사가 Amazon S3를 사용하여 독점 정보를 저장합니다. 개발팀은 매일 새로운 프로젝트를 위한 버킷을 만듭니다. 보안팀은 모든 기존 및 미래 버킷에 암호화, 로깅 및 버전 관리가 활성화되어 있는지 확인하려고 합니다. 또한 어떤 버킷도 공개적으로 읽거나 쓸 수 있는 권한이 없어야 합니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 무엇을 해야 합니까?

A. AWS CloudTrail을 활성화하고 AWS Lambda를 사용하여 자동 수정을 구성합니다.
B. AWS Config 규칙을 활성화하고 AWS Systems Manager 문서를 사용하여 자동 수정을 구성합니다. 가장 많이 투표된
C. AWS Trusted Advisor를 활성화하고 Amazon EventBridge를 사용하여 자동 수정을 구성합니다.
D. AWS Systems Manager를 활성화하고 Systems Manager 문서를 사용하여 자동 수정을 구성합니다.



### 질문 #115주제 1
DevOps 엔지니어가 AWS에서 이미지 일괄 처리 클러스터를 구현하는 가장 저렴한 방법을 연구하고 있습니다. 이 애플리케이션은 Docker 컨테이너에서 실행할 수 없으며 Amazon EC2에서 실행해야 합니다. 일괄 작업은 NFS 볼륨에 체크포인트 데이터를 저장하며 중단을 허용할 수 있습니다. 일반 EC2 Linux 이미지에서 클러스터 소프트웨어를 구성하는 데 30분이 걸립니다.

가장 비용 효율적인 솔루션은 무엇입니까?

A. 체크포인트 데이터에 Amazon EFS를 사용합니다. 작업을 완료하려면 EC2 Auto Scaling 그룹과 On-Demand 가격 책정 모델을 사용하여 EC2 인스턴스를 일시적으로 프로비저닝합니다.
B. 체크포인트 데이터에 대해 EC2 인스턴스에서 GlusterFS를 사용합니다. 일괄 작업을 실행하려면 EC2 인스턴스를 수동으로 구성합니다. 작업이 완료되면 인스턴스를 수동으로 종료합니다.
C. 체크포인트 데이터에 Amazon EFS를 사용합니다. EC2 Fleet를 사용하여 EC2 Spot Instances를 시작하고 사용자 데이터를 사용하여 시작 시 EC2 Linux 인스턴스를 구성합니다.
D. 체크포인트 데이터에 Amazon EFS를 사용합니다. EC2 Fleet를 사용하여 EC2 Spot 인스턴스를 시작합니다. 클러스터에 대한 사용자 지정 AMI를 만들고 인스턴스를 만들 때 최신 AMI를 사용합니다. 가장 많이 투표된



### 
8%

질문 #116주제 1
한 회사가 최근 온프레미스에서 AWS로 레거시 애플리케이션을 마이그레이션했습니다. 이 애플리케이션은 Amazon API Gateway 뒤에 있는 애플리케이션 로드 밸런서 뒤의 Amazon EC2 인스턴스에서 호스팅됩니다. 이 회사는 애플리케이션의 새 버전을 배포하는 동안 사용자가 최소한의 중단을 경험하도록 하려고 합니다. 또한 이 회사는 문제가 있는 경우 업데이트를 신속하게 롤백할 수 있도록 하려고 합니다.

어떤 솔루션이 애플리케이션에 최소한의 변경을 가하면서 이러한 요구 사항을 충족할까요?

A. 기존 환경과 병행되는 별도의 환경으로 변경 사항을 도입합니다. API Gateway를 구성하여 canary 릴리스 배포를 사용하여 사용자 트래픽의 작은 하위 집합을 새 환경으로 보냅니다. 가장 많이 투표된
B. 기존 환경과 평행한 별도의 환경으로 변경 사항을 도입합니다. 애플리케이션의 DNS 별칭 레코드를 업데이트하여 새 환경을 가리킵니다.
C. 기존 애플리케이션 로드 밸런서 뒤에 별도의 대상 그룹으로 변경 사항을 도입합니다. API Gateway를 구성하여 사용자 트래픽을 새 대상 그룹으로 단계별로 라우팅합니다.
D. 기존 애플리케이션 로드 밸런서 뒤에 별도의 대상 그룹으로 변경 사항을 도입합니다. 모든 트래픽을 애플리케이션 로드 밸런서로 라우팅하도록 API Gateway를 구성한 다음, 트래픽을 새 대상 그룹으로 보냅니다.



### 질문 #117주제 1
한 회사가 Amazon S3 버킷에 .csv 형식으로 100GB의 로그 데이터를 저장하고 있습니다. SQL 개발자는 이 데이터를 쿼리하고 그래프를 생성하여 시각화하려고 합니다. SQL 개발자는 또한 .csv 파일의 메타데이터를 저장하는 효율적이고 자동화된 방법이 필요합니다.

어떤 단계 조합이 최소한의 노력으로 이러한 요구 사항을 충족할 수 있을까요? (세 가지를 선택하세요.)

A. AWS X-Ray를 통해 데이터를 필터링하여 데이터를 시각화합니다.
B. Amazon QuickSight를 통해 데이터를 필터링하여 데이터를 시각화합니다. 가장 많이 투표된
C. Amazon Athena를 사용하여 데이터를 쿼리합니다. 가장 많이 투표된
D. Amazon Redshift로 데이터를 쿼리합니다.
E. AWS Glue 데이터 카탈로그를 영구 메타데이터 저장소로 사용합니다. 가장 많이 투표된
F. Amazon DynamoDB를 영구 메타데이터 저장소로 사용합니다.



### 질문 #118주제 1
한 회사가 여러 AWS 지역 및 가용성 영역에 걸쳐 AWS에서 기업 인프라를 배포합니다. 인프라는 Amazon EC2 인스턴스에 배포되고 AWS IoT Greengrass 기기와 연결됩니다. 이 회사는 본사에 있는 온프레미스 서버에 추가 리소스를 배포합니다.

이 회사는 리소스 유지 관리 및 업데이트에 관련된 오버헤드를 줄이고자 합니다. 이 회사의 DevOps 팀은 AWS Systems Manager를 사용하여 패치의 자동화된 관리 및 적용을 구현할 계획입니다. DevOps 팀은 리소스가 배포된 지역에서 Systems Manager를 사용할 수 있는지 확인합니다. Systems Manager는 본사 근처 지역에서도 사용할 수 있습니다. DevOps 팀

은 회사의 EC2 인스턴스, IoT 기기 및 온프레미스 인프라에서 자동화된 패치 및 구성 관리를 구현하기 위해 어떤 단계 조합을 취해야 합니까? (세 가지를 선택하십시오.)

A. 모든 EC2 인스턴스, AWS IoT Greengrass 디바이스 및 온프레미스 서버에 태그를 적용합니다. Systems Manager Session Manager를 사용하여 태그가 지정된 모든 디바이스에 패치를 푸시합니다.
B. Systems Manager Run Command를 사용하여 EC2 인스턴스, AWS IoT Greengrass 디바이스 및 온프레미스 서버에 대한 패치를 예약합니다.
C. Systems Manager Patch Manager를 사용하여 EC2 인스턴스, AWS IoT Greengrass 디바이스 및 온프레미스 서버에 대한 패치를 Systems Manager 유지 관리 창 작업으로 예약합니다. 가장 많이 투표된
D. Amazon EventBridge를 구성하여 Systems Manager Patch Manager에서 패치 기준선 업데이트를 모니터링합니다. Systems Manager Run Command를 이벤트와 연결하여 모든 EC2 인스턴스, AWS IoT Greengrass 디바이스 및 온프레미스 서버에 대한 패치 작업을 시작합니다.
E. Systems Manager에 대한 IAM 인스턴스 프로필을 만듭니다. 인스턴스 프로필을 AWS 계정의 모든 EC2 인스턴스에 연결합니다. AWS IoT Greengrass 디바이스와 온프레미스 서버의 경우 Systems Manager에 대한 IAM 서비스 역할을 만듭니다. 가장 많이 투표된
F. 관리형 인스턴스 활성화를 생성합니다. 활성화 코드와 활성화 ID를 사용하여 온프레미스 환경의 각 서버에 Systems Manager Agent(SSM Agent)를 설치합니다. AWS IoT Greengrass IAM 토큰 교환 역할을 업데이트합니다. 이 역할을 사용하여 모든 IoT 디바이스에 SSM Agent를 배포합니다. 가장 많이 투표된



### 질문 #119주제 1
한 회사가 애플리케이션 로드 밸런서 뒤의 Amazon EC2 인스턴스에서 실행되는 웹 애플리케이션을 테스트하고 있습니다. 인스턴스는 여러 가용성 영역에 걸쳐 자동 확장 그룹에서 실행됩니다. 이 회사는 새 소프트웨어를 배포할 때 변경 불가능한 인스턴스가 있는 블루/그린 배포 프로세스를 사용합니다.

테스트하는 동안 사용자는 무작위 시간에 애플리케이션에서 자동으로 로그아웃됩니다. 테스터는 또한 애플리케이션의 새 버전이 배포될 때 모든 사용자가 로그아웃된다고 보고합니다. 개발팀은 확장 이벤트와 애플리케이션 배포에서 사용자가 로그인 상태를 유지하도록 하는 솔루션이 필요합니다.

사용자가 로그인 상태를 유지하도록 하는 가장 운영 효율적인 방법은 무엇입니까?

A. 로드 밸런서에서 스마트 세션을 활성화하고 기존 세션을 확인하도록 애플리케이션을 수정합니다.
B. 로드 밸런서에서 세션 공유를 활성화하고 세션 저장소에서 읽도록 애플리케이션을 수정합니다.
C. Amazon S3 버킷에 사용자 세션 정보를 저장하고 버킷에서 세션 정보를 읽도록 애플리케이션을 수정합니다.
D. Amazon ElastiCache 클러스터에 사용자 세션 정보를 저장하도록 애플리케이션을 수정합니다. 가장 많이 투표된



### 질문 #120주제 1
DevOps 엔지니어는 기존 3계층 애플리케이션에 대한 블루/그린 배포를 구성해야 합니다. 애플리케이션은 Amazon EC2 인스턴스에서 실행되고 Amazon RDS 데이터베이스를 사용합니다. EC2 인스턴스는 ALB(Application Load Balancer) 뒤에서 실행되고 자동 확장 그룹에 있습니다.

DevOps 엔지니어는 블루 환경에 대한 시작 템플릿과 자동 확장 그룹을 만들었습니다. DevOps 엔지니어는 또한 그린 환경에 대한 시작 템플릿과 자동 확장 그룹을 만들었습니다. 각 자동 확장 그룹은 일치하는 블루 또는 그린 대상 그룹에 배포됩니다. 대상 그룹은 또한 EC2 인스턴스에 로드되는 블루 또는 그린 소프트웨어를 지정합니다. ALB는 트래픽을 블루 환경의 대상 그룹 또는 그린 환경의 대상 그룹으로 보내도록 구성할 수 있습니다. www.example.com의 Amazon Route 53 레코드는 ALB를 가리킵니다.

배포는 블루 환경의 EC2 인스턴스에 있는 소프트웨어와 그린 환경의 EC2 인스턴스에 새로 배포된 소프트웨어 간에 트래픽을 한 번에 모두 이동해야 합니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 무엇을 해야 합니까?

A. 그린 환경의 자동 스케일링 그룹의 롤링 재시작을 시작하여 그린 환경의 EC2 인스턴스에 새 소프트웨어를 배포합니다. 롤링 재시작이 완료되면 AWS CLI 명령을 사용하여 ALB를 업데이트하여 그린 환경의 대상 그룹으로 트래픽을 보냅니다. 가장 많이 투표된
B. AWS CLI 명령을 사용하여 ALB를 업데이트하여 트래픽을 그린 환경의 대상 그룹으로 보냅니다. 그런 다음 그린 환경의 자동 확장 그룹의 롤링 재시작을 시작하여 그린 환경의 EC2 인스턴스에 새 소프트웨어를 배포합니다.
C. 시작 템플릿을 업데이트하여 그린 환경의 소프트웨어를 블루 환경의 EC2 인스턴스에 배포합니다. 두 환경 모두에서 대상 그룹과 자동 확장 그룹을 변경하지 않습니다. 블루 환경의 EC2 인스턴스를 롤링 재시작합니다.
D. 그린 환경의 자동 확장 그룹의 롤링 재시작을 시작하여 그린 환경의 EC2 인스턴스에 새 소프트웨어를 배포합니다. 롤링 재시작이 완료되면 Route 53 DNS를 업데이트하여 ALB에서 그린 환경의 엔드포인트를 가리킵니다.




### 질문 #121주제 1
한 회사가 빌드 계정에서 AWS CodePipeline과 AWS CodeBuild를 사용하여 새로운 파이프라인을 빌드하고 있습니다. 파이프라인은 두 단계로 구성되어 있습니다. 첫 번째 단계는 AWS Lambda 함수를 빌드하고 패키징하는 CodeBuild 작업입니다. 두 번째 단계는 개발 환경 계정과 프로덕션 환경 계정이라는 두 개의 다른 AWS 계정에서 작동하는 배포 작업으로 구성되어 있습니다. 배포 단계에서는 CodePipeline이 호출하는 AWS CloudFormation 작업을 사용하여 Lambda 함수에 필요한 인프라를 배포합니다.

DevOps 엔지니어가 CodePipeline 파이프라인을 만들고 Amazon S3(aws/s3 키)에 대한 AWS Key Management Service(AWS KMS) AWS 관리 키를 사용하여 빌드 아티팩트를 암호화하도록 파이프라인을 구성합니다. 아티팩트는 S3 버킷에 저장됩니다. 파이프라인이 실행되면 CloudFormation 작업이 액세스 거부 오류와 함께 실패합니다.

DevOps 엔지니어가 이 오류를 해결하기 위해 수행해야 하는 작업 조합은 무엇입니까? (두 가지를 선택하세요.)

A. 아티팩트에 대한 각 AWS 계정에서 S3 버킷을 만듭니다. 파이프라인이 S3 버킷에 쓸 수 있도록 합니다. CodePipeline S3 작업을 만들어 각 AWS 계정의 S3 버킷에 아티팩트를 복사합니다. CloudFormation 작업을 업데이트하여 프로덕션 계정의 아티팩트 S3 버킷을 참조합니다.
B. 고객 관리 KMS 키를 만듭니다. CloudFormation 작업에서 사용하는 IAM 역할이 암호 해독 작업을 수행할 수 있도록 KMS 키 정책을 구성합니다. 고객 관리 KMS 키를 사용하여 아티팩트를 암호화하도록 파이프라인을 수정합니다. 가장 많이 투표된
C. AWS 관리형 KMS 키를 만듭니다. 개발 계정과 프로덕션 계정이 암호 해독 작업을 수행할 수 있도록 KMS 키 정책을 구성합니다. 파이프라인을 수정하여 KMS 키를 사용하여 아티팩트를 암호화합니다.
D. 개발 계정과 프로덕션 계정에서 CodePipeline에 대한 IAM 역할을 만듭니다. CloudFormation 작업을 수행할 수 있는 권한과 아티팩트 S3 버킷에서 객체를 검색하고 복호화할 수 있는 권한이 있는 역할을 구성합니다. CodePipeline 계정에서 역할을 사용하도록 CodePipeline CloudFormation 작업을 구성합니다.
E. 개발 계정과 프로덕션 계정에서 CodePipeline에 대한 IAM 역할을 만듭니다. CloudFormation 작업을 수행할 수 있는 권한과 아티팩트 S3 버킷에서 객체를 검색하고 복호화할 수 있는 권한이 있는 역할을 구성합니다. CodePipeline 계정에서 역할 액세스를 허용하도록 아티팩트 S3 버킷 정책을 수정합니다. 역할을 사용하도록 CodePipeline CloudFormation 작업을 구성합니다. 가장 많이 투표된



### 질문 #122주제 1
한 회사가 AWS Organizations에서 조직을 사용하여 여러 AWS 계정을 관리하고 있습니다. 이 회사의 개발팀은 AWS Lambda 함수를 사용하여 복원성 요구 사항을 충족하고자 하며 VPC에 배포된 Lambda 함수와 작동하도록 모든 애플리케이션을 다시 작성하고 있습니다. 개발팀은 조직의 계정 A에서 공유 스토리지로 Amazon Elastic File System(Amazon EFS)을 사용하고 있습니다.

이 회사는 Lambda와 함께 Amazon EFS를 계속 사용하려고 합니다. 회사 정책에 따라 모든 서버리스 프로젝트는 계정 B에 배포해야 합니다.

DevOps 엔지니어는 기존 EFS 파일 시스템을 재구성하여 Lambda 함수가 기존 EFS 액세스 지점을 통해 데이터에 액세스할 수 있도록 해야 합니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 어떤 단계 조합을 취해야 합니까? (세 가지를 선택하세요.)

A. EFS 파일 시스템 정책을 업데이트하여 계정 B가 계정 A의 EFS 파일 시스템을 마운트하고 쓸 수 있는 액세스 권한을 부여합니다. 가장 많이 투표된
B. Amazon EFS에 대한 세부적인 제어를 통해 권한 보호 장치를 설정하기 위해 SCP를 만듭니다.
C. 계정 B에 새 EFS 파일 시스템을 만듭니다. AWS Database Migration Service(AWS DMS)를 사용하여 계정 A와 계정 B의 데이터를 동기화합니다.
D. VPC 및 EFS 파일 시스템에 액세스할 수 있는 권한으로 Lambda 실행 역할을 업데이트합니다. 가장 많이 투표된
E. 계정 A를 계정 B에 연결하기 위해 VPC 피어링 연결을 생성합니다. 가장 많이 투표된
F. 계정 B에서 Lambda 함수를 구성하여 계정 A의 기존 IAM 역할을 맡습니다.



### 질문 #123주제 1
미디어 회사가 AWS 계정에 수천 개의 Amazon EC2 인스턴스를 보유하고 있습니다. 이 회사는 Slack과 공유 이메일 받은 편지함을 사용하여 팀 커뮤니케이션과 중요한 업데이트를 진행합니다. DevOps 엔지니어는 모든 AWS 예약 EC2 유지 관리 알림을 Slack 채널과 공유 받은 편지함으로 보내야 합니다. 솔루션에는 인스턴스의 이름과 소유자 태그가 포함되어야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS Trusted Advisor를 AWS Config와 통합합니다. AWS Lambda 함수를 호출하여 Amazon Simple Notification Service(Amazon SNS) 토픽에 알림을 게시하도록 사용자 지정 AWS Config 규칙을 구성합니다. Slack 채널 엔드포인트와 공유된 받은 편지함을 토픽에 구독합니다.
B. Amazon EventBridge를 사용하여 AWS Health 이벤트를 모니터링합니다. Amazon Simple Notification Service(Amazon SNS) 주제를 대상으로 유지 관리 이벤트를 구성합니다. AWS Lambda 함수를 SNS 주제에 구독하여 Slack 채널과 공유 받은 편지함에 알림을 보냅니다. 가장 많이 투표된
C. EC2 유지 관리 알림을 Slack 채널과 공유 받은 편지함으로 보내는 AWS Lambda 함수를 만듭니다. Amazon CloudWatch 메트릭을 사용하여 EC2 상태 이벤트를 모니터링합니다. 유지 관리 알림을 받으면 Lambda 함수를 호출하는 CloudWatch 알람을 구성합니다.
D. AWS CloudTrail과 AWS Support 통합을 구성합니다. CloudTrail 조회 이벤트를 생성하여 AWS Lambda 함수를 호출하여 EC2 유지 관리 알림을 Amazon Simple Notification Service(Amazon SNS)로 전달합니다. Amazon SNS를 구성하여 Slack 채널과 공유 받은 편지함을 타겟팅합니다.



### 질문 #124주제 1
AWS CodePipeline 파이프라인은 코드 릴리스 프로세스를 구현했습니다. 파이프라인은 AWS CodeDeploy와 통합되어 각 CodePipeline 단계에 대해 여러 Amazon EC2 인스턴스에 애플리케이션 버전을 배포합니다.

최근 배포 중에 파이프라인이 CodeDeploy 문제로 인해 실패했습니다. DevOps 팀은 배포 중 모니터링 및 알림을 개선하여 해결 시간을 단축하고자 합니다.

DevOps 엔지니어는 문제가 발견될 때 알림을 생성하기 위해 무엇을 해야 합니까?

A. CodePipeline 및 CodeDeploy에 대한 Amazon CloudWatch Logs를 구현하고, 코드 배포 문제를 평가하기 위한 AWS Config 규칙을 생성하고, 배포 문제를 이해 관계자에게 알리기 위한 Amazon Simple Notification Service(Amazon SNS) 주제를 생성합니다.
B. CodePipeline 및 CodeDeploy에 대해 Amazon EventBridge를 구현하고, 코드 배포 문제를 평가하는 AWS Lambda 함수를 생성하고, 배포 문제를 이해 관계자에게 알리는 Amazon Simple Notification Service(Amazon SNS) 주제를 생성합니다. 가장 많이 투표된
C. AWS CloudTrail을 구현하여 CodePipeline 및 CodeDeploy API 호출 정보를 기록하고, 코드 배포 문제를 평가하는 AWS Lambda 함수를 생성하고, Amazon Simple Notification Service(Amazon SNS) 주제를 생성하여 이해 관계자에게 배포 문제를 알립니다.
D. CodePipeline 및 CodeDeploy에 대해 Amazon EventBridge를 구현하고, 코드 배포 문제를 평가하기 위한 Amazon Inspector 평가 대상을 생성하고, 배포 문제를 이해 관계자에게 알리기 위한 Amazon Simple Notification Service(Amazon SNS) 주제를 생성합니다.



### 질문 #125주제 1
글로벌 회사는 AWS Control Tower를 사용하여 여러 AWS 계정을 관리합니다. 이 회사는 내부 애플리케이션과 퍼블릭 애플리케이션을 호스팅합니다.

회사의 각 애플리케이션 팀은 애플리케이션 호스팅을 위한 자체 AWS 계정을 가지고 있습니다. 계정은 AWS Organizations의 조직에 통합됩니다. AWS Control Tower 멤버 계정 중 하나는 애플리케이션 팀이 해당 대상 AWS 계정에 애플리케이션을 배포하는 데 사용하는 CI/CD 파이프라인이 있는 중앙 집중식 DevOps 계정 역할을 합니다. 중앙 집중식 DevOps 계정에 배포를 위한 IAM 역할이 있습니다.

애플리케이션 팀은 애플리케이션 AWS 계정의 Amazon Elastic Kubernetes Service(Amazon EKS) 클러스터에 애플리케이션을 배포하려고 합니다. 애플리케이션 AWS 계정에 배포를 위한 IAM 역할이 있습니다. 배포는 중앙 집중식 DevOps 계정에 설정된 AWS CodeBuild 프로젝트를 통해 이루어집니다. CodeBuild 프로젝트는 CodeBuild에 대한 IAM 서비스 역할을 사용합니다. CodeBuild에서 교차 계정 EKS 클러스터에 연결하려고 시도하는 동안 배포가 권한 없음 오류로 실패합니다.

이 오류를 해결하는 솔루션은 무엇입니까?

A. 중앙화된 DevOps 계정과 신뢰 관계를 갖도록 애플리케이션 계정의 배포 IAM 역할을 구성합니다. sts:AssumeRole 작업을 허용하도록 신뢰 관계를 구성합니다. EKS 클러스터에 필요한 액세스 권한을 갖도록 애플리케이션 계정의 배포 IAM 역할을 구성합니다. EKS 클러스터 aws-auth ConfigMap을 구성하여 역할을 적절한 시스템 권한에 매핑합니다. 가장 많이 투표된
B. 중앙화된 DevOps 계정의 배포 IAM 역할을 구성하여 애플리케이션 계정과 신뢰 관계를 맺습니다. sts:AssumeRole 작업을 허용하도록 신뢰 관계를 구성합니다. 중앙화된 DevOps 계정의 배포 IAM 역할을 구성하여 CodeBuild에 필요한 액세스를 허용합니다.
C. 중앙화된 DevOps 계정의 배포 IAM 역할을 구성하여 애플리케이션 계정과 신뢰 관계를 갖도록 합니다. sts:AssumeRoleWithSAML 작업을 허용하도록 신뢰 관계를 구성합니다. 중앙화된 DevOps 계정의 배포 IAM 역할을 구성하여 CodeBuild에 필요한 액세스를 허용합니다.
D. 애플리케이션 계정의 배포 IAM 역할을 AWS Control Tower 관리 계정과 신뢰 관계를 갖도록 구성합니다. sts:AssumeRole 작업을 허용하도록 신뢰 관계를 구성합니다. 애플리케이션 계정의 배포 IAM 역할을 구성하여 EKS 클러스터에 필요한 액세스 권한을 갖도록 구성합니다. EKS 클러스터 aws-auth ConfigMap을 구성하여 역할을 적절한 시스템 권한에 매핑합니다.



### 질문 #126주제 1
엄격하게 규제되는 한 회사에서는 DevOps 엔지니어가 비상 시를 제외하고는 Amazon EC2 인스턴스에 로그인해서는 안 된다는 정책을 가지고 있습니다. DevOps 엔지니어가 로그인하는 경우 보안팀은 발생 후 15분 이내에 알림을 받아야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 각 EC2 인스턴스에 Amazon Inspector 에이전트를 설치합니다. Amazon EventBridge 알림을 구독합니다. AWS Lambda 함수를 호출하여 메시지가 사용자 로그인에 대한 것인지 확인합니다. 그렇다면 Amazon SNS를 사용하여 보안 팀에 알림을 보냅니다.
B. 각 EC2 인스턴스에 Amazon CloudWatch 에이전트를 설치합니다. 에이전트를 구성하여 모든 로그를 Amazon CloudWatch Logs에 푸시하고 사용자 로그인을 검색하는 CloudWatch 메트릭 필터를 설정합니다. 로그인이 발견되면 Amazon SNS를 사용하여 보안 팀에 알림을 보냅니다. 가장 많이 투표된
C. Amazon CloudWatch Logs로 AWS CloudTrail을 설정합니다. CloudWatch Logs를 Amazon Kinesis에 구독합니다. AWS Lambda를 Kinesis에 연결하여 로그에 사용자 로그인이 포함되어 있는지 구문 분석하고 확인합니다. 포함되어 있으면 Amazon SNS를 사용하여 보안 팀에 알림을 보냅니다.
D. 각 Amazon EC2 인스턴스에 스크립트를 설정하여 모든 로그를 Amazon S3에 푸시합니다. AWS Lambda 함수를 호출하는 S3 이벤트를 설정하여 Amazon Athena 쿼리를 호출하여 실행합니다. Athena 쿼리는 로그인을 확인하고 Amazon SNS를 사용하여 보안 팀에 출력을 보냅니다.



### 질문 #127주제 1
한 회사가 중요한 비즈니스 애플리케이션에 대한 AWS CloudFormation 템플릿을 업데이트했습니다. 업데이트된 템플릿의 오류로 인해 스택 업데이트 프로세스가 실패했고, AWS CloudFormation이 자동으로 스택 롤백 프로세스를 시작했습니다. 나중에 DevOps 엔지니어가 애플리케이션을 여전히 사용할 수 없고 스택이 UPDATE_ROLLBACK_FAILED 상태임을 발견했습니다. DevOps

엔지니어가 스택 롤백을 성공적으로 완료하려면 어떤 작업 조합을 수행해야 합니까? (두 가지를 선택하세요.)

A. AWSCloudFormationFullAccess IAM 정책을 AWS CloudFormation 역할에 연결합니다.
B. AWS CloudFormation 드리프트 감지를 사용하여 스택 리소스를 자동으로 복구합니다.
C. AWS CloudFormation 콘솔이나 AWS CLI에서 ContinueUpdateRollback 명령을 실행합니다. 가장 많이 투표된
D. 스택의 기대치에 맞춰 리소스를 수동으로 조정합니다. 가장 많이 투표된
E. 원래 템플릿을 사용하여 기존 AWS CloudFormation 스택을 업데이트합니다.



### 질문 #128주제 1
개발팀은 로컬에서 아티팩트를 수동으로 빌드한 다음 Amazon S3 버킷에 넣습니다. 애플리케이션에는 배포가 발생할 때 지워야 하는 로컬 캐시가 있습니다. 팀은 이를 위해 명령을 실행하고 Amazon S3에서 아티팩트를 다운로드한 다음 아티팩트의 압축을 풀어 배포를 완료합니다.

DevOps팀은 CI/CD 프로세스로 마이그레이션하고 오류가 발생할 때 배포를 중지하고 롤백하는 검사를 빌드하려고 합니다. 이를 위해 팀은 배포 진행 상황을 추적해야 합니다.

어떤 작업 조합이 이를 달성할 수 있을까요? (세 가지를 선택하세요.)

A. 개발자가 코드를 코드 저장소에 체크인할 수 있도록 합니다. Amazon EventBridge를 사용하여 메인 브랜치로 가져올 때마다 AWS Lambda 함수를 호출하여 아티팩트를 빌드하고 Amazon S3에 저장합니다.
B. 캐시를 지우기 위한 사용자 지정 스크립트를 만듭니다. AppSpec 파일의 BeforeInstall 라이프사이클 후크에 스크립트를 지정합니다. 가장 많이 투표된
C. 캐시 지우기 스크립트가 포함된 각 Amazon EC2 인스턴스에 대한 사용자 데이터를 만듭니다. 배포되면 애플리케이션을 테스트합니다. 성공하지 못하면 다시 배포합니다.
D. AWS CodePipeline을 설정하여 애플리케이션을 배포합니다. 개발자가 파이프라인의 소스로 코드 저장소에 코드를 체크인할 수 있도록 허용합니다. 가장 많이 투표된
E. AWS CodeBuild를 사용하여 아티팩트를 빌드하고 Amazon S3에 배치합니다. AWS CodeDeploy를 사용하여 아티팩트를 Amazon EC2 인스턴스에 배포합니다. 가장 많이 투표된
F. AWS Systems Manager를 사용하여 Amazon S3에서 아티팩트를 가져와 모든 인스턴스에 배포합니다.



### 질문 #129주제 1
DevOps 엔지니어가 Amazon Linux에서 호스팅되는 프로젝트를 진행 중이며 보안 검토에 실패했습니다. DevOps 관리자는 AWS CodeBuild 프로젝트에 대한 회사 buildspec.yaml 파일을 검토하고 권장 사항을 제공하라는 요청을 받았습니다. buildspec.yaml 파일은 다음과 같이 구성되어 있습니다.



AWS 보안 모범 사례를 준수하기 위해 어떤 변경 사항을 권장해야 합니까? (세 가지를 선택하세요.)

A. 다른 CodeBuild 사용자가 해당 파일을 볼 수 없도록 종료 전에 컨테이너에서 임시 파일을 제거하는 빌드 후 명령을 추가합니다.
B. 필요한 권한으로 CodeBuild 프로젝트 역할을 업데이트한 다음 환경 변수에서 AWS 자격 증명을 제거합니다. 가장 많이 투표된
C. AWS Systems Manager Parameter Store에 DB_PASSWORD를 SecureString 값으로 저장한 다음 환경 변수에서 DB_PASSWORD를 제거합니다. 가장 많이 투표된
D. 환경 변수를 'db-deploy-bucket' Amazon S3 버킷으로 이동하고, 다운로드할 사전 빌드 단계를 추가한 다음 변수를 내보냅니다.
E. AWS Systems Manager run 명령을 사용하여 scp 및 ssh 명령을 인스턴스에 직접 사용합니다. 가장 많이 투표된
F. XOR을 사용한 후 Base64를 사용하여 환경 변수를 섞고 설치할 섹션을 추가한 다음 XOR과 Base64를 빌드 단계에 실행합니다.



### 질문 #130주제 1
회사에 레거시 애플리케이션이 있습니다. DevOps 엔지니어는 레거시 애플리케이션의 배포 가능한 아티팩트를 빌드하는 프로세스를 자동화해야 합니다. 솔루션은 향후 배포에서 참조할 수 있도록 배포 가능한 아티팩트를 기존 Amazon S3 버킷에 저장해야 합니다.

어떤 솔루션이 가장 운영적으로 효율적인 방식으로 이러한 요구 사항을 충족할까요?

A. 레거시 애플리케이션의 모든 종속성을 포함하는 사용자 지정 Docker 이미지를 만듭니다. 사용자 지정 Docker 이미지를 새 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에 저장합니다. 사용자 지정 Docker 이미지를 사용하여 배포 가능한 아티팩트를 빌드하고 아티팩트를 S3 버킷에 저장하도록 새 AWS CodeBuild 프로젝트를 구성합니다. 가장 많이 투표된
B. 새 Amazon EC2 인스턴스를 시작합니다. EC2 인스턴스에 레거시 애플리케이션의 모든 종속성을 설치합니다. EC2 인스턴스를 사용하여 배포 가능한 아티팩트를 빌드하고 아티팩트를 S3 버킷에 저장합니다.
C. 사용자 지정 EC2 Image Builder 이미지를 만듭니다. 이미지에 레거시 애플리케이션의 모든 종속성을 설치합니다. 이미지에서 새 Amazon EC2 인스턴스를 시작합니다. 새 EC2 인스턴스를 사용하여 배포 가능한 아티팩트를 빌드하고 아티팩트를 S3 버킷에 저장합니다.
D. 여러 가용성 영역에서 실행되는 AWS Fargate 프로필이 있는 Amazon Elastic Kubernetes Service(Amazon EKS) 클러스터를 만듭니다. 레거시 애플리케이션의 모든 종속성을 포함하는 사용자 지정 Docker 이미지를 만듭니다. 사용자 지정 Docker 이미지를 새 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에 저장합니다. EKS 클러스터 내부의 사용자 지정 Docker 이미지를 사용하여 배포 가능한 아티팩트를 빌드하고 아티팩트를 S3 버킷에 저장합니다.



### 질문 #131주제 1
한 회사가 Docker 명령을 실행하여 AWS CodeBuild 프로젝트에서 컨테이너 이미지를 빌드합니다. 컨테이너 이미지가 빌드된 후 CodeBuild 프로젝트는 컨테이너 이미지를 Amazon S3 버킷에 업로드합니다. CodeBuild 프로젝트에는 S3 버킷에 액세스할 수 있는 권한이 있는 IAM 서비스 역할이 있습니다.

DevOps 엔지니어는 컨테이너 이미지를 저장하기 위해 S3 버킷을 Amazon Elastic Container Registry(Amazon ECR) 리포지토리로 바꿔야 합니다. DevOps 엔지니어는 CodeBuild 프로젝트의 동일한 AWS 리전에 ECR 비공개 이미지 리포지토리를 만듭니다. DevOps 엔지니어는 새 ECR 리포지토리에서 작업하는 데 필요한 권한으로 IAM 서비스 역할을 조정합니다. DevOps 엔지니어는 또한 buildspec.yml 파일에서 사용되는 docker build 명령과 docker push 명령에 새 리포지토리 정보를 넣습니다.

CodeBuild 프로젝트에서 빌드 작업을 실행하면 작업이 ECR 리포지토리에 액세스하려고 하면 작업이 실패합니다.

ECR 리포지토리에 대한 액세스 실패 문제를 해결하는 솔루션은 무엇입니까?

A. buildspec.yml 파일을 업데이트하여 aws ecr get-login-password AWS CLI 명령을 사용하여 ECR 저장소에 로그인하여 인증 토큰을 얻습니다. docker login 명령을 업데이트하여 인증 토큰을 사용하여 ECR 저장소에 액세스합니다. 가장 많이 투표된
B. CodeBuild 프로젝트에 SECRETS_MANAGER 유형의 환경 변수를 추가합니다. 환경 변수에 CodeBuild 프로젝트의 IAM 서비스 역할의 ARN을 포함합니다. buildspec.yml 파일을 업데이트하여 새 환경 변수를 사용하여 docker login 명령으로 로그인하여 ECR 저장소에 액세스합니다.
C. ECR 저장소를 공개 이미지 저장소로 업데이트합니다. IAM 서비스 역할이 액세스할 수 있도록 허용하는 ECR 저장소 정책을 추가합니다.
D. AWS CLI를 사용하여 ECR 작업에 대한 IAM 서비스 역할을 맡도록 buildspec.yml 파일을 업데이트합니다. IAM 서비스 역할이 액세스할 수 있도록 허용하는 ECR 저장소 정책을 추가합니다.



### 질문 #132주제 1
회사에서 직원의 IAM 액세스를 수동으로 프로비저닝합니다. 회사에서는 수동 프로세스를 자동화된 프로세스로 대체하려고 합니다. 회사에는 외부 SAML 2.0 ID 공급자(IdP)로 구성된 기존 Active Directory 시스템이 있습니다.

회사에서는 직원이 기존 회사 자격 증명을 사용하여 AWS에 액세스하기를 원합니다. 기존 Active Directory 시스템의 그룹은 AWS Identity and Access Management(IAM)에서 권한 관리를 위해 사용할 수 있어야 합니다. DevOps 엔지니어가 회사의 AWS 계정에서 AWS IAM Identity Center(AWS Single Sign-On)의 초기 구성을 완료했습니다.

DevOps 엔지니어는 요구 사항을 충족하기 위해 다음에 무엇을 해야 합니까?

A. 외부 IdP를 ID 소스로 구성합니다. SCIM 프로토콜을 사용하여 사용자 및 그룹의 자동 프로비저닝을 구성합니다. 가장 많이 투표된
B. AWS Directory Service를 ID 소스로 구성합니다. SAML 프로토콜을 사용하여 사용자 및 그룹의 자동 프로비저닝을 구성합니다.
C. AD 커넥터를 ID 소스로 구성합니다. SCIM 프로토콜을 사용하여 사용자 및 그룹의 자동 프로비저닝을 구성합니다.
D. 외부 IdP를 ID 소스로 구성합니다. SAML 프로토콜을 사용하여 사용자 및 그룹의 자동 프로비저닝을 구성합니다.



### 질문 #133주제 1
한 회사가 AWS를 사용하여 디지털 워크로드를 실행하고 있습니다. 회사의 각 애플리케이션 팀은 애플리케이션 호스팅을 위한 자체 AWS 계정을 가지고 있습니다. 계정은 AWS Organizations의 조직에 통합되어 있습니다.

이 회사는 전체 조직에서 보안 표준을 시행하고자 합니다. 보안 오류로 인한 불이행을 방지하기 위해 이 회사는 AWS CloudFormation 사용을 시행했습니다. 프로덕션 지원 팀은 AWS Management Console을 사용하여 프로덕션 환경의 리소스를 수정하여 애플리케이션 관련 문제를 해결하고 문제를 해결할 수 있습니다.

DevOps 엔지니어는 불이행으로 이어지는 AWS 서비스 오류 구성을 거의 실시간으로 식별하는 솔루션을 구현해야 합니다. 이 솔루션은 식별 후 15분 이내에 문제를 자동으로 해결해야 합니다. 또한 이 솔루션은 정확한 타임스탬프가 있는 중앙 대시보드에서 불이행 리소스와 이벤트를 추적해야 합니다.

어떤 솔루션이 이러한 요구 사항을 가장 적은 개발 오버헤드로 충족할까요?

A. CloudFormation 드리프트 감지를 사용하여 비준수 리소스를 식별합니다. CloudFormation의 드리프트 감지 이벤트를 사용하여 수정을 위해 AWS Lambda 함수를 호출합니다. Lambda 함수를 구성하여 Amazon CloudWatch Logs 로그 그룹에 로그를 게시합니다. Amazon CloudWatch 대시보드를 구성하여 추적을 위해 로그 그룹을 사용합니다.
B. AWS 계정에서 AWS CloudTrail을 켭니다. Amazon Athena를 사용하여 CloudTrail 로그를 분석하여 비준수 리소스를 식별합니다. AWS Step Functions를 사용하여 Athena에서 드리프트 감지를 위한 쿼리 결과를 추적하고 수정을 위해 AWS Lambda 함수를 호출합니다. 추적을 위해 Athena를 데이터 소스로 사용하는 Amazon QuickSight 대시보드를 설정합니다.
C. 모든 AWS 계정에서 AWS Config의 구성 레코더를 켜서 비준수 리소스를 식별합니다. 모든 AWS 계정에서 --no-enable-default-standards 옵션으로 AWS Security Hub를 활성화합니다. AWS Config 관리 규칙과 사용자 지정 규칙을 설정합니다. AWS Config 적합성 팩을 사용하여 자동 수정을 설정합니다. 추적을 위해 지정된 Security Hub 관리자 계정에서 Security Hub에 대시보드를 설정합니다. 가장 많이 투표된
D. AWS 계정에서 AWS CloudTrail을 켭니다. Amazon CloudWatch Logs를 사용하여 CloudTrail 로그를 분석하여 규정을 준수하지 않는 리소스를 식별합니다. CloudWatch Logs 필터를 사용하여 드리프트 감지합니다. Amazon EventBridge를 사용하여 Lambda 함수를 호출하여 수정합니다. 필터링된 CloudWatch 로그를 Amazon OpenSearch Service로 스트리밍합니다. 추적을 위해 OpenSearch Service에 대시보드를 설정합니다.



### 질문 #134주제 1
한 회사에서 AWS Organizations를 사용하여 AWS 계정을 관리합니다. 조직 루트에는 Environments라는 OU가 있습니다. Environments OU에는 각각 Development와 Production이라는 두 개의 자식 OU가 있습니다.

Environments OU와 자식 OU에는 기본 FullAWSAccess 정책이 있습니다. DevOps 엔지니어는 Development OU에서 FullAWSAccess 정책을 제거하고 Amazon EC2 리소스에서 모든 작업을 허용하는 정책으로 정책을 대체할 계획입니다.

이 정책 대체의 결과는 무엇일까요?

A. 개발 OU의 모든 사용자는 모든 리소스에 대한 모든 API 작업이 허용됩니다.
B. 개발 OU의 모든 사용자는 EC2 리소스에서 모든 API 작업이 허용됩니다. 다른 모든 API 작업은 거부됩니다. 가장 많이 투표된
C. 개발 OU의 모든 사용자는 모든 리소스에 대한 모든 API 작업이 거부됩니다.
D. 개발 OU의 모든 사용자는 EC2 리소스에서 모든 API 작업이 거부됩니다. 다른 모든 API 작업은 허용됩니다.



### 질문 #135주제 1
한 회사가 재해 복구 기능을 검토하고 있으며 일상적인 운영을 보조 AWS 지역으로 전환할 수 있는 기능을 원합니다. 이 회사는 기본 지역에서 AWS CodeCommit을 소스 제어 도구로 사용합니다.

DevOps 엔지니어는 회사가 보조 지역에서 코드를 개발할 수 있는 기능을 제공해야 합니다. 회사가 보조 지역을 사용해야 하는 경우 개발자는 로컬 Git 구성에 추가 원격 URL을 추가할 수 있습니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 보조 리전에 CodeCommit 리포지토리를 만듭니다. AWS CodeBuild 프로젝트를 만들어 기본 리전의 CodeCommit 리포지토리를 보조 리전의 CodeCommit 리포지토리로 Git 미러링 작업을 수행합니다. CodeBuild 프로젝트를 호출하는 AWS Lambda 함수를 만듭니다. 기본 리전의 CodeCommit 리포지토리에서 병합 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. Lambda 함수를 호출하도록 EventBridge 규칙을 구성합니다. 가장 많이 투표된
B. 보조 리전에 Amazon S3 버킷을 만듭니다. AWS Fargate 작업을 만들어 기본 리전의 CodeCommit 리포지토리의 Git 미러 작업을 수행하고 결과를 S3 버킷에 복사합니다. Fargate 작업을 시작하는 AWS Lambda 함수를 만듭니다. CodeCommit 리포지토리의 병합 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. Lambda 함수를 호출하도록 EventBridge 규칙을 구성합니다.
C. 보조 리전에 AWS CodeArtifact 리포지토리를 만듭니다. 소스 작업에 기본 리전의 CodeCommit 리포지토리를 사용하는 AWS CodePipeline 파이프라인을 만듭니다. 파이프라인에 CodeCommit 리포지토리 콘텐츠를 패키징하고 풀 요청이 CodeCommit 리포지토리에 병합될 때 CodeArtifact 리포지토리에 콘텐츠를 저장하는 크로스 리전 단계를 만듭니다.
D. AWS Cloud9 환경과 보조 리전에 CodeCommit 리포지토리를 만듭니다. AWS Cloud9 환경에서 기본 리전의 CodeCommit 리포지토리를 원격 리포지토리로 구성합니다. 보조 리전의 CodeCommit 리포지토리를 AWS Cloud9 환경에 연결합니다.



### 질문 #136주제 1
DevOps 팀은 프로덕션 데이터베이스에 Amazon RDS Multi-AZ DB 클러스터를 사용하는 애플리케이션의 코드 개정을 병합하고 있습니다. DevOps 팀은 지속적인 통합을 사용하여 애플리케이션이 작동하는지 주기적으로 확인합니다. DevOps 팀은 프로덕션 데이터베이스에 변경 사항을 배포하기 전에 변경 사항을 테스트해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS CodeBuild의 buildspec 파일을 사용하여 프로덕션 데이터베이스의 스냅샷에서 DB 클러스터를 복원하고 통합 테스트를 실행한 후 확인 후 복원된 데이터베이스를 삭제합니다. 가장 많이 투표된
B. 애플리케이션을 프로덕션에 배포합니다. 검증이 실패할 경우 수행할 데이터베이스 활동을 캡처하기 위해 데이터 제어 언어(DCL) 작업의 감사 로그를 구성합니다.
C. 애플리케이션을 배포하기 전에 DB 클러스터의 스냅샷을 만듭니다. AWS CloudFormation의 DB 인스턴스에서 Update needs:Replacement 속성을 사용하여 애플리케이션을 배포하고 변경 사항을 적용합니다.
D. DB 클러스터가 Multi-AZ 배포인지 확인합니다. 업데이트와 함께 애플리케이션을 배포합니다. 검증이 실패하면 대기 인스턴스로 페일오버합니다.



### 질문 #137주제 1
한 회사가 VPC에서 멀티 테넌트 환경을 관리하고 해당 AWS 계정에 대해 Amazon GuardDuty를 구성했습니다. 이 회사는 모든 GuardDuty 결과를 AWS Security Hub로 보냅니다.

의심스러운 출처의 트래픽이 많은 수의 결과를 생성합니다. DevOps 엔지니어는 GuardDuty가 새로운 의심스러운 출처를 발견하면 전체 VPC에서 트래픽을 자동으로 거부하는 솔루션을 구현해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. GuardDuty 위협 목록을 만듭니다. GuardDuty가 목록을 참조하도록 구성합니다. 위협 목록을 업데이트하는 AWS Lambda 함수를 만듭니다. GuardDuty에서 나오는 새로운 Security Hub 결과에 응답하여 실행되도록 Lambda 함수를 구성합니다.
B. 사용자 지정 규칙 그룹을 포함하는 AWS WAF 웹 ACL을 구성합니다. 사용자 지정 규칙 그룹에서 차단 규칙을 만드는 AWS Lambda 함수를 만듭니다. GuardDuty에서 나오는 새로운 Security Hub 결과에 응답하여 실행되도록 Lambda 함수를 구성합니다.
C. AWS Network Firewall에서 방화벽을 구성합니다. 방화벽 정책에서 Drop 작업 규칙을 만드는 AWS Lambda 함수를 만듭니다. GuardDuty에서 나오는 새로운 Security Hub 결과에 응답하여 실행되도록 Lambda 함수를 구성합니다. 가장 많이 투표된
D. GuardDuty 억제 규칙을 생성하는 AWS Lambda 함수를 만듭니다. GuardDuty에서 나오는 새로운 Security Hub 결과에 대한 응답으로 실행되도록 Lambda 함수를 구성합니다.



### 질문 #138주제 1
한 회사에서 AWS Secrets Manager를 사용하여 AWS Lambda 함수가 사용하는 민감한 API 키 세트를 저장합니다. Lambda 함수가 호출되면 Lambda 함수는 API 키를 검색하고 외부 서비스에 API 호출을 합니다. Secrets Manager 비밀은 기본 AWS Key Management Service(AWS KMS) 키로 암호화됩니다.

DevOps 엔지니어는 Lambda 함수의 실행 역할만 Secrets Manager의 값에 액세스할 수 있도록 인프라를 업데이트해야 합니다. 솔루션은 최소 권한의 원칙을 적용해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. Secrets Manager의 기본 KMS 키를 업데이트하여 Lambda 함수의 실행 역할만 암호를 해독할 수 있도록 합니다.
B. Secrets Manager를 신뢰하고 Lambda 함수의 실행 역할이 암호를 해독할 수 있도록 하는 KMS 고객 관리 키를 만듭니다. Secrets Manager를 업데이트하여 새 고객 관리 키를 사용합니다. 가장 많이 투표된
C. Secrets Manager를 신뢰하고 계정의 루트 주체가 암호를 해독할 수 있도록 하는 KMS 고객 관리 키를 만듭니다. Secrets Manager를 업데이트하여 새 고객 관리 키를 사용합니다.
D. Lambda 함수의 실행 역할에 리소스 수준에서 범위가 지정된 KMS 권한이 있는지 확인합니다. KMS 키가 Secrets Manager 비밀을 암호화할 수 있도록 권한을 구성합니다. 가장 많이 투표된
E. Lambda 함수 실행 역할에서 모든 KMS 권한을 제거합니다.



### 질문 #139주제 1
한 회사의 DevOps 엔지니어가 Amazon Simple Notification Service(Amazon SNS) 토픽의 알림을 처리하는 AWS Lambda 함수를 만들고 있습니다. Lambda 함수는 알림 메시지를 처리하고 알림 메시지의 내용을 Amazon RDS Multi-AZ DB 인스턴스에 씁니다.

테스트 중에 데이터베이스 관리자가 실수로 DB 인스턴스를 종료했습니다. 데이터베이스가 다운된 동안 회사는 그 시간 동안 전달된 여러 SNS 알림 메시지를 잃었습니다.

DevOps 엔지니어는 앞으로 알림 메시지가 손실되는 것을 방지해야 합니다.

어떤 솔루션이 이 요구 사항을 충족할까요? (두 가지를 선택하세요.)

A. RDS Multi-AZ DB 인스턴스를 Amazon DynamoDB 테이블로 바꿉니다.
B. Lambda 함수의 대상으로 Amazon Simple Queue Service(Amazon SQS) 대기열을 구성합니다.
C. SNS 주제에 대한 Amazon Simple Queue Service(Amazon SQS) 배달 못한 편지 대기열을 구성합니다. 가장 많이 투표된
D. Amazon Simple Queue Service(Amazon SQS) 대기열을 SNS 토픽에 구독합니다. Lambda 함수를 구성하여 SQS 대기열의 메시지를 처리합니다. 가장 많이 투표된
E. SNS 토픽을 Amazon EventBridge 이벤트 버스로 바꿉니다. 각 이벤트에 대해 Lambda 함수를 호출하도록 새 이벤트 버스에서 EventBridge 규칙을 구성합니다.



### 질문 #140주제 1
한 회사에 Amazon EC2 인스턴스에서 실행되는 애플리케이션이 있습니다. 이 회사는 AWS CodePipeline 파이프라인을 사용하여 애플리케이션을 여러 AWS 리전에 배포합니다. 파이프라인은 각 리전에 대한 스테이지로 구성됩니다. 각 스테이지에는 각 리전에 대한 AWS CloudFormation 작업이 포함됩니다.

파이프라인이 리전에 애플리케이션을 배포할 때, 이 회사는 파이프라인이 다음 리전으로 이동하기 전에 애플리케이션이 정상 상태인지 확인하려고 합니다. Amazon Route 53 레코드 세트는 각 리전의 애플리케이션에 대해 구성됩니다. DevOps 엔지니어는 애플리케이션이 배포된 각 리전에 대한 Amazon CloudWatch 알람을 기반으로 하는 Route 53 상태 확인을 만듭니다.

DevOps 엔지니어는 요구 사항을 충족하기 위해 다음에 무엇을 해야 합니까?

A. CloudWatch 알람의 상태를 확인하기 위해 AWS Step Functions 워크플로를 만듭니다. 알람이 ALARM 상태인 경우 오류와 함께 종료되도록 Step Functions 워크플로를 구성합니다. 각 Region 배포 단계 사이의 파이프라인에 새 단계를 만듭니다. 각 새 단계에서 Step Functions 워크플로를 호출하는 작업을 포함합니다. 가장 많이 투표된
B. 자동 롤백을 사용하여 CloudFormation 템플릿을 배포하도록 AWS CodeDeploy 애플리케이션을 구성합니다. CloudWatch 알람을 CodeDeploy 애플리케이션의 인스턴스 상태 검사로 구성합니다. 파이프라인에서 CloudFormation 작업을 제거합니다. 각 리전의 파이프라인 단계에서 CodeDeploy 작업을 만듭니다.
C. 애플리케이션이 배포된 각 지역에 대해 새 파이프라인 단계를 만듭니다. 새 단계에 대해 CloudWatch 알람 작업을 구성하여 CloudWatch 알람 상태를 확인하고 알람이 ALARM 상태인 경우 오류와 함께 종료합니다.
D. EC2 인스턴스에서 CloudWatch 에이전트를 구성하여 Route 53 상태 검사에 애플리케이션 상태를 보고합니다. 애플리케이션이 배포된 각 지역에 대해 새 파이프라인 단계를 만듭니다. CloudWatch 알람이 ALARM 상태인 경우 오류와 함께 종료되도록 CloudWatch 알람 작업을 구성합니다.


### 질문 #141주제 1
한 회사가 Amazon CloudWatch를 사용하여 Amazon EC2 인스턴스를 모니터링하려고 합니다. 이 회사는 12시간 동안 NetworkPacketsIn 메트릭의 평균이 최소 3시간 동안 5 미만이면 EC2 인스턴스를 중지해야 합니다. 이 회사는 매시간 메트릭을 평가해야 합니다. 평가 기간 동안 NetworkPacketsIn 메트릭에 대한 데이터가 누락된 경우 EC2 인스턴스는 계속 실행되어야 합니다.

DevOps 엔지니어가 NetworkPacketsIn 메트릭에 대한 CloudWatch 알람을 생성합니다. DevOps 엔지니어는 임계값을 5로 구성하고 평가 기간을 1시간으로 구성합니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 어떤 추가 작업을 수행해야 합니까?

A. Datapoints to Alarm 값을 12개 중 3개로 구성합니다. 알람이 누락된 데이터를 임계값 위반으로 처리하도록 구성합니다. 알람이 ALARM 상태로 전환되면 인스턴스를 중지하는 AWS Systems Manager 작업을 추가합니다.
B. Datapoints to Alarm 값을 12개 중 3개로 구성합니다. 알람이 누락된 데이터를 임계값을 위반하지 않는 것으로 처리하도록 구성합니다. 알람이 ALARM 상태로 전환되면 인스턴스를 중지하는 EC2 작업을 추가합니다. 가장 많이 투표된
C. Datapoints to Alarm 값을 12개 중 9개로 구성합니다. 알람이 누락된 데이터를 임계값 위반으로 처리하도록 구성합니다. 알람이 ALARM 상태로 전환되면 인스턴스를 중지하는 EC2 작업을 추가합니다.
D. Datapoints to Alarm 값을 12개 중 9개로 구성합니다. 알람이 누락된 데이터를 임계값을 위반하지 않는 것으로 처리하도록 구성합니다. 알람이 ALARM 상태로 전환되면 인스턴스를 중지하는 AWS Systems Manager 작업을 추가합니다.



### 질문 #142주제 1
한 회사가 AWS Organizations에서 조직에 있는 500개의 AWS 계정을 관리합니다. 이 회사는 모든 계정에서 연결되지 않은 Amazon Elastic Block Store(Amazon EBS) 볼륨을 많이 발견합니다. 이 회사는 조사를 위해 연결되지 않은 EBS 볼륨에 자동으로 태그를 지정하려고 합니다.

DevOps 엔지니어는 모든 AWS 계정에 AWS Lambda 함수를 배포해야 합니다. Lambda 함수는 30분마다 실행되어 7일 이상 연결되지 않은 모든 EBS 볼륨에 태그를 지정해야 합니다.

어떤 솔루션이 가장 운영적으로 효율적인 방식으로 이러한 요구 사항을 충족할까요?

A. 조직에 대한 위임된 관리자 계정을 구성합니다. Lambda 함수가 포함된 AWS CloudFormation 템플릿을 만듭니다. CloudFormation StackSets를 사용하여 위임된 관리자 계정에서 조직의 모든 멤버 계정으로 CloudFormation 템플릿을 배포합니다. 위임된 관리자 계정에서 Amazon EventBridge 이벤트 버스를 만들어 30분마다 각 멤버 계정에서 Lambda 함수를 호출합니다.
B. 조직의 멤버 계정에서 교차 계정 IAM 역할을 만듭니다. AWSLambda_FullAccess 정책과 AWSCloudFormationFullAccess 정책을 역할에 연결합니다. Lambda 함수와 Amazon EventBridge 예약 규칙을 포함하는 AWS CloudFormation 템플릿을 만들어 30분마다 Lambda 함수를 호출합니다. 조직의 관리 계정에서 역할을 가정하고 CloudFormation 템플릿을 멤버 계정에 배포하는 사용자 지정 스크립트를 만듭니다.
C. 조직에 대한 위임된 관리자 계정을 구성합니다. Lambda 함수와 Amazon EventBridge 예약된 규칙을 포함하는 AWS CloudFormation 템플릿을 만들어 30분마다 Lambda 함수를 호출합니다. CloudFormation StackSets를 사용하여 위임된 관리자 계정에서 조직의 모든 멤버 계정으로 CloudFormation 템플릿을 배포합니다. 가장 많이 투표된
D. 조직의 멤버 계정에서 교차 계정 IAM 역할을 만듭니다. 역할에 AmazonS3FullAccess 정책과 AWSCodeDeployDeployerAccess 정책을 연결합니다. AWS CodeDeploy를 사용하여 조직의 관리 계정에서 Lambda 함수를 배포하는 역할을 맡습니다. 멤버 계정에서 Amazon EventBridge 예약 규칙을 구성하여 30분마다 Lambda 함수를 호출합니다.



### 질문 #143주제 1
회사의 프로덕션 환경에서는 AWS CodeDeploy 블루/그린 배포를 사용하여 애플리케이션을 배포합니다. 배포에는 Amazon Linux 2를 실행하는 인스턴스를 시작하는 Amazon EC2 Auto Scaling 그룹이 포함됩니다.

코드 리포지토리에 작동하는 appspec.yml 파일이 있으며 다음 텍스트가 포함되어 있습니다.

```yaml
version: 0.0
os: linux
files:
    - source:/
      destination: /var/ww/html/applicaiton
```


DevOps 엔지니어는 대체 인스턴스가 요청 트래픽을 처리하기 시작하기 전에 스크립트가 인스턴스에 라이선스 파일을 다운로드하여 설치하도록 해야 합니다. DevOps 엔지니어는 appspec.yml 파일에 후크 섹션을 추가합니다.

DevOps 엔지니어는 라이선스 파일을 다운로드하여 설치하는 스크립트를 실행하기 위해 어떤 후크를 사용해야 합니까?

A. AfterBlockTraffic
B. BeforeBlockTraffic
C. 설치 전 가장 많이 투표된
D. 다운로드 번들



### 질문 #144주제 1
회사에 AWS Lambda 함수가 포함된 애플리케이션이 있습니다. Lambda 함수는 AWS CodeCommit 저장소에 저장된 Python 코드를 실행합니다. 이 회사는 최근 Python 코드의 오류로 인해 프로덕션 환경에서 장애를 경험했습니다. 엔지니어는 Lambda 함수에 대한 단위 테스트를 작성하여 향후 프로덕션 환경에 결함이 발생하는 것을 방지했습니다.

이 회사의 DevOps 팀은 단위 테스트를 기존 AWS CodePipeline 파이프라인에 통합하는 솔루션을 구현해야 합니다. 이 솔루션은 회사에서 볼 수 있도록 단위 테스트에 대한 보고서를 생성해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. CodeCommit 리포지토리를 Amazon CodeGuru Reviewer와 연결합니다. 새 AWS CodeBuild 프로젝트를 만듭니다. CodePipeline 파이프라인에서 새 CodeBuild 프로젝트를 사용하는 테스트 단계를 구성합니다. CodeCommit 리포지토리에 buildspec.yml 파일을 만듭니다. buildspec yml 파일에서 CodeGuru 검토를 실행하는 작업을 정의합니다.
B. 새 AWS CodeBuild 프로젝트를 만듭니다. CodePipeline 파이프라인에서 새 CodeBuild 프로젝트를 사용하는 테스트 단계를 구성합니다. CodeBuild 보고서 그룹을 만듭니다. CodeCommit 리포지토리에 buildspec.yml 파일을 만듭니다. buildspec.yml 파일에서 빌드 단계 섹션에 JUNITXML 출력으로 단위 테스트를 실행하는 작업을 정의합니다. 새 CodeBuild 보고서 그룹에 업로드할 테스트 보고서를 구성합니다. 가장 많이 투표된
C. 새 AWS CodeArtifact 리포지토리를 만듭니다. 새 AWS CodeBuild 프로젝트를 만듭니다. CodePipeline 파이프라인에서 새 CodeBuild 프로젝트를 사용하는 테스트 단계를 구성합니다. 원래 CodeCommit 리포지토리에 appspec.yml 파일을 만듭니다. appspec.yml 파일에서 빌드 단계 섹션에 CUCUMBERJSON 출력으로 단위 테스트를 실행하는 작업을 정의합니다. 새 CodeArtifact 리포지토리로 보낼 테스트 보고서를 구성합니다.
D. 새 AWS CodeBuild 프로젝트를 만듭니다. CodePipeline 파이프라인에서 새 CodeBuild 프로젝트를 사용하는 테스트 단계를 구성합니다. 새 Amazon S3 버킷을 만듭니다. CodeCommit 리포지토리에 buildspec.yml 파일을 만듭니다. buildspec yml 파일에서 phases 섹션에 HTML 출력으로 단위 테스트를 실행하는 작업을 정의합니다. 보고서 섹션에서 테스트 보고서를 S3 버킷에 업로드합니다.



### 질문 #145주제 1
한 회사가 AWS Organizations에서 여러 AWS 계정을 관리합니다. 회사의 보안 정책에 따르면 멤버 계정에 대한 AWS 계정 루트 사용자 자격 증명은 사용해서는 안 됩니다. 회사는 루트 사용자 자격 증명에 대한 액세스를 모니터링합니다.

최근 알림에 따르면 멤버 계정의 루트 사용자가 Amazon EC2 인스턴스를 시작했습니다. DevOps 엔지니어는 멤버 계정의 루트 사용자가 AWS 서비스 API 호출을 하지 못하도록 조직의 루트 수준에서 SCP를 만들어야 합니다.

어떤 SCP가 이러한 요구 사항을 충족할까요?



### 질문 #146주제 1
한 회사가 AWS를 사용하고 예측 가능한 트래픽 패턴이 있는 중요한 컴퓨팅 인프라가 포함된 VPC를 보유하고 있습니다. 이 회사는 Amazon CloudWatch Logs의 로그 그룹에 게시되는 VPC 흐름 로그를 구성했습니다.

이 회사의 DevOps 팀은 VPC 흐름 로그에 대한 모니터링 솔루션을 구성하여 시간이 지남에 따라 VPC로의 네트워크 트래픽에서 이상을 식별해야 합니다. 모니터링 솔루션이 이상을 감지하면 이 회사는 이상에 대한 대응을 시작할 수 있어야 합니다.

DevOps 팀은 이러한 요구 사항을 충족하기 위해 모니터링 솔루션을 어떻게 구성해야 합니까?

A. Amazon Kinesis 데이터 스트림을 만듭니다. 로그 그룹을 데이터 스트림에 구독합니다. Amazon Kinesis Data Analytics를 구성하여 데이터 스트림에서 로그 이상을 감지합니다. 데이터 스트림의 출력으로 사용할 AWS Lambda 함수를 만듭니다. 이상 발견 시 기본 Amazon EventBridge 이벤트 버스에 쓰도록 Lambda 함수를 구성합니다.
B. Amazon S3 버킷에 이벤트를 전달하는 Amazon Kinesis Data Firehose 전달 스트림을 만듭니다. 전달 스트림에 로그 그룹을 구독합니다. Amazon Lookout for Metrics를 구성하여 S3 버킷의 데이터에서 이상 징후를 모니터링합니다. Lookout for Metrics 이상 징후 발견에 대한 응답으로 실행할 AWS Lambda 함수를 만듭니다. Lambda 함수를 구성하여 기본 Amazon EventBridge 이벤트 버스에 게시합니다. 가장 많이 투표된
C. AWS Lambda 함수를 만들어 이상을 감지합니다. Lambda 함수가 이상을 감지하면 기본 Amazon EventBridge 이벤트 버스에 이벤트를 게시하도록 Lambda 함수를 구성합니다. Lambda 함수를 로그 그룹에 구독합니다.
D. Amazon Kinesis 데이터 스트림을 만듭니다. 로그 그룹을 데이터 스트림에 구독합니다. 로그 이상을 감지하는 AWS Lambda 함수를 만듭니다. Lambda 함수가 이상을 감지하면 기본 Amazon EventBridge 이벤트 버스에 쓰도록 Lambda 함수를 구성합니다. Lambda 함수를 데이터 스트림의 프로세서로 설정합니다.



### 질문 #147주제 1
AnyCompany는 AWS Organizations를 사용하여 여러 AWS 계정을 만들고 관리합니다. AnyCompany는 최근 규모가 작은 회사인 Example Corp를 인수했습니다. 인수 과정에서 Example Corp의 단일 AWS 계정이 Organizations 초대를 통해 AnyCompany의 관리 계정에 가입했습니다. AnyCompany는 새 멤버 계정을 Example Corp에 전담된 OU로 옮겼습니다.

AnyCompany의 DevOps 엔지니어는 멤버 계정에 액세스하기 위해 OrganizationAccountAccessRole이라는 역할을 맡는 IAM 사용자가 있습니다. 이 역할은 전체 액세스 정책으로 구성되어 있습니다. DevOps 엔지니어가 AWS Management Console을 사용하여 Example Corp의 새 멤버 계정에서 역할을 맡으려고 하면 DevOps 엔지니어는 다음과 같은 오류 메시지를 받습니다. "하나 이상의 필드에 잘못된 정보가 있습니다. 정보를 확인하거나 관리자에게 문의하십시오."

어떤 솔루션을 사용하면 DevOps 엔지니어가 새 멤버 계정에 액세스할 수 있습니까?

A. 관리 계정에서 DevOps 엔지니어의 IAM 사용자에게 새 멤버 계정에서 OrganizationAccountAccessRole IAM 역할을 맡을 수 있는 권한을 부여합니다.
B. 관리 계정에서 새 SCP를 만듭니다. SCP에서 DevOps 엔지니어의 IAM 사용자에게 새 멤버 계정의 모든 리소스에 대한 전체 액세스 권한을 부여합니다. 새 멤버 계정이 포함된 OU에 SCP를 연결합니다.
C. 새 멤버 계정에서 OrganizationAccountAccessRole이라는 이름의 새 IAM 역할을 만듭니다. AdministratorAccess AWS 관리 정책을 역할에 연결합니다. 역할의 신뢰 정책에서 관리 계정에 역할을 맡을 수 있는 권한을 부여합니다. 가장 많이 투표된
D. 새 멤버 계정에서 OrganizationAccountAccessRole IAM 역할에 대한 신뢰 정책을 편집합니다. 관리 계정에 역할을 맡을 수 있는 권한을 부여합니다.



### 질문 #148주제 1
DevOps 엔지니어가 레거시 REST API와 통합되는 애플리케이션을 설계하고 있습니다. 이 애플리케이션에는 Amazon Kinesis 데이터 스트림에서 레코드를 읽는 AWS Lambda 함수가 있습니다. Lambda 함수는 레코드를 레거시 REST API로 전송합니다. Lambda 함수가

Kinesis 데이터 스트림에서 전송하는 레코드의 약 10%에 데이터 오류가 있으며 수동으로 처리해야 합니다. Lambda 함수 이벤트 소스 구성에는 실패 시 대상으로 Amazon Simple Queue Service(Amazon SQS) 배달 못한 편지 대기열이 있습니다. DevOps 엔지니어는 Lambda 함수를 구성하여 레코드를 일괄 처리하고 실패 시 재시도를 구현했습니다.

DevOps 엔지니어는 테스트 중에 배달 못한 편지 대기열에 데이터 오류가 없고 이미 레거시 REST API에서 처리한 레코드가 많이 포함되어 있음을 알아챘습니다. DevOps 엔지니어는 배달 못한 편지 대기열로 전송되는 오류 없는 레코드 수를 줄이기 위해 Lambda 함수의 이벤트 소스 옵션을 구성해야 합니다.

이러한 요구 사항을 충족하는 솔루션은 무엇입니까?

A. 재시도 횟수를 늘리세요.
B. 오류가 발생할 때 배치를 분할하도록 설정을 구성합니다. 가장 많이 투표된
C. 샤드당 동시 배치 수를 늘립니다.
D. 기록의 최대 연령을 낮춥니다.



### 질문 #149주제 1
한 회사에서는 Amazon DynamoDB에서 데이터를 읽는 AWS Lambda에서 실행되는 마이크로서비스를 보유하고 있습니다. Lambda 코드는 성공적인 테스트 후 개발자가 수동으로 배포합니다. 이제 회사는 테스트와 배포를 자동화하고 클라우드에서 실행해야 합니다. 또한 각 마이크로서비스의 새 버전으로의 트래픽은 배포 후 시간이 지남에 따라 점진적으로 이동해야 합니다.

모든 요구 사항을 충족하고 가장 빠른 개발자 속도를 보장하는 솔루션은 무엇입니까?

A. AWS CodePipeline 구성을 만들고 테스트가 통과한 후 파이프라인을 트리거하기 위한 post-commit 후크를 설정합니다. AWS CodeDeploy를 사용하고 트래픽 비율과 간격을 지정하는 Canary 배포 구성을 만듭니다.
B. 테스트 코드가 푸시될 때 트리거되는 AWS CodeBuild 구성을 만듭니다. AWS CloudFormation을 사용하여 새로운 Lambda 버전을 배포하고 트래픽 이동 비율과 간격을 지정하는 AWS CodePipeline 구성을 트리거합니다.
C. AWS CodePipeline 구성을 만들고 코드가 푸시될 때 트리거되도록 소스 코드 단계를 설정합니다. AWS CodeBuild를 사용하여 테스트를 실행하도록 빌드 단계를 설정합니다. 배포할 AWS CodeDeploy 구성을 설정한 다음 CodeDeployDefault.LambdaLinear10PercentEvery3Minutes 옵션을 선택합니다. 가장 많이 투표된
D. AWS CLI를 사용하여 테스트가 통과한 후 Amazon S3 버킷에 코드를 업로드하는 포스트 커밋 후크를 설정합니다. 새 버전을 배포하는 Lambda 함수를 실행하는 S3 이벤트 트리거를 설정합니다. Lambda 함수에서 간격을 사용하여 필요한 백분율로 시간 경과에 따라 코드를 배포합니다.



### 질문 #150주제 1
한 회사가 AWS Lambda와 Amazon API Gateway로 구동되는 서버리스 아키텍처를 사용하는 웹 및 모바일 애플리케이션을 구축하고 있습니다. 이 회사는 AWS CodeCommit 리포지토리의 적절한 환경 브랜치에 푸시된 코드를 기반으로 백엔드 Lambda 배포를 완전히 자동화하려고 합니다.

배포에는 다음이 있어야 합니다.

• 테스트 및 프로덕션을 위한 별도의 환경 파이프라인
• 테스트 환경에서만 발생하는 자동 배포

이러한 요구 사항을 충족하기 위해 어떤 단계를 거쳐야 합니까?

A. 새로운 AWS CodePipeline 서비스를 구성합니다. 각 환경에 대한 CodeCommit 리포지토리를 만듭니다. CodePipeline을 설정하여 적절한 리포지토리에서 소스 코드를 검색합니다. AWS CloudFormation으로 Lambda 함수를 배포하기 위한 배포 단계를 설정합니다.
B. 테스트 및 프로덕션 환경에 대한 두 개의 AWS CodePipeline 구성을 만듭니다. 프로덕션 파이프라인을 구성하여 수동 승인 단계를 갖도록 합니다. 각 환경에 대한 CodeCommit 리포지토리를 만듭니다. 각 CodePipeline을 설정하여 적절한 리포지토리에서 소스 코드를 검색합니다. AWS CloudFormation으로 Lambda 함수를 배포하도록 배포 단계를 설정합니다.
C. 테스트 및 프로덕션 환경에 대한 두 개의 AWS CodePipeline 구성을 만듭니다. 프로덕션 파이프라인을 구성하여 수동 승인 단계를 갖도록 합니다. 각 환경에 대한 브랜치가 있는 CodeCommit 리포지토리를 하나 만듭니다. 리포지토리의 적절한 브랜치에서 소스 코드를 검색하도록 각 CodePipeline을 설정합니다. AWS CloudFormation으로 Lambda 함수를 배포하도록 배포 단계를 설정합니다. 가장 많이 투표된
D. 테스트 및 프로덕션 환경에 대한 AWS CodeBuild 구성을 만듭니다. 프로덕션 파이프라인을 구성하여 수동 승인 단계를 갖도록 합니다. 각 환경에 대한 브랜치가 있는 CodeCommit 리포지토리를 하나 만듭니다. Lambda 함수 코드를 Amazon S3 버킷으로 푸시합니다. S3 버킷에서 Lambda 함수를 배포하도록 배포 단계를 설정합니다.



### 질문 #151주제 1
DevOps 엔지니어는 온프레미스에서 AWS로 애플리케이션을 마이그레이션하는 솔루션을 찾고자 합니다. 애플리케이션은 Linux에서 실행 중이며 제대로 작동하려면 특정 버전의 Apache Tomcat, HAProxy 및 Varnish Cache에서 실행해야 합니다. 애플리케이션의 운영 체제 수준 매개변수는 튜닝이 필요합니다. 솔루션에는 새 애플리케이션 버전의 배포를 자동화하는 방법이 포함되어야 합니다. 인프라는 확장 가능해야 하며 오류가 있는 서버는 자동으로 교체해야 합니다.

DevOps 엔지니어는 어떤 솔루션을 사용해야 합니까?

A. 모든 필수 소프트웨어가 포함된 Docker 이미지로 애플리케이션을 Amazon ECR에 업로드합니다. AWS Fargate 시작 유형과 자동 확장 그룹을 사용하여 Amazon ECS 클러스터를 만듭니다. Amazon ECR을 소스로 사용하고 Amazon ECS를 배포 공급자로 사용하는 AWS CodePipeline 파이프라인을 만듭니다.
B. 소프트웨어를 구성하고 설치하기 위해 저장된 구성 파일이 있는 AWS CodeCommit 저장소에 애플리케이션 코드를 업로드합니다. AWS Elastic Beanstalk 웹 서버 계층과 Tomcat 솔루션 스택을 사용하는 로드 밸런싱 유형 환경을 만듭니다. CodeCommit을 소스로 사용하고 Elastic Beanstalk을 배포 공급자로 사용하는 AWS CodePipeline 파이프라인을 만듭니다.
C. 소프트웨어를 구성하고 설치하기 위해 .ebextensions 파일 세트와 함께 AWS CodeCommit 리포지토리에 애플리케이션 코드를 업로드합니다. Tomcat 솔루션 스택을 사용하는 AWS Elastic Beanstalk 워커 티어 환경을 만듭니다. CodeCommit을 소스로 사용하고 Elastic Beanstalk를 배포 공급자로 사용하는 AWS CodePipeline 파이프라인을 만듭니다.
D. appspec.yml 파일을 사용하여 AWS CodeCommit 리포지토리에 애플리케이션 코드를 업로드하여 필요한 소프트웨어를 구성하고 설치합니다. Amazon EC2 Auto Scaling 그룹과 연결된 AWS CodeDeploy 배포 그룹을 만듭니다. CodeCommit을 소스로 사용하고 CodeDeploy를 배포 공급자로 사용하는 AWS CodePipeline 파이프라인을 만듭니다. 가장 많이 투표된



### 질문 #152주제 1
DevOps 엔지니어가 EC2 Auto Scaling 그룹의 Amazon EC2 인스턴스 플릿에서 AWS CodeDeploy를 사용하고 있습니다. EC2 Auto Scaling과 통합된 관련 CodeDeploy 배포 그룹은 CodeDeployDefault.OneAtATime을 사용하여 인플레이스 배포를 수행하도록 구성되어 있습니다. 진행 중인 새 배포 중에 엔지니어는 전체 배포가 성공적으로 완료되었지만 5개 인스턴스 중 2개에 이전 애플리케이션 개정판이 배포되어 있음을 발견했습니다. 나머지 3개 인스턴스에는 최신 애플리케이션 개정판이 있습니다.

이 문제의 원인은 무엇일까요?

A. 영향을 받은 두 인스턴스가 새 배포를 가져오지 못했습니다.
B. AfterInstall 라이프사이클 이벤트 후크가 실패하여 CodeDeploy 에이전트가 영향을 받은 인스턴스에서 이전 버전으로 롤백되었습니다.
C. 영향을 받은 두 인스턴스에는 CodeDeploy 에이전트가 설치되지 않았습니다.
D. EC2 자동 확장이 새 배포가 아직 완료되지 않은 상태에서 두 개의 새 인스턴스를 시작했기 때문에 이전 버전이 영향을 받은 인스턴스에 배포되었습니다. 가장 많이 투표된



### 질문 #153주제 1
보안팀은 개발자가 실수로 프로덕션에서 Amazon EC2 인스턴스에 Elastic IP 주소를 연결할 수 있다는 우려를 갖고 있습니다. 어떤 개발자도 인스턴스에 Elastic IP 주소를 연결할 수 없어야 합니다. 프로덕션 서버에 언제든지 Elastic IP 주소가 있는 경우 보안팀에 알려야 합니다.

이 작업을 어떻게 자동화할 수 있습니까?

A. Amazon Athena를 사용하여 AWS CloudTrail 로그를 쿼리하여 연관 주소 시도가 있는지 확인합니다. AWS Lambda 함수를 만들어 인스턴스에서 Elastic IP 주소를 분리하고 보안 팀에 알립니다.
B. 개발자의 IAM 그룹에 IAM 정책을 연결하여 associate-address 권한을 거부합니다. Elastic IP 주소가 production으로 태그된 인스턴스와 연결되어 있는지 확인하는 사용자 지정 AWS Config 규칙을 만들고 보안 팀에 경고합니다. 가장 많이 투표된
C. 개발자와 연결된 모든 IAM 그룹에 associate-address 권한이 없는지 확인합니다. 예약된 AWS Lambda 함수를 만들어서 Elastic IP 주소가 production으로 태그된 인스턴스와 연결되어 있는지 확인하고 인스턴스에 Elastic IP 주소가 연결되어 있으면 보안 팀에 알립니다.
D. AWS Config 규칙을 만들어 모든 프로덕션 인스턴스에 deny associate-address 권한이 포함된 EC2 IAM 역할이 있는지 확인합니다. 인스턴스와 연결된 Elastic IP 주소가 있는지 확인하고 인스턴스에 연결된 Elastic IP 주소가 있는 경우 보안 팀에 경고합니다.



### 질문 #154주제 1
한 회사가 AWS Organizations를 사용하여 각 부서에 대해 별도의 AWS 계정을 만들고 있습니다. 이 회사는 다음 작업을 자동화해야 합니다.

• Linux AMI를 주기적으로 새 패치로 업데이트하고 골든 이미지 생성
• 사용 가능한 경우 골든 이미지에 Chef 에이전트의 새 버전 설치
• 새로 생성된 AMI를 부서 계정에 제공

어떤 솔루션이 가장 적은 관리 오버헤드로 이러한 요구 사항을 충족합니까?

A. 이전 골든 이미지에서 Amazon EC2 인스턴스를 시작하는 스크립트를 작성합니다. 패치 업데이트를 적용합니다. Chef 에이전트의 새 버전을 설치하고, 새 골든 이미지를 생성한 다음 AMI 권한을 수정하여 부서 계정과만 새 이미지를 공유합니다.
B. Amazon EC2 Image Builder를 사용하여 기본 Linux AMI와 Chef 에이전트를 설치하는 구성 요소로 구성된 이미지 파이프라인을 만듭니다. AWS Resource Access Manager를 사용하여 EC2 Image Builder 이미지를 부서 계정과 공유합니다. 가장 많이 투표된
C. AWS Systems Manager Automation 런북을 사용하여 이전 이미지를 사용하여 Linux AMI를 업데이트합니다. Chef 에이전트를 업데이트할 스크립트의 URL을 제공합니다. AWS Organizations를 사용하여 부서 계정의 이전 골든 이미지를 대체합니다.
D. Amazon EC2 Image Builder를 사용하여 기본 Linux AMI와 Chef 에이전트를 설치하기 위한 구성 요소로 구성된 이미지 파이프라인을 만듭니다. 부서 계정에서 참조할 수 있는 새 AMI ID를 저장하기 위해 AWS Systems Manager Parameter Store에 매개변수를 만듭니다.



### 질문 #155주제 1
한 회사가 자동 스케일링을 사용하는 AWS에서 미션 크리티컬 애플리케이션을 보유하고 있습니다. 이 회사는 배포 라이프사이클이 다음 매개변수를 충족하기를 원합니다.

• 나머지 플릿이 트래픽을 계속 처리하도록 하려면 애플리케이션을 한 번에 한 인스턴스씩 배포해야 합니다.
• 애플리케이션은 CPU 집약적이며 면밀히 모니터링해야 합니다.
• 배포 인스턴스의 CPU 사용률이 85%를 초과하면 배포가 자동으로 롤백되어야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS CloudFormation을 사용하여 AWS Step Functions 상태 머신과 Auto Scaling 라이프사이클 후크를 만들어 한 번에 한 인스턴스씩 대기 상태로 이동합니다. AWS Systems Manager 자동화를 사용하여 각 인스턴스에 업데이트를 배포하고 하트비트 시간 초과를 사용하여 Auto Scaling 그룹으로 다시 이동합니다.
B. Amazon EC2 Auto Scaling과 함께 AWS CodeDeploy 사용 CPU 사용률 메트릭에 연결된 알람을 구성합니다. 배포 전략으로 CodeDeployDefault OneAtAtime 구성을 사용합니다. 알람 임계값이 초과되면 배포를 롤백하기 위해 배포 그룹 내에서 자동 롤백을 구성합니다. 가장 많이 투표된
C. 로드 밸런싱 및 AWS 자동 확장에 AWS Elastic Beanstalk를 사용합니다. CPU 사용률 메트릭에 연결된 알람을 구성합니다. 고정된 배치 크기가 인스턴스 하나인 롤링 배포를 구성합니다. 향상된 상태를 활성화하여 배포 상태를 모니터링하고 이전에 생성된 알람을 기반으로 롤백합니다.
D. AWS Systems Manager를 사용하여 Amazon EC2 Auto Scaling으로 블루/그린 배포를 수행합니다. CPU 사용률 메트릭에 연결된 알람을 구성합니다. 한 번에 하나씩 업데이트를 배포합니다. 알람 임계값이 초과되면 배포를 롤백하기 위해 Auto Scaling 그룹 내에서 자동 롤백을 구성합니다.



### 질문 #156주제 1
한 회사에 자동화된 배포 파이프라인을 위한 코드를 작성하는 개발자가 한 명 있습니다. 개발자는 각 프로젝트의 Amazon S3 버킷에 소스 코드를 저장하고 있습니다. 회사는 팀에 개발자를 더 추가하고 싶지만 코드 충돌과 작업 손실에 대해 우려하고 있습니다. 회사는 또한 테스트를 위해 새 버전의 코드를 배포하고 개발자가 저장소에서 코드가 변경되면 두 환경 모두에 자동으로 배포할 수 있도록 테스트 환경을 구축하려고 합니다.

이러한 요구 사항을 충족하는 가장 효율적인 방법은 무엇입니까?

A. 각 프로젝트에 대한 AWS CodeCommit 리포지토리를 만들고, 프로덕션 코드에 메인 브랜치를 사용하고, 테스트에 배포된 코드에 대한 테스트 브랜치를 만듭니다. 기능 브랜치를 사용하여 새로운 기능을 개발하고 풀 리퀘스트를 사용하여 코드를 테스트 및 메인 브랜치에 병합합니다. 가장 많이 투표된
B. 각 프로젝트에 대해 테스트 코드를 위한 또 다른 S3 버킷을 만들고 AWS Lambda 함수를 사용하여 테스트 버킷과 프로덕션 버킷 간의 코드 변경을 홍보합니다. 모든 버킷에서 버전 관리를 활성화하여 코드 충돌을 방지합니다.
C. 각 프로젝트에 대한 AWS CodeCommit 리포지토리를 만들고, 각 환경에 대해 다른 배포 파이프라인을 사용하여 프로덕션 및 테스트 코드에 메인 브랜치를 사용합니다. 기능 브랜치를 사용하여 새로운 기능을 개발합니다.
D. 각 S3 버킷에서 버전 관리 및 분기를 활성화하고, 프로덕션 코드에는 메인 분기를 사용하고, 테스트에 배포된 코드에는 테스트 분기를 만듭니다. 개발자가 각 환경에서 개발에 각 분기를 사용하도록 합니다.



### 질문 #157주제 1
DevOps 엔지니어는 Auto Scaling 그룹의 Application Load Balancer 뒤에서 실행되는 모든 Amazon EC2 인스턴스가 사용자 요청에 응답하지 않는다는 것을 알아챘습니다. EC2 인스턴스는 대상 그룹 HTTP 상태 검사에도 실패합니다.

엔지니어는 검사 결과 애플리케이션 프로세스가 어떤 EC2 인스턴스에서도 실행되지 않는다는 것을 알아챘습니다. 시스템 로그에 메모리 부족 메시지가 상당히 많이 있습니다. 엔지니어는 잠재적인 애플리케이션 메모리 누수에 대처하기 위해 애플리케이션의 복원력을 개선해야 합니다. 문제가 있을 때 경고하도록 모니터링 및 알림을 활성화해야 합니다.

이러한 요구 사항을 충족하는 작업의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. 로드 밸런서의 상태 검사에 실패할 경우 인스턴스를 대체하도록 자동 크기 조정 구성을 변경합니다. 가장 많이 투표된
B. 대상 그룹 상태 검사 HealthCheckIntervalSeconds 매개변수를 변경하여 상태 검사 간 간격을 줄입니다.
C. 대상 그룹 상태 검사를 HTTP에서 TCP로 변경하여 애플리케이션이 수신 대기하는 포트에 도달 가능한지 확인합니다.
D. 전체 Auto Scaling 그룹에 대해 Amazon CloudWatch 대시보드 내에서 사용 가능한 메모리 소비 메트릭을 활성화합니다. 메모리 사용률이 높을 때 알람을 생성합니다. 알람이 울릴 때 알림을 받으려면 Amazon SNS 토픽을 알람에 연결합니다.
E. Amazon CloudWatch 에이전트를 사용하여 Auto Scaling 그룹의 EC2 인스턴스의 메모리 사용률을 수집합니다. 메모리 사용률이 높을 때 알람을 생성하고 Amazon SNS 토픽을 연결하여 알림을 받습니다. 가장 많이 투표된



### 질문 #158주제 1
전자상거래 회사는 많은 수의 Amazon Elastic Block Store(Amazon EBS) 지원 Amazon EC2 인스턴스를 사용합니다. 모든 인스턴스에서 수동 작업을 줄이기 위해 DevOps 엔지니어는 EC2 인스턴스 은퇴 이벤트가 예약될 때 재시작 작업을 자동화하는 업무를 맡습니다.

이를 어떻게 달성할 수 있을까요?

A. 일주일에 한 번 EC2 인스턴스가 은퇴를 위해 예약되어 있는지 확인하는 AWS Systems Manager Automation 런북을 실행하기 위해 예약된 Amazon EventBridge 규칙을 만듭니다. 인스턴스가 은퇴를 위해 예약되어 있는 경우 런북은 인스턴스를 최대 절전 모드로 전환합니다.
B. 모든 인스턴스에서 EC2 자동 복구를 활성화합니다. 유지 관리 기간 동안만 복구가 발생하도록 제한하는 AWS Config 규칙을 만듭니다.
C. 표준 업무 시간 외의 승인된 유지 관리 기간 동안 모든 EC2 인스턴스를 재부팅합니다. 인스턴스가 EC2 인스턴스 상태 확인에 실패하는 경우 알림을 보내도록 Amazon CloudWatch 알람을 설정합니다.
D. 은퇴 예약 이벤트가 발생할 때 EC2 인스턴스를 중지하고 시작하는 AWS Systems Manager Automation 런북을 실행하기 위한 AWS Health Amazon EventBridge 규칙을 설정합니다. 가장 많이 투표된



### 질문 #159주제 1
한 회사가 AWS Control Tower에서 애플리케이션 팀의 AWS 계정을 관리합니다. 개별 애플리케이션 팀은 각자의 AWS 계정을 보호할 책임이 있습니다.

DevOps 엔지니어는 애플리케이션 팀이 아직 GuardDuty를 활성화하지 않은 모든 AWS 계정에 대해 Amazon GuardDuty를 활성화해야 합니다. DevOps 엔지니어는 AWS Control Tower 관리 계정에서 AWS CloudFormation StackSets를 사용하고 있습니다.

DevOps 엔지니어는 StackSets 배포 중에 실패를 방지하기 위해 CloudFormation 템플릿을 어떻게 구성해야 합니까?

A. AWS Lambda 함수를 호출하는 CloudFormation 사용자 지정 리소스를 만듭니다. GuardDuty가 계정에서 아직 활성화되지 않은 경우 GuardDuty를 조건부로 활성화하도록 Lambda 함수를 구성합니다. 가장 많이 투표된
B. CloudFormation 템플릿의 조건 섹션을 사용하여 GuardDuty가 아직 활성화되지 않은 계정에서 GuardDuty를 활성화합니다.
C. CloudFormation Fn::GetAtt 내장 함수를 사용하여 GuardDuty가 이미 활성화되었는지 확인합니다. GuardDuty가 아직 활성화되지 않은 경우 CloudFormation 템플릿의 리소스 섹션을 사용하여 GuardDuty를 활성화합니다.
D. GuardDuty가 활성화되지 않은 AWS 계정 ID 목록을 수동으로 검색합니다. CloudFormation Fn::ImportValue 내장 함수를 사용하여 계정 ID 목록을 CloudFormation 템플릿으로 가져와 나열된 AWS 계정에 대한 배포를 건너뜁니다.



### 질문 #160주제 1
회사에 AWS Control Tower 랜딩 존이 있습니다. 회사의 DevOps 팀은 워크로드 OU를 만듭니다. 개발 OU와 프로덕션 OU는 워크로드 OU 아래에 중첩됩니다. 회사는 사용자에게 회사의 AWS 계정에 대한 전체 액세스 권한을 부여하여 애플리케이션을 배포합니다.

DevOps 팀은 프로덕션 OU에서만 특정 관리 IAM 역할이 모든 AWS 계정의 IAM 역할과 정책을 관리하도록 허용해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. 조직 루트에 대한 관리 IAM 역할을 제외하는 조건으로 전체 액세스를 거부하는 SCP를 만듭니다.
B. FullAWSAccess SCP가 조직 루트에 적용되었는지 확인합니다. 가장 많이 투표된
C. IAM 관련 작업을 허용하는 SCP를 만듭니다. SCP를 개발 OU에 연결합니다.
D. 관리 IAM 역할을 제외하는 조건으로 IAM 관련 작업을 거부하는 SCP를 만듭니다. SCP를 워크로드 OU에 연결합니다.
E. 관리 IAM 역할을 제외하는 조건으로 IAM 관련 작업을 거부하는 SCP를 만듭니다. SCP를 프로덕션 OU에 연결합니다. 가장 많이 투표된



### 질문 #161주제 1
한 회사가 내부 보안 침해를 시뮬레이션하기 위해 침투 테스터를 고용했습니다. 테스터는 회사의 Amazon EC2 인스턴스에서 포트 스캔을 수행했습니다. 회사의 보안 조치는 포트 스캔을 감지하지 못했습니다.

이 회사는 EC2 인스턴스에서 포트 스캔이 수행될 때 자동으로 알림을 제공하는 솔루션이 필요합니다. 이 회사는 Amazon Simple Notification Service(Amazon SNS) 토픽을 생성하고 구독합니다.

이 회사는 요구 사항을 충족하기 위해 다음에 무엇을 해야 합니까?

A. Amazon GuardDuty가 활성화되었는지 확인합니다. 감지된 EC2 및 포트 스캔 결과에 대한 Amazon CloudWatch 알람을 만듭니다. 알람을 SNS 토픽에 연결합니다. 가장 많이 투표된
B. Amazon Inspector가 활성화되었는지 확인합니다. 포트 스캔을 나타내는 탐지된 네트워크 도달 가능성 결과에 대한 Amazon EventBridge 이벤트를 만듭니다. 이벤트를 SNS 토픽에 연결합니다.
C. Amazon Inspector가 활성화되었는지 확인합니다. 오픈 포트 취약성을 유발하는 감지된 CVE에 대한 Amazon EventBridge 이벤트를 만듭니다. 이벤트를 SNS 토픽에 연결합니다.
D. AWS CloudTrail이 활성화되었는지 확인합니다. IP 주소 범위에서 비정상적인 양의 트래픽에 대한 CloudTrail 로그를 분석하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 SNS 토픽에 연결합니다.



### 질문 #162주제 1
한 회사가 Amazon Elastic Kubernetes Service(Amazon EKS) 클러스터에서 애플리케이션을 실행합니다. EKS 클러스터는 애플리케이션 로드 밸런서를 사용하여 클러스터에서 실행되는 애플리케이션으로 트래픽을 라우팅합니다.

EKS 클러스터로 마이그레이션된 새 애플리케이션의 성능이 좋지 않습니다. EKS 클러스터의 다른 모든 애플리케이션은 적절한 작업을 유지합니다. 새 애플리케이션은 사용자 트래픽이 웹 애플리케이션으로 라우팅되기 전에 배포 즉시 미리 구성된 최대 포드 수로 수평적으로 확장됩니다.

EKS 클러스터에서 웹 애플리케이션의 확장 동작을 해결할 솔루션은 무엇입니까?

A. EKS 클러스터에 Horizontal Pod Autoscaler를 구현합니다.
B. EKS 클러스터에 Vertical Pod Autoscaler를 구현합니다. 가장 많이 투표된
C. 클러스터 자동 확장기를 구현합니다.
D. EKS 클러스터에 AWS Load Balancer Controller를 구현합니다.



### 질문 #163주제 1
한 회사에는 AWS Organizations에서 조직을 관리하는 AWS Control Tower 랜딩 존이 있습니다. 이 회사는 회사의 요구 사항에 따라 OU 구조를 만들었습니다. 이 회사의 DevOps 팀은 솔루션에 대한 핵심 계정과 모든 중앙 집중식 AWS CloudFormation 및 AWS Service Catalog 솔루션에 대한 계정을 설정했습니다.

이 회사는 AWS Control Tower를 통해 계정이 요청할 수 있는 일련의 사용자 지정을 제공하려고 합니다.

이러한 요구 사항을 충족하는 단계 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. 서비스 관리 권한을 사용하여 조직에서 CloudFormation에 대한 신뢰할 수 있는 액세스를 활성화합니다.
B. AWSControlTowerBlueprintAccess라는 이름의 IAM 역할을 만듭니다. 관리 계정의 AWSControlTowerAdmin 역할이 역할을 맡을 수 있도록 하는 신뢰 정책으로 역할을 구성합니다. AWSServiceCatalogAdminFullAccess IAM 정책을 AWSControlTowerBlueprintAccess 역할에 연결합니다. 가장 많이 투표된
C. 각 CloudFormation 템플릿에 대한 서비스 카탈로그 제품을 만듭니다. 가장 많이 투표된
D. 각 CloudFormation 템플릿에 대해 CloudFormation 스택 세트를 만듭니다. 각 스택 세트에 대해 자동 배포를 활성화합니다. 특정 OU를 대상으로 하는 CloudFormation 스택 인스턴스를 만듭니다.
E. AWS Control Tower(CfCT) CloudFormation 스택에 대한 사용자 정의를 배포합니다.
F. 각 사용자 정의에 대한 리소스가 포함된 CloudFormation 템플릿을 만듭니다. 가장 많이 투표된



### 질문 #164주제 1
한 회사가 Amazon EC2 인스턴스에서 워크로드를 실행합니다. 이 회사에는 AWS 계정의 모든 EC2 인스턴스에서 Instance Metadata Service Version 2(IMDSv2)를 사용해야 하는 컨트롤이 필요합니다. EC2 인스턴스가 Instance Metadata Service Version 1(IMDSv1) 사용을 방해하지 않는 경우 EC2 인스턴스를 종료해야 합니다.

이러한 요구 사항을 충족하는 솔루션은 무엇입니까?

A. 계정에서 AWS Config를 설정합니다. 관리되는 규칙을 사용하여 EC2 인스턴스를 확인합니다. AWS Systems Manager Automation을 사용하여 인스턴스를 종료하여 결과를 수정하도록 규칙을 구성합니다. 가장 많이 투표된
B. ec2:MetadataHttpTokens 조건 키가 필수 값으로 설정되지 않은 경우 ec2:RunInstance 작업을 방지하는 권한 경계를 만듭니다. 인스턴스를 시작하는 데 사용된 IAM 역할에 권한 경계를 연결합니다.
C. 계정에서 Amazon Inspector를 설정합니다. EC2 인스턴스에 대한 심층 검사를 활성화하도록 Amazon Inspector를 구성합니다. Inspector2 발견에 대한 Amazon EventBridge 규칙을 만듭니다. 인스턴스를 종료하기 위한 대상으로 AWS Lambda 함수를 설정합니다.
D. EC2 인스턴스 시작 성공 이벤트에 대한 Amazon EventBridge 규칙을 만듭니다. 이벤트를 AWS Lambda 함수로 보내 EC2 메타데이터를 검사하고 인스턴스를 종료합니다.



### 질문 #165주제 1
한 회사가 Auto Scaling 그룹에 있는 Amazon EC2 인스턴스 앞에 Application Load Balancer를 사용하는 애플리케이션을 빌드합니다. 이 애플리케이션은 상태 비저장입니다. Auto Scaling 그룹은 완전히 사전 빌드된 사용자 지정 AMI를 사용합니다. EC2 인스턴스에는 사용자 지정 부트스트래핑 프로세스가 없습니다.

Auto Scaling 그룹이 사용하는 AMI는 최근에 삭제되었습니다. AMI ID가 없기 때문에 Auto Scaling 그룹의 확장 활동이 실패로 표시됩니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 어떤 단계 조합을 취해야 합니까? (세 가지를 선택하십시오.)

A. 새 AMI를 사용하는 새로운 시작 템플릿을 만듭니다. 가장 많이 투표된
B. 새로운 시작 템플릿을 사용하도록 자동 크기 조정 그룹을 업데이트합니다. 가장 많이 투표된
C. 자동 크기 조정 그룹의 원하는 용량을 0으로 줄입니다.
D. 자동 크기 조정 그룹의 원하는 용량을 1만큼 늘립니다.
E. 자동 확장 그룹에서 실행 중인 EC2 인스턴스에서 새 AMI를 생성합니다. 가장 많이 투표된
F. EC2 인스턴스가 사용하는 운영 체제의 최신 공개 AMI를 복사하여 새 AMI를 만듭니다.



### 질문 #166주제 1
한 회사가 Application Load Balancer(ALB) 뒤에 있는 Amazon EC2 인스턴스에 웹 애플리케이션을 배포합니다. 이 회사는 AWS CodeCommit 리포지토리에 애플리케이션 코드를 저장합니다. 코드가 메인 브랜치에 병합되면 AWS Lambda 함수가 AWS CodeBuild 프로젝트를 호출합니다. CodeBuild 프로젝트는 코드를 패키징하고, 패키징된 코드를 AWS CodeArtifact에 저장하고, AWS Systems Manager Run Command를 호출하여 패키징된 코드를 EC2 인스턴스에 배포합니다.

이전 배포에서 결함, 최신 버전의 패키징된 코드를 실행하지 않는 EC2 인스턴스, 인스턴스 간 불일치가 발생했습니다.

DevOps 엔지니어가 보다 안정적인 배포 솔루션을 구현하기 위해 취해야 할 조치의 조합은 무엇입니까? (두 가지를 선택하세요.)

A. CodeCommit 리포지토리를 소스 공급자로 사용하는 AWS CodePipeline에서 파이프라인을 만듭니다. 애플리케이션을 빌드하고 테스트하기 위해 CodeBuild 프로젝트를 병렬로 실행하는 파이프라인 단계를 구성합니다. 파이프라인에서 CodeBuild 프로젝트 출력 아티팩트를 AWS CodeDeploy 작업에 전달합니다.
B. CodeCommit 리포지토리를 소스 공급자로 사용하는 AWS CodePipeline에서 파이프라인을 만듭니다. CodeBuild 프로젝트를 실행하여 애플리케이션을 빌드한 다음 테스트하는 별도의 파이프라인 단계를 만듭니다. 파이프라인에서 CodeBuild 프로젝트 출력 아티팩트를 AWS CodeDeploy 작업에 전달합니다. 가장 많이 투표된
C. AWS CodeDeploy 애플리케이션과 배포 그룹을 생성하여 패키지된 코드를 EC2 인스턴스에 배포합니다. 배포 그룹에 대한 ALB를 구성합니다. 가장 많이 투표된
D. Systems Manager 대신 AWS CodeDeploy를 사용하여 빌드, 테스트 및 배포 작업을 실행하는 개별 Lambda 함수를 만듭니다.
E. Amazon S3 버킷을 만듭니다. CodeBuild 프로젝트를 수정하여 CodeArtifact 대신 S3 버킷에 패키지를 저장합니다. CodeDeploy에서 배포 작업을 사용하여 아티팩트를 EC2 인스턴스에 배포합니다.



### 질문 #167주제 1
한 회사가 AWS Organizations에서 조직을 사용하여 AWS 계정을 관리합니다. 회사의 자동화 계정에는 새 AWS 계정을 만들고 구성하는 CI/CD 파이프라인이 포함되어 있습니다.

회사에는 조직의 계정에 서비스를 제공하는 내부 서비스 팀 그룹이 있습니다. 서비스 팀은 일련의 서비스 계정에서 운영됩니다. 서비스 팀은 CreateAccount API 호출이 새 계정을 만들 때 서비스 계정에서 AWS CloudTrail 이벤트를 수신하려고 합니다.

회사는 이 CloudTrail 이벤트를 서비스 계정과 어떻게 공유해야 합니까?

A. 자동화 계정에서 Amazon EventBridge 규칙을 만들어 서비스 계정의 기본 이벤트 버스로 계정 생성 이벤트를 보냅니다. 서비스 계정의 기본 이벤트 버스를 업데이트하여 자동화 계정의 이벤트를 허용합니다. 가장 많이 투표된
B. 서비스 계정에서 사용자 지정 Amazon EventBridge 이벤트 버스를 만듭니다. 사용자 지정 이벤트 버스를 업데이트하여 자동화 계정의 이벤트를 허용합니다. 서비스 계정에서 자동화 계정의 CloudTrail 이벤트를 직접 수신하는 EventBridge 규칙을 만듭니다.
C. 자동화 계정과 서비스 계정에서 사용자 정의 Amazon EventBridge 이벤트 버스를 만듭니다. 자동화 계정과 서비스 계정에 있는 사용자 정의 이벤트 버스를 연결하는 EventBridge 규칙과 정책을 만듭니다.
D. 자동화 계정에서 사용자 지정 Amazon EventBridge 이벤트 버스를 만듭니다. 사용자 지정 이벤트 버스를 서비스 계정의 기본 이벤트 버스에 연결하는 EventBridge 규칙과 정책을 만듭니다.



### 
나(16%)

질문 #168주제 1
DevOps 엔지니어가 Amazon Simple Queue Service(Amazon SQS) 표준 대기열을 사용하는 솔루션을 구축하고 있습니다. 이 솔루션에는 AWS Lambda 함수와 Amazon DynamoDB 테이블도 포함되어 있습니다. Lambda 함수는 SQS 대기열 이벤트 소스에서 콘텐츠를 가져와 DynamoDB 테이블에 씁니다.

이 솔루션은 Lambda의 확장성을 극대화해야 하며 성공적으로 처리된 SQS 메시지가 여러 번 처리되는 것을 방지해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 람다 함수의 이벤트 소스 매핑을 구성할 때 일괄 처리 창을 1초로 줄입니다.
B. Lambda 함수의 이벤트 소스 매핑을 구성할 때 배치 크기를 1로 줄입니다.
C. Lambda 함수의 이벤트 소스 매핑에 있는 FunctionResponseTypes 목록에 ReportBatchItemFailures 값을 포함합니다. 가장 많이 투표된
D. Lambda 함수의 이벤트 소스 매핑에서 대기열 가시성 시간 초과를 설정하여 Lambda 함수의 호출 제한을 고려합니다.



### 질문 #169주제 1
한 회사에 팀이 다양한 애플리케이션을 배포하는 데 사용할 새로운 AWS 계정이 있습니다. 팀은 애플리케이션별 목적과 AWS CloudTrail 로그를 저장하기 위해 많은 Amazon S3 버킷을 만듭니다. 회사는 계정에 Amazon Macie를 활성화했습니다.

DevOps 엔지니어는 계정의 기능을 손상시키지 않으면서 계정에 대한 Macie 비용을 최적화해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요? (두 가지를 선택하세요.)

A. CloudTrail 로그가 포함된 S3 버킷을 자동 검색에서 제외합니다. 가장 많이 투표된
B. 공개 읽기 액세스 권한이 있는 S3 버킷을 자동 검색에서 제외합니다.
C. 계정의 모든 S3 버킷에 대해 예약된 일일 검색 작업을 구성합니다.
D. 마지막으로 수정된 기준에 따라 S3 객체를 포함하도록 검색 작업을 구성합니다. 가장 많이 투표된
E. 프로덕션으로만 태그가 지정된 S3 객체를 포함하도록 검색 작업을 구성합니다.



### 질문 #170주제 1
한 회사가 AWS Organizations에서 조직을 사용하여 AWS 계정을 관리합니다. 이 회사는 최근 독립형 AWS 계정이 있는 다른 회사를 인수했습니다. 인수한 회사의 DevOps 팀은 두 회사의 AWS 계정 관리를 통합하고 계정에 대한 전체 관리 제어권을 유지해야 합니다. DevOps 팀은 또한 모든 계정에서 결과를 수집하고 그룹화하여 보안 태세를 구현하고 유지해야 합니다.

DevOps 팀은 이러한 요구 사항을 충족하기 위해 어떤 단계 조합을 취해야 합니까? (두 가지를 선택하세요.)

A. 인수한 회사의 AWS 계정을 조직에 가입하도록 초대합니다. 전체 관리자 권한이 있는 SCP를 만듭니다. SCP를 관리 계정에 연결합니다.
B. 인수한 회사의 AWS 계정을 조직에 가입하도록 초대합니다. 초대된 계정에서 OrganizationAccountAccessRole IAM 역할을 만듭니다. 관리 계정에 역할을 맡을 수 있는 권한을 부여합니다. 가장 많이 투표된
C. AWS Security Hub를 사용하여 모든 계정에서 결과를 수집하고 그룹화합니다. Security Hub를 사용하여 조직에 계정이 추가될 때 자동으로 새 계정을 감지합니다. 가장 많이 투표된
D. AWS Firewall Manager를 사용하여 모든 계정에서 결과를 수집하고 그룹화합니다. 조직의 모든 기능을 활성화합니다. 조직의 계정을 Firewall Manager의 위임된 관리자 계정으로 지정합니다.
E. Amazon Inspector를 사용하여 모든 계정에서 결과를 수집하고 그룹화합니다. 조직의 계정을 Amazon Inspector의 위임된 관리자 계정으로 지정합니다.



### 질문 #171주제 1
회사에 애플리케이션과 CI/CD 파이프라인이 있습니다. CI/CD 파이프라인은 AWS CodePipeline 파이프라인과 AWS CodeBuild 프로젝트로 구성됩니다. CodeBuild 프로젝트는 빌드 프로세스의 일부로 애플리케이션에 대한 테스트를 실행하고 테스트 보고서를 출력합니다. 회사는 테스트 보고서를 90일 동안 보관해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. CodeBuild 프로젝트가 포함된 단계 뒤에 CodePipeline 파이프라인에 새 단계를 추가합니다. 보고서를 저장할 Amazon S3 버킷을 만듭니다. 보고서에 적합한 경로와 형식으로 새 CodePipeline 단계에서 S3 배포 작업 유형을 구성합니다.
B. CodeBuild 프로젝트 buildspec 파일에 보고서의 적절한 경로와 형식으로 보고서 그룹을 추가합니다. 보고서를 저장할 Amazon S3 버킷을 만듭니다. 빌드가 완료되면 보고서를 S3 버킷에 복사하기 위해 AWS Lambda 함수를 호출하는 Amazon EventBridge 규칙을 구성합니다. 90일 후에 객체를 만료시키는 S3 Lifecycle 규칙을 만듭니다. 가장 많이 투표된
C. CodePipeline 파이프라인에 새 단계를 추가합니다. 보고서에 적합한 경로와 형식으로 테스트 작업 유형을 구성합니다. CodeBuild 프로젝트 buildspec 파일에서 보고서 만료 시간을 90일로 구성합니다.
D. CodeBuild 프로젝트 buildspec 파일에 보고서의 적절한 경로와 형식으로 보고서 그룹을 추가합니다. 보고서를 저장할 Amazon S3 버킷을 만듭니다. CodeBuild 프로젝트 buildspec 파일에서 보고서 그룹을 아티팩트로 구성합니다. S3 버킷을 아티팩트 대상으로 구성합니다. 객체 만료일을 90일로 설정합니다.



### 질문 #172주제 1
한 회사가 Amazon API Gateway 지역 REST API를 사용하여 애플리케이션 API를 호스팅합니다. REST API에는 사용자 지정 도메인이 있습니다. REST API의 기본 엔드포인트는 비활성화됩니다.

회사의 내부 팀은 API를 사용합니다. 회사는 API와 내부 팀 간의 상호 TLS를 추가 인증 계층으로 사용하려고 합니다.

이러한 요구 사항을 충족하는 단계 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. AWS Certificate Manager(ACM)를 사용하여 개인 인증 기관(CA)을 만듭니다. 개인 CA에서 서명한 클라이언트 인증서를 제공합니다. 가장 많이 투표된
B. 공공 인증 기관(CA)에서 서명한 클라이언트 인증서를 제공합니다. 인증서를 AWS Certificate Manager(ACM)로 가져옵니다.
C. 제공된 클라이언트 인증서를 Amazon S3 버킷에 업로드합니다. S3 버킷에 저장된 클라이언트 인증서를 신뢰 저장소로 사용하도록 API Gateway 상호 TLS를 구성합니다.
D. 제공된 클라이언트 인증서 개인 키를 Amazon S3 버킷에 업로드합니다. S3 버킷에 저장된 개인 키를 신뢰 저장소로 사용하도록 API Gateway 상호 TLS를 구성합니다.
E. 루트 개인 인증 기관(CA) 인증서를 Amazon S3 버킷에 업로드합니다. S3 버킷에 저장된 개인 CA 인증서를 신뢰 저장소로 사용하도록 API Gateway 상호 TLS를 구성합니다. 가장 많이 투표된



### 질문 #173주제 1
한 회사에서는 AWS Directory Service for Microsoft Active Directory를 ID 공급자(IdP)로 사용합니다. 이 회사에서는 모든 인프라가 AWS CloudFormation에서 정의되고 배포되어야 합니다.

DevOps 엔지니어는 애플리케이션을 호스팅하기 위해 Windows 기반 Amazon EC2 인스턴스 플릿을 만들어야 합니다. DevOps 엔지니어는 EC2 시작 템플릿, IAM 역할, EC2 보안 그룹, EC2 자동 확장 그룹이 포함된 CloudFormation 템플릿을 만들었습니다. DevOps 엔지니어는 모든 EC2 인스턴스를 AWS Managed Microsoft AD 디렉터리의 도메인에 조인하는 솔루션을 구현해야 합니다.

어떤 솔루션이 가장 높은 운영 효율성으로 이러한 요구 사항을 충족할까요?

A. CloudFormation 템플릿에서 기존 디렉토리의 매개변수를 사용하여 EC2 인스턴스를 AWS Managed Microsoft AD 도메인에 조인하는 AWS::SSM::Document 리소스를 만듭니다. SSMAssociation 속성을 포함하도록 시작 템플릿을 업데이트하여 새 SSM 문서를 사용합니다. AmazonSSMManagedInstanceCore 및 AmazonSSMDirectoryServiceAccess AWS 관리 정책을 EC2 인스턴스가 사용하는 IAM 역할에 연결합니다.
B. CloudFormation 템플릿에서 시작 시 전파되는 특정 태그를 포함하도록 시작 템플릿을 업데이트합니다. AWS::SSM::Association 리소스를 생성하여 AWS-JoinDirectoryServiceDomain Automation 런북을 지정된 태그가 있는 EC2 인스턴스와 연결합니다. AWS Managed Microsoft AD 디렉터리에 가입하는 데 필요한 매개변수를 정의합니다. EC2 인스턴스가 사용하는 IAM 역할에 AmazonSSMManagedInstanceCore 및 AmazonSSMDirectoryServiceAccess AWS 관리 정책을 연결합니다. 가장 많이 투표된
C. 기존 AWS Managed Microsoft AD 도메인 연결 세부 정보를 AWS Secrets Manager에 저장합니다. CloudFormation 템플릿에서 AWS::SSM::Association 리소스를 만들어 AWS-CreateManagedWindowsInstanceWithApproval Automation 런북을 EC2 Auto Scaling 그룹과 연결합니다. Secrets Manager에서 매개변수에 대한 ARN을 전달하여 도메인에 가입합니다. AmazonSSMDirectoryServiceAccess 및 SecretsManagerReadWrite AWS 관리 정책을 EC2 인스턴스가 사용하는 IAM 역할에 연결합니다.
D. 기존 AWS Managed Microsoft AD 도메인 관리자 자격 증명을 AWS Secrets Manager에 저장합니다. CloudFormation 템플릿에서 EC2 시작 템플릿을 업데이트하여 사용자 데이터를 포함합니다. Secrets Manager에서 관리자 자격 증명을 가져오고 AWS Managed Microsoft AD 도메인에 가입하도록 사용자 데이터를 구성합니다. EC2 인스턴스가 사용하는 IAM 역할에 AmazonSSMManagedInstanceCore 및 SecretsManagerReadWrite AWS 관리 정책을 연결합니다.



### 질문 #174주제 1
한 회사에서 AWS Organizations를 사용하여 AWS 계정을 관리합니다. 이 회사에는 자식 OU가 있는 루트 OU가 있습니다. 루트 OU에는 모든 리소스에 대한 모든 작업을 허용하는 SCP가 있습니다. 자식 OU에는 Amazon DynamoDB 및 AWS Lambda에 대한 모든 작업을 허용하고 다른 모든 작업을 거부하는 SCP가 있습니다.

이 회사에는 자식 OU에 vendor-data라는 AWS 계정이 있습니다. DevOps 엔지니어는 vendor-data 계정의 관리자 액세스 IAM 정책에 연결된 IAM 사용자가 있습니다. DevOps 엔지니어는 vendor-data 계정에서 Amazon EC2 인스턴스를 시작하려고 하지만 액세스 거부 오류가 발생합니다. DevOps 엔지니어

는 vendor-data 계정에서 EC2 인스턴스를 시작하기 위해 어떤 변경을 해야 합니까?

A. AmazonEC2FullAccess IAM 정책을 IAM 사용자에게 연결합니다.
B. Amazon EC2에 대한 모든 작업을 허용하는 새 SCP를 만듭니다. SCP를 vendor-data 계정에 연결합니다.
C. 자식 OU의 SCP를 업데이트하여 Amazon EC2에 대한 모든 작업을 허용합니다. 가장 많이 투표된
D. Amazon EC2에 대한 모든 작업을 허용하는 새 SCP를 만듭니다. SCP를 루트 OU에 연결합니다.



### 질문 #175주제 1
회사의 보안 정책은 프로덕션 환경에서 보안 강화 AMI를 사용해야 합니다. DevOps 엔지니어는 EC2 Image Builder를 사용하여 반복 일정에 따라 AMI를 빌드하는 파이프라인을 만들었습니다.

DevOps 엔지니어는 회사의 Auto Scaling 그룹의 시작 템플릿을 업데이트해야 합니다. Auto Scaling 그룹은 Amazon EC2 인스턴스를 시작하는 동안 최신 AMI를 사용해야 합니다.

어떤 솔루션이 가장 높은 운영 효율성으로 이러한 요구 사항을 충족할까요?

A. Image Builder에서 새 AMI 이벤트를 수신하도록 Amazon EventBridge 규칙을 구성합니다. 최신 AMI ID로 Auto Scaling 그룹의 시작 템플릿을 업데이트하는 AWS Systems Manager Run Command 문서를 대상으로 합니다.
B. Image Builder에서 새 AMI 이벤트를 수신하도록 Amazon EventBridge 규칙을 구성합니다. 최신 AMI ID로 Auto Scaling 그룹의 시작 템플릿을 업데이트하는 AWS Lambda 함수를 대상으로 합니다.
C. AWS Systems Manager Parameter Store의 값을 AMI ID에 사용하도록 시작 템플릿을 구성합니다. Image Builder 파이프라인을 구성하여 Parameter Store 값을 최신 AMI ID로 업데이트합니다.
D. Image Builder 배포 설정을 구성하여 최신 AMI로 실행 템플릿을 업데이트합니다. 자동 크기 조정 그룹이 최신 버전의 실행 템플릿을 사용하도록 구성합니다. 가장 많이 투표된



### 질문 #176주제 1
한 회사가 AWS Lambda 함수에서 Amazon S3 이벤트 소스를 구성했습니다. 이 회사는 특정 S3 버킷에서 새 객체가 생성되거나 기존 객체가 수정될 때 Lambda 함수가 실행되어야 합니다. Lambda 함수는 들어오는 이벤트의 S3 버킷 이름과 S3 객체 키를 사용하여 생성되거나 수정된 ​​S3 객체의 내용을 읽습니다. Lambda 함수는 내용을 구문 분석하고 구문 분석된 내용을 Amazon DynamoDB 테이블에 저장합니다. Lambda

함수의 실행 역할에는 S3 버킷에서 읽고 DynamoDB 테이블에 쓸 수 있는 권한이 있습니다. 테스트하는 동안 DevOps 엔지니어는 객체가 S3 버킷에 추가되거나 기존 객체가 수정될 때 Lambda 함수가 실행되지 않는다는 것을 발견했습니다.

어떤 솔루션이 이 문제를 해결할까요?

A. Lambda 함수의 메모리를 늘려서 함수가 S3 버킷에서 대용량 파일을 처리할 수 있도록 합니다.
B. Lambda 함수에서 리소스 정책을 생성하여 Amazon S3가 S3 버킷에 대해 Lambda 함수를 호출할 수 있는 권한을 부여합니다. 가장 많이 투표된
C. Lambda 함수에 대한 OnFailure 대상으로 Amazon Simple Queue Service(Amazon SQS) 대기열을 구성합니다.
D. Lambda 함수의 /tmp 폴더에 공간을 프로비저닝하여 함수가 S3 버킷에서 대용량 파일을 처리할 수 있는 기능을 제공합니다.



### 질문 #177주제 1
한 회사가 두 AWS 지역에 중요한 애플리케이션을 배포했습니다. 이 애플리케이션은 두 지역 모두에서 애플리케이션 로드 밸런서(ALB)를 사용합니다. 이 회사는 두 ALB에 대한 Amazon Route 53 별칭 DNS 레코드를 가지고 있습니다.

이 회사는 Amazon Route 53 애플리케이션 복구 컨트롤러를 사용하여 애플리케이션이 두 지역 간에 장애 조치를 수행할 수 있도록 합니다. Route 53 ARC 구성에는 두 지역에 대한 라우팅 제어가 포함되어 있습니다. 이 회사는 Route 53 ARC를 사용하여 분기별 재해 복구(DR) 테스트를 수행합니다.

가장 최근의 DR 테스트 중에 DevOps 엔지니어가 실수로 두 라우팅 제어를 모두 껐습니다. 이 회사는 항상 최소한 하나의 라우팅 제어가 켜져 있는지 확인해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Route 53 ARC에서 새로운 어설션 안전 규칙을 만듭니다. 어설션 안전 규칙을 두 개의 라우팅 제어에 적용합니다. 임계값이 1인 ATLEAST 유형으로 규칙을 구성합니다. 가장 많이 투표된
B. Route 53 ARC에서 새로운 게이팅 안전 규칙을 만듭니다. 두 개의 라우팅 제어에 어설션 안전 규칙을 적용합니다. 임계값이 1인 OR 유형으로 규칙을 구성합니다.
C. Route 53 ARC에서 새 리소스 세트를 만듭니다. AWS::Route53::HealthCheck 리소스 유형으로 리소스 세트를 구성합니다. 두 라우팅 컨트롤의 ARN을 대상 리소스로 지정합니다. 리소스 세트에 대한 새 준비성 검사를 만듭니다.
D. Route 53 ARC에서 새 리소스 세트를 만듭니다. AWS::Route53RecoveryReadiness::DNSTargetResource 리소스 유형으로 리소스 세트를 구성합니다. 두 Route 53 별칭 DNS 레코드의 도메인 이름을 대상 리소스로 추가합니다. 리소스 세트에 대한 새 준비 상태 검사를 만듭니다.



### 질문 #178주제 1
의료 서비스 회사는 환자 건강 모니터링을 위한 애플리케이션의 소프트웨어 라이선스 비용이 증가하는 것에 대해 우려하고 있습니다. 이 회사는 애플리케이션이 Amazon EC2 전용 호스트에서만 실행되도록 감사 프로세스를 만들고자 합니다. DevOps 엔지니어는 규정 준수를 보장하기 위해 애플리케이션을 감사하는 워크플로를 만들어야 합니다.

엔지니어는 최소한의 관리 오버헤드로 이 요구 사항을 충족하기 위해 어떤 단계를 거쳐야 합니까?

A. AWS Systems Manager Configuration Compliance를 사용합니다. put-compliance-items API 작업에 대한 호출을 사용하여 호스트 배치 구성을 기반으로 비준수 EC2 인스턴스의 데이터베이스를 스캔하고 빌드합니다. Amazon DynamoDB 테이블을 사용하여 이러한 인스턴스 ID를 저장하여 빠르게 액세스합니다. list-compliance-summaries API 작업을 호출하여 Systems Manager를 통해 보고서를 생성합니다.
B. EC2 인스턴스에서 실행되는 사용자 지정 Java 코드를 사용합니다. 검사할 인스턴스 수에 따라 인스턴스에 대한 EC2 자동 확장을 설정합니다. 비준수 EC2 인스턴스 ID 목록을 Amazon SQS 대기열로 보냅니다. SQS 대기열에서 인스턴스 ID를 처리하고 Amazon DynamoD에 쓸 다른 작업자 인스턴스를 설정합니다. AWS Lambda 함수를 사용하여 대기열에서 얻은 비준수 인스턴스 ID를 종료하고 배포를 위해 Amazon SNS 이메일 주제로 보냅니다.
C. AWS Config를 사용합니다. 해당 지역의 모든 Amazon EC2 리소스에서 Config Recording을 활성화하여 감사할 모든 EC2 인스턴스를 식별합니다. "config-rule-change -triggered" 블루프린트를 사용하여 AWS Lambda 함수를 트리거하는 사용자 지정 AWS Config 규칙을 만듭니다. Lambda evaluateCompliance() 함수를 수정하여 인스턴스가 EC2 전용 호스트에서 실행되지 않는 경우 NON_COMPLIANT 결과를 반환하도록 호스트 배치를 확인합니다. AWS Config 보고서를 사용하여 비준수 인스턴스를 처리합니다. 가장 많이 투표된
D. AWS CloudTrail을 사용합니다. EC2 RunCommand API 작업에 대한 모든 호출을 분석하여 감사할 모든 EC2 인스턴스를 식별합니다. 인스턴스의 호스트 배치를 분석하는 AWS Lambda 함수를 호출합니다. 비준수 리소스의 EC2 인스턴스 ID를 Amazon RDS for MySQL DB 인스턴스에 저장합니다. RDS 인스턴스를 쿼리하고 쿼리 결과를 CSV 텍스트 파일로 내보내 보고서를 생성합니다.



### 질문 #179주제 1
DevOps 엔지니어가 Ruby 기반 애플리케이션을 프로덕션에 배포하려고 계획하고 있습니다. 이 애플리케이션은 Amazon RDS for MySQL 데이터베이스와 상호 작용해야 하며 자동 확장 및 고가용성이 있어야 합니다. 데이터베이스에 저장된 데이터는 중요하며 애플리케이션 스택의 상태와 관계없이 유지되어야 합니다.

DevOps 엔지니어는 자동 롤백을 사용하여 애플리케이션에 대한 자동화된 배포 전략을 설정해야 합니다. 솔루션은 또한 배포가 실패할 때 애플리케이션 팀에 경고해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. AWS Elastic Beanstalk에 애플리케이션을 배포합니다. Elastic Beanstalk 구성의 일부로 Amazon RDS for MySQL DB 인스턴스를 배포합니다.
B. AWS Elastic Beanstalk에 애플리케이션을 배포합니다. Elastic Beanstalk 외부에 별도의 Amazon RDS for MySQL DB 인스턴스를 배포합니다. 가장 많이 투표된
C. AWS Elastic Beanstalk 구성에서 애플리케이션 팀에 알림을 보내는 알림 이메일 주소를 구성합니다. 가장 많이 투표된
D. AWS Health 이벤트를 모니터링하기 위해 Amazon EventBridge 규칙을 구성합니다. Amazon Simple Notification Service(Amazon SNS) 토픽을 대상으로 사용하여 애플리케이션 팀에 경고합니다.
E. 변경 불가능한 배포 방법을 사용하여 새로운 애플리케이션 버전을 배포합니다. 가장 많이 투표된
F. 롤링 배포 방식을 사용하여 새로운 애플리케이션 버전을 배포합니다.




### 질문 #180주제 1
한 회사가 AWS CodePipeline을 사용하여 애플리케이션을 배포하고 있습니다. 새로운 가이드라인에 따르면, 회사 보안팀 구성원은 변경 사항이 프로덕션에 배포되기 전에 모든 애플리케이션 변경 사항에 서명해야 합니다. 승인은 기록하고 보관해야 합니다.

이러한 요구 사항을 충족하는 작업 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. CodePipeline을 구성하여 Amazon CloudWatch Logs에 작업을 작성합니다.
B. 각 파이프라인 단계의 끝에서 Amazon S3 버킷에 작업을 쓰도록 CodePipeline을 구성합니다.
C. Amazon S3에 로그를 전송하기 위한 AWS CloudTrail 트레일을 생성합니다. 가장 많이 투표된
D. 승인을 위해 AWS Lambda 함수를 호출하는 CodePipeline 사용자 지정 작업을 만듭니다. 보안 팀에 CodePipeline 사용자 지정 작업을 관리할 수 있는 액세스 권한을 부여하는 정책을 만듭니다.
E. 배포 단계 전에 CodePipeline 수동 승인 작업을 만듭니다. 보안 팀에 수동 승인 단계를 승인할 수 있는 액세스 권한을 부여하는 정책을 만듭니다. 가장 많이 투표된



### 질문 #181주제 1
한 회사에서는 내부 비즈니스 팀이 사전 승인된 AWS CloudFormation 템플릿을 통해서만 리소스를 시작하도록 요구합니다. 보안 팀은 리소스가 예상 상태에서 벗어나는 경우 자동화된 모니터링을 요구합니다.

이러한 요구 사항을 충족하기 위해 어떤 전략을 사용해야 합니까?

A. 사용자가 CloudFormation 서비스 역할만 사용하여 CloudFormation 스택을 배포하도록 허용합니다. CloudFormation 드리프트 감지를 사용하여 리소스가 예상 상태에서 벗어나는 경우를 감지합니다.
B. 사용자가 CloudFormation 서비스 역할만 사용하여 CloudFormation 스택을 배포하도록 허용합니다. AWS Config 규칙을 사용하여 리소스가 예상 상태에서 벗어난 경우를 감지합니다.
C. 사용자가 AWS Service Catalog만 사용하여 CloudFormation 스택을 배포하도록 허용합니다. 시작 제약 조건의 사용을 강제합니다. AWS Config 규칙을 사용하여 리소스가 예상 상태에서 벗어난 경우를 감지합니다. 가장 많이 투표된
D. 사용자가 AWS Service Catalog만 사용하여 CloudFormation 스택을 배포하도록 허용합니다. 템플릿 제약 조건의 사용을 강제합니다. Amazon EventBridge 알림을 사용하여 리소스가 예상 상태에서 벗어나는 경우를 감지합니다.



### 질문 #182주제 1
한 회사에는 단일 공유 AWS 계정에서 작업하는 여러 개발 그룹이 있습니다. 그룹의 상임 관리자는 리소스 생성이 계정의 서비스 한도에 도달하면 타사 API 호출을 통해 알림을 받고 싶어합니다.

어떤 솔루션이 최소한의 개발 노력으로 이를 달성할까요?

A. 주기적으로 실행되고 AWS Lambda 함수를 대상으로 하는 Amazon EventBridge 규칙을 만듭니다. Lambda 함수 내에서 AWS 환경의 현재 상태를 평가하고 배포된 리소스 값을 계정의 리소스 제한과 비교합니다. 계정이 서비스 제한에 접근하는 경우 상급 관리자에게 알립니다.
B. AWS Trusted Advisor 검사를 새로 고치는 AWS Lambda 함수를 배포하고 Lambda 함수를 주기적으로 실행하도록 Amazon EventBridge 규칙을 구성합니다. Trusted Advisor 이벤트와 대상 Lambda 함수가 일치하는 이벤트 패턴으로 다른 EventBridge 규칙을 만듭니다. 대상 Lambda 함수에서 상급 관리자에게 알립니다. 가장 많이 투표된
C. AWS Health Dashboard 검사를 새로 고치는 AWS Lambda 함수를 배포하고 Lambda 함수를 주기적으로 실행하도록 Amazon EventBridge 규칙을 구성합니다. Health Dashboard 이벤트와 대상 Lambda 함수가 일치하는 이벤트 패턴으로 다른 EventBridge 규칙을 만듭니다. 대상 Lambda 함수에서 상급 관리자에게 알립니다.
D. 주기적으로 실행되고, AWS 서비스 제한 상태를 확인하고, Amazon Simple Notification Service(Amazon SNS) 토픽으로 알림을 스트리밍하는 AWS Config 사용자 지정 규칙을 추가합니다. 상급 관리자에게 알리는 AWS Lambda 함수를 배포하고 Lambda 함수를 SNS 토픽에 구독합니다.



### 질문 #183주제 1
DevOps 엔지니어가 컨테이너 기반 아키텍처를 설정하고 있습니다. 이 엔지니어는 AWS CloudFormation을 사용하여 Amazon ECS 클러스터와 Amazon EC2 Auto Scaling 그룹을 자동으로 프로비저닝하여 EC2 컨테이너 인스턴스를 시작하기로 결정했습니다. CloudFormation 스택을 성공적으로 생성한 후, 엔지니어는 ECS 클러스터와 EC2 인스턴스가 성공적으로 생성되었고 스택이 생성을 완료했지만 EC2 인스턴스가 다른 클러스터와 연결되어 있다는 것을 알아챘습니다.

DevOps 엔지니어는 이 문제를 해결하기 위해 CloudFormation 템플릿을 어떻게 업데이트해야 합니까?

A. AWS::ECS::Cluster 리소스에서 EC2 인스턴스를 참조하고 AWS::ECS::Service 리소스에서 ECS 클러스터를 참조합니다.
B. UserData 속성의 AWS::AutoScaling::LaunchConfiguration 리소스에서 ECS 클러스터를 참조합니다. 가장 많이 투표된
C. UserData 속성의 AWS::EC2::Instance 리소스에서 ECS 클러스터를 참조합니다.
D. AWS::CloudFormation::CustomResource 리소스에서 ECS 클러스터를 참조하여 적절한 ECS 클러스터에 EC2 인스턴스를 등록하는 AWS Lambda 함수를 트리거합니다.



### 질문 #184주제 1
DevOps 엔지니어가 인프라를 미국 내에 두어야 하는 회사에 대한 거버넌스 제어를 구현하고 있습니다. 엔지니어는 사용할 수 있는 AWS 리전을 제한해야 하며 거버넌스 정책 외부의 활동이 발생하면 가능한 한 빨리 알림을 보내야 합니다. 미국(US) 외부의 모든 새 리전에서 제어를 자동으로 활성화해야 합니다.

이러한 요구 사항을 충족하는 작업 조합은 무엇입니까? (두 가지를 선택하세요.)

A. 미국 외 지역의 모든 비 글로벌 서비스에 대한 액세스를 거부하는 AWS Organizations SCP를 만듭니다. 정책을 조직의 루트에 첨부합니다. 가장 많이 투표된
B. AWS CloudTrail을 구성하여 Amazon CloudWatch Logs에 로그를 보내고 모든 리전에 대해 활성화합니다. CloudWatch Logs 메트릭 필터를 사용하여 미국 이외 리전의 모든 서비스 활동에 대한 알림을 보냅니다. 가장 많이 투표된
C. AWS 서비스 활동을 확인하고 모든 리전에 배포하는 AWS Lambda 함수를 사용합니다. 매 시간 Lambda 함수를 실행하고 미국 이외 리전에서 활동이 발견되면 알림을 보내는 Amazon EventBridge 규칙을 작성합니다.
D. AWS Lambda 함수를 사용하여 Amazon Inspector에 쿼리를 보내 미국 이외 지역의 서비스 활동을 확인하고 활동이 발견되면 알림을 보냅니다.
E. aws:RequestedRegion 조건 키를 사용하여 US 지역에 대한 액세스를 제한하는 SCP를 작성합니다. 모든 사용자, 그룹 및 역할에 정책을 적용합니다.



### 질문 #185주제 1
한 회사가 전자상거래 웹 애플리케이션을 통해 제품을 판매합니다. 이 회사는 제품 거래 세부 정보의 파이 차트를 보여주는 대시보드를 원합니다. 이 회사는 대시보드를 회사의 기존 Amazon CloudWatch 대시보드와 통합하려고 합니다.

어떤 솔루션이 가장 높은 운영 효율성으로 이러한 요구 사항을 충족할까요?

A. e커머스 애플리케이션을 업데이트하여 처리된 각 거래에 대해 CloudWatch 로그 그룹에 JSON 객체를 방출합니다. CloudWatch Logs Insights를 사용하여 로그 그룹을 쿼리하고 파이 차트 형식으로 결과를 시각화합니다. 결과를 원하는 CloudWatch 대시보드에 연결합니다. 가장 많이 투표된
B. 각 처리된 거래에 대해 Amazon S3 버킷에 JSON 객체를 내보내도록 전자상거래 애플리케이션을 업데이트합니다. Amazon Athena를 사용하여 S3 버킷을 쿼리하고 파이 차트 형식으로 결과를 시각화합니다. Athena에서 결과를 내보냅니다. 결과를 원하는 CloudWatch 대시보드에 첨부합니다.
C. AWS X-Ray를 계측에 사용하도록 전자상거래 애플리케이션을 업데이트합니다. 새로운 X-Ray 하위 세그먼트를 만듭니다. 처리된 각 거래에 대한 주석을 추가합니다. X-Ray 추적을 사용하여 데이터를 쿼리하고 파이 차트 형식으로 결과를 시각화합니다. 결과를 원하는 CloudWatch 대시보드에 연결합니다.
D. 처리된 각 거래에 대해 CloudWatch 로그 그룹에 JSON 객체를 내보내도록 전자상거래 애플리케이션을 업데이트합니다. 결과를 집계하여 Amazon DynamoDB에 쓰는 AWS Lambda 함수를 만듭니다. 로그 파일에 대한 Lambda 구독 필터를 만듭니다. 결과를 원하는 CloudWatch 대시보드에 첨부합니다.



### 질문 #186주제 1
회사에서 애플리케이션을 시작합니다. 애플리케이션은 승인된 AWS 서비스만 사용해야 합니다. 애플리케이션을 실행하는 계정은 1년 이내에 생성되었으며 AWS Organizations OU에 할당되었습니다.

회사는 새 Organizations 계정 구조를 만들어야 합니다. 계정 구조에는 현재 AWS 계정에서 활성화된 서비스만 사용할 수 있는 적절한 SCP가 있어야 합니다. 회사는 솔루션에서 AWS Identity and Access Management(IAM) Access Analyzer를 사용합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. IAM Access Analyzer가 식별하는 서비스를 허용하는 SCP를 만듭니다. 계정에 대한 OU를 만듭니다. 계정을 새 OU로 이동합니다. 새 SCP를 새 OU에 연결합니다. 새 OU에서 기본 FullAWSAccess SCP를 분리합니다. 가장 많이 투표된
B. IAM Access Analyzer가 식별하는 서비스를 거부하는 SCP를 만듭니다. 계정에 대한 OU를 만듭니다. 계정을 새 OU로 이동합니다. 새 SCP를 새 OU에 연결합니다.
C. IAM Access Analyzer가 식별하는 서비스를 허용하는 SCP를 만듭니다. 새 SCP를 조직의 루트에 연결합니다.
D. IAM Access Analyzer가 식별하는 서비스를 허용하는 SCP를 만듭니다. 계정에 대한 OU를 만듭니다. 계정을 새 OU로 이동합니다. 새 SCP를 관리 계정에 연결합니다. 새 OU에서 기본 FullAWSAccess SCP를 분리합니다.



### 질문 #187주제 1
한 회사에는 공유된 단일 AWS 계정에서 작업하는 여러 사업부에 여러 개발 팀이 있습니다. 계정에서 생성된 모든 Amazon EC2 리소스에는 리소스를 만든 사람을 지정하는 태그가 포함되어야 합니다. 태그 지정은 리소스 생성 후 첫 시간 내에 이루어져야 합니다.

DevOps 엔지니어는 리소스를 만든 사용자 ID와 비용 센터 ID를 포함하는 태그를 생성된 리소스에 추가해야 합니다. DevOps 엔지니어는 비용 센터 매핑을 사용하여 리소스에 태그를 지정하기 위해 AWS Lambda 함수를 구성합니다. DevOps 엔지니어는 또한 AWS 계정에서 AWS CloudTrail을 설정합니다. Amazon S3 버킷은 CloudTrail 이벤트 로그를 저장합니다.

어떤 솔루션이 태그 지정 요구 사항을 충족할까요?

A. S3 버킷에서 S3 이벤트 알림을 생성하여 s3:ObjectTagging:Put 이벤트에 대한 Lambda 함수를 호출합니다. S3 버킷에서 버킷 버전 관리를 활성화합니다.
B. S3 버킷에서 서버 액세스 로깅을 활성화합니다. s3:ObjectTagging:* 이벤트에 대한 S3 버킷에서 S3 이벤트 알림을 만듭니다.
C. Lambda 함수를 호출하는 반복되는 시간별 Amazon EventBridge 예약 규칙을 만듭니다. Lambda 함수를 수정하여 S3 버킷에서 로그를 읽습니다.
D. Amazon EC2를 이벤트 소스로 사용하는 Amazon EventBridge 규칙을 만듭니다. CloudTrail에서 전달한 이벤트와 일치하도록 규칙을 구성합니다. Lambda 함수를 대상으로 규칙을 구성합니다. 가장 많이 투표된



### 질문 #188주제 1
한 회사가 단일 AWS 계정에서 여러 환경에 대한 애플리케이션을 실행합니다. AWS CodePipeline 파이프라인은 개발 Amazon Elastic Container Service(Amazon ECS) 클러스터를 사용하여 Amazon Elastic Container Registry(Amazon ECR) 저장소에서 애플리케이션의 이미지를 테스트합니다. 파이프라인은 이미지를 프로덕션 ECS 클러스터로 승격합니다.

회사는 프로덕션 클러스터를 동일한 AWS 리전의 별도 AWS 계정으로 옮겨야 합니다. 프로덕션 클러스터는 개인 연결을 통해 이미지를 다운로드할 수 있어야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Amazon ECR VPC 엔드포인트와 Amazon S3 게이트웨이 엔드포인트를 사용합니다. 별도의 AWS 계정에서 ECR 리포지토리를 만듭니다. 프로덕션 ECS 작업이 기본 AWS 계정에서 이미지를 가져올 수 있도록 리포지토리 정책을 설정합니다. 프로덕션 ECS 작업 실행 역할을 구성하여 ECR 리포지토리에서 이미지를 다운로드할 수 있는 권한을 갖도록 합니다.
B. 메인 AWS 계정의 프로덕션 ECR 리포지토리에 리포지토리 정책을 설정합니다. 리포지토리 정책을 구성하여 별도의 AWS 계정에서 프로덕션 ECS 작업이 메인 계정에서 이미지를 가져올 수 있도록 합니다. 프로덕션 ECS 작업 실행 역할에 ECR 리포지토리에서 이미지를 다운로드할 수 있는 권한을 부여합니다.
C. AWS 계정의 메인에서 ECR 개인 이미지 복제를 구성합니다. 계정 간 복제를 활성화합니다. 별도의 AWS 계정의 대상 계정 ID를 정의합니다.
D. Amazon ECR VPC 엔드포인트와 Amazon S3 게이트웨이 엔드포인트를 사용합니다. 메인 AWS 계정의 프로덕션 ECR 리포지토리에 리포지토리 정책을 설정합니다. 리포지토리 정책을 구성하여 별도의 AWS 계정에서 프로덕션 ECS 작업이 메인 계정에서 이미지를 가져올 수 있도록 합니다. 프로덕션 ECS 작업 실행 역할을 구성하여 ECR 리포지토리에서 이미지를 다운로드할 수 있는 권한을 갖도록 합니다. 가장 많이 투표된



### 질문 #189주제 1
회사는 AWS 계정의 모든 기존 및 새 VPC에 대해 플로우 로그가 구성된 상태로 유지되도록 해야 합니다. 회사는 AWS CloudFormation 스택을 사용하여 VPC를 관리합니다. 회사는 모든 IAM 사용자가 만든 모든 VPC에 적합한 솔루션이 필요합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. VPC를 생성하는 CloudFormation 스택에 AWS::EC2::FlowLog 리소스를 추가합니다.
B. AWS Organizations에서 조직을 만듭니다. 회사의 AWS 계정을 조직에 추가합니다. 사용자가 VPC 흐름 로그를 수정하지 못하도록 SCP를 만듭니다.
C. AWS Config를 켭니다. VPC 흐름 로그가 켜져 있는지 확인하기 위한 AWS Config 규칙을 만듭니다. VPC 흐름 로그를 켜기 위한 자동 수정을 구성합니다. 가장 많이 투표된
D. VPC 흐름 로그에 대한 API 호출 사용을 거부하는 IAM 정책을 만듭니다. 모든 IAM 사용자에게 IAM 정책을 연결합니다.



### 질문 #190주제 1
회사의 애플리케이션 팀은 애플리케이션에 AWS CodeCommit 리포지토리를 사용합니다. 애플리케이션 팀은 여러 AWS 계정에 리포지토리를 가지고 있습니다. 모든 계정은 AWS Organizations의 Organization에 있습니다.

각 애플리케이션 팀은 외부 IdP로 구성된 AWS IAM Identity Center(AWS Single Sign-On)를 사용하여 개발자 IAM 역할을 맡습니다. 개발자 역할을 통해 애플리케이션 팀은 Git을 사용하여 리포지토리의 코드로 작업할 수 있습니다.

보안 감사 결과 애플리케이션 팀은 모든 리포지토리의 메인 브랜치를 수정할 수 있음이 밝혀졌습니다. DevOps 엔지니어는 애플리케이션 팀이 관리하는 리포지토리의 메인 브랜치만 수정할 수 있는 솔루션을 구현해야 합니다.

이러한 요구 사항을 충족하는 단계 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. SAML 어설션을 업데이트하여 사용자의 팀 이름을 전달합니다. IAM 역할의 신뢰 정책을 업데이트하여 팀 이름이 있는 access-team 세션 태그를 추가합니다. 가장 많이 투표된
B. 조직 관리 계정에서 각 팀에 대한 승인 규칙 템플릿을 만듭니다. 템플릿을 모든 리포지토리와 연결합니다. 개발자 역할 ARN을 승인자로 추가합니다.
C. 각 계정에 대한 승인 규칙 템플릿을 만듭니다. 템플릿을 모든 리포지토리와 연결합니다. 승인 규칙 템플릿에 "aws:ResourceTag/access-team": "$ ;{aws:PrincipalTag/access-team}" 조건을 추가합니다.
D. 각 CodeCommit 저장소에 대해 연관된 팀의 이름으로 설정된 값을 갖는 access-team 태그를 추가합니다. 가장 많이 투표된
E. SCP를 계정에 첨부합니다. 다음 진술을 포함합니다.가장 많이 투표된
F. 각 계정에서 IAM 권한 경계를 만듭니다. 다음 문장을 포함합니다.



### 질문 #191주제 1
한 회사가 AWS WAF를 사용하여 클라우드 인프라를 보호합니다. DevOps 엔지니어는 운영 팀에 AWS WAF의 로그 메시지를 분석할 수 있는 기능을 제공해야 합니다. 운영 팀은 로그 출력의 특정 패턴에 대한 알람을 생성할 수 있어야 합니다.

어떤 솔루션이 최소한의 운영 오버헤드로 이러한 요구 사항을 충족할까요?

A. Amazon CloudWatch Logs 로그 그룹을 만듭니다. 로그 메시지를 로그 그룹으로 보내기 위해 적절한 AWS WAF 웹 ACL을 구성합니다. 운영 팀에 CloudWatch 메트릭 필터를 만들도록 지시합니다. 가장 많이 투표된
B. Amazon OpenSearch Service 클러스터와 적절한 인덱스를 만듭니다. Amazon Kinesis Data Firehose 전달 스트림을 구성하여 로그 데이터를 인덱스로 스트리밍합니다. OpenSearch Dashboards를 사용하여 필터와 위젯을 만듭니다.
C. 로그 출력을 위한 Amazon S3 버킷을 만듭니다. AWS WAF를 구성하여 로그 출력을 S3 버킷으로 보냅니다. 운영 팀에 원하는 각 로그 메시지 패턴을 감지하는 AWS Lambda 함수를 만들도록 지시합니다. Lambda 함수를 구성하여 Amazon Simple Notification Service(Amazon SNS) 토픽에 게시합니다.
D. 로그 출력을 위한 Amazon S3 버킷을 만듭니다. AWS WAF를 구성하여 로그 출력을 S3 버킷으로 보냅니다. Amazon Athena를 사용하여 로그 메시지 패턴에 맞는 외부 테이블 정의를 만듭니다. 운영 팀에 SQL 쿼리를 작성하고 Athena 쿼리에 대한 Amazon CloudWatch 메트릭 필터를 만들도록 지시합니다.



### 질문 #192주제 1
소프트웨어 팀은 AWS CodePipeline을 사용하여 Java 애플리케이션 릴리스 파이프라인을 자동화하고 있습니다. 파이프라인은 소스 단계, 빌드 단계, 배포 단계로 구성됩니다. 각 단계에는 runOrder 값이 1인 단일 작업이 포함됩니다.

팀은 기존 릴리스 파이프라인에 단위 테스트를 통합하려고 합니다. 팀은 모든 단위 테스트를 통과하는 코드 변경 사항만 배포하는 솔루션이 필요합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 빌드 단계를 수정합니다. runOrder 값이 1인 테스트 작업을 추가합니다. AWS CodeDeploy를 작업 공급자로 사용하여 단위 테스트를 실행합니다.
B. 빌드 단계를 수정합니다. runOrder 값이 2인 테스트 작업을 추가합니다. AWS CodeBuild를 작업 공급자로 사용하여 단위 테스트를 실행합니다. 가장 많이 투표된
C. 배포 단계를 수정합니다. runOrder 값이 1인 테스트 작업을 추가합니다. AWS CodeDeploy를 작업 공급자로 사용하여 단위 테스트를 실행합니다.
D. 배포 단계를 수정합니다. runOrder 값이 2인 테스트 작업을 추가합니다. AWS CodeBuild를 작업 공급자로 사용하여 단위 테스트를 실행합니다.



### 질문 #193주제 1
한 회사가 AWS Organizations에서 조직을 사용하여 회사 개발자가 사용하는 여러 AWS 계정을 관리합니다. 이 회사는 모든 데이터가 전송 중 암호화되도록 요구합니다.

개발자 계정에서 생성된 여러 Amazon S3 버킷은 암호화되지 않은 연결을 허용합니다. DevOps 엔지니어는 조직의 계정에서 생성된 모든 기존 S3 버킷에 대해 전송 중 데이터 암호화를 시행해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS CloudFormation StackSets를 사용하여 각 계정에 AWS Network Firewall 방화벽을 배포합니다. AWS 환경에서 모든 아웃바운드 요청을 방화벽을 통해 라우팅합니다. 포트 80에서 모든 아웃바운드 요청에 대한 액세스를 차단하는 정책을 배포합니다.
B. AWS CloudFormation StackSets를 사용하여 각 계정에 AWS Network Firewall 방화벽을 배포합니다. 방화벽을 통해 AWS 환경으로 들어오는 모든 요청을 라우팅합니다. 포트 80에서 들어오는 모든 요청에 ​​대한 액세스를 차단하는 정책을 배포합니다.
C. 조직에 대한 AWS Config를 켭니다. s3-bucket-ssl-requests-only 관리 규칙과 AWS Systems Manager Automation 런북을 사용하는 적합성 팩을 배포합니다. aws:SecureTransport 조건 키 값이 false일 때 S3 버킷에 대한 액세스를 거부하는 버킷 정책 문을 추가하는 런북을 사용합니다. 가장 많이 투표된
D. 조직에 대한 AWS Config를 켭니다. s3-bucket-ssl-requests-only 관리 규칙과 AWS Systems Manager Automation 런북을 사용하는 적합성 팩을 배포합니다. s3:x-amz-server-side-encryption-aws-kms-key-id 조건 키의 값이 null일 때 S3 버킷에 대한 액세스를 거부하는 버킷 정책 문을 추가하는 런북을 사용합니다.



### 질문 #194주제 1
한 회사가 IAM 정책을 검토하고 있습니다. DevOps 엔지니어가 작성한 정책 중 하나가 너무 관대한 것으로 표시되었습니다. 이 정책은 주말에 Environment: NonProduction 태그가 지정된 Amazon EC2 인스턴스에 중지 명령을 내리는 AWS Lambda 함수에서 사용됩니다. 현재 정책은 다음과 같습니다.



엔지니어가 최소 권한 정책을 달성하기 위해 어떤 변경을 해야 합니까? (세 가지를 선택하세요.)

A. 다음 조건식을 추가합니다.

B. "Resource": "*"를 "Resource": "arn:aws:ec2:*:*:instance/*"로 변경합니다. 가장 많이 투표된
C. 다음 조건식을 추가합니다.

D. 다음 조건식을 추가합니다.

E. "Action": "ec2:*"를 "Action": "ec2:StopInstances"로 변경합니다.
F. 다음 조건식을 추가합니다.



### 질문 #195주제 1
한 회사가 로그 이벤트를 생성하는 애플리케이션을 개발하고 있습니다. 로그 이벤트는 1/10초마다 5개의 고유한 메트릭으로 구성되며 많은 양의 데이터를 생성합니다.

이 회사는 Amazon Timestream에 로그를 쓰도록 애플리케이션을 구성해야 합니다. 이 회사는 Timestream 테이블에 대한 일일 쿼리를 구성합니다.

어떤 단계 조합이 가장 빠른 쿼리 성능으로 이러한 요구 사항을 충족시킬까요? (세 가지를 선택하세요.)

A. 일괄 쓰기를 사용하면 단일 쓰기 작업으로 여러 로그 이벤트를 쓸 수 있습니다. 가장 많이 투표된
B. 각 로그 이벤트를 단일 쓰기 작업으로 작성합니다.
C. 각 로그를 단일 측정 레코드로 처리합니다.
D. 각 로그를 다중 측정 레코드로 처리합니다. 가장 많이 투표된
E. 메모리 저장 보존 기간을 자기 저장 보존 기간보다 길게 구성합니다.
F. 메모리 저장 보존 기간을 자기 저장 보존 기간보다 짧게 구성합니다. 가장 많이 투표된



### 질문 #196주제 1
DevOps 엔지니어가 Amazon EC2 인스턴스에 애플리케이션을 배포하는 AWS CloudFormation 템플릿을 만들었습니다. EC2 인스턴스는 Amazon Linux를 실행합니다. 애플리케이션은 사용자 데이터가 포함된 셸 스크립트를 사용하여 EC2 인스턴스에 배포됩니다. EC2 인스턴스에는 AmazonSSMManagedinstanceCore 관리 정책이 첨부된 IAM 역할이 있는 IAM 인스턴스 프로필이 있습니다.

DevOps 엔지니어는 CloudFormation 템플릿의 사용자 데이터를 수정하여 새 버전의 애플리케이션을 설치했습니다. 엔지니어는 또한 스택 업데이트를 적용했습니다. 그러나 실행 중인 EC2 인스턴스에서 애플리케이션이 업데이트되지 않았습니다. 엔지니어는 애플리케이션의 변경 사항이 실행 중인 EC2 인스턴스에 설치되었는지 확인해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. Multipurpose Internet Mail Extensions(MIME) 멀티파트 형식을 사용하도록 사용자 데이터 콘텐츠를 구성합니다. text/cloud-config 섹션에서 scripts-user 매개변수를 always로 설정합니다.
B. cfn-init 헬퍼 스크립트를 사용하도록 사용자 데이터 명령을 리팩토링합니다. 사용자 데이터를 업데이트하여 cfn-hup 및 cfn-init 헬퍼 스크립트를 설치하고 구성하여 메타데이터 변경 사항을 모니터링하고 적용합니다. 가장 많이 투표된
C. EC2 인스턴스에 대한 EC2 시작 템플릿을 구성합니다. 새 EC2 자동 확장 그룹을 만듭니다. 자동 확장 그룹을 EC2 시작 템플릿과 연결합니다. 자동 확장 그룹에 대한 AutoScalingScheduledAction 업데이트 정책을 사용합니다.
D. AWS Systems Manager 문서(SSM 문서)를 사용하도록 사용자 데이터 명령을 리팩토링합니다. 사용자 데이터에 AWS CLI 명령을 추가하여 Systems Manager Run Command를 사용하여 SSM 문서를 EC2 인스턴스에 적용합니다.
E. AWS Systems Manager 문서(SSM 문서)를 사용하도록 사용자 데이터 명령을 리팩토링합니다. Systems Manager State Manager를 사용하여 SSM 문서와 EC2 인스턴스 간의 연결을 만듭니다. 가장 많이 투표된



### 질문 #197주제 1
한 회사가 AWS를 사용하기 위해 애플리케이션을 리팩토링하고 있습니다. 이 회사는 특정 AWS 계정에서 Amazon S3 API 호출을 해야 하는 내부 웹 애플리케이션을 식별합니다.

이 회사는 기존 ID 공급자(IdP) auth.company.com을 인증에 사용하려고 합니다. IdP는 OpenID Connect(OIDC)만 지원합니다. DevOps 엔지니어는 AWS 계정에 대한 웹 애플리케이션의 액세스를 보호해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. AWS IAM Identity Center(AWS Single Sign-On)를 구성합니다. IdP를 구성합니다. 기존 IdP에서 IdP 메타데이터를 업로드합니다.
B. 기존 IP의 공급자 URL, 대상 및 서명을 사용하여 IAM IdP를 생성합니다. 가장 많이 투표된
C. 필요한 S3 작업을 허용하는 정책이 있는 IAM 역할을 만듭니다. sts.amazon.com:aud 컨텍스트 키가 appid_from_idp인 경우 OIDC IP가 역할을 맡을 수 있도록 역할의 신뢰 정책을 구성합니다.
D. 필요한 S3 작업을 허용하는 정책이 있는 IAM 역할을 만듭니다. auth.company.com:aud 컨텍스트 키가 appid_from_idp인 경우 OIDC IP가 역할을 맡을 수 있도록 역할의 신뢰 정책을 구성합니다. 가장 많이 투표된
E. AssumeRoleWithWebIdentity API 작업을 사용하여 임시 자격 증명을 검색하도록 웹 애플리케이션을 구성합니다. 임시 자격 증명을 사용하여 S3 API 호출을 수행합니다. 가장 많이 투표된
F. GetFederationToken API 작업을 사용하여 임시 자격 증명을 검색하도록 웹 애플리케이션을 구성합니다. 임시 자격 증명을 사용하여 S3 API 호출을 수행합니다.



### 질문 #198주제 1
한 회사가 AWS 계정의 모든 데이터베이스에 Amazon RDS를 사용합니다. 이 회사는 AWS Control Tower를 사용하여 감사 및 로깅 계정이 있는 랜딩 존을 구축합니다. 모든 데이터베이스는 규정 준수를 위해 휴면 상태에서 암호화되어야 합니다. 이 회사의 보안 엔지니어는 회사 계정에 있는 모든 비준수 데이터베이스에 대한 알림을 받아야 합니다.

어떤 솔루션이 이러한 요구 사항을 가장 높은 운영 효율성으로 충족할까요?

A. AWS Control Tower를 사용하여 RDS 스토리지가 암호화되었는지 확인하기 위해 선택적 탐지 제어(가드레일)를 활성화합니다. 회사의 감사 계정에서 Amazon Simple Notification Service(Amazon SNS) 토픽을 만듭니다. AWS Control Tower 제어(가드레일)에서 비준수 이벤트를 필터링하여 SNS 토픽에 알리는 Amazon EventBridge 규칙을 만듭니다. 보안 엔지니어의 이메일 주소를 SNS 토픽에 구독합니다. 가장 많이 투표된
B. AWS CloudFormation StackSets를 사용하여 모든 계정에 AWS Lambda 함수를 배포합니다. Lambda 함수 코드를 작성하여 함수가 배포된 계정에서 RDS 스토리지가 암호화되었는지 확인합니다. 결과를 Amazon CloudWatch 메트릭으로 관리 계정에 보냅니다. Amazon Simple Notification Service(Amazon SNS) 토픽을 만듭니다. 메트릭 임계값에 도달하면 SNS 토픽에 알리는 CloudWatch 알람을 만듭니다. 보안 엔지니어의 이메일 주소를 SNS 토픽에 구독합니다.
C. 모든 계정에서 RDS 스토리지가 암호화되었는지 확인하기 위한 사용자 지정 AWS Config 규칙을 만듭니다. 감사 계정에서 Amazon Simple Notification Service(Amazon SNS) 토픽을 만듭니다. AWS Control Tower 제어(가드레일)에서 규정을 준수하지 않는 이벤트를 필터링하여 SNS 토픽에 알리는 Amazon EventBidge 규칙을 만듭니다. 보안 엔지니어의 이메일 주소를 SNS 토픽에 구독합니다.
D. Amazon C2 인스턴스를 시작합니다. AWS CLI를 사용하여 매시간 cron 작업을 실행하여 각 AWS 계정에서 RDS 스토리지가 암호화되었는지 확인합니다. 결과를 RDS 데이터베이스에 저장합니다. 비준수가 감지되면 EC2 인스턴스에서 이메일 메시지를 보내 보안 엔지니어에게 알립니다.



### 질문 #199주제 1
회사가 온프레미스 데이터 센터에서 AWS로 마이그레이션하고 있습니다. 이 회사는 현재 소프트웨어를 빌드하고 패키징하기 위해 맞춤형 온프레미스 Cl/CD 파이프라인 솔루션을 사용합니다. 이 회사

는 애플리케이션별 파이프라인을 쉽게 생성할 수 있도록 소프트웨어 패키지와 종속 퍼블릭 리포지토리를 AWS CodeArtifact에서 사용할 수 있기를 원합니다.

이 회사는 CI/CD 파이프라인 솔루션을 업데이트하고 최소한의 운영 오버헤드로 CodeArtifact를 구성하기 위해 어떤 단계 조합을 취해야 합니까? (두 가지를 선택하세요.)

A. C1ICD 파이프라인을 업데이트하여 새로 패키징된 소프트웨어가 포함된 VM 이미지를 만듭니다. AWS Import/Export를 사용하여 VM 이미지를 Amazon EC2 AMI로 제공합니다. CodeArtifact 작업을 허용하는 연결된 IAM 인스턴스 프로필로 AMI를 시작합니다. AWS CLI 명령을 사용하여 패키지를 CodeArtifact 리포지토리에 게시합니다.
B. AWS Identity and Access Management Roles Anywhere 신뢰 앵커를 만듭니다. CodeArtifact 작업을 허용하고 신뢰 앵커에 신뢰 관계가 있는 IAM 역할을 만듭니다. 온프레미스 CI/CD 파이프라인을 업데이트하여 새 IAM 역할을 맡고 패키지를 CodeArtifact에 게시합니다. 가장 많이 투표된
C. 새 Amazon S3 버킷을 만듭니다. PutObject 요청을 허용하는 미리 서명된 URL을 생성합니다. 미리 서명된 URL을 사용하여 온프레미스 위치에서 S3 버킷으로 패키지를 게시하도록 온프레미스 CI/CD 파이프라인을 업데이트합니다. put 명령을 통해 버킷에서 패키지가 생성될 때 실행되는 AWS Lambda 함수를 만듭니다. Lambda 함수를 구성하여 CodeArtifact에 패키지를 게시합니다.
D. 각 퍼블릭 리포지토리에 대해 외부 연결로 구성된 CodeArutact 리포지토리를 만듭니다. 종속 리포지토리를 업스트림 퍼블릭 리포지토리로 구성합니다. 가장 많이 투표된
E. 공개 저장소에 대한 외부 연결 세트로 구성된 Codeartitact 저장소를 만듭니다. 외부 연결을 저장소의 다운스트림으로 구성합니다.



### 질문 #200주제 1
DevOps 팀은 AWS CodePipeline, AWS CodeBuild, AWS CodeDeploy를 사용하여 애플리케이션을 배포합니다. 이 애플리케이션은 AWS Lambda 함수와 Amazon API Gateway를 사용하는 REST API입니다. 최근 배포에서 많은 고객에게 영향을 미치는 오류가 발생했습니다.

DevOps 팀은 오류가 감지되면 최신 안정적인 버전의 애플리케이션으로 돌아가는 솔루션이 필요합니다. 솔루션은 가능한 한 적은 고객에게 영향을 미쳐야 합니다.

어떤 솔루션이 가장 높은 운영 효율성으로 이러한 요구 사항을 충족할까요?

A. CodeDeploy에서 배포 구성을 LambdaAllAtOnce로 설정합니다. 배포 그룹에서 자동 롤백을 구성합니다. API Gateway에서 HTTP Bad Gateway 오류를 감지하는 Amazon CloudWatch 알람을 만듭니다. 알람 수가 알람 임계값에 도달하면 롤백하도록 배포 그룹을 구성합니다.
B. CodeDeploy에서 배포 구성을 LambdaCanary10Percent10Minutes로 설정합니다. 배포 그룹에서 자동 롤백을 구성합니다. API Gateway에서 HTTP Bad Gateway 오류를 감지하는 Amazon CloudWatch 알람을 만듭니다. 알람 수가 알람 임계값에 도달하면 롤백하도록 배포 그룹을 구성합니다. 가장 많이 투표된
C. CodeDeploy에서 배포 구성을 LambdaAllAtOnce로 설정합니다. 배포 그룹에서 수동 롤백을 구성합니다. 배포가 실패할 때마다 알림을 보내도록 Amazon Simple Notification Service(Amazon SNS) 토픽을 만듭니다. 현재 배포를 중지하고 가장 최근에 성공한 배포를 시작하는 새 Lambda 함수를 호출하도록 SNS 토픽을 구성합니다.
D. CodeDeploy에서 배포 구성을 LambdaCanary10Percent10Minutes로 설정합니다. 배포 그룹에서 수동 롤백을 구성합니다. API Gateway에서 HTTP Bad Gateway 오류를 모니터링하기 위해 Amazon CloudWatch 로그 그룹에 메트릭 필터를 만듭니다. 현재 배포를 중지하고 가장 최근에 성공한 배포를 시작하는 새 Lambda 함수를 호출하도록 메트릭 필터를 구성합니다.



### 질문 #201주제 1
한 회사가 최근 AWS에 웹 애플리케이션을 배포했습니다. 이 회사는 대규모 판매 이벤트를 준비하고 있으며 웹 애플리케이션이 수요에 맞게 확장될 수 있도록 해야 합니다.

애플리케이션의 프런트엔드 인프라에는 Amazon S3 버킷을 출처로 하는 Amazon CloudFront 배포가 포함됩니다. 백엔드 인프라에는 Amazon API Gateway API, 여러 AWS Lambda 함수, Amazon Aurora DB 클러스터가 포함됩니다.

이 회사의 DevOps 엔지니어는 부하 테스트를 수행하고 Lambda 함수가 최대 요청 수를 충족할 수 있음을 확인합니다. 그러나 DevOps 엔지니어는 요청이 처음 급증하는 동안 요청 지연을 알아차립니다. Lambda 함수에 대한 대부분의 요청은 데이터베이스에 대한 쿼리를 생성합니다. 호출 시간의 상당 부분은 데이터베이스 연결을 설정하는 데 사용됩니다.

어떤 단계 조합이 애플리케이션에 필요한 확장성을 제공할까요? (세 가지를 선택하세요.)

A. Lambda 함수에 대해 더 높은 예약된 동시성을 구성합니다.
B. Lambda 함수에 대해 더 높은 프로비저닝된 동시성을 구성합니다. 가장 많이 투표된
C. DB 클러스터를 Aurora 글로벌 데이터베이스로 변환합니다. 회사 고객의 위치에 따라 AWS 지역에 Aurora 복제본을 추가합니다. 가장 많이 투표된
D. Lambda 함수를 리팩토링합니다. 데이터베이스 연결을 초기화하는 코드 블록을 함수 핸들러로 이동합니다.
F. Amazon RDS Proxy를 사용하여 Aurora 데이터베이스에 대한 프록시를 만듭니다. Lambda 함수를 업데이트하여 데이터베이스 연결에 프록시 엔드포인트를 사용합니다. 가장 많이 투표된




### 질문 #202주제 1
한 회사가 여러 가용성 영역에 걸쳐 확장되는 웹 애플리케이션을 실행합니다. 이 회사는 라우팅에 Application Load Balancer(ALB), 애플리케이션에 AWS Fargate, 애플리케이션 데이터에 Amazon Aurora를 사용합니다. 이 회사는 AWS CloudFormation 템플릿을 사용하여 애플리케이션을 배포합니다. 이 회사는 모든 Docker 이미지를 동일한 AWS 계정과 AWS 리전의 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에 저장합니다.

DevOps 엔지니어는 다른 리전에 재해 복구(DR) 프로세스를 설정해야 합니다. 솔루션은 8시간의 RPO와 2시간의 RTO를 충족해야 합니다. 이 회사는 Dockerfile에서 Docker 이미지를 빌드하는 데 2시간 이상이 필요할 때가 있습니다.

어떤 솔루션이 RTO 및 RPO 요구 사항을 가장 비용 효율적으로 충족할까요?

A. CloudFormation 템플릿과 Dockerfile을 DR 지역의 Amazon S3 버킷에 복사합니다. AWS Backup을 사용하여 자동화된 Aurora 지역 간 시간별 스냅샷을 구성합니다. DR의 경우 가장 최근의 Docker 이미지를 빌드하고 Docker 이미지를 DR 지역의 ECR 저장소에 업로드합니다. 가장 최근의 Aurora 스냅샷과 ECR 저장소의 Docker 이미지가 있는 CloudFormation 템플릿을 사용하여 DR 지역에서 새 CloudFormation 스택을 시작합니다. 애플리케이션 DNS 레코드를 업데이트하여 새 ALB를 가리킵니다.
B. DR 지역의 Amazon S3 버킷에 CloudFormation 템플릿을 복사합니다. Aurora 자동 백업 지역 간 복제를 구성합니다. ECR 지역 간 복제를 구성합니다. DR의 경우 가장 최근의 Aurora 스냅샷과 로컬 ECR 저장소의 Docker 이미지가 있는 CloudFormation 템플릿을 사용하여 DR 지역에서 새 CloudFormation 스택을 시작합니다. 애플리케이션 DNS 레코드를 업데이트하여 새 ALB를 가리킵니다. 가장 많이 투표된
C. DR 지역의 Amazon S3 버킷에 CloudFormation 템플릿을 복사합니다. Amazon EventBridge를 사용하여 AWS Lambda 함수를 예약하여 Aurora 데이터베이스와 ECR 리포지토리의 가장 최근 Docker 이미지의 매시간 스냅샷을 찍습니다. 스냅샷과 Docker 이미지를 DR 지역으로 복사합니다. DR의 경우 로컬 ECR 리포지토리의 가장 최근 Aurora 스냅샷과 Docker 이미지가 있는 CloudFormation 템플릿을 사용하여 DR 지역에서 새 CloudFormation 스택을 시작합니다.
D. DR 지역의 Amazon S3 버킷에 CloudFormation 템플릿을 복사합니다. DR 지역에 두 번째 애플리케이션 CloudFormation 스택을 배포합니다. Aurora를 글로벌 데이터베이스로 재구성합니다. 현재 지역에서 새 애플리케이션 릴리스가 필요할 때 두 CloudFormation 스택을 모두 업데이트합니다. DR의 경우 애플리케이션 DNS 레코드를 업데이트하여 새 ALB를 가리킵니다.



### 질문 #203주제 1
회사의 애플리케이션은 Amazon EC2 인스턴스에서 실행됩니다. 애플리케이션은 로그인의 사용자 이름, 날짜, 시간 및 소스 IP 주소를 기록하는 로그 파일에 씁니다. 로그는 Amazon CloudWatch Logs의 로그 그룹에 게시됩니다.

회사는 전날 발생한 이벤트에 대한 근본 원인 분석을 수행하고 있습니다. 회사는 지난 7일 동안 특정 사용자의 로그인 수를 알아야 합니다.

어떤 솔루션이 이 정보를 제공할까요?

A. 로그 그룹에 CloudWatch Logs 메트릭 필터를 만듭니다. 사용자 이름과 일치하는 필터 패턴을 사용합니다. 지난 7일 동안 로그인 수를 합산한 CloudWatch 메트릭을 게시합니다.
B. 로그 그룹에서 CloudWatch Logs 구독을 만듭니다. 사용자 이름과 일치하는 필터 패턴을 사용합니다. 지난 7일 동안 로그인 수를 합산한 CloudWatch 메트릭을 게시합니다.
C. 지난 7일 동안 사용자 이름에 대한 로그인 수를 계산하기 위해 집계 함수를 사용하는 CloudWatch Logs Insights 쿼리를 만듭니다. 로그 그룹에 대해 쿼리를 실행합니다. 가장 많이 투표된
D. CloudWatch 대시보드를 만듭니다. 로그 그룹에서 직접 지난 7일 동안 사용자 이름에 대한 로그인 수를 계산하는 필터 패턴이 있는 숫자 위젯을 추가합니다.



### 질문 #204주제 1
회사에 AWS CodeDeploy 애플리케이션이 있습니다. 이 애플리케이션에는 애플리케이션 배포를 위한 인스턴스를 식별하기 위해 단일 태그 그룹을 사용하는 배포 그룹이 있습니다. 단일 태그 그룹 구성은 ApplicationA 배포를 위한 Environment=Production 및 Name=ApplicationA 태그가 있는 인스턴스를 식별합니다.

이 회사는 Department=Marketing, Environment=Production 및 Name=ApplicationB 태그가 있는 추가 Amazon EC2 인스턴스를 시작합니다. Application의 다음 CodeDeploy 배포에서 추가 인스턴스에는 ApplicationA가 설치되어 있습니다. DevOps 엔지니어는 기존 배포 그룹을 구성하여 ApplicationA가 추가 인스턴스에 설치되지 않도록 해야 합니다.

이러한 요구 사항을 충족하는 솔루션은 무엇입니까?

A. 현재 단일 태그 그룹을 변경하여 Environment=Production 태그만 포함합니다. Name=ApplicationA 태그만 포함하는 또 다른 단일 태그 그룹을 추가합니다. 가장 많이 투표된
B. 현재 단일 태그 그룹을 변경하여 Department=Marketing, Environment=production, Name=ApplicationA 태그를 포함시킵니다.
C. Department=Marketing 태그만 포함하는 또 다른 단일 태그 그룹을 추가합니다. Environment=Production 및 Name=ApplicationA 태그는 현재 단일 태그 그룹과 함께 유지합니다.
D. 현재 단일 태그 그룹을 변경하여 Environment=Production 태그만 포함합니다. Department=Marketing 태그만 포함하는 또 다른 단일 태그 그룹을 추가합니다.



### 질문 #205주제 1
한 회사가 Amazon S3 버킷에 원시 데이터를 저장하는 애플리케이션을 출시하고 있습니다. 보고서를 생성하려면 세 개의 애플리케이션이 데이터에 액세스해야 합니다. 애플리케이션이 데이터에 액세스하려면 각 애플리케이션에서 데이터를 다르게 편집해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 각 애플리케이션에 대해 S3 버킷을 만듭니다. 원시 데이터의 S3 버킷에서 각 애플리케이션의 S3 버킷으로 S3 동일 지역 복제(SRR)를 구성합니다. 각 애플리케이션이 자체 S3 버킷에서 데이터를 사용하도록 구성합니다.
B. Amazon Kinesis 데이터 스트림을 만듭니다. 원시 데이터의 S3 버킷에서 객체 생성 이벤트에 의해 호출되는 AWS Lambda 함수를 만듭니다. Lambda 함수를 프로그래밍하여 각 애플리케이션의 데이터를 편집합니다. Kinesis 데이터 스트림에 데이터를 게시합니다. 각 애플리케이션이 Kinesis 데이터 스트림의 데이터를 사용하도록 구성합니다.
C. 각 애플리케이션에 대해 원시 데이터의 S3 버킷을 대상으로 사용하는 S3 액세스 포인트를 만듭니다. 원시 데이터의 S3 버킷에서 객체 생성 이벤트에 의해 호출되는 AWS Lambda 함수를 만듭니다. 각 애플리케이션의 데이터를 수정하도록 Lambda 함수를 프로그래밍합니다. 각 애플리케이션의 S3 액세스 포인트에 데이터를 저장합니다. 각 애플리케이션이 자체 S3 액세스 포인트에서 데이터를 사용하도록 구성합니다.
D. 원시 데이터의 S3 버킷을 대상으로 사용하는 S3 액세스 포인트를 만듭니다. 각 애플리케이션에 대해 S3 액세스 포인트를 사용하는 S3 Object Lambda 액세스 포인트를 만듭니다. 각 S3 Object Lambda 액세스 포인트에 대해 AWS Lambda 함수를 구성하여 객체가 검색될 때 데이터를 삭제합니다. 각 애플리케이션이 자체 S3 Object Lambda 액세스 포인트에서 데이터를 사용하도록 구성합니다. 가장 많이 투표된




### 질문 #206주제 1
한 회사에서는 AWS Control Tower와 AWS CloudFormation을 사용하여 AWS 계정을 관리하고 AWS 리소스를 만듭니다. 이 회사는 CloudFormation 스택에서 S3 버킷을 만들 때 모든 Amazon S3 버킷을 AWS Key Management Service(AWS KMS)로 암호화하도록 요구합니다.

어떤 솔루션이 이 요구 사항을 충족할까요?

A. AWS Organizations를 사용합니다. 요청에 AWS KMS 키(SSE-KMS)를 사용한 서버 측 암호화를 요청하는 x-amz-server-side-encryption 헤더가 포함되지 않은 경우 s3:PutObject 권한을 거부하는 SCP를 연결합니다.
B. 다중 계정 환경에서 AWS Control Tower를 사용합니다. CloudFormation 후크를 사용하여 모든 OU에서 사전 예방적 AWS Control Tower 제어를 구성하고 활성화합니다. 가장 많이 투표된
C. 다중 계정 환경에서 AWS Control Tower를 사용합니다. CloudFormation 후크를 사용하여 모든 OU에서 탐지 AWS Control Tower 컨트롤을 구성하고 활성화합니다.
D. AWS Organizations를 사용합니다. AWS Config 조직 규칙을 만들어 모든 S3 버킷에 KMS 암호화 키가 활성화되어 있는지 확인합니다. 규칙을 배포합니다. SCP를 만들어 적용하여 사용자가 모든 AWS 계정에서 AWS Config를 중지하고 삭제하지 못하도록 합니다.



### 질문 #207주제 1
DevOps 엔지니어가 AWS Lambda 함수를 개발했습니다. Lambda 함수는 특정 CloudFormation 스택에 대해 지원되는 모든 리소스에서 AWS CloudFormation 드리프트 감지 작업을 시작합니다. 그런 다음 Lambda 함수는 호출을 종료합니다.

DevOps 엔지니어는 매시간 Lambda 함수를 호출하는 Amazon EventBridge 예약 규칙을 만들었습니다. AWS 계정에 Amazon Simple Notification Service(Amazon SNS) 토픽이 이미 있습니다. DevOps 엔지니어는 알림을 받기 위해 SNS 토픽을 구독했습니다.

DevOps 엔지니어는 이 특정 스택 구성에서 드리프트가 감지되면 가능한 한 빨리 알림을 받아야 합니다.

이러한 요구 사항을 충족하는 솔루션은 무엇입니까?

A. 기존 EventBridge 규칙을 구성하여 SNS 토픽도 대상으로 지정합니다. CloudFormation 스택과 일치하도록 SNS 구독 필터 정책을 구성합니다. 구독 필터 정책을 SNS 토픽에 연결합니다.
B. 스택의 드리프트 감지 결과에 대해 CloudFormation API를 쿼리하는 두 번째 Lambda 함수를 만듭니다. 드리프트가 감지되면 두 번째 Lambda 함수가 SNS 토픽에 메시지를 게시하도록 구성합니다. 기존 EventBridge 규칙을 조정하여 두 번째 Lambda 함수도 대상으로 지정합니다.
C. 모든 CloudFormation 스택에 대해 드리프트 감지가 있는 계정에서 Amazon GuardDuty를 구성합니다. 특정 CloudFormation 스택에 대한 GuardDuty 드리프트 감지 이벤트 발견에 반응하는 두 번째 EventBridge 규칙을 만듭니다. 두 번째 EventBridge 규칙의 대상으로 SNS 토픽을 구성합니다.
D. 계정에서 AWS Config를 구성합니다. cloudformation-stack-drift-detection-check 관리 규칙을 사용합니다. CloudFormation 스택에 대한 규정 준수 변경 이벤트에 대응하는 두 번째 EventBridge 규칙을 만듭니다. SNS 토픽을 두 번째 EventBridge 규칙의 대상으로 구성합니다. 가장 많이 투표된



### 질문 #208주제 1
한 회사가 AWS에 복잡한 컨테이너 기반 워크로드를 배포했습니다. 워크로드는 모니터링을 위해 Amazon Managed Service for Prometheus를 사용합니다. 워크로드는
AWS 계정의 Amazon Elastic Kubernetes Service(Amazon EKS) 클러스터에서 실행됩니다.

회사의 DevOps 팀은 회사의 Amazon Simple Notification Service(Amazon SNS) 토픽을 사용하여 워크로드 알림을 수신하려고 합니다. SNS 토픽은 EKS 클러스터와 동일한 AWS 계정에 있습니다.

이러한 요구 사항을 충족하는 단계 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. Amazon Managed Service for Prometheus 원격 쓰기 URL을 사용하여 SNS 주제에 알림을 보냅니다.
B. 각 워크로드 컨테이너의 가용성을 확인하는 알림 규칙을 만듭니다. 가장 많이 투표된
C. SNS 주제에 대한 알림 관리자 구성을 만듭니다. 가장 많이 투표된
D. SNS 토픽의 액세스 정책을 수정합니다. aps.amazonaws.com 서비스 주체에게 sns:Publish 권한과 SNS 토픽에 대한 sns:GetTopicAttributes 권한을 부여합니다. 가장 많이 투표된
E. Amazon Managed Service for Prometheus에서 사용하는 IAM 역할을 수정합니다. 역할에 sns:Publish 권한과 SNS 주제에 대한 sns:GetTopicAttributes 권한을 부여합니다.
F. EKS 클러스터에 대한 OpenID Connect(OIDC) 공급자를 만듭니다. 클러스터 서비스 계정을 만듭니다. IAM 역할을 사용하여 계정에 sns:Publish 권한과 sns:GetTopicAttributes 권한을 부여합니다.



### 질문 #209주제 1
AWS Organizations의 회사 조직에는 단일 OU가 있습니다. 회사는 OU 계정에서 Amazon EC2 인스턴스를 실행합니다. 회사는 각 EC2 인스턴스의 자격 증명 사용을 자격 증명이 할당된 특정 EC2 인스턴스로 제한해야 합니다. DevOps 엔지니어는 EC2 인스턴스에 대한 보안을 구성해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. VPC CIDR 블록을 지정하는 SCP를 만듭니다. SCP를 구성하여 aws:VpcSourcelp 조건 키의 값이 지정된 블록에 있는지 확인합니다. 동일한 SCP 확인에서 aws:EC2InstanceSourcePrivatelPv4 및 aws:SourceVpc 조건 키의 값이 같은지 확인합니다. 두 조건 중 하나가 거짓이면 액세스를 거부합니다. SCP를 OU에 적용합니다.
B. aws:EC2InstanceSourceVPC 및 aws:SourceVpc 조건 키의 값이 같은지 확인하는 SCP를 만듭니다. 값이 같지 않으면 액세스를 거부합니다. 동일한 SCP 확인에서 aws:EC2InstanceSourcePrivateIPv4 및 aws:VpcSourceIp 조건 키의 값이 같은지 확인합니다. 값이 같지 않으면 액세스를 거부합니다. SCP를 OU에 적용합니다. 가장 많이 투표된
C. 허용 가능한 VPC 값 목록을 포함하고 aws:SourceVpc 조건 키 값이 목록에 있는지 확인하는 SCP를 만듭니다. 동일한 SCP 확인에서 허용 가능한 IP 주소 값 목록을 정의하고 aws:VpcSourceIp 조건 키 값이 목록에 있는지 확인합니다. 두 조건 중 하나가 거짓이면 액세스를 거부합니다. 조직의 각 계정에 SCP를 적용합니다.
D. aws:EC2InstanceSourceVPC 및 aws:VpcSourceIp 조건 키의 값이 같은지 확인하는 SCP를 만듭니다. 값이 같지 않으면 액세스를 거부합니다. 동일한 SCP 확인에서 aws:EC2InstanceSourcePrivateIPv4 및 aws:SourceVpc 조건 키의 값이 같은지 확인합니다. 값이 같지 않으면 액세스를 거부합니다. 조직의 각 계정에 SCP를 적용합니다.



### 질문 #210주제 1
한 회사에는 단일 AWS 계정에서 Linux를 실행하는 Amazon EC2 인스턴스가 있습니다. 이 회사는 EC2 인스턴스에서 AWS Systems Manager Automation 작업을 사용하고 있습니다.

가장 최근의 패치 주기 동안 여러 EC2 인스턴스가 사용 가능한 디스크 공간이 부족하여 오류 상태가 되었습니다. DevOps 엔지니어는 향후 패치 프로세스 중에 EC2 인스턴스에 사용 가능한 디스크 공간이 충분한지 확인해야 합니다.

이러한 요구 사항을 충족하는 단계 조합은 무엇입니까? (두 가지를 선택하세요.)

A. 모든 EC2 인스턴스에 Amazon CloudWatch 에이전트가 설치되어 있는지 확인하세요. 가장 많이 투표된
B. 각 EC2 인스턴스에 설치되는 cron 작업을 생성하여 임시 파일을 주기적으로 삭제합니다.
C. EC2 인스턴스에 대한 Amazon CloudWatch 로그 그룹을 만듭니다. 각 EC2 인스턴스에 설치된 cron 작업을 구성하여 관련 EC2 인스턴스에 대한 CloudWatch 로그 스트림에 사용 가능한 디스크 공간을 씁니다.
D. 모든 EC2 인스턴스에서 사용 가능한 디스크 공간을 모니터링하기 위해 Amazon CloudWatch 알람을 만듭니다. 알람을 Systems Manager Automation 작업에 안전 제어로 추가합니다. 가장 많이 투표된
E. 각 EC2 인스턴스의 Amazon CloudWatch 로그 스트림을 평가하여 모든 EC2 인스턴스에 사용 가능한 디스크 공간이 충분한지 주기적으로 확인하는 AWS Lambda 함수를 생성합니다.



### 질문 #211주제 1
DevOps 엔지니어가 AWS Lambda 함수를 사용하여 Amazon Aurora MySQL DB 클러스터를 쿼리하는 애플리케이션을 빌드하고 있습니다. Lambda 함수는 읽기 쿼리만 수행합니다. Amazon EventBridge 이벤트는 Lambda 함수를 호출합니다.

매초 Lambda 함수를 호출하는 이벤트가 많아질수록 데이터베이스의 지연 시간이 증가하고 데이터베이스의 처리량이 감소합니다. DevOps 엔지니어는 애플리케이션의 성능을 개선해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. Amazon RDS Proxy를 사용하여 프록시를 만듭니다. 프록시를 Aurora 클러스터 리더 엔드포인트에 연결합니다. 프록시에서 최대 연결 백분율을 설정합니다. 가장 많이 투표된
B. Lambda 코드 내에서 데이터베이스 연결 풀링을 구현합니다. 데이터베이스 연결 풀에서 최대 연결 수를 설정합니다.
C. Lambda 이벤트 핸들러 코드 외부에서 데이터베이스 연결 열기를 구현합니다. 가장 많이 투표된
D. Lambda 이벤트 핸들러 코드 내에서 데이터베이스 연결 열기 및 닫기를 구현합니다.
E. Lambda 함수에서 프록시 엔드포인트에 연결합니다. 가장 많이 투표된
F. Lambda 함수에서 Aurora 클러스터 엔드포인트에 연결합니다.



### 질문 #212주제 1
한 회사에 단일 AWS 계정에 배포된 AWS CloudFormation 스택이 있습니다. 이 회사는 Amazon Simple Notification Service(Amazon SNS) 토픽에 이벤트 알림을 보내도록 스택을 구성했습니다.

DevOps 엔지니어는 스택 업데이트가 성공적으로 이루어진 후에만 특정 CloudFormation 스택 인스턴스에 태그를 적용하는 자동화된 솔루션을 구현해야 합니다. DevOps 엔지니어는 특정 스택 인스턴스에 이 태그를 적용하고 업데이트하는 AWS Lambda 함수를 만들었습니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Systems Manager가 CloudFormation 스택의 인스턴스 상태에 대해 UPDATE_COMPLETE 이벤트를 감지하면 AWS-UpdateCloudFormationStack AWS Systems ManagerAutomation 런북을 실행합니다. Lambda 함수를 호출하도록 런북을 구성합니다.
B. CloudFormation 스택에 UPDATE_COMPLETE 인스턴스 상태가 있는 경우 규정 준수 변경 이벤트를 생성하는 사용자 지정 AWS Config 규칙을 만듭니다. AWS Config를 구성하여 Lambda 함수를 직접 호출하여 변경 이벤트를 자동으로 수정합니다.
C. CloudFormation 스택의 인스턴스 상태에 대한 UPDATE_COMPLETE 이벤트 패턴과 일치하는 Amazon EventBridge 규칙을 만듭니다. Lambda 함수를 호출하도록 규칙을 구성합니다. 가장 많이 투표된
D. CloudFormation 스택의 구성을 조정하여 UPDATE_COMPLETE 인스턴스 상태 이벤트에 대한 알림만 SNS 토픽으로 보냅니다. Lambda 함수를 SNS 토픽에 구독합니다.




### 질문 #213주제 1
한 회사가 두 개의 AWS 리전에 애플리케이션을 배포합니다. 애플리케이션은 애플리케이션과 동일한 리전에 있는 Amazon S3 버킷에 객체를 생성하여 저장합니다. 두 애플리케이션 배포 모두 두 리전의 모든 객체와 해당 메타데이터에 액세스할 수 있어야 합니다. 회사는 S3 버킷 간에 양방향 복제를 구성하고 각 S3 버킷에서 S3 복제 메트릭을 활성화했습니다.

DevOps 엔지니어는 객체가 복제에 실패하면 복제 프로세스를 재시도하는 솔루션을 구현해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 실패한 복제 이벤트에 대한 S3 이벤트 알림을 수신하는 Amazon EventBridge 규칙을 만듭니다. 실패한 복제 객체를 다운로드한 다음 대상 버킷에 객체에 대한 PutObject 명령을 실행하는 AWS Lambda 함수를 만듭니다. 복제에 실패한 객체를 처리하기 위해 Lambda 함수를 호출하도록 EventBridge 규칙을 구성합니다.
B. Amazon Simple Queue Service(Amazon SQS) 대기열을 만듭니다. S3 이벤트 알림을 구성하여 실패한 복제 알림을 SQS 대기열로 보냅니다. 실패한 복제 객체를 다운로드한 다음 대상 버킷에 객체에 대한 PutObject 명령을 실행하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 구성하여 알림을 처리하기 위해 대기열을 폴링합니다.
C. 실패한 복제에 대한 S3 이벤트 알림을 수신하는 Amazon EventBridge 규칙을 만듭니다. 실패한 복제 객체를 다운로드한 다음 대상 버킷에 객체에 대한 PutObject 명령을 실행하는 AWS Lambda 함수를 만듭니다.
D. S3 배치 작업을 사용하여 실패한 복제에 대한 기존 객체에서 복제를 재시도하는 AWS Lambda 함수를 만듭니다. 실패한 복제 알림을 Lambda 함수로 보내도록 S3 이벤트 알림을 구성합니다. 가장 많이 투표된



### 질문 #214주제 1
회사에서 애플리케이션에 대한 장애 조치를 구현해야 합니다. 애플리케이션에는 Amazon CloudFront 배포판과 AWS 지역의 퍼블릭 애플리케이션 로드 밸런서(ALB)가 포함됩니다. 회사에서는 ALB를 배포판의 기본 오리진으로 구성했습니다.

최근 애플리케이션 중단 후 회사는 0초 RTO를 원합니다. 회사는 웜 스탠바이 구성에서 보조 지역에 애플리케이션을 배포합니다. DevOps 엔지니어는 HTTP GET 요청이 원하는 RTO를 충족하도록 보조 지역에 대한 애플리케이션 장애 조치를 자동화해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 보조 ALB를 기본 오리진으로 하는 두 번째 CloudFront 배포를 만듭니다. 장애 조치 정책이 있고 두 CloudFront 배포 모두에 대해 Evaluate Target Health가 Yes로 설정된 Amazon Route 53 별칭 레코드를 만듭니다. 새 레코드 세트를 사용하도록 애플리케이션을 업데이트합니다.
B. 2차 AL에 대한 배포에서 새 오리진을 만듭니다. 새 오리진 그룹을 만듭니다. 원래 ALB를 기본 오리진으로 설정합니다. HTTP 5xx 상태 코드에 대해 장애 조치를 취하도록 오리진 그룹을 구성합니다. 오리진 그룹을 사용하도록 기본 동작을 업데이트합니다. 가장 많이 투표된
C. 장애 조치 정책이 있고 두 ALB 모두에 대해 Evaluate Target Health가 Yes로 설정된 Amazon Route 53 별칭 레코드를 만듭니다. 두 레코드의 TTL을 0으로 설정합니다. 배포의 원점을 업데이트하여 새 레코드 세트를 사용합니다.
D. HTTP 5xx 상태 코드를 감지하는 CloudFront 함수를 만듭니다. 함수가 5xx 상태 코드를 감지하면 보조 ALB에 307 임시 리디렉션 오류 응답을 반환하도록 함수를 구성합니다. 배포의 기본 동작을 업데이트하여 함수에 원본 응답을 보냅니다.



### 질문 #215주제 1
클라우드 팀은 AWS Organizations와 AWS IAM Identity Center(AWS Single Sign-On)를 사용하여 회사의 AWS 계정을 관리합니다. 이 회사는 최근에 연구팀을 구성했습니다. 연구팀에는 계정의 리소스를 완전히 관리할 수 있는 기능이 필요합니다. 연구팀에서는 IAM 사용자를 만들 수 없어야 합니다.

클라우드 팀은 연구팀을 위해 IAM Identity Center에서 Research Administrator 권한 집합을 만듭니다. 권한 집합에는 AdministratorAccess AWS 관리 정책이 첨부되어 있습니다. 클라우드 팀은 연구팀의 아무도 IAM 사용자를 만들 수 없도록 해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. iam:CreateUser 작업을 거부하는 IAM 정책을 만듭니다. IAM 정책을 Research Administrator 권한 집합에 연결합니다.
B. iam:CreateUser 작업을 제외한 모든 작업을 허용하는 IAM 정책을 만듭니다. IAM 정책을 사용하여 Research Administrator 권한 집합에 대한 권한 경계를 설정합니다.
C. iam:CreateUser 액션을 거부하는 SCP를 만듭니다. SCP를 연구팀의 AWS 계정에 연결합니다. 가장 많이 투표된
D. IAM 사용자를 삭제하는 AWS Lambda 함수를 만듭니다. IAM CreateUser 이벤트를 감지하는 Amazon EventBridge 규칙을 만듭니다. Lambda 함수를 호출하도록 규칙을 구성합니다.



### 질문 #216주제 1
회사에서 새 AWS 계정에서 새 애플리케이션을 출시합니다. 이 애플리케이션에는 Amazon Simple Queue Service(Amazon SQS) 표준 대기열에서 메시지를 처리하는 AWS Lambda 함수가 포함되어 있습니다. Lambda 함수는 추가 다운스트림 처리를 위해 Amazon S3 버킷에 결과를 저장합니다. Lambda 함수는 메시지가 게시된 후 특정 기간 내에 메시지를 처리해야 합니다. Lambda 함수의 배치 크기는 10개 메시지이고 메시지 배치를 처리하는 데 몇 초가 걸립니다.

애플리케이션의 첫 서비스 날에 부하가 증가함에 따라 대기열의 메시지는 Lambda 함수가 메시지를 처리할 수 있는 것보다 더 빠른 속도로 누적됩니다. 일부 메시지는 필요한 처리 타임라인을 놓칩니다. 로그에 따르면 대기열의 많은 메시지에 유효하지 않은 데이터가 있습니다. 이 회사는 유효한 데이터가 있는 메시지에 대한 타임라인 요구 사항을 충족해야 합니다.

이러한 요구 사항을 충족하는 솔루션은 무엇입니까?

A. Lambda 함수의 배치 크기를 늘립니다. SQS 표준 큐를 SQS FIFO 큐로 변경합니다. AWS 리전에서 Lambda 동시성 증가를 요청합니다.
B. Lambda 함수의 배치 크기를 줄입니다. SQS 메시지 처리량 할당량을 늘립니다. AWS 지역에서 Lambda 동시성 증가를 요청합니다.
C. Lambda 함수의 배치 크기를 늘립니다. S3 버킷에서 S3 Transfer Acceleration을 구성합니다. SQS Dead-Letter 대기열을 구성합니다.
D. Lambda 함수의 배치 크기를 동일하게 유지합니다. 실패한 배치 항목을 보고하도록 Lambda 함수를 구성합니다. SQS 배달 못한 편지 대기열을 구성합니다. 가장 많이 투표된



### 질문 #217주제 1
한 회사에 AWS Lambda에서 실행되고 Amazon CloudWatch Logs에 로그를 보내는 애플리케이션이 있습니다. Amazon Kinesis 데이터 스트림은 CloudWatch Logs의 로그 그룹에 구독됩니다. 단일 소비자 Lambda 함수는 데이터 스트림의 로그를 처리하고 Amazon S3 버킷에 로그를 저장합니다.

이 회사의 DevOps 팀은 일부 로그의 처리 및 수집 중에 높은 지연 시간을 발견했습니다.

어떤 단계 조합이 지연 시간을 줄일 수 있을까요? (세 가지를 선택하세요.)

A. 향상된 팬아웃을 사용하여 데이터 스트림 소비자를 만듭니다. 로그를 처리하는 Lambda 함수를 소비자로 설정합니다. 가장 많이 투표된
B. Lambda 이벤트 소스 매핑에서 ParallelizationFactor 설정을 늘립니다. 가장 많이 투표된
C. 로그를 처리하는 Lambda 함수에 대해 예약된 동시성을 구성합니다.
D. Kinesis 데이터 스트림의 배치 크기를 늘립니다.
E. Lambda 이벤트 소스 매핑에서 ReportBatchItemFailures 설정을 끕니다.
F. Kinesis 데이터 스트림의 샤드 수를 늘립니다. 가장 많이 투표된



### 질문 #218주제 1
한 회사가 AWS Organizations의 회사 조직에 있는 AWS 계정에서 민감한 워크로드를 운영합니다. 이 회사는 IP 주소 범위를 사용하여 Amazon VPC CIDR 블록과 모든 비클라우드 하드웨어에 대한 IP 주소를 위임합니다.

이 회사는 회사의 IP 주소 범위 밖에 있는 주체가 조직의 계정에서 AWS 작업을 수행하지 못하도록 하는 솔루션이 필요합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 조직에 대한 AWS Firewall Manager를 구성합니다. 회사의 IP 주소 범위에서만 소스 트래픽을 허용하는 AWS Network Firewall 정책을 만듭니다. 정책 범위를 조직의 모든 계정으로 설정합니다.
B. 조직에서 회사의 IP 주소 범위를 벗어난 소스 IP 주소를 거부하는 SCP를 만듭니다. SCP를 조직의 루트에 연결합니다. 가장 많이 투표된
C. 조직에 Amazon GuardDuty를 구성합니다. 회사의 IP 범위에 대한 GuardDuty 신뢰할 수 있는 IP 주소 목록을 만듭니다. 조직에 대한 신뢰할 수 있는 IP 목록을 활성화합니다.
D. 조직에서 회사의 IP 주소 범위 내에 있는 소스 IP 주소를 허용하는 SCP를 만듭니다. SCP를 조직의 루트에 연결합니다.



### 질문 #219주제 1
한 회사가 두 개의 AWS 지역에 애플리케이션을 배포합니다. 이 애플리케이션은 현재 기본 지역의 Amazon S3 버킷을 사용하여 데이터를 저장합니다.

DevOps 엔지니어는 두 지역에서 모두 애플리케이션이 고가용성인지 확인해야 합니다. DevOps 엔지니어는 보조 지역에 새 S3 버킷을 만들었습니다. 모든 기존 및 새 객체는 두 S3 버킷에 있어야 합니다. 애플리케이션은 데이터 손실 없이 두 지역 간에 장애 조치되어야 합니다.

어떤 단계 조합이 이러한 요구 사항을 가장 높은 운영 효율성으로 충족할 수 있을까요? (세 가지를 선택하세요.)

A. Amazon S3 및 S3 배치 작업 서비스 주체가 S3 복제에 필요한 권한이 있는 역할을 맡을 수 있도록 새로운 IAM 역할을 생성합니다. 가장 많이 투표된
B. AWS Batch 서비스 주체가 S3 복제에 필요한 권한이 있는 역할을 맡을 수 있도록 새로운 IAM 역할을 생성합니다.
C. 소스 S3 버킷에서 S3 Cross-Region Replication(CRR) 규칙을 만듭니다. Amazon S3가 대상 S3 버킷에 복제하기 위해 IAM 역할을 사용하도록 규칙을 구성합니다.
D. 소스 S3 버킷에서 양방향 복제 규칙을 만듭니다. Amazon S3의 IAM 역할을 사용하여 대상 S3 버킷으로 복제하도록 규칙을 구성합니다. 가장 많이 투표된
E. AWS Fargate 오케스트레이션 유형이 있는 AWS Batch 작업을 만듭니다. AWS Batch에 대한 IAM 역할을 사용하도록 작업을 구성합니다. AWS CLI를 사용하여 소스 S3 버킷과 대상 S3 버킷의 내용을 동기화하는 Bash 명령을 지정합니다.
F. S3 Batch Operations에서 소스 S3 버킷의 내용을 대상 S3 버킷으로 복제하는 작업을 만듭니다. Amazon S3에 대한 IAM 역할을 사용하도록 작업을 구성합니다. 가장 많이 투표된



### 질문 #220주제 1
한 회사가 AWS Organizations에서 조직을 사용하여 여러 AWS 계정을 관리합니다. 이 회사는 인스턴스가 특정 태그를 받을 때 손상된 Amazon EC2 인스턴스를 격리하기 위해 모든 AWS 계정에서 자동화된 프로세스가 필요합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. AWS CloudFormation StackSets를 사용하여 모든 AWS 계정에 CloudFormation 스택을 배포합니다. 가장 많이 투표된
B. "aws:RequestTag/isolation": false 조건을 갖는 ec2:* 작업에 대한 Deny 문이 있는 SCP를 생성합니다.
C. SCP를 조직의 루트에 첨부합니다.
D. IAM 정책이 연결되지 않은 EC2 인스턴스 역할을 만드는 AWS CloudFormation 템플릿을 만듭니다. 모든 트래픽에 대한 명시적 거부 규칙이 있는 보안 그룹을 갖도록 템플릿을 구성합니다. CloudFormation 템플릿을 사용하여 인스턴스에 IAM 역할을 연결하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 구성하여 네트워크 ACL을 추가합니다. 특정 태그가 손상된 EC2 인스턴스에 적용될 때 Lambda 함수를 호출하도록 Amazon EventBridge 규칙을 설정합니다.
E. IAM 정책이 첨부되지 않은 EC2 인스턴스 역할을 만드는 AWS CloudFormation 템플릿을 만듭니다. 인바운드 규칙이나 아웃바운드 규칙이 없는 보안 그룹을 갖도록 템플릿을 구성합니다. CloudFormation 템플릿을 사용하여 인스턴스에 IAM 역할을 첨부하는 AWS Lambda 함수를 만듭니다. 기존 보안 그룹을 새 보안 그룹으로 바꾸도록 Lambda 함수를 구성합니다. 특정 태그가 손상된 EC2 인스턴스에 적용될 때 Lambda 함수를 호출하도록 Amazon EventBridge 규칙을 설정합니다. 가장 많이 투표된



### 질문 #221주제 1
한 회사는 다양한 사업부별로 OU가 있는 AWS Organizations를 사용하여 여러 AWS 계정을 관리합니다. 이 회사는 새로운 IP 주소 범위를 사용하도록 회사 네트워크를 업데이트하고 있습니다. 이 회사는 다양한 AWS 계정에 Amazon S3 버킷 10개를 가지고 있습니다. S3 버킷은 다양한 사업부에 대한 보고서를 저장합니다. S3 버킷 구성은 개인 회사 네트워크 IP 주소만 S3 버킷에 액세스할 수 있도록 허용합니다.

DevOps 엔지니어는 S3 버킷의 콘텐츠에 액세스할 수 있는 권한이 있는 IP 주소 범위를 변경해야 합니다. 또한 DevOps 엔지니어는 회사의 두 OU에 대한 권한을 취소해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 두 개의 문장이 있는 새 SCP를 만듭니다. 하나는 모든 S3 버킷에 대한 새로운 IP 주소 범위에 대한 액세스를 허용하고 다른 하나는 모든 S3 버킷에 대한 이전 IP 주소 범위에 대한 액세스를 거부합니다. 두 OU에서 OrganizationAccountAccessRole 역할에 대한 권한 경계를 설정하여 S3 버킷에 대한 액세스를 거부합니다.
B. S3 버킷에 액세스할 수 있는 새로운 IP 주소 범위만 허용하는 문장이 있는 새 SCP를 만듭니다. S3 버킷에 대한 액세스를 거부하는 또 다른 SCP를 만듭니다. 두 번째 SCP를 두 OU에 연결합니다.
C. 모든 S3 버킷에서 새 IP 주소 범위만 S3 버킷에 액세스할 수 있도록 리소스 기반 정책을 구성합니다. S3 버킷에 대한 액세스를 거부하는 새 SCP를 만듭니다. SCP를 두 OU에 연결합니다. 가장 많이 투표된
D. 모든 S3 버킷에서 새 IP 주소 범위만 S3 버킷에 액세스할 수 있도록 리소스 기반 정책을 구성합니다. 두 OU에서 OrganizationAccountAccessRole 역할에 대한 권한 경계를 설정하여 S3 버킷에 대한 액세스를 거부합니다.



### 질문 #222주제 1
한 회사가 여러 팀에서 AWS를 사용하기 시작했습니다. 각 팀에는 여러 계정과 고유한 보안 프로필이 있습니다. 이 회사는 AWS Organizations에서 조직의 계정을 관리합니다. 각 계정에는 고유한 구성과 보안 제어가 있습니다.

이 회사의 DevOps 팀은 예방 및 탐지 제어를 사용하여 모든 계정을 관리하려고 합니다. DevOps 팀은 회사가 조직에 새 계정을 만들 때 현재와 미래에 계정의 보안을 보장해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 조직을 사용하여 각 팀에 적합한 SCP가 첨부된 OU를 만듭니다. 보안 제어를 적용하려면 적절한 OU에 팀 계정을 배치합니다. 적절한 OU에 새 팀 계정을 만듭니다.
B. AWS Control Tower 랜딩 존을 만듭니다. 기존 팀에 대한 AWS Control Tower에서 OU와 적절한 컨트롤을 구성합니다. AWS Control Tower에 대한 신뢰할 수 있는 액세스를 구성합니다. 각 팀의 적절한 보안 정책과 일치하는 적절한 OU에 기존 계정을 등록합니다. AWS Control Tower를 사용하여 모든 새 계정을 프로비저닝합니다. 가장 많이 투표된
C. 조직의 관리 계정에서 AWS CloudFormation 스택 세트를 만듭니다. 조직의 각 계정에 대한 모든 컨트롤에 대한 구성 규칙 및 수정 조치와 함께 AWS Config를 배포하는 스택 세트를 구성합니다. 계정이 생성됨에 따라 스택 세트를 업데이트하여 새 계정에 배포합니다.
D. 조직의 모든 AWS 계정에서 AWS Config 규칙을 관리하도록 AWS Config를 구성합니다. 조직 전체에서 AWS Config 규칙과 수정 조치를 제공하는 적합성 팩을 배포합니다.



### 질문 #223주제 1
한 회사는 AWS CodeCommit 리포지토리를 사용하여 소스 코드와 해당 단위 테스트를 저장합니다. 이 회사는 리포지토리의 메인 브랜치에 코드가 병합될 때 실행되는 AWS CodeBuild 프로젝트를 포함하는 AWS CodePipeline 파이프라인을 구성했습니다.

이 회사는 CodeBuild 프로젝트에서 단위 테스트를 실행하기를 원합니다. 단위 테스트가 통과하면 CodeBuild 프로젝트는 가장 최근의 커밋에 태그를 지정해야 합니다.

이 회사는 이러한 요구 사항을 충족하기 위해 CodeBuild 프로젝트를 어떻게 구성해야 합니까?

A. CodeBuild 프로젝트를 구성하여 CodeCommit 리포지토리를 완료하기 위해 네이티브 Git을 사용합니다. 프로젝트를 구성하여 단위 테스트를 실행합니다. 프로젝트를 구성하여 네이티브 Git을 사용하여 태그를 만들고 코드가 단위 테스트를 통과하면 Git 태그를 리포지토리에 푸시합니다. 가장 많이 투표된
B. CodeBuild 프로젝트를 구성하여 CodeCommit 리포지토리를 완료하기 위해 네이티브 Git을 사용합니다. 프로젝트를 구성하여 단위 테스트를 실행합니다. 프로젝트를 구성하여 AWS CLI 명령을 사용하여 코드가 단위 테스트를 통과하면 리포지토리에 새 리포지토리 태그를 만듭니다.
C. CodeBuild 프로젝트를 구성하여 AWS CLI 명령을 사용하여 CodeCommit 리포지토리에서 코드를 복사합니다. 프로젝트를 구성하여 단위 테스트를 실행합니다. 코드가 단위 테스트를 통과하면 AWS CLI 명령을 사용하여 리포지토리에 새 Git 태그를 생성하도록 프로젝트를 구성합니다.
D. CodeBuild 프로젝트를 구성하여 AWS CLI 명령을 사용하여 CodeCommit 리포지토리에서 코드를 복사합니다. 프로젝트를 구성하여 단위 테스트를 실행합니다. 코드가 단위 테스트를 통과하면 AWS CLI 명령을 사용하여 리포지토리에 새 리포지토리 태그를 생성하도록 프로젝트를 구성합니다.



### 질문 #224주제 1
DevOps 엔지니어는 회사의 Amazon Elastic Container Service(Amazon ECS) 클러스터를 관리합니다. 클러스터는 Auto Scaling 그룹에 있는 여러 Amazon EC2 인스턴스에서 실행됩니다. DevOps 엔지니어는 중단된 모든 작업을 기록하고 오류를 검토하는 솔루션을 구현해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Amazon EventBridge 규칙을 만들어 작업 상태 변경을 캡처합니다. 이벤트를 Amazon CloudWatch Logs로 보냅니다. CloudWatch Logs Insights를 사용하여 중지된 작업을 조사합니다. 가장 많이 투표된
B. 임베디드 메트릭 형식으로 로그 데이터를 작성하도록 작업을 구성합니다. Amazon CloudWatch Logs에 로그를 저장합니다. ContainerInstanceCount 메트릭의 변경 사항을 모니터링합니다.
C. Amazon CloudWatch Logs에 로그를 저장하도록 EC2 인스턴스를 구성합니다. EC2 인스턴스 로그 데이터를 사용하는 CloudWatch Contributor Insights 규칙을 만듭니다. Contributor Insights 규칙을 사용하여 중지된 작업을 조사합니다.
D. EC2_INSTANCE_TERMINATING 스케일인 이벤트에 대한 EC2 자동 스케일링 라이프사이클 후크를 구성합니다. SystemEventLog 파일을 Amazon S3에 씁니다. Amazon Athena를 사용하여 로그 파일에서 오류를 쿼리합니다.


### 질문 #225주제 1
한 회사가 수백 개의 Amazon EC2 인스턴스에 워크로드를 배포하려고 합니다. 이 회사는 시작 템플릿을 사용하여 Auto Scaling 그룹에서 EC2 인스턴스를 프로비저닝합니다.

워크로드는 Amazon S3 버킷에서 파일을 가져오고, 데이터를 처리하고, 결과를 다른 S3 버킷에 넣습니다. EC2 인스턴스는 최소 권한 권한이 있어야 하며 임시 보안 자격 증명을 사용해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. S3 버킷에 대한 적절한 권한이 있는 IAM 역할을 생성합니다. 인스턴스 프로필에 IAM 역할을 추가합니다. 가장 많이 투표된
B. IAM 인스턴스 프로필을 포함하도록 시작 템플릿을 업데이트합니다. 가장 많이 투표된
C. Amazon S3에 대한 적절한 권한이 있는 IAM 사용자를 생성합니다. 비밀 키와 토큰을 생성합니다.
D. 신뢰 앵커와 프로필을 만듭니다. 프로필에 IAM 역할을 연결합니다.
E. 출시 템플릿을 업데이트합니다. 새로운 비밀 키와 토큰을 사용하도록 사용자 데이터를 수정합니다.



### 질문 #226주제 1
한 회사에서 AWS CodeDeploy를 사용하여 소프트웨어 배포를 자동화하고 있습니다. 배포는 다음 요구 사항을 충족해야 합니다.

• 배포 중에 트래픽을 처리할 수 있는 여러 인스턴스가 있어야 합니다. 트래픽은 해당 인스턴스 간에 균형을 이루어야 하며, 장애 발생 시 인스턴스가 자동으로 복구되어야 합니다. • 수동 프로비저닝 없이 새 개정판을 자동으로 배포하기 위해 새 인스턴스 플릿을 시작해야 합니다.
• 트래픽은 한 번에 새 인스턴스의 절반으로 새 환경으로 다시 라우팅해야 합니다. 트래픽이 인스턴스의 절반 이상으로 다시 라우팅되면 배포가 성공해야 합니다. 그렇지 않으면 실패해야 합니다.
• 새 인스턴스 플릿으로 트래픽을 라우팅하기 전에 배포 프로세스 중에 생성된 임시 파일을 삭제해야 합니다.
• 배포가 성공적으로 끝나면 비용을 줄이기 위해 배포 그룹의 원래 인스턴스를 즉시 삭제해야 합니다.

DevOps 엔지니어는 이러한 요구 사항을 어떻게 충족할 수 있습니까?

A. Application Load Balancer와 인플레이스 배포를 사용합니다. 배포 그룹과 자동 확장 그룹을 연결합니다. 자동 확장 그룹 자동 복사 옵션을 사용하고 배포 구성으로 CodeDeployDefault.OneAtAtime을 사용합니다. AWS CodeDeploy에 배포 그룹의 원래 인스턴스를 종료하도록 지시하고 appspec.yml 내의 AllowTraffic 후크를 사용하여 임시 파일을 삭제합니다.
B. 애플리케이션 로드 밸런서와 블루/그린 배포를 사용합니다. 배포 그룹과 자동 확장 그룹 및 애플리케이션 로드 밸런서 대상 그룹을 연결합니다. 자동 확장 그룹 자동 복사 옵션을 사용하고, 최소 정상 호스트를 50%로 정의하여 사용자 지정 배포 구성을 만들고, 배포 그룹에 구성을 할당합니다. AWS CodeDeploy에 배포 그룹의 원래 인스턴스를 종료하도록 지시하고, appspec.yml 내의 BeforeBlockTraffic 후크를 사용하여 임시 파일을 삭제합니다.
C. Application Load Balancer와 blue/green 배포를 사용합니다. 배포 그룹과 Auto Scaling 그룹 및 Application Load Balancer 대상 그룹을 연결합니다. Automatically copy Auto Scaling group 옵션을 사용하고 CodeDeployDefault.HalfAtAtime을 배포 구성으로 사용합니다. AWS CodeDeploy에 배포 그룹의 원래 인스턴스를 종료하도록 지시하고 appspec.yml 내의 BeforeAllowTraffic 후크를 사용하여 임시 파일을 삭제합니다. 가장 많이 투표된
D. Application Load Balancer와 인플레이스 배포를 사용합니다. 배포 그룹과 Auto Scaling 그룹 및 Application Load Balancer 대상 그룹을 연결합니다. Automatically copy Auto Scaling group 옵션을 사용하고 CodeDeployDefault.AllatOnce를 배포 구성으로 사용합니다. AWS CodeDeploy에 배포 그룹의 원래 인스턴스를 종료하도록 지시하고 appspec.yml 내의 BlockTraffic 후크를 사용하여 임시 파일을 삭제합니다.



### 질문 #227주제 1
회사에서는 애플리케이션과 관련 CI/CD 인프라를 배포하기 위해 다중 계정 전략을 채택해야 합니다. 이 회사는 모든 기능이 활성화된 AWS Organizations에서 조직을 만들었습니다. 이 회사는 AWS Control Tower를 구성하고 랜딩 존을 설정했습니다.

이 회사는 조직의 모든 AWS 계정에서 AWS Control Tower 컨트롤(가드레일)을 사용해야 합니다. 이 회사는 다중 환경 애플리케이션에 대한 계정을 만들어야 하며 모든 계정이 초기 기준선에 맞게 구성되었는지 확인해야 합니다.

어떤 솔루션이 최소한의 운영 오버헤드로 이러한 요구 사항을 충족할까요?

A. 기준 구성을 사용하는 AWS Control Tower Account Factory Customization(AFC) 블루프린트를 만듭니다. AWS Control Tower Account Factory를 사용하여 블루프린트를 사용하여 각 환경에 대한 전용 AWS 계정과 CI/CD 계정을 프로비저닝합니다. 가장 많이 투표된
B. AWS Control Tower Account Factory를 사용하여 각 환경에 대한 전용 AWS 계정과 CI/CD 계정을 프로비저닝합니다. AWS CloudFormation StackSets를 사용하여 기준 구성을 새 계정에 적용합니다.
C. Organizations를 사용하여 다중 환경 AWS 계정과 CI/CD 계정을 프로비저닝합니다. Organizations 관리 계정에서 Organizations 액세스 역할을 가정하여 새 계정에 기준 구성을 적용하는 AWS Lambda 함수를 만듭니다.
D. Organizations를 사용하여 각 환경에 대한 전담 AWS 계정, 감사 계정 및 CI/CD 계정을 프로비저닝합니다. AWS CloudFormation StackSets를 사용하여 기준 구성을 새 계정에 적용합니다.



### 질문 #228주제 1
DevOps 팀이 AWS Config에서 사용자 지정 Lambda 규칙을 만들었습니다. 이 규칙은 ecr:* 작업에 대한 Amazon Elastic Container Repository(Amazon ECR) 정책 문을 모니터링합니다. 규정을 준수하지 않는 리포지토리가 감지되면 Amazon EventBridge는 Amazon Simple Notification Service(Amazon SNS)를 사용하여 알림을 보안 팀으로 라우팅합니다.

사용자 지정 AWS Config 규칙이 평가되면 AWS Lambda 함수가 실행되지 않습니다.

어떤 솔루션으로 문제를 해결할 수 있을까요?

A. Lambda 함수의 리소스 정책을 수정하여 AWS Config가 해당 함수를 호출할 수 있는 권한을 부여합니다. 가장 많이 투표된
B. EventBridge가 SNS 주제에 게시할 수 있도록 구성 변경 사항을 포함하도록 SNS 주제 정책을 수정합니다.
C. 사용자 지정 AWS Config 규칙에 대한 구성 변경 사항을 포함하도록 Lambda 함수의 실행 역할을 수정합니다.
D. 모든 ECR 저장소 정책을 수정하여 AWS Config에 필요한 ECR API 작업에 대한 액세스 권한을 부여합니다.



### 질문 #229주제 1
개발자가 새로운 SaaS(Software as a Service) 애플리케이션에 대한 개념 증명을 만들고 있습니다. 애플리케이션은 AWS Organizations의 조직에 속하는 공유 개발 AWS 계정에 있습니다.

개발자는 개념 증명을 위해 고려 중인 AWS 서비스에 대한 서비스 연결 IAM 역할을 만들어야 합니다. 솔루션은 개발자에게 서비스 연결 역할만 만들고 구성할 수 있는 기능을 제공해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 조직의 관리 계정에서 개발자를 위한 IAM 사용자를 만듭니다. 개발자가 사용할 수 있도록 개발 계정에서 교차 계정 역할을 구성합니다. 교차 계정 역할의 범위를 공통 서비스로 제한합니다.
B. 개발자를 IAM 그룹에 추가합니다. PowerUserAccess 관리 정책을 IAM 그룹에 연결합니다. 사용자 계정에 다중 요소 인증(MFA)을 적용합니다.
C. Organizations에서 개발 계정에 SCP를 추가합니다. 개발자의 액세스를 제한하기 위해 iam:*에 대한 Deny 규칙으로 SCP를 구성합니다.
D. 개발자가 정책과 역할을 만들 수 있도록 필요한 IAM 액세스 권한이 있는 IAM 역할을 만듭니다. 역할에 권한 경계를 만들고 연결합니다. 개발자에게 역할을 맡을 수 있는 액세스 권한을 부여합니다. 가장 많이 투표된



### 문 #230주제 1
한 회사가 AWS Organizations를 사용하여 AWS 계정을 관리합니다. 이 회사는 루트 사용자가 로그인할 때 모니터링 시스템에 알림을 받고 싶어합니다. 또한 이 회사는 루트 사용자가 생성하는 모든 로그 활동을 표시하는 대시보드가 ​​필요합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. 다중 계정 애그리게이터로 AWS Config를 활성화합니다. Amazon CloudWatch Logs로 로그 전달을 구성합니다.
B. Amazon CloudWatch Logs 쿼리를 사용하는 Amazon QuickSight 대시보드를 만듭니다.
C. 루트 사용자 로그인 이벤트와 일치하도록 Amazon CloudWatch Logs 메트릭 필터를 만듭니다. CloudWatch 알람과 Amazon Simple Notification Service(Amazon SNS) 토픽을 구성하여 회사 모니터링 시스템에 알림을 보냅니다. 가장 많이 투표된
D. 루트 사용자 로그인 이벤트와 일치하도록 Amazon CloudWatch Logs 구독 필터를 만듭니다. 이벤트를 Amazon Simple Notification Service(Amazon SNS) 토픽으로 전달하도록 필터를 구성합니다. 회사의 모니터링 시스템에 알림을 보내도록 SNS 토픽을 구성합니다.
E. AWS CloudTrail 조직 트레일을 만듭니다. 조직 트레일을 구성하여 Amazon CloudWatch Logs로 이벤트를 보냅니다. 가장 많이 투표된
F. CloudWatch Logs Insights 쿼리를 사용하는 Amazon CloudWatch 대시보드를 만듭니다. 가장 많이 투표된



### 질문 #231주제 1
한 회사가 AWS Organizations를 사용하여 AWS 계정을 관리합니다. DevOps 엔지니어는 AWS Management Console에 액세스하는 모든 사용자가 회사의 기업 ID 공급자(IdP)를 통해 인증되었는지 확인해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하세요.)

A. 위임된 관리자 계정으로 Amazon GuardDuty를 사용합니다. GuardDuty를 사용하여 IAM 사용자 로그인 거부를 시행합니다.
B. AWS IAM Identity Center를 사용하여 SAML 2.0으로 ID 페더레이션을 구성합니다. 가장 많이 투표된
C. AWS IAM Identity Center에서 권한 경계를 생성하여 IAM 사용자의 비밀번호 로그인을 거부합니다.
D. 조직 관리 계정에서 IAM 그룹을 생성하여 모든 IAM 사용자에게 일관된 권한을 적용합니다.
E. 조직에서 SCP를 생성하여 IAM 사용자의 비밀번호 생성을 거부합니다. 가장 많이 투표된



### 질문 #232주제 1
한 회사가 Amazon Elastic Kubernetes Service(Amazon EKS)에서 실행되는 새로운 플랫폼을 배포했습니다. 새로운 플랫폼은 사용자가 자주 업데이트하는 웹 애플리케이션을 호스팅합니다. 애플리케이션 개발자는 애플리케이션의 Docker 이미지를 빌드하고 Docker 이미지를 플랫폼에 수동으로 배포합니다.

플랫폼 사용량은 매일 500명 이상의 사용자로 증가했습니다. 빈번한 업데이트, 애플리케이션의 업데이트된 Docker 이미지 빌드, Docker 이미지를 플랫폼에 수동으로 배포하는 것은 모두 관리하기 어려워졌습니다.

Docker 이미지 검사에서 운영 체제 또는 프로그래밍 언어 패키지 취약성에 대한 HIGH 또는 CRITICAL 결과가 반환되면 회사는 Amazon Simple Notification Service(Amazon SNS) 알림을 받아야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. Dockerfile 및 Kubernetes 배포 파일을 저장할 AWS CodeCommit 리포지토리를 만듭니다. AWS CodePipeline에서 파이프라인을 만듭니다. Amazon S3 이벤트를 사용하여 Dockerfile의 새 버전이 커밋될 때 파이프라인을 호출합니다. 파이프라인에 단계를 추가하여 AWS CodeBuild 프로젝트를 시작합니다.
B. Dockerfile 및 Kubernetes 배포 파일을 저장할 AWS CodeCommit 리포지토리를 만듭니다. AWS CodePipeline에서 파이프라인을 만듭니다. Amazon EventBridge 이벤트를 사용하여 Dockerfile의 새 버전이 커밋될 때 파이프라인을 호출합니다. 파이프라인에 단계를 추가하여 AWS CodeBuild 프로젝트를 시작합니다. 가장 많이 투표된
C. Docker 이미지를 빌드하고 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에 Docker 이미지를 저장하는 AWS CodeBuild 프로젝트를 만듭니다. ECR 리포지토리에 대한 기본 스캐닝을 켭니다. Amazon GuardDuty 이벤트를 모니터링하는 Amazon EventBridge 규칙을 만듭니다. finding-severity-counts 매개변수가 CRITICAL 또는 HIGH 수준에서 0보다 클 때 SNS 토픽에 이벤트를 보내도록 EventBridge 규칙을 구성합니다.
D. Docker 이미지를 빌드하고 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에 Docker 이미지를 저장하는 AWS CodeBuild 프로젝트를 만듭니다. ECR 리포지토리에 대한 향상된 스캐닝을 켭니다. ECR 이미지 스캔 이벤트를 모니터링하는 Amazon EventBridge 규칙을 만듭니다. finding-severity-counts 매개변수가 CRITICAL 또는 HIGH 수준에서 0보다 클 때 SNS 토픽에 이벤트를 보내도록 EventBridge 규칙을 구성합니다. 가장 많이 투표된
E. Dockerfile을 스캔하는 AWS CodeBuild 프로젝트를 만듭니다. 스캔이 성공하면 Docker 이미지를 빌드하고 Amazon Elastic Container Registry(Amazon ECR) 저장소에 Docker 이미지를 저장하도록 프로젝트를 구성합니다. 스캔에서 취약점이 반환되면 알림을 제공하도록 SNS 토픽을 구성합니다.



### 질문 #233주제 1
한 회사가 AWS Organizations의 조직에 있는 OU에서 AWS 계정을 그룹화합니다. 이 회사는 Organizations 계정 중 하나에 Amazon API Gateway API 세트를 배포했습니다. API는 계정의 VPC에 바인딩되어 있으며 기존 인증 메커니즘이 없습니다. 특정 OU의 주체만 API를 호출할 수 있는 권한을 가질 수 있습니다.

이 회사는 다음 정책을 API Gateway 인터페이스 VPC 엔드포인트에 적용합니다.



또한 이 회사는 인터페이스 VPC 엔드포인트를 통해 들어오지 않는 호출을 거부하도록 API Gateway 리소스 정책을 업데이트합니다. 업데이트 후 인터페이스 VPC 엔드포인트 URL을 사용하여 API를 호출하려고 시도하는 동안 다음 오류 메시지가 나타납니다. "사용자: 익명은 권한이 없습니다."

이 문제를 해결하는 단계 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. AWS JAM을 인증 방법으로 설정하여 모든 API 메서드에서 IAM 인증을 활성화합니다. 가장 많이 투표된
B. 호출자의 ID를 전달자 토큰으로 전달하는 토큰 기반 AWS Lambda 권한 부여자를 생성합니다.
C. 헤더, 쿼리 문자열 매개변수, 단계 변수 및 $cortext 변수를 조합하여 호출자의 ID를 전달하는 요청 매개변수 기반 AWS Lambda 권한 부여자를 만듭니다.
D. Amazon Cognito 사용자 풀을 승인자로 사용하여 API에 대한 액세스를 제어합니다.
E. AWS 자격 증명을 사용하여 클라이언트 요청에 서명하고 Signature Version 4를 사용하여 요청자의 신원을 확인합니다. 가장 많이 투표된



### 질문 #234주제 1
어떤 회사는 새로운 기능을 개발하는 데 걸리는 시간을 줄이고 싶어합니다. 이 회사는 AWS CodeBuild와 AWS CodeDeploy를 사용하여 애플리케이션을 빌드하고 배포합니다. 이 회사는 AWS CodePipeline을 사용하여 각 마이크로서비스를 자체 CI/CD 파이프라인으로 배포합니다.

이 회사는 새로운 기능의 릴리스와 실패한 배포 후 복구하는 데 걸리는 평균 시간 사이의 평균 시간에 대한 가시성이 더 필요합니다.

어떤 솔루션이 가장 적은 구성 노력으로 이러한 가시성을 제공할까요?

A. 각 파이프라인에 대한 성공한 실행과 실패한 실행에 대한 정보를 사용하여 Amazon CloudWatch 사용자 지정 메트릭을 생성하는 AWS Lambda 함수를 프로그래밍합니다. 5분마다 Lambda 함수를 호출하는 Amazon EventBridge 규칙을 만듭니다. 메트릭을 사용하여 CloudWatch 대시보드를 빌드합니다.
B. 각 파이프라인에 대한 성공한 실행과 실패한 실행에 대한 정보를 사용하여 Amazon CloudWatch 사용자 지정 메트릭을 생성하는 AWS Lambda 함수를 프로그래밍합니다. 모든 성공한 실행과 모든 실패한 실행 후에 Lambda 함수를 호출하는 Amazon EventBridge 규칙을 만듭니다. 메트릭을 사용하여 CloudWatch 대시보드를 빌드합니다. 가장 많이 투표된
C. Amazon DynamoDB에 성공한 실행과 실패한 실행에 대한 정보를 쓰는 AWS Lambda 함수를 프로그래밍합니다. 모든 성공한 실행과 모든 실패한 실행 후에 Lambda 함수를 호출하는 Amazon EventBridge 규칙을 만듭니다. DynamoDB의 정보를 표시하는 Amazon QuickSight 대시보드를 빌드합니다.
D. Amazon DynamoDB에 성공한 실행과 실패한 실행에 대한 정보를 쓰는 AWS Lambda 함수를 프로그래밍합니다. 5분마다 Lambda 함수를 호출하는 Amazon EventBridge 규칙을 만듭니다. DynamoDB의 정보를 표시하는 Amazon QuickSight 대시보드를 빌드합니다.



### 질문 #235주제 1
한 회사가 Amazon S3 버킷에 호스팅된 정적 웹사이트를 개발했습니다. 이 웹사이트는 AWS CloudFormation을 사용하여 배포됩니다. CloudFormation 템플릿은 S3 버킷과 소스 위치에서 버킷으로 콘텐츠를 복사하는 사용자 지정 리소스를 정의합니다.

이 회사는 웹사이트를 새 위치로 옮겨야 한다고 결정했으므로 기존 CloudFormation 스택을 삭제하고 다시 만들어야 합니다. 그러나 CloudFormation은 스택을 깨끗하게 삭제할 수 없다고 보고합니다.

가장 가능성 있는 원인은 무엇이며 DevOps 엔지니어는 이 버전과 향후 버전의 웹사이트에서 이 문제를 어떻게 완화할 수 있습니까?

A. S3 버킷에 활성 웹사이트 구성이 있기 때문에 삭제가 실패했습니다. CloudFormation 템플릿을 수정하여 S3 버킷 리소스에서 WebsiteConfiguration 속성을 제거합니다.
B. S3 버킷이 비어 있지 않아 삭제가 실패했습니다. RequestType이 Delete일 때 버킷을 재귀적으로 비우도록 사용자 지정 리소스의 AWS Lambda 함수 코드를 수정합니다. 가장 많이 투표된
C. 사용자 지정 리소스가 삭제 정책을 정의하지 않았기 때문에 삭제가 실패했습니다. RemoveOnDeletion 값을 사용하여 사용자 지정 리소스 정의에 DeletionPolicy 속성을 추가합니다.
D. S3 버킷이 비어 있지 않아 삭제가 실패했습니다. CloudFormation 템플릿에서 S3 버킷 리소스를 수정하여 Empty 값을 갖는 DeletionPolicy 속성을 추가합니다.



### 질문 #236주제 1
한 회사가 Amazon EC2를 기본 컴퓨팅 플랫폼으로 사용합니다. DevOps 팀은 회사의 EC2 인스턴스를 감사하여 EC2 인스턴스에 금지된 애플리케이션이 설치되었는지 확인하려고 합니다.

어떤 솔루션이 가장 높은 운영 효율성으로 이러한 요구 사항을 충족할까요?

A. 각 인스턴스에서 AWS Systems Manager를 구성합니다. AWS Systems Manager Inventory를 사용합니다. Systems Manager 리소스 데이터 동기화를 사용하여 Amazon S3 버킷에서 결과를 동기화하고 저장합니다. S3 버킷에 새 객체가 추가될 때 실행되는 AWS Lambda 함수를 만듭니다. 금지된 애플리케이션을 식별하도록 Lambda 함수를 구성합니다.
B. 각 인스턴스에서 AWS Systems Manager를 구성합니다. Systems Manager Inventory를 사용합니다. Systems Manager Inventory에서 변경 사항을 모니터링하여 금지된 애플리케이션을 식별하는 AWS Config 규칙을 만듭니다. 가장 많이 투표된
C. 각 인스턴스에서 AWS Systems Manager를 구성합니다. Systems Manager Inventory를 사용합니다. Systems Manager Inventory 이벤트에 대한 AWS CloudTrail의 트레일을 필터링하여 금지된 애플리케이션을 식별합니다.
D. 모든 애플리케이션 인스턴스의 로그 대상으로 Amazon CloudWatch Logs를 지정합니다. 모든 인스턴스에서 자동화된 스크립트를 실행하여 설치된 애플리케이션의 인벤토리를 만듭니다. 스크립트를 구성하여 결과를 CloudWatch Logs로 전달합니다. 필터 패턴을 사용하여 로그 데이터를 검색하여 금지된 애플리케이션을 식별하는 CloudWatch 알람을 만듭니다.



### 질문 #237주제 1
회사에 이벤트 기반 JavaScript 애플리케이션이 있습니다. 이 애플리케이션은 이벤트를 게시, 소비, 라우팅하는 분리된 AWS 관리 서비스를 사용합니다. 애플리케이션 테스트 중에 이벤트는 Amazon EventBridge 규칙에서 지정한 대상에 전달되지 않습니다.

DevOps 팀은 애플리케이션 테스터에게 애플리케이션을 다시 배포하지 않고도 이벤트를 보고, 문제를 해결하고, 손실을 방지할 수 있는 추가 기능을 제공해야 합니다. DevOps 팀

은 이러한 요구 사항을 충족하기 위해 어떤 단계 조합을 취해야 합니까? (세 가지를 선택하세요.)

A. 표준 테스트 환경과 프로젝트로 AWS Device Farm을 실행하여 애플리케이션의 특정 빌드를 실행합니다.
B. Amazon S3 버킷을 만듭니다. AWS CloudTrail을 활성화합니다. S3 버킷을 저장 위치로 지정하는 CloudTrail 트레일을 만듭니다. 가장 많이 투표된
C. Amazon Simple Queue Service(Amazon SQS) 표준 대기열을 배달 못한 편지 대기열로 사용하도록 EventBridge 규칙을 구성합니다. 가장 많이 투표된
D. Amazon Simple Queue Service(Amazon SQS) FIFO 대기열을 배달 못한 편지 대기열로 사용하도록 EventBridge 규칙을 구성합니다.
E. Amazon CloudWatch Logs에서 로그 그룹을 만듭니다. 로그 그룹을 EventBridge 규칙의 추가 대상으로 지정합니다. 가장 많이 투표된
F. AWS X-Ray SDK 추적 기능을 사용하여 X-Amzn-Trace-Id 헤더를 지원하는 코드를 구현하기 위해 애플리케이션 코드 베이스를 업데이트합니다.


### 질문 #238주제 1
한 회사가 컨테이너 기반 워크로드를 AWS Organizations 다중 계정 환경으로 마이그레이션하고 있습니다. 이 환경은 회사에서 컨테이너화된 워크로드를 배포하고 실행하는 데 사용하는 애플리케이션 워크로드 계정으로 구성되어 있습니다. 이 회사는 또한 조직의 공유 워크로드에 대한 공유 서비스 계정을 프로비저닝했습니다.

이 회사는 엄격한 규정을 따라야 합니다. 모든 컨테이너 이미지는 모든 환경에 배포되기 전에 보안 검사를 받아야 합니다. 이미지는 심각한 취약점 없이 검사를 통과한 후 다운스트림 배포 메커니즘에서 사용할 수 있습니다. 사전 검사 및 사후 검사 이미지는 배포에서 사전 검사 이미지를 사용할 수 없도록 서로 분리해야 합니다.

DevOps 엔지니어는 이 프로세스를 중앙 집중화하기 위한 전략을 만들어야 합니다.

어떤 단계 조합이 이러한 요구 사항을 최소한의 관리 오버헤드로 충족할 수 있을까요? (두 가지를 선택하세요.)

A. 공유 서비스 계정에서 Amazon Elastic Container Registry(Amazon ECR) 저장소를 만듭니다. 사전 검사 이미지마다 저장소 하나, 사후 검사 이미지마다 저장소 하나. 사전 검사 저장소에 새 이미지가 푸시될 때 실행되도록 Amazon ECR 이미지 스캐닝을 구성합니다. 리소스 기반 정책을 사용하여 조직에 사전 검사 저장소에 대한 쓰기 액세스 권한과 사후 검사 저장소에 대한 읽기 액세스 권한을 부여합니다. 가장 많이 투표된
B. 컨테이너 이미지를 게시하는 각 계정에서 사전 검사 Amazon Elastic Container Registry(Amazon ECR) 저장소를 만듭니다. 공유 서비스 계정에서 사후 검사 이미지에 대한 저장소를 만듭니다. 사전 검사 저장소에 대한 새 이미지 푸시에서 실행되도록 Amazon ECR 이미지 스캐닝을 구성합니다. 리소스 기반 정책을 사용하여 조직에 사후 검사 저장소에 대한 읽기 액세스 권한을 부여합니다.
C. 이미지의 사전 스캔 저장소에서 이미지의 사후 스캔 저장소로 각 이미지에 대한 이미지 복제를 구성합니다.
D. 각 사전 검사 저장소에 대해 AWS CodePipeline에서 파이프라인을 만듭니다. 사전 검사 저장소에 새 이미지가 푸시될 때 실행되는 소스 단계를 만듭니다. 작업 공급자로 AWS CodeBuild를 사용하는 단계를 만듭니다. 이미지 스캐닝 상태를 결정하고 심각한 취약점이 없는 이미지를 사후 검사 저장소에 푸시하는 buildspec.yaml 정의를 작성합니다.
E. AWS Lambda 함수를 만듭니다. 이미지 스캐닝 완료 이벤트에 반응하고 Lambda 함수를 호출하는 Amazon EventBridge 규칙을 만듭니다. 이미지 스캐닝 상태를 확인하고 심각한 취약점이 없는 이미지를 스캔 후 리포지토리에 푸시하는 함수 코드를 작성합니다. 가장 많이 투표된



### 질문 #239주제 1
한 회사에서 Amazon Elastic Kubernetes Service(Amazon EKS) 클러스터를 사용하여 컨테이너에 웹 애플리케이션을 배포합니다. 웹 애플리케이션에는 특정 자격 증명 없이는 해독할 수 없는 기밀 데이터가 포함되어 있습니다.

DevOps 엔지니어가 AWS Secrets Manager에 자격 증명을 저장했습니다. 비밀은 AWS Key Management Service(AWS KMS) 고객 관리 키로 암호화됩니다. 타사 도구의 Kubernetes 서비스 계정은 애플리케이션에서 비밀을 사용할 수 있도록 합니다. 서비스 계정은 회사에서 비밀에 액세스하기 위해 만든 IAM 역할을 가정합니다. 서비스 계정은

Secrets Manager에서 비밀을 검색하는 동안 액세스 거부(403 금지) 오류를 수신합니다.

이 문제의 근본 원인은 무엇입니까?

A. EKS 클러스터에 연결된 IAM 역할에는 Secrets Manager에서 비밀을 검색할 수 있는 액세스 권한이 없습니다.
B. 고객 관리 키에 대한 주요 정책은 Kubernetes 서비스 계정 IAM 역할이 키를 사용하는 것을 허용하지 않습니다. 가장 많이 투표된
C. 고객 관리 키에 대한 주요 정책은 EKS 클러스터 IAM 역할이 키를 사용하는 것을 허용하지 않습니다.
D. Kubernetes 서비스 계정에서 수행하는 IAM 역할에는 EKS 클러스터에 액세스할 수 있는 권한이 없습니다.



### 질문 #240주제 1
한 회사가 온프레미스 데이터 센터에서 하이브리드 환경으로 제품 개발 팀을 이전하고 있습니다. 새로운 환경에는 4개의 AWS 지역이 추가되고 개발자는 지리적으로 가장 가까운 지역을 사용할 수 있습니다.

모든 개발 팀은 공유 Linux 애플리케이션 세트를 사용합니다. 온프레미스 데이터 센터는 NetApp ONTAP 스토리지 디바이스에 애플리케이션을 저장합니다. 스토리지 볼륨은 개발 온프레미스 VM에서 읽기 전용으로 마운트됩니다. 회사는 일주일에 한 번 공유 볼륨에서 애플리케이션을 업데이트합니다.

DevOps 엔지니어는 모든 새로운 지역에 데이터를 복제해야 합니다. DevOps 엔지니어는 중복 제거를 통해 데이터가 항상 최신 상태인지 확인해야 합니다. 또한 데이터는 온프레미스 스토리지 디바이스의 가용성에 종속되어서는 안 됩니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 온프레미스 데이터 센터에 Amazon S3 파일 게이트웨이를 만듭니다. 각 리전에 S3 버킷을 만듭니다. 스토리지 디바이스에서 S3 파일 게이트웨이로 데이터를 복사하는 cron 작업을 설정합니다. 각 리전의 S3 버킷에 S3 크로스 리전 복제(CRR)를 설정합니다.
B. 한 지역에서 Amazon FSx 파일 게이트웨이를 만듭니다. 각 지역에서 Amazon FSx for Windows 파일 서버에 파일 서버를 만듭니다. 스토리지 장치에서 FSx 파일 게이트웨이로 데이터를 복사하는 cron 작업을 설정합니다.
C. 각 지역에서 NetApp ONTAP 인스턴스 및 볼륨을 위한 다중 AZ Amazon FSx를 만듭니다. 온프레미스 스토리지 장치와 ONTAP 인스턴스용 FSx 간에 예약된 SnapMirror 관계를 구성합니다. 가장 많이 투표된
D. 각 리전에 Amazon Elastic File System(Amazon EFS) 파일 시스템을 만듭니다. 온프레미스 데이터 센터에 AWS DataSync 에이전트를 배포합니다. DataSync가 매일 Amazon EFS에 데이터를 복사하도록 일정을 구성합니다.



### 질문 #241주제 1
한 회사에는 Amazon S3 버킷에 개인 식별 정보(PII)가 포함된 데이터를 저장하는 애플리케이션이 있습니다. 모든 데이터는 AWS Key Management Service(AWS KMS) 고객 관리 키로 암호화됩니다. 모든 AWS 리소스는 AWS CloudFormation 템플릿에서 배포됩니다.

DevOps 엔지니어는 다른 AWS 계정에서 애플리케이션에 대한 개발 환경을 설정해야 합니다. 개발 환경의 S3 버킷에 있는 데이터는 프로덕션 환경의 S3 버킷에서 일주일에 한 번 업데이트해야 합니다.

회사는 PII를 먼저 익명화하지 않고 프로덕션 환경에서 PII를 이동해서는 안 됩니다. 각 환경의 데이터는 다른 KMS 고객 관리 키로 암호화해야 합니다.

DevOps 엔지니어는 이러한 요구 사항을 충족하기 위해 어떤 단계 조합을 취해야 합니까? (두 가지를 선택하세요.)

A. 프로덕션 계정의 S3 버킷에서 Amazon Macie를 활성화합니다. AWS Step Functions 상태 머신을 만들어 검색 작업을 시작하고 모든 PII를 수정한 다음 개발 계정의 S3 버킷에 파일을 복사합니다. 상태 머신 작업에 프로덕션 계정의 KMS 키에 대한 암호 해독 권한을 부여합니다. 상태 머신 작업에 개발 계정의 KMS 키에 대한 암호화 권한을 부여합니다. 가장 많이 투표된
B. 프로덕션 S3 버킷과 개발 S3 버킷 간에 S3 복제를 설정합니다. 개발 S3 버킷에서 Amazon Macie를 활성화합니다. AWS Step Functions 상태 머신을 생성하여 검색 작업을 시작하고 파일이 개발 S3 버킷에 복사될 때 모든 PII를 삭제합니다. 상태 머신 작업에 개발 계정의 KMS 키에 대한 암호화 및 암호 해독 권한을 부여합니다.
C. 프로덕션 S3 버킷에서 개발 S3 버킷으로 파일을 복사하기 위한 S3 Batch Operations 작업을 설정합니다. 개발 계정에서 모든 PII를 수정하도록 AWS Lambda 함수를 구성합니다. S3 GET 요청에 Lambda 함수를 사용하도록 S3 Object Lambda를 구성합니다. 개발 계정에서 Lambda 함수의 IAM 역할에 KMS 키에 대한 암호화 및 복호화 권한을 부여합니다.
D. 개발 계정의 CloudFormation 템플릿에서 개발 환경을 만듭니다. 일주일에 한 번 AWS Step Functions 상태 머신을 시작하도록 Amazon EventBridge 규칙을 예약합니다. 가장 많이 투표된
E. 개발 계정의 CloudFormation 템플릿에서 개발 환경을 만듭니다. Amazon EC2 인스턴스에서 일주일에 한 번 실행되도록 cron 작업을 예약하여 S3 배치 작업 작업을 시작합니다.



### 질문 #242주제 1
한 회사에서 Amazon Elastic Kubernetes Service(Amazon EKS) 클러스터를 사용하여 머신 러닝(ML) 애플리케이션을 호스팅합니다. ML 모델과 컨테이너 이미지 크기가 커짐에 따라 새 포드가 시작되는 데 걸리는 시간이 몇 분으로 늘어났습니다.

DevOps 엔지니어는 시작 시간을 몇 초로 줄여야 합니다. 이 솔루션은 포드가 최근에 클러스터에 추가된 노드에서 실행되는 경우에도 시작 시간을 몇 초로 줄여야 합니다.

DevOps 엔지니어는 AWS Systems Manager에서 자동화를 호출하는 Amazon EventBridge 규칙을 만듭니다. 이 자동화는 새 이미지가 리포지토리에 푸시되면 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에서 컨테이너 이미지를 미리 가져옵니다. DevOps 엔지니어는 또한 클러스터와 노드 그룹에 적용할 태그를 구성합니다.

DevOps 엔지니어는 요구 사항을 충족하기 위해 다음에 무엇을 해야 합니까?

A. EventBridge가 Systems Manager를 사용하여 EKS 클러스터의 제어 평면 노드에서 명령을 실행할 수 있도록 허용하는 정책이 있는 IAM 역할을 만듭니다. 제어 평면 노드의 태그를 사용하여 해당 컨테이너 이미지를 미리 가져오는 Systems Manager State Manager 연결을 만듭니다.
B. EventBridge가 Systems Manager를 사용하여 EKS 클러스터 노드에서 명령을 실행할 수 있도록 허용하는 정책이 있는 IAM 역할을 만듭니다. 노드의 머신 크기를 사용하여 해당 컨테이너 이미지를 미리 가져오는 Systems Manager State Manager 연결을 만듭니다.
C. EventBridge가 Systems Manager를 사용하여 EKS 클러스터 노드에서 명령을 실행할 수 있도록 허용하는 정책이 있는 IAM 역할을 만듭니다. 노드의 태그를 사용하여 해당 컨테이너 이미지를 미리 가져오는 Systems Manager State Manager 연결을 만듭니다. 가장 많이 투표된
D. EventBridge가 Systems Manager를 사용하여 EKS 클러스터의 제어 평면 노드에서 명령을 실행할 수 있도록 허용하는 정책이 있는 IAM 역할을 만듭니다. 노드의 태그를 사용하여 해당 컨테이너 이미지를 미리 가져오는 Systems Manager State Manager 연결을 만듭니다.



### 질문 #243주제 1
회사의 애플리케이션에는 워크로드 메트릭을 검색하는 API가 있습니다. 회사는 애플리케이션에서 이러한 메트릭을 감사, 분석 및 시각화하여 대규모 문제를 감지해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. Amazon EventBridge 일정을 구성하여 워크로드 메트릭을 검색하기 위해 API를 호출하는 AWS Lambda 함수를 호출합니다. 워크로드 메트릭 데이터를 Amazon S3 버킷에 저장합니다. 가장 많이 투표된
B. API를 호출하여 워크로드 메트릭을 검색하는 AWS Lambda 함수를 호출하도록 Amazon EventBridge 일정을 구성합니다. DynamoDB 스트림이 활성화된 Amazon DynamoDB 테이블에 워크로드 메트릭 데이터를 저장합니다.
C. Amazon S3 버킷의 워크로드 메트릭 데이터를 카탈로그화하기 위해 AWS Glue 크롤러를 만듭니다. 카탈로그화된 데이터에 대한 Amazon Athena에서 뷰를 만듭니다. 가장 많이 투표된
D. AWS Glue 크롤러를 Amazon DynamoDB 스트림에 연결하여 워크로드 메트릭 데이터를 카탈로그화합니다. 카탈로그화된 데이터에 대한 Amazon Athena에서 뷰를 만듭니다.
E. Amazon Athena 뷰에서 Amazon QuickSight 데이터 세트를 만듭니다. QuickSight 분석을 만들어 워크로드 메트릭 데이터를 대시보드로 시각화합니다. 가장 많이 투표된
F. AWS Lambda 함수를 호출하는 사용자 지정 위젯이 있는 Amazon CloudWatch 대시보드를 만듭니다. Amazon Athena 뷰에서 워크로드 메트릭 데이터를 쿼리하도록 Lambda 함수를 구성합니다.



### 질문 #244주제 1
DevOps 엔지니어가 애플리케이션의 인프라를 구축하고 있습니다. 애플리케이션은 Amazon EC2 인스턴스를 포함하는 Amazon Elastic Kubernetes Service(Amazon EKS) 클러스터에서 실행되어야 합니다. EC2 인스턴스는 Amazon Elastic File System(Amazon EFS) 파일 시스템을 스토리지 백엔드로 사용해야 합니다. Amazon EFS Container Storage Interface(CSI) 드라이버는 EKS 클러스터에 설치됩니다.

DevOps 엔지니어가 애플리케이션을 시작하면 EC2 인스턴스는 EFS 파일 시스템을 마운트하지 않습니다.

어떤 솔루션이 문제를 해결할까요? (세 가지를 선택하세요.)

A. EKS 노드를 Amazon EC2에서 AWS Fargate로 전환합니다.
B. EKS 클러스터에서 NFS 트래픽을 허용하기 위해 EFS 파일 시스템의 보안 그룹에 인바운드 규칙을 추가합니다. 가장 많이 투표된
C. Amazon EFS CSI 드라이버가 파일 시스템과 상호 작용할 수 있도록 하는 IAM 역할을 생성합니다. 가장 많이 투표된
D. AWS DataSync를 설정하여 EFS 파일 시스템과 EKS 노드 간 파일 전송을 구성합니다.
E. EKS 노드의 서브넷에 있는 EFS 파일 시스템에 대한 마운트 대상을 만듭니다. 가장 많이 투표된
F. 암호화 또는 EFS 파일 시스템을 비활성화합니다.



### 질문 #245주제 1
회사에서 회사의 온프레미스 데이터 센터에 있는 온프레미스 디바이스에 애플리케이션을 배포합니다. 회사는 데이터 센터와 회사의 AWS 계정 간에 AWS Direct Connect 연결을 사용합니다. 온프레미스 디바이스의 초기 설정과 애플리케이션 업데이트 중에 애플리케이션은 Amazon Elastic File System(Amazon EFS) 파일 시스템에서 구성 파일을 검색해야 합니다. 온프레미스

디바이스에서 Amazon EFS로의 모든 트래픽은 비공개로 유지되고 암호화되어야 합니다. 온프레미스 디바이스는 AWS 액세스에 대한 최소 권한 원칙을 따라야 합니다. 회사의 DevOps 팀은 다른 디바이스의 액세스에 영향을 미치지 않고 단일 디바이스의 액세스를 취소할 수 있어야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. 각 기기에 대한 액세스 키와 비밀 키가 있는 IAM 사용자를 만듭니다. 모든 IAM 사용자에게 AmazonElasticFileSystemFullAccess 정책을 연결합니다. 온프레미스 기기에서 AWS CLI를 구성하여 IAM 사용자의 액세스 키와 비밀 키를 사용합니다.
B. AWS Private Certificate Authority에서 온프레미스 디바이스마다 인증서를 생성합니다. AWS Private CA를 참조하는 IAM Roles Anywhere에서 신뢰 앵커를 만듭니다. IAM Roles Anywhere를 신뢰하는 IAM 역할을 만듭니다. 역할에 AmazonElasticFileSystemClientReadWriteAccess를 연결합니다. IAM 역할에 대한 IAM Roles Anywhere 프로필을 만듭니다. 온프레미스 디바이스에서 AWS CLI를 구성하여 aws_signing_helper 명령을 사용하여 자격 증명을 얻습니다. 가장 많이 투표된
C. 모든 기기에 대한 액세스 키와 비밀 키가 있는 IAM 사용자를 만듭니다. AmazonElasticFileSystemClientReadWriteAccess 정책을 IAM 사용자에게 연결합니다. 온프레미스 기기에서 AWS CLI를 구성하여 IAM 사용자의 액세스 키와 비밀 키를 사용합니다.
D. amazon-efs-utils 패키지를 사용하여 EFS 파일 시스템을 마운트합니다. 가장 많이 투표된
E. 기본 Linux NFS 클라이언트를 사용하여 EFS 파일 시스템을 마운트합니다.



### 질문 #246주제 1
DevOps 엔지니어가 AWS CodeDeploy와 AWS CloudFormation을 사용하여 애플리케이션에 대한 Amazon Elastic Container Service(Amazon ECS) 블루/그린 배포를 설정하고 있습니다. 배포 기간 동안 애플리케이션은 고가용성이어야 하며 CodeDeploy는 모든 트래픽이 전환될 때까지 매분 트래픽의 10%를 애플리케이션의 새 버전으로 전환해야 합니다.

이러한 요구 사항을 충족하기 위해 DevOps 엔지니어는 CloudFormation 템플릿에 어떤 구성을 추가해야 합니까?

A. CodeDeployDefault.ECSLinearl OPercentEveryl Minutes 배포 구성을 포함하는 AppSpec 파일을 추가합니다.
B. CodeDeployDefault.ECSLinear10PercentEvery1Minutes 배포 구성으로 AWS::CodeDeployBlueGreen 변환과 AWS::CodeDeploy::BlueGreen 후크 매개변수를 추가합니다. 가장 많이 투표된
C. ECSCanary10Percent5Minutes 배포 구성을 사용하여 AppSpec 파일을 추가합니다.
D. ECSCanary10Percent5Minutes 배포 구성으로 AWS::CodeDeployBlueGreen 변환과 AWS::CodeDepioy::BlueGreen 후크 매개변수를 추가합니다.



### 질문 #247주제 1
한 회사가 AWS Organizations에서 조직을 사용하여 AWS 계정을 관리합니다. 이 회사의 DevOps 팀은 Organizations API를 호출하여 새 AWS 계정을 만드는 AWS Lambda 함수를 개발했습니다.

Lambda 함수는 조직의 관리 계정에서 실행됩니다. DevOps 팀은 Lambda 함수를 관리 계정에서 전용 AWS 계정으로 옮겨야 합니다. DevOps 팀은 Lambda 함수를 새 계정에 배포하기 전에 Lambda 함수가 Organizations에서만 새 AWS 계정을 만들 수 있는지 확인해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 관리 계정에서 Organizations에서 새 계정을 만드는 데 필요한 권한이 있는 새 IAM 역할을 만듭니다. 새 AWS 계정에서 Lambda 실행 역할이 역할을 맡도록 허용합니다. Lambda 함수가 새 AWS 계정을 만들 때 역할을 맡도록 Lambda 함수 코드를 업데이트합니다. Lambda 실행 역할을 업데이트하여 새 역할을 맡을 수 있는 권한이 있는지 확인합니다. 가장 많이 투표된
B. 관리 계정에서 Organizations에 대한 위임된 관리를 켭니다. Organizations에서 새 AWS 계정을 만들 수 있는 권한을 새 AWS 계정에 부여하는 새 위임 정책을 만듭니다. Lambda 실행 역할에 organizations:CreateAccount 권한이 있는지 확인합니다.
C. 관리 계정에서 Organizations에서 새 계정을 만드는 데 필요한 권한이 있는 새 IAM 역할을 만듭니다. Lambda 서비스 주체가 역할을 맡도록 허용합니다. Lambda 함수가 새 AWS 계정을 만들 때 역할을 맡도록 Lambda 함수 코드를 업데이트합니다. Lambda 실행 역할을 업데이트하여 새 역할을 맡을 수 있는 권한이 있는지 확인합니다.
D. 관리 계정에서 AWS Control Tower를 활성화합니다. AWS Control Tower에 대한 위임된 관리를 켭니다. 새 AWS 계정이 AWS Control Tower에서 새 AWS 계정을 만들 수 있도록 허용하는 리소스 정책을 만듭니다. 새 AWS 계정에서 AWS Control Tower API를 사용하도록 Lambda 함수 코드를 업데이트합니다. Lambda 실행 역할에 controltower:CreateManagedAccount 권한이 있는지 확인합니다.



### 질문 #248주제 1
한 회사가 단일 AWS 리전에 애플리케이션을 배포했습니다. 애플리케이션 백엔드는 Amazon DynamoDB 테이블과 Amazon S3 버킷을 사용합니다.

회사는 보조 리전에 애플리케이션을 배포하려고 합니다. 회사는 DynamoDB 테이블과 S3 버킷의 데이터가 두 리전에서 지속되도록 해야 합니다. 또한 데이터는 리전 간에 즉시 전파되어야 합니다.

어떤 솔루션이 가장 높은 운영 효율성으로 이러한 요구 사항을 충족할까요?

A. 기본 지역의 S3 버킷과 보조 지역의 S3 버킷 간에 양방향 S3 버킷 복제를 구현합니다. DynamoDB 테이블을 글로벌 테이블로 변환합니다. 보조 지역을 추가 지역으로 설정합니다. 가장 많이 투표된
B. 모든 S3 버킷에 대해 기본 지역과 보조 지역 간에 S3 일괄 작업 복사 작업을 구현합니다. DynamoDB 테이블을 글로벌 테이블로 변환합니다. 보조 지역을 추가 지역으로 설정합니다.
C. 기본 지역의 S3 버킷과 보조 지역의 S3 버킷 간에 양방향 S3 버킷 복제를 구현합니다. 두 지역의 DynamoDB 테이블에서 DynamoDB 스트림을 활성화합니다. 각 지역에서 DynamoDB 스트림을 구독하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 구성하여 다른 지역의 DynamoDB 테이블에 새 레코드를 복사합니다.
D. 모든 S3 버킷에 대해 기본 지역과 보조 지역 간에 S3 배치 작업 복사 작업을 구현합니다. 두 지역의 DynamoDB 테이블에서 DynamoDB 스트림을 활성화합니다. 각 지역에서 DynamoDB 스트림을 구독하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 구성하여 다른 지역의 DynamoDB 테이블에 새 레코드를 복사합니다.



### 질문 #249주제 1
한 회사가 RDS DB 인스턴스에 대해 Amazon RDS 스토리지 자동 확장을 구성했습니다. DevOps 팀은 Amazon CloudWatch 대시보드에서 자동 확장 이벤트를 시각화해야 합니다.

어떤 솔루션이 이 요구 사항을 충족할까요?

A. RDS 이벤트에서 RDS 스토리지 자동 확장 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. CloudWatch 사용자 지정 메트릭을 게시하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 호출하도록 EventBridge 규칙을 구성합니다. CloudWatch 대시보드를 사용하여 사용자 지정 메트릭을 시각화합니다. 가장 많이 투표된
B. 관리 이벤트가 구성된 AWS CloudTrail을 사용하여 트레일을 만듭니다. 관리 이벤트를 Amazon CloudWatch Logs로 보내도록 트레일을 구성합니다. RDS 스토리지 자동 확장 이벤트와 일치하도록 CloudWatch Logs에서 메트릭 필터를 만듭니다. CloudWatch 대시보드를 사용하여 메트릭 필터를 시각화합니다.
C. RDS 이벤트에서 RDS 스토리지 자동 확장 이벤트에 반응하는 Amazon EventBridge 규칙을 만듭니다. CloudWatch 알람을 만듭니다. CloudWatch 알람의 상태를 변경하도록 EventBridge 규칙을 구성합니다. CloudWatch 대시보드를 사용하여 알람 상태를 시각화합니다.
D. AWS CloudTrail을 사용하여 데이터 이벤트가 구성된 트레일을 만듭니다. 트레일을 구성하여 데이터 이벤트를 Amazon CloudWatch Logs로 보냅니다. RDS 스토리지 자동 확장 이벤트와 일치하도록 CloudWatch Logs에서 메트릭 필터를 만듭니다. CloudWatch 대시보드를 사용하여 메트릭 필터를 시각화합니다.



### 질문 #250주제 1
한 회사가 애플리케이션에 컨테이너를 사용합니다. 이 회사는 일부 컨테이너 이미지에 필수 보안 구성이 누락되어 있음을 알게 되었습니다.

DevOps 엔지니어는 표준 기본 이미지를 만드는 솔루션을 구현해야 합니다. 솔루션은 기본 이미지를 us-west-2 Region, us-east-2 Region, eu-central-1 Region에 매주 게시해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 컨테이너 레시피를 사용하여 이미지를 빌드하는 EC2 Image Builder 파이프라인을 만듭니다. 파이프라인을 구성하여 이미지를 us-west-2의 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에 배포합니다. us-west-2에서 us-east-2로, us-east-2에서 eu-central-1로 ECR 복제를 구성합니다. 파이프라인을 매주 실행하도록 구성합니다.
B. AWS CodeBuild 프로젝트를 사용하여 이미지를 빌드하는 AWS CodePipeline 파이프라인을 만듭니다. AWS CodeDeploy를 사용하여 이미지를 us-west-2의 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에 게시합니다. us-west-2에서 us-east-2로, us-east-2에서 eu-central-1로 ECR 복제를 구성합니다. 파이프라인을 매주 실행하도록 구성합니다.
C. 컨테이너 레시피를 사용하여 이미지를 빌드하는 EC2 Image Builder 파이프라인을 만듭니다. 파이프라인을 구성하여 이미지를 세 지역의 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에 배포합니다. 파이프라인을 매주 실행하도록 구성합니다. 가장 많이 투표된
D. AWS CodeBuild 프로젝트를 사용하여 이미지를 빌드하는 AWS CodePipeline 파이프라인을 만듭니다. AWS CodeDeploy를 사용하여 이미지를 세 리전 모두의 Amazon Elastic Container Registry(Amazon ECR) 리포지토리에 게시합니다. 파이프라인을 매주 실행하도록 구성합니다.



### 질문 #251주제 1
DevOps 엔지니어는 AWS 계정의 모든 Amazon EC2 인스턴스에 바이러스 백신 소프트웨어를 설치하는 솔루션을 구현해야 합니다. EC2 인스턴스는 최신 버전의 Amazon Linux를 실행합니다.

솔루션은 모든 인스턴스를 감지해야 하며 소프트웨어가 없는 경우 AWS Systems Manager 문서를 사용하여 소프트웨어를 설치해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. Systems Manager State Manager에서 연결을 만듭니다. 모든 관리 노드를 대상으로 합니다. 소프트웨어를 연결에 포함합니다. Systems Manager 문서를 사용하도록 연결을 구성합니다. 가장 많이 투표된
B. AWS Config를 설정하여 계정의 모든 리소스를 기록합니다. AWS Config 사용자 지정 규칙을 만들어 소프트웨어가 모든 EC2 인스턴스에 설치되어 있는지 확인합니다. 비준수 EC2 인스턴스에 대해 Systems Manager 문서를 사용하는 자동 수정 작업을 구성합니다.
C. Amazon Inspector에서 Amazon EC2 스캐닝을 활성화하여 소프트웨어가 모든 EC2 인스턴스에 설치되어 있는지 확인합니다. 결과를 Systems Manager 문서와 연결합니다.
D. AWS CloudTrail을 사용하여 Runinstances API 호출을 감지하는 Amazon EventBridge 규칙을 만듭니다. Systems Manager Inventory에서 인벤토리 수집을 구성하여 소프트웨어가 EC2 인스턴스에 설치되어 있는지 확인합니다. Systems Manager 인벤토리를 Systems Manager 문서와 연결합니다.



### 질문 #252주제 1
한 회사가 프로덕션 환경에서 실행되는 컨테이너 이미지의 보안을 강화해야 합니다. 이 회사는 CI/CD 파이프라인의 컨테이너에 대한 운영 체제 스캐닝과 프로그래밍 언어 패키지 취약성 스캐닝을 통합하려고 합니다. CI/CD 파이프라인은 AWS CodeBuild 빌드 프로젝트, AWS CodeDeploy 작업, Amazon Elastic Container Registry(Amazon ECR) 리포지토리를 포함하는 AWS CodePipeline 파이프라인입니다.

DevOps 엔지니어는 CI/CD 파이프라인에 이미지 스캔을 추가해야 합니다. CI/CD 파이프라인은 CRITICAL 및 HIGH 결과가 없는 이미지만 프로덕션에 배포해야 합니다.

이러한 요구 사항을 충족하는 단계 조합은 무엇입니까? (두 가지를 선택하세요.)

A. Amazon ECR 기본 스캐닝을 사용합니다.
B. Amazon ECR 강화된 스캐닝을 사용합니다. 가장 많이 투표된
C. 이미지 검사 결과가 CRITICAL 또는 HIGH 결과를 반환하는 경우 CI/CD 파이프라인에 거부됨 상태를 제출하도록 Amazon ECR을 구성합니다.
D. 이미지 스캔이 완료되면 AWS Lambda 함수를 호출하도록 Amazon EventBridge 규칙을 구성합니다. Lambda 함수를 구성하여 Amazon Inspector 스캔 상태를 사용하고 CI/CD 파이프라인에 승인됨 또는 거부됨 상태를 제출합니다. 가장 많이 투표된
E. 이미지 스캔이 완료되면 AWS Lambda 함수를 호출하도록 Amazon EventBridge 규칙을 구성합니다. Lambda 함수를 구성하여 Clair 스캔 상태를 사용하고 CI/CD 파이프라인에 승인됨 또는 거부됨 상태를 제출합니다.



### 질문 #253주제 1
회사의 DevOps 팀은 AWS Organizations의 조직에 있는 일련의 AWS 계정을 관리합니다.

이 회사에는 모든 Amazon EC2 인스턴스가 DevOps 팀이 관리하는 승인된 AM을 사용하도록 보장하는 솔루션이 필요합니다. 이 솔루션은 또한 승인되지 않은 AMI의 사용을 수정해야 합니다. 개별 계정 관리자는 승인된 AMI를 사용하는 제한을 제거할 수 없어야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS CloudFormation StackSets를 사용하여 각 계정에 Amazon EventBridge 규칙을 배포합니다. Amazon EC2에 대한 AWS CloudTrail 이벤트에 반응하고 Amazon Simple Notification Service(Amazon SNS) 토픽에 알림을 보내도록 규칙을 구성합니다. DevOps 팀을 SNS 토픽에 구독합니다.
B. AWS CloudFormation StackSets를 사용하여 approved-amis-by-id AWS Config 관리 규칙을 각 계정에 배포합니다. 승인된 AMI 목록으로 규칙을 구성합니다. 비준수 EC2 인스턴스에 대해 AWS-StopEC2Instance AWS Systems Manager Automation 런북을 실행하도록 규칙을 구성합니다.
C. Amazon EC2에 대한 AWS CloudTrail 이벤트를 처리하는 AWS Lambda 함수를 만듭니다. Lambda 함수를 구성하여 Amazon Simple Notification Service(Amazon SNS) 토픽에 알림을 보냅니다. DevOps 팀을 SNS 토픽에 구독합니다. 조직의 각 계정에 Lambda 함수를 배포합니다. 각 계정에 Amazon EventBridge 규칙을 만듭니다. Amazon EC2에 대한 AWS CloudTrail 이벤트에 반응하고 Lambda 함수를 호출하도록 EventBridge 규칙을 구성합니다.
D. 조직 전체에서 AWS Config를 활성화합니다. 승인된 AMI 목록과 함께 approved-amis-by-id AWS Config 관리 규칙을 사용하는 적합성 팩을 만듭니다. 조직 전체에 적합성 팩을 배포합니다. 비준수 EC2 인스턴스에 대해 AWS-StopEC2Instance AWS Systems Manager Automation 런북을 실행하도록 규칙을 구성합니다. 가장 많이 투표된



### 질문 #254주제 1
한 회사가 직원들에게 AWS에 대한 제한적인 권한을 부여했습니다. DevOps 엔지니어는 관리자 역할을 맡을 수 있습니다. 추적 목적으로 보안 팀은 관리자 역할이 맡을 때 거의 실시간 알림을 받고 싶어합니다.

이를 어떻게 달성해야 할까요?

A. AWS Config를 구성하여 Amazon S3 버킷에 로그를 게시합니다. Amazon Athena를 사용하여 로그를 쿼리하고 관리자 역할이 가정되면 보안 팀에 알림을 보냅니다.
B. 관리자 역할이 가정될 때 모니터링하고 보안 팀에 알림을 보내도록 Amazon GuardDuty를 구성합니다.
C. AWS Management Console 로그인 이벤트 이벤트 패턴을 사용하여 관리자 역할이 가정된 경우 Amazon SNS 주제에 메시지를 게시하는 Amazon EventBridge 이벤트 규칙을 생성합니다.
D. 관리자 역할이 가정된 경우 Amazon SNS 주제에 메시지를 게시하는 AWS Lambda 함수를 호출하기 위해 AWS CloudTrail 이벤트 패턴을 사용하는 AWS API 호출을 사용하여 Amazon EventBridge 이벤트 규칙을 생성합니다. 가장 많이 투표된



### 질문 #255주제 1
어떤 회사에서는 데이터와 애플리케이션의 장애 조치 및 재해 복구를 위한 전략이 필요합니다. 이 애플리케이션은 MySQL 데이터베이스와 Amazon EC2 인스턴스를 사용합니다. 이 회사는 데이터와 애플리케이션에 대해 항상 최대 2시간의 RPO와 최대 10분의 RTO가 필요합니다.

어떤 배포 전략 조합이 이러한 요구 사항을 충족할까요? (두 가지를 선택하세요.)

A. 여러 AWS 지역에 Amazon Aurora Single-AZ 클러스터를 데이터 저장소로 만듭니다. 재해 발생 시 Aurora의 자동 복구 기능을 사용합니다.
B. 두 개의 AWS 리전에 Amazon Aurora 글로벌 데이터베이스를 데이터 저장소로 만듭니다. 장애가 발생하면 보조 리전을 애플리케이션의 기본 리전으로 승격합니다. 보조 리전에서 Aurora 클러스터 엔드포인트를 사용하도록 애플리케이션을 업데이트합니다. 가장 많이 투표된
C. 여러 AWS 리전에 Amazon Aurora 클러스터를 데이터 저장소로 만듭니다. Network Load Balancer를 사용하여 다른 리전의 데이터베이스 트래픽을 균형 있게 조정합니다.
D. 두 AWS 리전에 애플리케이션을 설정합니다. 두 리전 모두에서 애플리케이션 로드 밸런서를 가리키는 Amazon Route 53 장애 조치 라우팅을 사용합니다. 각 리전에서 상태 확인 및 자동 확장 그룹을 사용합니다. 가장 많이 투표된
E. 두 AWS 리전에서 애플리케이션을 설정합니다. AWS Global Accelerator를 두 리전 모두의 애플리케이션 로드 밸런서(ALB)를 가리키도록 구성합니다. 두 ALB를 단일 엔드포인트 그룹에 추가합니다. 각 리전에서 상태 확인 및 자동 확장 그룹을 사용합니다.



### 질문 #256주제 1
개발자는 AWS Serverless Application Model(AWS SAM)을 사용하여 AWS Lambda 함수의 프로토타입을 만들고 있습니다. AWS SAM 템플릿에는 Amazon S3 위치를 가리키는 CodeUri 속성이 있는 AWS::Serverless::Function 리소스가 포함되어 있습니다. 개발자는 CI/CD 파이프라인을 만들기 전에 배포에 대한 올바른 명령을 식별하려고 합니다. 개발자는

package.zip이라는 이름의 Lambda 함수 코드의 아카이브를 만듭니다. 개발자는 CodeUri 속성에 지정된 S3 위치에 .zip 파일 아카이브를 업로드합니다. 개발자는 sam deploy 명령을 실행하고 Lambda 함수를 배포합니다. 개발자는 Lambda 함수 코드를 업데이트하고 동일한 단계를 사용하여 새 버전의 Lambda 함수를 배포합니다. sam deploy 명령이 실패하고 배포할 변경 사항이 없다는 오류를 반환합니다.

어떤 솔루션이 새 버전을 배포할까요? (두 가지를 선택하세요.)

A. sam deploy 명령 대신 aws cloudformation update-stack 명령을 사용하세요.
B. sam deploy 명령 대신 aws cloudformation update-stack-instances 명령을 사용합니다.
C. 로컬 애플리케이션 코드 폴더를 참조하도록 CodeUri 속성을 업데이트합니다. sam deploy 명령을 사용합니다. 가장 많이 투표된
D. 로컬 애플리케이션 코드 폴더를 참조하도록 CodeUri 속성을 업데이트합니다. aws cloudformation create-change-set 명령과 aws cloudformation execute-change-set 명령을 사용합니다.
E. CodeUri 속성을 업데이트하여 로컬 애플리케이션 코드 폴더를 참조합니다. aws cloudformation package 명령과 aws cloudformation deploy 명령을 사용합니다. 가장 많이 투표된



### 질문 #257주제 1
한 회사가 AWS App Runner에서 컨테이너 워크로드를 실행합니다. DevOps 엔지니어가 Amazon Elastic Container Registry(Amazon ECR)에서 회사의 컨테이너 리포지토리를 관리합니다.

DevOps 엔지니어는 컨테이너 리포지토리를 지속적으로 모니터링하는 솔루션을 구현해야 합니다. 솔루션은 운영 체제 취약성이나 언어 패키지 취약성을 감지하면 새 컨테이너 이미지를 생성해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. EC2 Image Builder를 사용하여 컨테이너 이미지 파이프라인을 만듭니다. Amazon ECR을 대상 저장소로 사용합니다. ECR 저장소에서 향상된 스캐닝을 켭니다. Inspector? 찾기 이벤트를 캡처하기 위한 Amazon EventBridge 규칙을 만듭니다. 이벤트를 사용하여 이미지 파이프라인을 호출합니다. 컨테이너를 저장소에 다시 업로드합니다. 가장 많이 투표된
B. EC2 Image Builder를 사용하여 컨테이너 이미지 파이프라인을 만듭니다. Amazon ECR을 대상 리포지토리로 사용합니다. 컨테이너 워크로드에서 Amazon GuardDuty Malware Protection을 활성화합니다. GuardDuty 발견 이벤트를 캡처하기 위한 Amazon EventBridge 규칙을 만듭니다. 이벤트를 사용하여 이미지 파이프라인을 호출합니다.
C. AWS CodeBuild 프로젝트를 만들어 컨테이너 이미지를 만듭니다. Amazon ECR을 대상 리포지토리로 사용합니다. 리포지토리에서 기본 스캐닝을 켭니다. Amazon EventBridge 규칙을 만들어 ECR 이미지 작업 이벤트를 캡처합니다. 이벤트를 사용하여 CodeBuild 프로젝트를 호출합니다. 컨테이너를 리포지토리에 다시 업로드합니다.
D. 컨테이너 이미지를 생성하기 위해 AWS CodeBuild 프로젝트를 만듭니다. Amazon ECR을 대상 리포지토리로 사용합니다. 모든 관리 노드를 스캔하도록 AWS Systems Manager Compliance를 구성합니다. 구성 준수 상태 변경 이벤트를 캡처하기 위해 Amazon EventBridge 규칙을 만듭니다. 이벤트를 사용하여 CodeBuild 프로젝트를 호출합니다.



### 질문 #258주제 1
한 회사에서는 개발자를 위해 실제 노트북을 부트스트랩하기 위해 AWS Systems Manager 문서를 사용하고자 합니다. 부트스트랩 코드는 GitHub에 저장됩니다. DevOps 엔지니어는 이미 Systems Manager 활성화를 생성하고 등록 코드로 Systems Manager 에이전트를 설치하고 모든 노트북에 활성화 ID를 설치했습니다.

그 다음에 어떤 단계를 거쳐야 할까요?

A. AWS-RunShellScript 명령을 사용하여 GitHub에서 Amazon S3로 파일을 복사하도록 Systems Manager 문서를 구성한 다음, sourceType을 S3로 지정하여 aws-downloadContent 플러그인을 사용합니다.
B. 설치 작업과 함께 aws-configurePackage 플러그인을 사용하고 Git 저장소를 가리키도록 Systems Manager 문서를 구성합니다.
C. GitHub의 sourceType과 저장소 세부 정보가 있는 sourceInfo를 사용하여 aws-downloadContent 플러그인을 사용하도록 Systems Manager 문서를 구성합니다. 가장 많이 투표된
D. aws:softwareInventory 플러그인을 사용하여 Systems Manager 문서를 구성하고 Git 저장소에서 스크립트를 실행합니다.



### 질문 #259주제 1
회사의 개발팀은 AWS CloudFormation을 사용하여 애플리케이션 리소스를 배포합니다. 팀은 환경에 대한 모든 변경 사항에 CloudFormation을 사용해야 합니다. 팀은 AWS Management Console 또는 AWS CLI를 사용하여 직접 수동으로 변경할 수 없습니다.

팀은 개발자 IAM 역할을 사용하여 환경에 액세스합니다. 이 역할은 AdministratorAccess 관리형 IAM 정책으로 구성됩니다. 회사는 다음 정책이 첨부된 새 CloudFormationDeployment IAM 역할을 만들었습니다.



회사는 CloudFormation만 새 역할을 사용할 수 있도록 하려고 합니다. 개발팀은 배포된 리소스를 수동으로 변경할 수 없습니다.

이러한 요구 사항을 충족하는 단계 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. AdministratorAccess 정책을 제거합니다. ReadOnlyAccess 관리형 IAM 정책을 개발자 역할에 할당합니다. 개발자가 새 스택을 배포할 때 CloudFormationDeployment 역할을 CloudFormation 서비스 역할로 사용하도록 개발자에게 지시합니다. 가장 많이 투표된
B. CloudFormationDeployment 역할의 신뢰 정책을 업데이트하여 개발자 IAM 역할이 CloudFormationDeployment 역할을 맡을 수 있도록 허용합니다.
C. iam:PassedToService가 .이면 CloudFormationDeployment 역할을 가져오고 전달할 수 있도록 개발자 IAM 역할을 구성합니다. 모든 리소스에 대한 모든 cloudformation 작업을 허용하도록 CloudFormationDeployment 역할을 구성합니다.
D. CloudFormationDeployment 역할의 신뢰 정책을 업데이트하여 cloudformation.amazonaws.com AWS 보안 주체가 iam:AssumeRole 작업을 수행할 수 있도록 허용합니다. 가장 많이 투표된
E. AdministratorAccess 정책을 제거합니다. ReadOnlyAccess 관리형 IAM 정책을 개발자 역할에 할당합니다. 개발자가 새 스택을 배포할 때 CloudFormationDeployment 역할을 맡도록 개발자에게 지시합니다.
F. CloudFormationDeployment 역할에 IAM 정책을 추가하여 모든 리소스에서 cloudformation:*를 허용합니다. iam:PassedToService가 cloudformation.amazonaws.com과 같은 경우 CloudFormationDeployment 역할의 ARN에 대한 iam:PassRole 작업을 허용하는 정책을 추가합니다. 가장 많이 투표된



### 질문 #260주제 1
한 회사가 AWS CloudFormation을 사용하여 웹 애플리케이션의 인프라를 개발하고 있습니다. 데이터베이스 엔지니어링 팀은 CloudFormation 템플릿에서 데이터베이스 리소스를 유지 관리하고 소프트웨어 개발 팀은 별도의 CloudFormation 템플릿에서 웹 애플리케이션 리소스를 유지 관리합니다. 애플리케이션의 범위가 커짐에 따라 소프트웨어 개발 팀은 데이터베이스 엔지니어링 팀이 유지 관리하는 리소스를 사용해야 합니다. 그러나 두 팀 모두 유지하려는 자체 검토 및 수명 주기 관리 프로세스가 있습니다. 두 팀 모두 리소스 수준 변경 세트 검토도 필요합니다. 소프트웨어 개발 팀은 CI/CD 파이프라인을 사용하여 이 템플릿에 변경 사항을 배포하려고 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 데이터베이스 CloudFormation 템플릿에서 스택 내보내기를 만들고 해당 참조를 웹 애플리케이션 CloudFormation 템플릿으로 가져옵니다. 가장 많이 투표된
B. CloudFormation 중첩 스택을 생성하여 두 스택 모두에서 크로스 스택 리소스 참조 및 매개변수를 사용할 수 있도록 합니다.
C. 두 스택 모두에서 크로스 스택 리소스 참조 및 매개변수를 사용할 수 있도록 CloudFormation 스택 세트를 생성합니다.
D. 웹 애플리케이션 CloudFormation 템플릿에서 입력 매개변수를 만들고 데이터베이스 스택에서 리소스 이름과 ID를 전달합니다.



### 질문 #261주제 1
회사에 AWS Organizations에 조직이 있습니다. DevOps 엔지니어는 조직의 여러 OU에 속하는 여러 AWS 계정을 유지 관리해야 합니다. 계정 내의 IAM 정책 및 Amazon S3 정책을 포함한 모든 리소스는 AWS CloudFormation을 통해 배포됩니다. 모든 템플릿과 코드는 AWS CodeCommit 리포지토리에서 유지 관리됩니다. 최근 일부 개발자는 조직의 일부 계정에서 S3 버킷에 액세스할 수 없었습니다.

다음 정책이 S3 버킷에 첨부되었습니다.



DevOps 엔지니어는 이 액세스 문제를 해결하기 위해 무엇을 해야 합니까?

A. S3 버킷 정책을 수정합니다. S3 버킷에서 S3 Block Public Access 설정을 끕니다. S3 정책에서 aws:SourceAccount 조건을 추가합니다. 문제를 겪고 있는 모든 개발자의 AWS 계정 ID를 추가합니다.
B. 개발자가 S3 버킷에 액세스하는 것을 거부하는 IAM 권한 경계가 없는지 확인합니다. IAM 권한 경계에 필요한 변경을 합니다. 문제가 발생한 개별 개발자 계정에서 AWS Config 레코더를 사용하여 액세스를 차단하는 모든 변경 사항을 되돌립니다. 수정 사항을 CodeCommit 리포지토리에 다시 커밋합니다. CloudFormation을 통해 배포를 호출하여 변경 사항을 적용합니다.
C. 개발자 OU에서 IAM 리소스를 수정하는 것을 막는 SCP를 구성합니다. S3 정책에서 aws:SourceAccount 조건을 추가합니다. 문제가 발생한 모든 개발자의 AWS 계정 ID를 추가합니다. 수정 사항을 CodeCommit 리포지토리에 다시 커밋합니다. CloudFormation을 통해 배포를 호출하여 변경 사항을 적용합니다.
D. SCP가 개발자의 S3 버킷 액세스를 차단하지 않는지 확인합니다. IAM 정책 권한 경계가 개발자 IAM 사용자의 액세스를 거부하지 않는지 확인합니다. CodeCommit 리포지토리에서 SCP 및 IAM 정책 권한 경계를 필요한 대로 변경합니다. CloudFormation을 통해 배포를 호출하여 변경 사항을 적용합니다. 가장 많이 투표된



### 질문 #262주제 1
한 회사가 다중 계정 환경을 위해 AWS Organizations에 조직을 두고 있습니다. DevOps 엔지니어가 조직 전체에서 애플리케이션 패키지 관리를 위한 AWS CodeArtifact 기반 전략을 개발하고 있습니다. 회사의 각 애플리케이션 팀은 조직 내에 자체 계정을 가지고 있습니다. 각 애플리케이션 팀은 또한 중앙 집중화된 공유 서비스 계정에 대한 제한된 액세스 권한을 가지고 있습니다.

각 애플리케이션 팀은 자체 패키지를 다운로드, 게시 및 액세스 권한을 부여하기 위한 전체 액세스 권한이 필요합니다. 애플리케이션 팀이 사용하는 일부 공통 라이브러리 패키지도 전체 조직과 공유해야 합니다.


어떤 단계 조합이 이러한 요구 사항을 최소한의 관리 오버헤드로 충족할 수 있을까요? (세 가지를 선택하세요.)

A. 각 애플리케이션 팀의 계정에 도메인을 만듭니다. 각 애플리케이션 팀의 계정에 애플리케이션 팀의 도메인에 대한 전체 읽기 액세스 및 쓰기 액세스 권한을 부여합니다.
B. 공유 서비스 계정에서 도메인을 만듭니다. 조직에 읽기 액세스 권한과 CreateRepository 액세스 권한을 부여합니다. 가장 많이 투표된
C. 각 애플리케이션 팀의 계정에 저장소를 만듭니다. 각 애플리케이션 팀의 계정에 자체 저장소에 대한 전체 읽기 액세스 및 쓰기 액세스 권한을 부여합니다. 가장 많이 투표된
D. 공유 서비스 계정에서 리포지토리를 만듭니다. 조직에 공유 서비스 계정의 리포지토리에 대한 읽기 액세스 권한을 부여합니다. 각 애플리케이션 팀의 리포지토리에서 리포지토리를 업스트림 리포지토리로 설정합니다. 가장 많이 투표된
E. 공유 패키지가 필요한 팀의 경우 다른 애플리케이션 팀의 계정에서 저장소에 대한 읽기 액세스를 허용하는 리소스 기반 정책을 만듭니다.
F. 다른 애플리케이션 팀의 저장소를 업스트림 저장소로 설정합니다.



### 질문 #263주제 1
한 회사가 Amazon EC2 인스턴스에 애플리케이션을 배포합니다. 이 애플리케이션은 Amazon Linux 2를 실행하고 AWS CodeDeploy를 사용합니다. 이 애플리케이션은 코드 저장소에 대해 다음과 같은 파일 구조를 갖습니다.



appspec.yml 파일의 파일 섹션에는 다음과 같은 내용이 있습니다.



config.txt 파일을 배포하면 어떤 결과가 나올까요?

A. config.txt 파일은 /var/www/html/config/config.txt에만 배포됩니다.
B. config.txt 파일은 /usr/local/src/config.txt와 /var/www/html/config/config.txt에 배포됩니다. 가장 많이 투표된
C. config.txt 파일은 /usr/local/src/config.txt에만 배포됩니다.
D. config.txt 파일은 /usr/local/src/config.txt와 /var/www/html/application/web/config.txt에 배포됩니다.



### 질문 #264주제 1
한 회사가 퍼블릭 업스트림 리포지토리와 함께 AWS CodeArtifact 리포지토리를 설정했습니다. 회사의 개발팀은 회사 내부 네트워크의 리포지토리에서 오픈 소스 종속성을 사용합니다. 회사의

보안팀은 최근 개발팀이 사용하는 패키지의 최신 버전에서 심각한 취약성을 발견했습니다. 보안팀은 취약성을 수정하기 위해 패치 버전을 만들었습니다. 회사는 취약한 버전이 다운로드되는 것을 방지해야 합니다. 또한 회사는 보안팀이 패치 버전을 게시할 수 있도록 허용해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. 영향을 받는 CodeArtifact 패키지 버전의 상태를 '목록 없음'으로 업데이트합니다.
B. 영향을 받은 CodeArtifact 패키지 버전의 상태를 삭제됨으로 업데이트합니다.
C. 영향을 받은 CodeArtifact 패키지 버전의 상태를 보관됨으로 업데이트합니다. 가장 많이 투표된
D. CodeArtifact 패키지 원본 제어 설정을 업데이트하여 직접 게시를 허용하고 업스트림 작업을 차단합니다. 가장 많이 투표된
E. CodeArtifact 패키지 원본 제어 설정을 업데이트하여 직접 게시를 차단하고 업스트림 작업을 허용합니다.



### 
비디(35%)

질문 #265주제 1
한 회사에서 레코드를 처리하는 맞춤형 애플리케이션을 실행하고 있습니다. 모든 구성 요소는 Auto Scaling 그룹에서 실행되는 Amazon EC2 인스턴스에서 실행됩니다. 각 레코드의 처리 과정은 컴퓨팅 집약적인 다단계 순차적 작업입니다. 각 단계는 항상 5분 이내에 완료됩니다.

현재 시스템의 한계는 단계가 실패하면 애플리케이션이 처음부터 레코드를 다시 처리해야 한다는 것입니다. 이 회사는 애플리케이션이 실패한 단계만 다시 처리하도록 아키텍처를 업데이트하려고 합니다.

이러한 요구 사항을 충족하는 가장 운영 효율적인 솔루션은 무엇입니까?

A. Amazon S3에 레코드를 쓸 웹 애플리케이션을 만듭니다. S3 Event Notifications를 사용하여 Amazon Simple Notification Service(Amazon SNS) 토픽에 게시합니다. EC2 인스턴스를 사용하여 Amazon SNS를 폴링하고 처리를 시작합니다. 중간 결과를 Amazon S3에 저장하여 다음 단계로 전달합니다.
B. 애플리케이션의 로직을 사용하여 처리 단계를 수행합니다. 애플리케이션 코드를 컨테이너에서 실행되도록 변환합니다. AWS Fargate를 사용하여 컨테이너 인스턴스를 관리합니다. 컨테이너가 자체를 호출하여 상태를 한 단계에서 다음 단계로 전달하도록 구성합니다.
C. Amazon Kinesis 데이터 스트림에 레코드를 전달하는 웹 애플리케이션을 만듭니다. Kinesis 데이터 스트림과 AWS Lambda 함수를 사용하여 처리를 분리합니다.
D. AWS Step Functions에 레코드를 전달하는 웹 애플리케이션을 만듭니다. 처리를 Step Functions 작업과 AWS Lambda 함수로 분리합니다. 가장 많이 투표된



### 질문 #266주제 1
한 회사가 온프레미스 Windows 애플리케이션과 Linux 애플리케이션을 AWS로 마이그레이션하고 있습니다. 이 회사는 자동화를 사용하여 Amazon EC2 인스턴스를 시작하여 온프레미스 구성을 미러링합니다. 마이그레이션된 애플리케이션은 Windows의 경우 SMB를 사용하고 Linux의 경우 NFS를 사용하는 공유 스토리지에 액세스해야 합니다.

이 회사는 또한 다른 AWS 리전에서 파일럿 라이트 재해 복구(DR) 환경을 만들고 있습니다. 이 회사는 자동화를 사용하여 DR 리전에서 EC2 인스턴스를 시작하고 구성합니다. 이 회사는 스토리지를 DR 리전에 복제해야 합니다.

어떤 스토리지 솔루션이 이러한 요구 사항을 충족할까요?

A. 애플리케이션 스토리지에 Amazon S3를 사용합니다. 기본 리전에 S3 버킷을 만들고 DR 리전에 S3 버킷을 만듭니다. 기본 리전에서 DR 리전으로 S3 크로스 리전 복제(CRR)를 구성합니다.
B. 애플리케이션 스토리지에 Amazon Elastic Block Store(Amazon EBS)를 사용합니다. AWS Backup에서 기본 리전에 있는 EBS 볼륨의 스냅샷을 생성하고 스냅샷을 DR 리전에 복제하는 백업 계획을 만듭니다.
C. 애플리케이션 스토리지를 위해 AWS Storage Gateway에서 Volume Gateway를 사용합니다. 기본 지역에서 DR 지역으로 Volume Gateway의 Cross-Region Replication(CRR)을 구성합니다.
D. 애플리케이션 스토리지에 Amazon FSx for NetApp ONTAP을 사용합니다. DR 지역에서 FSx for ONTAP 인스턴스를 만듭니다. 기본 지역에서 DR 지역으로 NetApp SnapMirror 복제를 구성합니다. 가장 많이 투표된



### 질문 #267주제 1
회사의 애플리케이션은 Amazon EC2 On-Demand 인스턴스의 플릿을 사용하여 데이터를 분석하고 처리합니다. EC2 인스턴스는 자동 확장 그룹에 있습니다. 자동 확장 그룹은 애플리케이션 로드 밸런서(ALB)의 대상 그룹입니다. 애플리케이션은 중단을 허용할 수 없는 중요한 데이터를 분석합니다. 또한 애플리케이션은 중단을 견딜 수 있는 비중요한 데이터를 분석합니다.

중요한 데이터 분석에는 실시간 애플리케이션 수요에 대응하여 빠른 확장성이 필요합니다. 비중요한 데이터 분석에는 메모리 소비가 포함됩니다. DevOps 엔지니어는 중요한 데이터의 확장 대기 시간을 줄이는 솔루션을 구현해야 합니다. 솔루션은 또한 비중요한 데이터를 처리해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (두 가지를 선택하십시오.)

A. 중요 데이터의 경우 기존 Auto Scaling 그룹을 수정합니다. 중지된 상태에서 웜 풀 인스턴스를 만듭니다. 웜 풀 크기를 정의합니다. 자세한 모니터링이 활성화된 새 버전의 시작 템플릿을 만듭니다. 스팟 인스턴스를 사용합니다.
B. 중요 데이터의 경우 기존 자동 확장 그룹을 수정합니다. 중지된 상태에서 웜 풀 인스턴스를 만듭니다. 웜 풀 크기를 정의합니다. 자세한 모니터링이 활성화된 새 버전의 시작 템플릿을 만듭니다. 온디맨드 인스턴스를 사용합니다. 가장 많이 투표된
C. 중요 데이터의 경우 기존 자동 확장 그룹을 수정합니다. 부트스트랩 스크립트가 성공적으로 완료되도록 라이프사이클 후크를 만듭니다. 인스턴스가 등록되기 전에 인스턴스의 애플리케이션이 트래픽을 허용할 준비가 되었는지 확인합니다. 자세한 모니터링이 활성화된 새 버전의 시작 템플릿을 만듭니다.
D. 비중요 데이터의 경우, 시작 템플릿을 사용하는 두 번째 자동 확장 그룹을 만듭니다. 시작 템플릿을 구성하여 통합 Amazon CloudWatch 에이전트를 설치하고 사용자 지정 메모리 사용률 메트릭으로 CloudWatch 에이전트를 구성합니다. 스팟 인스턴스를 사용합니다. 새 자동 확장 그룹을 ALB의 대상 그룹으로 추가합니다. 애플리케이션을 수정하여 중요 데이터와 비중요 데이터에 대해 두 개의 대상 그룹을 사용합니다. 가장 많이 투표된
E. 비중요 데이터의 경우 두 번째 자동 확장 그룹을 만듭니다. 대상 추적 확장 정책에 대해 미리 정의된 메모리 사용률 메트릭 유형을 선택합니다. 스팟 인스턴스를 사용합니다. ALB의 대상 그룹으로 새 자동 확장 그룹을 추가합니다. 중요 데이터와 비중요 데이터에 대해 두 개의 대상 그룹을 사용하도록 애플리케이션을 수정합니다.



### 질문 #268주제 1
한 회사가 최근 Amazon EC2 인스턴스를 사용하는 Amazon Elastic Kubernetes Service(Amazon EKS) 클러스터로 애플리케이션을 마이그레이션했습니다. 이 회사는 CPU 사용률에 따라 자동으로 확장되도록 애플리케이션을 구성했습니다.

이 애플리케이션은 부하가 많을 때 메모리 오류를 생성합니다. 또한 애플리케이션은 증가된 부하를 처리할 만큼 충분히 확장되지 않습니다. 이 회사는 시간이 지남에 따라 애플리케이션의 메모리 메트릭을 수집하고 분석해야 합니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. CloudWatchAgentServerPolicy 관리형 IAM 정책을 클러스터가 사용하는 IAM 인스턴스 프로필에 연결합니다. 가장 많이 투표된
B. CloudWatchAgentServerPolicy 관리형 IAM 정책을 클러스터의 서비스 계정 역할에 연결합니다.
C. 클러스터의 기존 EC2 인스턴스에 통합 Amazon CloudWatch 에이전트를 배포하여 성능 지표를 수집합니다. 클러스터에 추가된 모든 새 EC2 인스턴스에 대해 AMI에 에이전트를 추가합니다. 가장 많이 투표된
D. AWS Distro for OpenTelemetry 수집기를 DaemonSet으로 배포하여 성능 로그를 수집합니다.
E. Service 차원을 사용하여 ContainerInsights 네임스페이스의 pod_memory_utilization Amazon CloudWatch 메트릭을 분석합니다. 가장 많이 투표된
F. ClusterName 차원을 사용하여 ContainerInsights 네임스페이스의 node_memory_utilization Amazon CloudWatch 메트릭을 분석합니다.



### 질문 #269주제 1
회사의 비디오 스트리밍 플랫폼 사용량이 여러 국가에서 매일 10,000명에서 매일 50,000명으로 증가했습니다. 이 회사는 Amazon Elastic Kubernetes Service(Amazon EKS)에 스트리밍 플랫폼을 배포합니다. EKS 워크로드는 최대 시청 시간 동안 수천 개의 노드로 확장됩니다.

이 회사의 사용자는 무단 로그인 발생을 보고합니다. 사용자는 또한 플랫폼에서 갑작스러운 중단 및 로그아웃을 보고합니다.

이 회사는 전체 플랫폼에 대한 추가 보안 조치를 원합니다. 이 회사는 또한 회사의 전체 AWS 환경에서 리소스 동작 및 상호 작용에 대한 요약된 보기가 필요합니다. 요약된 보기에는 로그인 시도, API 호출 및 네트워크 트래픽이 표시되어야 합니다. 이 솔루션은 로그 관리 오버헤드를 최소화하면서 네트워크 트래픽 분석을 허용해야 합니다. 이 솔루션은 또한 EKS 워크로드와 관련된 잠재적인 악의적 동작을 신속하게 조사해야 합니다.

이러한 요구 사항을 충족하는 솔루션은 무엇입니까?

A. EKS 감사 로그 모니터링을 위해 Amazon GuardDuty를 활성화합니다. AWS CloudTrail 로그를 활성화합니다. EKS 감사 로그와 CloudTrail 로그 파일을 Amazon S3 버킷에 저장합니다. Amazon Athena를 사용하여 외부 테이블을 만듭니다. Amazon QuickSight를 사용하여 대시보드를 만듭니다.
B. EKS 감사 로그 모니터링을 위해 Amazon GuardDuty를 활성화합니다. 회사의 AWS 계정에서 Amazon Detective를 활성화합니다. Detective에서 선택적 소스 패키지의 EKS 감사 로그를 활성화합니다. 가장 많이 투표된
C. Amazon CloudWatch Container Insights를 활성화합니다. AWS CloudTrail 로그를 활성화합니다. EKS 감사 로그와 CloudTrail 로그 파일을 Amazon S3 버킷에 저장합니다. Amazon Athena를 사용하여 외부 테이블을 만듭니다. Amazon QuickSight를 사용하여 대시보드를 만듭니다.
D. EKS 감사 로그 모니터링을 위해 Amazon GuardDuty를 활성화합니다. Amazon CloudWatch Container Insights 및 VPC Flow Logs를 활성화합니다. AWS CloudTrail 로그를 활성화합니다.



### 질문 #270주제 1
한 회사가 AWS Organizations를 사용하여 수백 개의 AWS 계정을 관리합니다. 이 회사에는 AWS Identity and Access Management(IAM)를 담당하는 팀이 있습니다.

IAM 팀은 AWS IAM Identity Center(AWS Single Sign-On)를 구현하려고 합니다. IAM 팀은 IAM Identity Center를 관리하는 데 필요한 최소한의 권한만 있어야 합니다. IAM 팀은 Organizations 관리 계정에 대한 불필요한 액세스 권한을 얻을 수 없어야 합니다. IAM 팀은 기존 및 새 멤버 계정에 대한 새 IAM Identity Center 권한 집합과 할당을 프로비저닝할 수 있어야 합니다.

이러한 요구 사항을 충족하는 단계 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. IAM 팀을 위한 새 AWS 계정을 만듭니다. 새 계정에서 IAM Identity Center를 활성화합니다. Organizations 관리 계정에서 새 계정을 IAM Identity Center의 위임된 관리자로 등록합니다. 가장 많이 투표된
B. IAM 팀을 위한 새 AWS 계정을 만듭니다. Organizations 관리 계정에서 IAM Identity Center를 활성화합니다. Organizations 관리 계정에서 새 계정을 IAM Identity Center의 위임된 관리자로 등록합니다.
C. IAM Identity Center에서 IAM 팀의 사용자와 그룹을 만듭니다. 사용자를 그룹에 추가합니다. 새 권한 집합을 만듭니다. AWSSSODirectoryAdministrator 관리형 IAM 정책을 그룹에 연결합니다.
D. IAM Identity Center에서 IAM 팀의 사용자와 그룹을 만듭니다. 사용자를 그룹에 추가합니다. 새 권한 집합을 만듭니다. AWSSSOMemberAccountAdministrator 관리형 IAM 정책을 그룹에 연결합니다. 가장 많이 투표된
E. 조직 관리 계정에 권한 집합을 할당합니다. IAM 팀 그룹이 권한 집합을 사용하도록 허용합니다.
F. 새로운 AWS 계정에 권한 집합을 할당합니다. IAM 팀 그룹이 권한 집합을 사용하도록 허용합니다. 가장 많이 투표된



### 질문 #271주제 1
한 회사가 모든 기능이 활성화된 AWS Organizations의 조직을 사용합니다. 이 회사는 기본 계정에서 AWS Backup을 사용하고 AWS Key Management Service(AWS KMS) 키를 사용하여 백업을 암호화합니다.

이 회사는 AWS Backup이 기본 계정에서 백업하는 리소스의 교차 계정 백업을 자동화해야 합니다. 이 회사는 Organizations 관리 계정에서 교차 계정 백업을 구성합니다. 이 회사는 조직에 새 AWS 계정을 만들고 새 계정에 AWS Backup 백업 볼트를 구성합니다. 이 회사는 새 계정에 KMS 키를 만들어 백업을 암호화합니다. 마지막으로 이 회사는 기본 계정에서 새 백업 계획을 구성합니다. 새 백업 계획의 대상은 새 계정의 백업 볼트입니다.

기본 계정에서 AWS Backup 작업이 호출되면 해당 작업이 기본 계정에 백업을 만듭니다. 그러나 백업은 새 계정의 백업 볼트에 복사되지 않습니다.

백업을 새 계정의 백업 볼트에 복사할 수 있도록 이 회사는 어떤 단계 조합을 수행해야 합니까? (두 가지를 선택하세요.)

A. 새 계정의 백업 볼트 액세스 정책을 편집하여 기본 계정에 대한 액세스를 허용합니다. 가장 많이 투표된
B. 기본 계정의 백업 볼트 액세스 정책을 편집하여 새 계정에 대한 액세스를 허용합니다.
C. 기본 계정의 백업 볼트 액세스 정책을 편집하여 새 계정에서 KMS 키에 대한 액세스를 허용합니다.
D. 기본 계정의 KMS 키에 대한 키 정책을 편집하여 새 계정과 키를 공유합니다. 가장 많이 투표된
E. 새 계정의 KMS 키에 대한 키 정책을 편집하여 기본 계정과 키를 공유합니다.



### 질문 #272주제 1
한 회사가 Amazon S3 버킷을 사용하여 이미지를 저장하는 애플리케이션을 실행합니다. DevOps 엔지니어는 S3 버킷에 저장된 객체에 대한 다중 지역 전략을 구현해야 합니다. 회사는 다른 AWS 지역의 S3 버킷으로 장애 조치할 수 있어야 합니다. 이미지가 두 S3 버킷 중 하나에 추가되면 15분 이내에 다른 S3 버킷으로 이미지를 복제해야 합니다.

DevOps 엔지니어는 S3 버킷 간에 양방향 복제를 활성화합니다.

DevOps 엔지니어는 요구 사항을 충족하기 위해 다음에 어떤 단계 조합을 수행해야 합니까? (세 가지를 선택하십시오.)

A. 각 복제 규칙에서 S3 복제 시간 제어(S3 RTC)를 활성화합니다. 가장 많이 투표된
B. 액티브-패시브 구성으로 S3 다중 지역 액세스 포인트를 생성합니다. 가장 많이 투표된
C. 회사에서 다른 지역의 S3 버킷으로 장애 조치(failover)해야 하는 경우 AWS API에서 SubmitMultiRegionAccessPointRoutes 작업을 호출합니다. 가장 많이 투표된
D. 두 S3 버킷 모두에서 S3 전송 가속을 활성화합니다.
E. Amazon Route 53 Recovery Controller에서 라우팅 제어를 구성합니다. 액티브-패시브 구성으로 S3 버킷을 추가합니다.
F. 회사에서 다른 지역의 S3 버킷으로 장애 조치(failover)해야 하는 경우 AWS API에서 UpdateRoutingControlStates 작업을 호출합니다.



### 질문 #273주제 1
한 회사에서 AWS Cloud Development Kit(AWS CDK)를 사용하여 애플리케이션을 정의합니다. 이 회사는 AWS CodePipeline과 AWS CodeBuild로 구성된 파이프라인을 사용하여 CDK 애플리케이션을 배포합니다.

이 회사는 다양한 인프라 구성 요소를 테스트하기 위해 파이프라인에 단위 테스트를 도입하려고 합니다. 이 회사는 단위 테스트에서 실패가 발생하지 않으면 배포가 진행되도록 하려고 합니다.

파이프라인에서 테스트 요구 사항을 강제할 단계 조합은 무엇입니까? (두 가지를 선택하세요.)

A. CodeBuild 빌드 단계 명령을 업데이트하여 테스트를 실행한 다음 애플리케이션을 배포합니다. OnFailure 단계 속성을 ABORT로 설정합니다. 가장 많이 투표된
B. CodeBuild 빌드 단계 명령을 업데이트하여 테스트를 실행한 다음 애플리케이션을 배포합니다. cdk deploy 명령에 --rollback true 플래그를 추가합니다.
C. CodeBuild 빌드 단계 명령을 업데이트하여 테스트를 실행한 다음 애플리케이션을 배포합니다. cdk deploy 명령에 --require-approval any-change 플래그를 추가합니다.
D. AWS CDK 어설션 모듈을 사용하는 테스트를 만듭니다. template.hasResourceProperties 어설션을 사용하여 리소스에 예상 속성이 있는지 테스트합니다. 가장 많이 투표된
E. cdk diff 명령을 사용하는 테스트를 만듭니다. 리소스가 변경되면 테스트가 실패하도록 구성합니다.


### 질문 #274주제 1
한 회사에는 애플리케이션 로드 밸런서(ALB) 뒤의 Amazon EC2 인스턴스에서 실행되는 애플리케이션이 있습니다. EC2 인스턴스는 여러 가용 영역에 있습니다. 애플리케이션이 단일 가용 영역에서 잘못 구성되어 애플리케이션이 부분적으로 중단되었습니다.

DevOps 엔지니어는 한 가용 영역의 비정상 EC2 인스턴스가 다른 가용 영역의 정상 EC2 인스턴스에 영향을 미치지 않도록 변경했습니다. DevOps 엔지니어는 애플리케이션의 장애 조치를 테스트하고 ALB가 트래픽을 보내는 위치를 변경해야 합니다. 장애 조치 중에 ALB는 장애가 발생한 가용 영역으로 트래픽을 보내지 않아야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. ALB에서 크로스 존 로드 밸런싱을 끕니다. Amazon Route 53 Application Recovery Controller를 사용하여 가용성 영역에서 벗어나 존 이동을 시작합니다. 가장 많이 투표된
B. ALB의 대상 그룹에서 크로스 존 로드 밸런싱을 끕니다. Amazon Route 53 Application Recovery Controller를 사용하여 가용성 영역에서 벗어나 존 이동을 시작합니다.
C. ALB의 DNS 호스트 이름을 사용하는 Amazon Route 53 Application Recovery Controller 리소스 세트를 만듭니다. 가용성 영역에서 리소스 세트에 대한 영역 이동을 시작합니다.
D. ALB 대상 그룹의 ARN을 사용하는 Amazon Route 53 Application Recovery Controller 리소스 세트를 만듭니다. ElbV2TargetGroupsCanServeTraffic 규칙을 사용하는 준비 상태 확인을 만듭니다.



### 질문 #275주제 1
한 회사가 AWS 네트워크 방화벽 플로우 로그를 Amazon S3 버킷으로 보냅니다. 그런 다음 회사는 Amazon Athena를 사용하여 플로우 로그를 분석합니다. 회사는

플로우 로그를 변환하고 추가 데이터를 추가한 후에 플로우 로그를 기존 S3 버킷에 전달해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. AWS Lambda 함수를 만들어 데이터를 변환하고 기존 S3 버킷에 새 객체를 씁니다. 기존 S3 버킷에 대한 S3 트리거로 Lambda 함수를 구성합니다. 이벤트 유형에 대한 모든 객체 생성 이벤트를 지정합니다. 재귀적 호출을 확인합니다.
B. 기존 S3 버킷에서 Amazon EventBridge 알림을 활성화합니다. 사용자 지정 EventBridge 이벤트 버스를 만듭니다. 사용자 지정 이벤트 버스와 연결된 EventBridge 규칙을 만듭니다. 기존 S3 버킷의 모든 객체 생성 이벤트에 반응하고 AWS Step Functions 워크플로를 호출하도록 규칙을 구성합니다. 데이터를 변환하고 새 S3 버킷에 데이터를 쓰도록 Step Functions 작업을 구성합니다.
C. 기본 EventBridge 이벤트 버스와 연결된 Amazon EventBridge 규칙을 만듭니다. 기존 S3 버킷에 대한 모든 객체 생성 이벤트에 반응하도록 규칙을 구성합니다. 규칙의 대상으로 새 S3 버킷을 정의합니다. 이벤트를 규칙 대상으로 전달하기 전에 이벤트를 사용자 지정하기 위해 EventBridge 입력 변환을 만듭니다.
D. AWS Lambda 변환기로 구성된 Amazon Kinesis Data Firehose 전송 스트림을 만듭니다. 기존 S3 버킷을 대상으로 지정합니다. 네트워크 방화벽 로깅 대상을 Amazon S3에서 Kinesis Data Firehose로 변경합니다. 가장 많이 투표된



### 질문 #276주제 1
DevOps 엔지니어는 Amazon Elastic Container Service(Amazon ECS) 서비스에 대한 기존 AWS CodePipeline CI/CD 워크플로에 통합 테스트를 구현해야 합니다. CI/CD 워크플로는 AWS CodeCommit 리포지토리에서 새 애플리케이션 코드를 검색하고 컨테이너 이미지를 빌드합니다. 그런 다음 Cl/CD 워크플로는 컨테이너 이미지를 새 이미지 태그 버전과 함께 Amazon Elastic Container Registry(Amazon ECR)에 업로드합니다.

통합 테스트는 새 버전의 서비스 엔드포인트에 도달할 수 있고 다양한 API 메서드가 성공적인 응답 데이터를 반환하는지 확인해야 합니다. DevOps 엔지니어는 이미 서비스를 테스트하기 위해 ECS 클러스터를 만들었습니다.

어떤 단계 조합이 이러한 요구 사항을 가장 적은 관리 오버헤드로 충족할 수 있을까요? (세 가지를 선택하세요.)

A. 파이프라인에 배포 단계를 추가합니다. Amazon ECS를 작업 공급자로 구성합니다. 가장 많이 투표된
B. 파이프라인에 배포 단계를 추가합니다. AWS CodeDeploy를 작업 공급자로 구성합니다.
C. CodeCommit 저장소에 appspec.yml 파일을 추가합니다.
D. 이미지 빌드 파이프라인 단계를 업데이트하여 새 이미지 태그를 참조하는 imagedefinitions.json 파일을 출력합니다. 가장 많이 투표된
E. 서비스에 대한 연결 확인 및 API 호출을 실행하는 AWS Lambda 함수를 만듭니다. Lambda 액션 단계를 사용하여 Lambda 함수를 CodePipeline과 통합합니다. 가장 많이 투표된
F. 서비스에 대한 통합 테스트를 실행하는 스크립트를 작성합니다. 스크립트를 Amazon S3 버킷에 업로드합니다. S3 작업 단계를 사용하여 S3 버킷의 스크립트를 CodePipeline과 통합합니다.



### 질문 #277주제 1
한 회사가 Windows 및 Linux Amazon EC2 인스턴스에서 애플리케이션을 실행합니다. 인스턴스는 AWS 지역의 여러 가용성 영역에서 실행됩니다. 이 회사는 각 애플리케이션에 대해 Auto Scaling 그룹을 사용합니다.

이 회사는 인스턴스에 대한 내구성 있는 스토리지 솔루션이 필요합니다. 이 솔루션은 Windows의 경우 SMB를 사용하고 Linux의 경우 NFS를 사용해야 합니다. 이 솔루션은 또한 밀리초 미만의 지연 시간을 가져야 합니다. 모든 인스턴스는 데이터를 읽고 씁니다.

이러한 요구 사항을 충족하는 단계의 조합은 무엇입니까? (세 가지를 선택하십시오.)

A. 여러 가용 영역에 대상이 있는 Amazon Elastic File System(Amazon EFS) 파일 시스템을 만듭니다.
B. Amazon FSx for NetApp ONTAP Multi-AZ 파일 시스템을 만듭니다. 가장 많이 투표된
C. 공유 스토리지로 사용할 범용 SSD(gp3) Amazon Elastic Block Store(Amazon EBS) 볼륨을 생성합니다.
D. 각 애플리케이션의 실행 템플릿에 대한 사용자 데이터를 업데이트하여 파일 시스템을 마운트합니다. 가장 많이 투표된
E. 각 자동 크기 조정 그룹에서 인스턴스 새로 고침을 수행합니다. 가장 많이 투표된
F. 새 인스턴스가 시작될 때 파일 시스템을 마운트하도록 각 애플리케이션의 EC2 인스턴스를 업데이트합니다.



### 질문 #278주제 1
한 회사에서 보안 팀과 DevOps 팀이 관리하는 AWS Organizations의 조직을 사용합니다. 두 팀 모두 AWS IAM Identity Center를 사용하여 계정에 액세스합니다.

각 팀에 대한 전담 그룹이 생성되었습니다. DevOps 팀의 그룹에는 DevOps라는 권한 집합이 할당되었습니다. 권한 집합에는 AdministratorAccess 관리형 IAM 정책이 첨부되었습니다. 권한 집합은 조직의 모든 계정에 적용되었습니다.

보안 팀은 DevOps 팀이 조직의 관리 계정에서 IAM Identity Center에 액세스할 수 없도록 하려고 합니다. 보안 팀은 다음 SCP를 조직 루트에 첨부했습니다.



정책을 구현한 후 보안 팀은 DevOps 팀이 여전히 IAM Identity Center에 액세스할 수 있음을 발견했습니다.

어떤 솔루션이 문제를 해결할까요?

A. 조직의 관리 계정에서 새 OU를 만듭니다. 조직의 관리 계정을 새 OU로 이동합니다. 조직 루트에서 SCP를 분리합니다. SCP를 새 OU에 연결합니다.
B. 조직의 관리 계정에서 SCP 조건 참조를 DevOps 팀의 그룹 역할의 ARN으로 업데이트하여 조직의 관리 계정의 AWS 계정 ID를 포함합니다.
C. IAM Identity Center에서 새 권한 집합을 만듭니다. 할당된 정책에 전체 액세스 권한이 있지만 sso:* 작업과 sso-directory:* 작업에 대한 권한을 명시적으로 거부하는지 확인합니다. 조직의 관리 계정에서 DevOps 팀의 그룹 역할에 대한 할당된 권한 집합을 업데이트합니다. SCP를 삭제합니다.
D. IAM Identity Center에서 DevOps 권한 집합을 업데이트합니다. 할당된 정책에 전체 액세스 권한이 있지만 sso:* 작업과 sso-directory:* 작업에 대한 권한을 명시적으로 거부하는지 확인합니다. Deny 문에서 aws:SourceAccount 글로벌 조건 컨텍스트 키를 조직의 관리 계정 IDelete와 비교하는 StringEquals 조건을 추가합니다. SCP를 삭제합니다. 가장 많이 투표된



### 질문 #279주제 1
Amazon EC2 Auto Scaling 그룹은 AMI에서 생성된 EC2 인스턴스를 관리합니다. AMI에는 AWS Systems Manager Agent가 설치되어 있습니다. EC2 인스턴스가 Auto Scaling 그룹에서 시작되면 태그가 EC2 인스턴스에 적용됩니다.

Auto Scaling 그룹에서 시작하는 EC2 인스턴스는 올바른 운영 체제 구성을 가져야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 원하는 인스턴스 구성을 구성하는 Systems Manager Run Command 문서를 만듭니다. EC2 인스턴스가 최신 패치를 준수하지 않을 때 Run Command 문서를 호출하도록 Systems Manager Compliance를 설정합니다.
B. Systems Manager 명령 문서에 연결되는 Systems Manager State Manager 연결을 만듭니다. 즉시 실행되는 태그 쿼리를 만듭니다. 가장 많이 투표된
C. 원하는 인스턴스 구성을 지정하는 Systems Manager Run Command 작업을 만듭니다. Systems Manager Maintenance Windows에서 매일 실행되는 유지 관리 창을 만듭니다. Run Command 작업을 유지 관리 창에 등록합니다. 대상을 지정합니다.
D. Systems Manager Patch Manager 패치 기준선과 Auto Scaling 그룹이 적용하는 것과 동일한 태그를 사용하는 패치 그룹을 만듭니다. 패치 그룹을 패치 기준선에 등록합니다. 인스턴스를 패치하기 위한 Systems Manager 명령 문서를 정의합니다. Systems Manager Run Command를 사용하여 문서를 호출합니다.



### 질문 #280주제 1
한 회사에서 AWS Organizations를 사용하여 AWS 계정을 관리합니다. 조직 루트에는 Department라는 자식 OU가 있습니다. Department OU에는 Engineering이라는 자식 OU가 있습니다. 기본 FullAWSAccess 정책은 루트, Department OU 및 Engineering OU에 연결됩니다.

이 회사는 Engineering OU에 많은 AWS 계정을 가지고 있습니다. 각 계정에는 AdministratorAccess IAM 정책이 연결된 관리 IAM 역할이 있습니다. 기본 FullAWSAccessPolicy도 각 계정에 연결됩니다.

DevOps 엔지니어는 Department OU에서 FullAWSAccess 정책을 제거할 계획입니다. DevOps 엔지니어는 모든 Amazon EC2 API 작업에 대한 Allow 문이 포함된 정책으로 정책을 대체합니다.

이 변경으로 인해 관리 1AM 역할의 권한은 어떻게 됩니까?

A. 모든 리소스에 대한 모든 API 작업이 허용됩니다.
B. EC2 리소스에 대한 모든 API 작업이 허용됩니다. 다른 모든 API 작업은 거부됩니다. 가장 많이 투표된
C. 모든 리소스에 대한 모든 API 작업이 거부됩니다.
D. EC2 리소스에 대한 모든 API 작업은 거부됩니다. 다른 모든 API 작업은 허용됩니다.



### 질문 #281주제 1
한 회사가 AWS Organizations에서 AWS 계정을 관리합니다. 이 회사는 전용 AWS 계정의 Amazon S3 버킷으로 Amazon CloudWatch Logs 데이터를 보내는 솔루션이 필요합니다. 이 솔루션은 모든 기존 및 미래 CloudWatch Logs 로그 그룹을 지원해야 합니다.

어떤 솔루션이 이러한 요구 사항을 충족할까요?

A. 조직 백업 정책을 활성화하여 모든 로그 그룹을 전용 S3 버킷에 백업합니다. 회사에 속한 모든 계정에서 액세스할 수 있는 S3 버킷 정책을 추가합니다.
B. AWS Backup에서 백업 계획을 만듭니다. 전용 S3 버킷을 백업 볼트로 지정합니다. 모든 CloudWatch Logs 로그 그룹 리소스를 백업 계획에 할당합니다. 회사에 속한 모든 계정에 대한 백업 계획에서 리소스 할당을 만듭니다.
C. AWS Backup에서 백업 계획을 만듭니다. 전용 S3 버킷을 백업 볼트로 지정합니다. 모든 기존 로그 그룹을 백업 계획에 할당합니다. 회사에 속한 모든 계정에 대한 백업 계획에서 리소스 할당을 만듭니다. AWS Systems Manager Automation 런북을 만들어 로그 그룹을 백업 계획에 할당합니다. 모든 비준수 로그 그룹에 대한 자동 수정 작업이 있는 AWS Config 규칙을 만듭니다. 런북을 규칙의 대상으로 지정합니다.
D. 전용 AWS 계정에서 CloudWatch Logs 대상과 Amazon Kinesis Data Firehose 전송 스트림을 만듭니다. 전송 스트림의 대상으로 S3 버킷을 지정합니다. 모든 계정의 모든 기존 로그 그룹에 대한 구독 필터를 만듭니다. CloudWatch Logs PutSubscriptionFilter API 작업을 호출하는 AWS Lambda 함수를 만듭니다. CreateLogGroup 이벤트가 발생할 때 Lambda 함수를 호출하는 Amazon EventBridge 규칙을 만듭니다. 가장 많이 투표된


