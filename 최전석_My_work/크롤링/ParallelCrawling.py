import concurrent.futures
from NaverCrawling import NaverCrawling


def main():
    # API 키 정보 - 실제 값으로 대체해야 함
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"

    # 크롤링할 검색어 리스트
    search_words = ['검색어1', '검색어2', '검색어3']

    # 결과를 저장할 파일 이름
    link_file_name = 'links.csv'
    result_file_name = 'results.csv'
    blacklist_file = 'blacklist.csv'

    # 크롤러 객체 생성
    crawler = NaverCrawling(client_id, client_secret)

    # 병렬 처리를 위한 ThreadPoolExecutor 설정
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        # 각 검색어에 대해 병렬로 검색 실행
        future_to_search = {executor.submit(crawler.search_and_save_api_results, word, link_file_name, 10): word for
                            word in search_words}

        # 모든 검색 작업이 완료될 때까지 대기
        for future in concurrent.futures.as_completed(future_to_search):
            word = future_to_search[future]
            try:
                future.result()
                print(f"{word} 검색 완료")
            except Exception as e:
                print(f"{word} 검색 중 에러 발생: {e}")

    # 링크 전처리
    links_count = crawler.preprocess_links(link_file_name, blacklist_file)
    print(f'Preprocessed {links_count} links.')

    # 크롤링 및 데이터 정제 병렬 처리
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # 링크 파일을 크롤링
        crawl_future = executor.submit(crawler.crawling, link_file_name, result_file_name)
        # 크롤링이 끝난 후 데이터 정제
        extract_future = executor.submit(crawler.extract_columns, result_file_name)

        # 두 작업이 모두 완료될 때까지 대기
        concurrent.futures.wait([crawl_future, extract_future])

    print('크롤링 및 데이터 정제가 완료되었습니다.')


if __name__ == '__main__':
    main()
