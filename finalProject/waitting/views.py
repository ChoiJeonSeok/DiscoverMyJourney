from django.shortcuts import render
from .models import Place
import random
import json
import pandas as pd
from django.http import JsonResponse
from django.views import View
from waitting.models import Area  
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def read_json_file(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def recommend_areas(cluster_df, survey_data):
    # 문자열 표현의 average_vector를 실제 numpy 배열로 변환
    try:
        cluster_df['average_vector'] = cluster_df['average_vector'].apply(lambda vector_str: np.array([float(num) for num in vector_str[1:-1].split()]))
    except:
        print(cluster_df['average_vector'])
        pass
    similar_areas = pd.DataFrame()
    input_areas = []
    # JSON 파일의 각 지역에 대해
    for myarea in ['myarea_1', 'myarea_2', 'myarea_3']:
        # 지역이 비어있지 않다면
        if survey_data[myarea]:
            # 지역의 클러스터 값을 cluster에 저장
            cluster = cluster_df[cluster_df['area'] == survey_data[myarea]]['cluster'].values[0]
            # 지역의 평균 벡터를 area_vector에 저장
            area_vector = cluster_df[cluster_df['area'] == survey_data[myarea]]['average_vector'].values[0]
            # 지역과 같은 클러스터에 속하는 모든 지역의 행을 same_cluster에 저장
            same_cluster = cluster_df[cluster_df['cluster'] == cluster].copy()  
            # 지역과 같은 클러스터의 다른 지역들 사이의 코사인 유사도 계산
            same_cluster['similarity'] = same_cluster['average_vector'].apply(lambda x: cosine_similarity(area_vector.reshape(1, -1), x.reshape(1, -1))[0][0])
            # same_cluster에서 입력 지역 제거
            same_cluster = same_cluster[same_cluster['area'] != survey_data[myarea]]
            # same_cluster를 similar_areas에 추가
            similar_areas = pd.concat([similar_areas, same_cluster])
            # 입력한 지역을 리스트에 추가
            input_areas.append(survey_data[myarea])           
    # 입력한 모든 지역을 similar_areas에서 제거
    for area in input_areas:
        similar_areas = similar_areas[similar_areas['area'] != area]     
    # 중복된 행 제거: 각 지역에 대해 유사도가 가장 높은 행만 남김
    similar_areas = similar_areas.sort_values('similarity', ascending=False).drop_duplicates('area')
    # 입력한 모든 지역과 같은 클러스터에 속하는 지역들을 유사도가 높은 순으로 정렬하고 상위 5개의 지역 추출
    top_5_areas = similar_areas.sort_values('similarity', ascending=False)['area'].values[:5].tolist()
    return top_5_areas

  
class Survey_simila_View(View):
    def get(self, request):
        file_path = 'survey_data.json'
        survey_data = read_json_file(file_path)
        
        gender = survey_data.get('gender', '')
        age = survey_data.get('age', '')
        family = survey_data.get('family', '')

        filtered_data = Place.objects.filter(gender=gender, age=age, family=family)
        top_places = filtered_data.order_by('-rating')[:15]


        recommended_places = random.sample(list(top_places), min(len(top_places), 5))

  
        similadest = {
            'place_gender': gender,
            'place_age': age,
            'place_family': family,
            'place_location': [place.location for place in recommended_places],
        }

        result_file_path = 'similadest.json'
        with open(result_file_path, 'w',encoding='utf-8') as file:
            json.dump(similadest , file,ensure_ascii=False)


        df = pd.DataFrame(Area.objects.values())  # 데이터베이스에서 모든 지역을 불러옴
        # df = pd.DataFrame(Area.objects.values('name', 'average_vector'))
        destination = recommend_areas(df, survey_data)

        destination_file_path = './destination.json'
        with open(destination_file_path, 'w', encoding='utf-8') as file:
            json.dump(destination, file, ensure_ascii=False)

        print('top_5: ',destination )
        
        print(f"similadest : {similadest }")
        print(f"destination : {destination  }")
        return render(request, 'waitting/waitting.html', {'similadest': similadest, 'destination':destination} )    

