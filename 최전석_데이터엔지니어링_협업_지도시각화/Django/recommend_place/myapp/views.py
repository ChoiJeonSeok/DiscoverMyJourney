# Create your views here.
from django.shortcuts import render
from .models import Place
import random

def index(request):
    return render(request, 'myapp/index.html')

def recommend(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        companion = request.POST.get('companion')

        # Filter data based on the input
        filtered_data = Place.objects.filter(gender=gender, age=age, companion=companion)
        print(f"Filtered data: {filtered_data}")
    
        # Sort by rating and select top 15
        top_places = filtered_data.order_by('-rating')[:15]
        print(f"Top places: {top_places}")
    
        # Randomly select 5 places
        recommended_places = random.sample(list(top_places), min(len(top_places), 5))
        print(f"Recommended places: {recommended_places}")
    
        return render(request, 'myapp/results.html', {'recommended_places': recommended_places})
    else:
        return render(request, 'index.html')
