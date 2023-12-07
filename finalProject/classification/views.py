from django.shortcuts import render
import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def index(request):
    similadest_file_path = './similadest.json'
    destination_file_path = './destination.json'
    survey_data_file_path = './survey_data.json'

    with open(similadest_file_path, 'r', encoding='utf-8') as json_file:
        similadest_data = json.load(json_file)
    with open(destination_file_path, 'r', encoding='utf-8') as json_file:
        destination_data = json.load(json_file)
    survey_data = read_json_file(survey_data_file_path)

    data = {
        'destination_data': destination_data,
        'similadest_data': similadest_data,
        'survey_data': survey_data, 
    }

    return render(request, 'classification/classification.html', {'data': data})