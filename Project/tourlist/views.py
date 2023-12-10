from django.shortcuts import render
from .models import Tourmodel
import json
from django.http import JsonResponse

# def read_json_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     return data


def surveydest_view(request):
    with open('./survey_data.json', 'r', encoding='utf-8') as json_file:
        survey_data_data = json.load(json_file)    
   
    survey_data_list = []  

    for location in [survey_data_data['myarea_1'], survey_data_data['myarea_2'], survey_data_data['myarea_3']]:
        try:
            db_object = Tourmodel.objects.get(location=location)
            survey_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('survey_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(survey_data_list, json_file)
 
    return render(request, 'tourlist/surveydest.html', {'survey_data_list': survey_data_list})



def similadest_view(request):
    with open('./similadest.json', 'r', encoding='utf-8') as json_file:
        similadest_data = json.load(json_file)

    location_s = similadest_data['place_location']  
    similadest_data_list = []  

    # try:
    for location in location_s:
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(similadest_data_list, json_file)
    # print('6',similadest_data_list)
    return render(request, 'tourlist/similadest.html', {'similadest_data_list': similadest_data_list})


def destination_view(request):
    with open('./destination.json', 'r', encoding='utf-8') as json_file:
        destination_data = json.load(json_file)
        
    destination_data_list = []  

    for area in destination_data:  
        try:
            db_object = Tourmodel.objects.get(location=area)
            destination_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('destination_data_list.json', 'w') as json_file:
        json.dump(destination_data_list, json_file)
    # print('7',destination_data_list)
    return render(request, 'tourlist/destination.html', {'destination_data_list': destination_data_list})

def surveylist1(request):
    with open('./survey_data.json', 'r', encoding='utf-8') as json_file:
        survey_data_data = json.load(json_file)    
   
    survey_data_list = []  

    for location in [survey_data_data['myarea_1'], survey_data_data['myarea_2'], survey_data_data['myarea_3']]:
        try:
            db_object = Tourmodel.objects.get(location=location)
            survey_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('survey_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(survey_data_list, json_file)
 
    return render(request, 'tourlist/surveylist1.html', {'survey_data_list': survey_data_list})

def surveylist2(request):
    with open('./survey_data.json', 'r', encoding='utf-8') as json_file:
        survey_data_data = json.load(json_file)    
   
    survey_data_list = []  

    for location in [survey_data_data['myarea_1'], survey_data_data['myarea_2'], survey_data_data['myarea_3']]:
        try:
            db_object = Tourmodel.objects.get(location=location)
            survey_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('survey_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(survey_data_list, json_file)
 
    return render(request, 'tourlist/surveylist2.html', {'survey_data_list': survey_data_list})

def surveylist3(request):
    with open('./survey_data.json', 'r', encoding='utf-8') as json_file:
        survey_data_data = json.load(json_file)    
   
    survey_data_list = []  

    for location in [survey_data_data['myarea_1'], survey_data_data['myarea_2'], survey_data_data['myarea_3']]:
        try:
            db_object = Tourmodel.objects.get(location=location)
            survey_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('survey_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(survey_data_list, json_file)
 
    return render(request, 'tourlist/surveylist3.html', {'survey_data_list': survey_data_list})

def simlist1(request):
    with open('./similadest.json', 'r', encoding='utf-8') as json_file:
        similadest_data = json.load(json_file)

    location_s = similadest_data['place_location']  
    similadest_data_list = []  

    # try:
    for location in location_s:
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(similadest_data_list, json_file)

    return render(request, 'tourlist/simlist1.html', {'similadest_data_list': similadest_data_list})

def simlist2(request):
    with open('./similadest.json', 'r', encoding='utf-8') as json_file:
        similadest_data = json.load(json_file)

    location_s = similadest_data['place_location']  
    similadest_data_list = []  

    # try:
    for location in location_s:
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(similadest_data_list, json_file)

    return render(request, 'tourlist/simlist2.html', {'similadest_data_list': similadest_data_list})

def simlist3(request):
    with open('./similadest.json', 'r', encoding='utf-8') as json_file:
        similadest_data = json.load(json_file)

    location_s = similadest_data['place_location']  
    similadest_data_list = []  

    # try:
    for location in location_s:
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(similadest_data_list, json_file)

    return render(request, 'tourlist/simlist3.html', {'similadest_data_list': similadest_data_list})

def simlist4(request):
    with open('./similadest.json', 'r', encoding='utf-8') as json_file:
        similadest_data = json.load(json_file)

    location_s = similadest_data['place_location']  
    similadest_data_list = []  

    # try:
    for location in location_s:
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(similadest_data_list, json_file)

    return render(request, 'tourlist/simlist4.html', {'similadest_data_list': similadest_data_list})

def simlist5(request):
    with open('./similadest.json', 'r', encoding='utf-8') as json_file:
        similadest_data = json.load(json_file)

    location_s = similadest_data['place_location']  
    similadest_data_list = []  

    # try:
    for location in location_s:
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative': db_object.negative,
                'image': db_object.image.url,
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(similadest_data_list, json_file)
 
    return render(request, 'tourlist/simlist5.html', {'similadest_data_list': similadest_data_list})



def deslist1(request):
    with open('./destination.json', 'r', encoding='utf-8') as json_file:
        destination_data = json.load(json_file)
        
    destination_data_list = []  

    for area in destination_data:  
        try:
            db_object = Tourmodel.objects.get(location=area)
            destination_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass

    with open('destination_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(destination_data_list, json_file)

    return render(request, 'tourlist/deslist1.html', {'destination_data_list': destination_data_list})

def deslist2(request):
    with open('./destination.json', 'r', encoding='utf-8') as json_file:
        destination_data = json.load(json_file)
        
    destination_data_list = []  

    for area in destination_data:  
        try:
            db_object = Tourmodel.objects.get(location=area)
            destination_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass

    with open('destination_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(destination_data_list, json_file)

    return render(request, 'tourlist/deslist2.html', {'destination_data_list': destination_data_list})

def deslist3(request):
    with open('./destination.json', 'r', encoding='utf-8') as json_file:
        destination_data = json.load(json_file)
        
    destination_data_list = []  

    for area in destination_data:  
        try:
            db_object = Tourmodel.objects.get(location=area)
            destination_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass

    with open('destination_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(destination_data_list, json_file)

    return render(request, 'tourlist/deslist3.html', {'destination_data_list': destination_data_list})

def deslist4(request):
    with open('./destination.json', 'r', encoding='utf-8') as json_file:
        destination_data = json.load(json_file)
        
    destination_data_list = []  

    for area in destination_data:  
        try:
            db_object = Tourmodel.objects.get(location=area)
            destination_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass

    with open('destination_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(destination_data_list, json_file)

    return render(request, 'tourlist/deslist4.html', {'destination_data_list': destination_data_list})

def deslist5(request):
    with open('./destination.json', 'r', encoding='utf-8') as json_file:
        destination_data = json.load(json_file)
        
    destination_data_list = []  

    for area in destination_data:  
        try:
            db_object = Tourmodel.objects.get(location=area)
            destination_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc_1': db_object.tour_loc_1,
                'tour_loc_2': db_object.tour_loc_2,
                'tour_loc_3': db_object.tour_loc_3,
            })
        except Tourmodel.DoesNotExist:
            pass

    with open('destination_data_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(destination_data_list, json_file)

    return render(request, 'tourlist/deslist5.html', {'destination_data_list': destination_data_list})

