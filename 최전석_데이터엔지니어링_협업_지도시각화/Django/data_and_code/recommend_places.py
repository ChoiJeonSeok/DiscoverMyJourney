import pandas as pd
import random

# data load
data = pd.read_csv('국민여행조사데이터_20230724.csv')

def recommend_places(data, gender, age, companion):
    # Filter data based on the input
    filtered_data = data[(data['성별'] == gender) & 
                        (data['연령대'] == age) & 
                        (data['동반자유형'] == companion)]
    
    # 평점 상위 15개 장소 추출
    top_places = filtered_data.sort_values('평점', ascending=False).head(15)
    
    # 5곳 랜덤 선정
    recommended_places = top_places.sample(5)
    
    return recommended_places

# Test the function
# recommended_places = recommend_places(data, '남', '20대', '비가족')
# recommended_places_cities = recommended_places['시군구'].tolist()
# recommended_places_cities