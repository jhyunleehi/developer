## 1. AWS 핵심 서비스 이해
1) 컴퓨팅
* EC2: 다양한 인스턴스 유형, Auto Scaling, ELB(Elastic Load Balancer) 설정.
* AWS Lambda: 서버리스 컴퓨팅. Lambda를 통한 자동 확장 및 이벤트 기반 아키텍처 구현.
* Elastic Beanstalk: 애플리케이션을 쉽게 배포하고 관리할 수 있는 플랫폼.
2) 스토리지
* S3: 객체 스토리지. 버킷 정책, 퍼블릭 액세스 설정, 버전 관리.
* EFS (Elastic File System): 파일 기반 스토리지로 EC2와 연동.
* Amazon RDS: 관계형 데이터베이스 관리 (MySQL, PostgreSQL 등).
3) 데이터베이스
* DynamoDB: 서버리스 NoSQL 데이터베이스. 파티셔닝, 프로비저닝된 처리량 관리.
* Amazon RDS: 관계형 데이터베이스 서비스. Aurora와 같은 고성능 옵션.
4) API 및 컨테이너
* API Gateway: RESTful API 생성 및 관리.
* ECS/EKS: 컨테이너 오케스트레이션 도구로 애플리케이션 배포 및 관리.

## 2. 애플리케이션 개발 및 배포
1) CI/CD
* CodeBuild: 빌드 및 테스트 자동화.
* CodeDeploy: 애플리케이션 배포 자동화.
* CodePipeline: 전체 CI/CD 파이프라인을 자동화.
2) 서버리스 애플리케이션 개발
* Lambda, API Gateway, DynamoDB를 사용한 서버리스 애플리케이션 구현.
3) 모니터링 및 로깅
* CloudWatch: 모니터링 및 로깅 서비스.
* AWS X-Ray: 분산 애플리케이션의 트랜잭션 추적 및 디버깅.

## 3. 보안 및 권한 관리
1) IAM (Identity and Access Management)
* 사용자, 그룹, 역할 및 정책을 설정하여 권한 관리.
* 정책 (Policy) 작성 및 JSON 문법 이해.
2) S3 보안
* 버킷 정책 및 ACL(Access Control List) 설정, 객체 암호화.
3) AWS KMS (Key Management Service)
* 데이터 암호화 및 키 관리.
4) AWS Cognito
* 사용자 인증 및 권한 관리.

## 4. 애플리케이션 트러블슈팅 및 최적화
1) 성능 최적화
* Auto Scaling: 트래픽 증가에 따른 EC2 인스턴스 자동 확장.
* Elastic Load Balancing (ELB): 트래픽을 여러 인스턴스로 분산.
* CloudFront: CDN을 이용한 콘텐츠 배포 최적화.
* ElastiCache: 캐싱으로 데이터베이스 성능 개선.
2) 비용 최적화
* 예약 인스턴스와 스팟 인스턴스를 활용해 EC2 비용 절감.
* S3 인텔리전트 티어링을 통한 비용 관리.
3) 트러블슈팅
* CloudWatch를 이용한 애플리케이션 모니터링.
* X-Ray를 통한 서버리스 및 마이크로서비스 애플리케이션 디버깅.