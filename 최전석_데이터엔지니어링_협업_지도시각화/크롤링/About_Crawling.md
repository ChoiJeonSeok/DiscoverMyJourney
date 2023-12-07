# 크롤링을 해보며 느낀점.

- 적절하게 데이터를 수집하는 수단인지 생각해봤다. 크롤링이라는 방법이 개발되었을 때 네이버 블로그 본문이나 수집하려고 개발하지는 않았을 것이다. 
- 웹 페이지에서 데이터를 수집하기 위해 개발되었는데, 왜 웹 페이지에서 데이터를 수집해야만 했는지에 대해 생각해봤다. 간단한 검색 끝에 크롤링이 없으면 안되는 경우를 알 수 있었다.
- 구글, 네이버, 다음, 빙 등 검색 엔진은 우리가 키워드를 검색하면 그 키워드에 대한 검색 결과를 내놓는다. 이때 그 결과는 어떠한 글이나 이미지같은 것이 아니라, 무수히 많은 링크들이다. 정확히는 하이퍼링크가 걸린 글의 제목이다.
- 그 수많은 웹 사이트들은 어떻게 검색엔진의 DB에 수집되었을까? 크롤링이 없었다면, 사이트를 일일이 수집하고 인덱싱하는데 아주 힘들었을 것이다.
- 검색엔진의 탄생에 크롤링이 아주 큰 기여를 한 셈이다.

## 오늘날의 크롤링
- 오늘날 크롤링은 검색 엔진뿐만 아니라 다양한 분야에서 활용되고 있다. 
- 데이터 수집과 분석 분야에 주로 사용되며 경우에 따라서는 학문 분야에도 사용된다고 한다.

## 크롤링의 윤리
- 크롤링은 분명히 유용한 도구이나 타인의 웹 사이트의 정보를 가져오기에 주의해야 할 점이 있다.

### 웹 사이트의 로봇 배제 표준 준수
- robots.txt 파일은 웹 사이트의 소유자가 크롤링 봇이 자신의 사이트를 크롤링하는 것을 허용하거나 제한하는 규칙을 정의한 파일이다. 크롤러는 이 파일을 확인하여 로봇 배제 규칙을 따라야 한다. 웹 사이트 소유자가 일부 페이지 또는 전체 페이지를 크롤링으로부터 제외하게끔 한다면 해당 페이지들은 크롤링 되어서는 안된다.
```
예시1 : 모든 크롤러들에 대해 전체 웹 사이트를 허용하는 경우
User-agent: *
Disallow:

예시2 : 모든 크롤러들에 대해 전체 웹 사이트를 차단하는 경우
User-agent: *
Disallow: /

예시 3 : 구글 봇에 대해 전체 웹 사이트를 허용하고, 다른 봇들에 대해 모든 접근을 차단하는 경우
User-agent: Googlebot
Disallow:

User-agent: *
Disallow: /
```
- User-agent: 
  - 크롤러 봇의 이름을 지정한다. 
  - 여러 개의 User-agent를 사용하여 다른 크롤러들에 대해 서로 다른 지침을 제공할 수 있다.
- Disallow: 
  - 해당 크롤러 봇이 접근할 수 없는 경로를 지정한다. 
  - 만약 루트 경로(/)를 Disallow로 지정하면 해당 크롤러는 웹 사이트의 모든 페이지에 접근할 수 없다. 
  - 만약 아무 경로도 제한하고 싶지 않다면 Disallow 값을 비워놓는다. 
  - 크롤러가 해당 파일을 발견하지 못하거나 지정된 User-agent가 없는 경우 모든 크롤러에 대해 기본 동작이 적용된다. 일반적으로 기본 동작은 모든 경로를 허용하는 것.

### 저작권
- 데이터를 사용하거나 배포할 때는 주의해야 한다. 
- 원작자의 허락을 구하지 않거나 저작권 법을 준수하지 않는 경우는 없어야 한다.

### 개인정보 보호
- 수집되는 데이터에 개인정보의 유무를 고려해야 한다. 
- 자칫하다가는 개인정보를 무단으로 수집하고 사용하게 된다. 
- 적절한 수집이었다고 할지라도 민감한 개인정보는 수집하지 않는 편이 좋으며, 수집하게 되었을 때는 익명화, 암호화 등 보안 조치를 취해야 한다.

