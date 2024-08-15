## REST Client

설명
클래스 생성자 (__init__): API 클라이언트의 기본 URL과 API 키를 설정합니다. 세션 객체를 생성하는 _create_session 메서드를 호출합니다.
* 세션 생성 메서드 (_create_session): 새로운 세션 객체를 생성하고, API 키가 있다면 헤더에 추가합니다.
* 클라이언트 재설정 메서드 (reset_client): 새로운 API 키를 설정하고, 세션 객체를 다시 생성합니다.
* GET 요청 메서드 (get): 지정된 엔드포인트로 GET 요청을 보냅니다. 요청이 성공하면 JSON 응답을 반환하고, 실패하면 에러 메시지를 출력합니다.

이 예제는 API 클라이언트를 재설정하고, 새로운 API 키로 요청을 다시 보낼 수 있는 기능을 포함하고 있습니다. 이를 통해 초기화 및 재설정 과정에서 발생할 수 있는 문제를 해결할 수 있습니다


```py
import requests
from requests.exceptions import RequestException

class APIClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.session = self._create_session()
    
    def _create_session(self):
        session = requests.Session()
        if self.api_key:
            session.headers.update({'Authorization': f'Bearer {self.api_key}'})
        return session
    
    def reset_client(self, new_api_key=None):
        self.api_key = new_api_key
        self.session = self._create_session()

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"An error occurred: {e}")
            return None

# Example usage
if __name__ == "__main__":
    client = APIClient(base_url="https://api.example.com", api_key="initial_api_key")
    
    # Making a request
    response = client.get("some/endpoint", params={"param1": "value1"})
    print(response)
    
    # Resetting the client with a new API key
    client.reset_client(new_api_key="new_api_key")
    
    # Making another request with the new API key
    response = client.get("some/endpoint", params={"param1": "value1"})
    print(response)

```