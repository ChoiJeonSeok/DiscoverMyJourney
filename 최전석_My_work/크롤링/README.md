# 크롤링 시스템 사용 가이드

## 소개
- 이 문서는 네이버 API를 활용한 크롤링 시스템 사용 가이드입니다. 
- 이 시스템은 일반 크롤링과 병렬 크롤링, 두 가지 모드로 대량의 데이터를 효율적으로 수집할 수 있도록 설계되었습니다.

## 시퀀스 다이어그램
![크롤링 과정](https://github.com/ChoiJeonSeok/DiscoverMyJourney/assets/82266289/0140bb13-3977-4c37-9792-dec61773dd14)


## 설치 방법
크롤링 시스템을 사용하기 위해서는 Python 3.8 이상이 설치되어 있어야 하며, 필요한 라이브러리를 설치해야 합니다.
```
pip install -r requirements.txt
```

## 사용 방법
크롤링을 시작하기 전에 `NaverCrawling.py` 파일 내에 있는 `client_id`와 `client_secret`을 사용자의 네이버 API 키 정보로 업데이트해야 합니다.

### 일반 크롤링
단일 스레드를 사용하는 일반 크롤링 모드는 `NaverCrawling.py`를 통해 실행할 수 있습니다.

### 병렬 크롤링
병렬 처리를 사용하는 크롤링 모드는 `ParallelCrawling.py`를 실행하여 시작할 수 있습니다.
```
python ParallelCrawling.py
```

## `NaverCrawling.py`의 주요 함수 설명
- `__init__(self, client_id, client_secret)`: 클래스의 생성자입니다. 네이버 API의 클라이언트 ID와 secret을 설정합니다.
- `search_and_save_api_results(self, text, output_file, iterations)`: 네이버 블로그 검색 API를 사용하여 주어진 검색어에 대한 블로그를 검색하고 결과를 CSV 파일에 저장합니다.
- `preprocess_links(self, link_file, blacklist_file)`: 주어진 링크 파일을 전처리하고, 블랙리스트에 있는 URL을 제외합니다. 
  - 링크 파일은 네이버 api를 통해 얻어진 블로그 링크 및 정보들이 포함된 파일입니다. `강남구_links.csv`이 예시입니다.
  - 블랙리스트는 1개의 column으로 이루어진 csv 파일이며 link column에는 크롤링을 제외할 링크들이 값으로 들어 있습니다.
- `extract_columns(self, csv_file)`: 주어진 CSV 파일에서 필요한 열만을 선택하여 정제하고, 결과를 기존 CSV 파일에 덮어씌웁니다.
- `crawl_links(self, link_file_name, result_file_name, i)`: 주어진 링크 파일에서 블로그 링크를 크롤링하여 본문 내용을 추출하고, 필요한 열만을 정제하여 결과 파일에 저장합니다.

## 코드 설명
- `NaverCrawling.py`: 네이버 API를 사용하여 크롤링하는 주요 클래스를 포함하고 있습니다. 이 클래스는 일반 및 병렬 크롤링 모드를 지원합니다.
- `ParallelCrawling.py`: 병렬 처리를 위한 메인 스크립트입니다.
- `(예시)강남구_links.csv`: 크롤링할 링크의 예시 리스트를 포함하고 있습니다.
- `NaverCrawling_with_Class.ipynb`: Jupyter 노트북 형태로 `NaverCrawling` 클래스의 사용 예시를 제공합니다.
- `About_Crawling.md`: 크롤링에 대한 추가 정보와 가이드를 제공합니다.
- 병렬로 실행할 숫자는 `with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:`의 max_worker 수를 조절하면 됩니다. 
  - CPU 코어 수에 맞게 설정하여 사용하였습니다.

## 실행 결과
- 스크립트를 실행하면, 네이버 블로그 검색 결과를 크롤링하여 지정된 CSV 파일에 저장합니다. 병렬 크롤링 모드에서는 여러 스레드를 사용하여 동시에 다수의 페이지를 크롤링합니다. 이 과정에서 진행 상황이 터미널에 출력됩니다.

- 또는 먼저 네이버 블로그 검색 결과를 API로 수집하고 검수한 후 크롤링을 진행할 수도 있습니다.