### 서버 부하 최소화
- 크롤링은 해당 웹 사이트에 요청을 보낸 후 데이터를 수집한다. 따라서 웹 사이트들의 서버에 부하를 최소화하기 위해 적절한 딜레이나 제한을 설정해야 한다.
- 지나친 속도나 요청은 해당 웹 사이트의 서버를 공격하는게 될 수 있다.
- 서버를 공격하는 것으로 받아들여지면, 해당 웹 사이트로부터 IP가 차단당할 수 있다.


### 윤리적인 목적
- 법의 테두리 안에서, 해당 웹 사이트를 공격하지 않는 선에서 크롤링은 진행되어야 한다. 
- 사람이 직접 해당 웹 사이트를 방문하여 사용하는 수준이 적절하다.

예시 코드

```python
import requests
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

def is_allowed_by_robots_txt(url, user_agent):
    try:
        # URL에서 도메인 부분 추출
        domain = urljoin(url, '/')

        # robots.txt 파일 URL 생성
        robots_txt_url = urljoin(domain, 'robots.txt')

        # robots.txt 파일 가져오기
        response = requests.get(robots_txt_url)

        # 가져온 robots.txt 파일을 파싱하여 준수 여부 확인
        if response.status_code == 200:
            robot_parser = RobotFileParser()
            robot_parser.parse(response.text.splitlines())

            # 해당 크롤러 봇의 이름으로 설정한 user_agent에 대한 Disallow 지시사항 확인
            return robot_parser.can_fetch(user_agent, url)
        
        # robots.txt 파일이 없는 경우는 기본적으로 허용
        return True
    
    except Exception as e:
        print(f"Error checking robots.txt: {e}")
        return False

# 크롤링을 진행할 URL과 사용자 에이전트를 설정합니다.
url_to_crawl = "크롤링을 진행할 사이트의 주소"
user_agent = "지정하지 않으면 python-requests/x.x 등의 기본 user_agent 사용. 이때 x.x는 requests 라이브러리의 버전 번호."

# robots.txt를 준수하는지 확인
if is_allowed_by_robots_txt(url_to_crawl, user_agent):
    # 크롤링 코드를 작성합니다.
    # (robots.txt를 준수하는 경우에만 크롤링 코드를 실행합니다.)
    print("robots.txt를 준수하여 크롤링을 진행합니다.")
else:
    print("robots.txt를 준수하지 않아 크롤링이 차단되었습니다.")
```

1. 도메인 부분을 추출하는 이유 
   1. 크롤링을 진행할 URL에서 도메인 부분을 추출하는 이유는 robots.txt 파일을 가져오기 위함.
   2. robots.txt 파일은 웹 사이트의 루트 도메인에서만 확인할 수 있음.
   3. robots.txt 파일은 해당 도메인 아래의 모든 페이지 및 경로에 대한 크롤링 규칙을 담고 있음.
2. 추출 결과 예시
   1. 도메인 부분을 추출하면 해당 URL의 루트 도메인이 얻어지게 된다.
   2. `https://www.google.com/doodles` 에서 추출하면 `https://www.google.com/` 가 된다.
3. robots 파일 URL 생성
   1. URL의 도메인 부분과 robots.txt를 합치면 robots.txt 파일의 URL이 생성된다.
   2. urljoin() 함수를 사용하면 상대경로를 절대 경로로 변환할 수 있다. 
4. robots.txt 파일을 가져온다는 것의 의미.
   1. requests 라이브러리를 사용하여 생성된 robots.txt 파일의 URL에 GET 요청을 보내서 해당 파일의 내용을 가져오는 것을 의미함.
   2. 해당 웹 사이트의 크롤링 규칙을 확인할 수 있음.
5. robots.txt 파싱 후 준수 확인 과정
   1. urllib.robotparser 라이브러리로 robots.txt 파일을 파싱.
   2. 크롤러가 특정 User-Agent로 어떤 URL에 접근할 수 있는지 확인 가능.
   3. can_fetch() method로 특정 User-Agent와 URL이 허용되는지 여부를 확인할 수 있다.