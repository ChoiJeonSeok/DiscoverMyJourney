from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import SurveyForm
from .models import Survey
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
       
        if form.is_valid():
           
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            family = form.cleaned_data['family']
            region_1 = form.cleaned_data['region_1']
            area_1 = form.cleaned_data['area_1']
            region_2 = form.cleaned_data['region_2']
            area_2 = form.cleaned_data['area_2']
            region_3 = form.cleaned_data['region_3']
            area_3 = form.cleaned_data['area_3']
            
            survey_instance = Survey(
                gender=gender,
                age=age,
                family=family,
                region_1=region_1,
                area_1=area_1,
                region_2=region_2,
                area_2=area_2,
                region_3=region_3,
                area_3=area_3,
            )
       

            survey_instance.regionsave()
            survey_instance.save() 
            
            survey_data = {
                'gender': gender,
                'age': age,
                'family' : family,
                'myarea_1': survey_instance.myarea_1,
                'myarea_2': survey_instance.myarea_2,
                'myarea_3': survey_instance.myarea_3,
            }
            with open('survey_data.json', 'w') as json_file:
                json.dump(survey_data, json_file)


            # print(survey_data) 
            return redirect('waitting:Survey_simila_View')  # 저장 후 리다이렉트할 URL-html에서 작성
    
    else:
        form = SurveyForm()
    
    return render(request, 'survey/survey.html')