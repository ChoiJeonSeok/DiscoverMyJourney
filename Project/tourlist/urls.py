from django.urls import path

from . import views

app_name = 'tourlist'

urlpatterns = [
    # path('', views.index, name='index1'),
    path('similadest_view/', views.similadest_view, name='similadest_view'),
    path('destination_view/', views.destination_view, name='destination_view'),
    path('surveydest_view/', views.surveydest_view, name='surveydest_view'),

    path('similadest_view/list1/', views.simlist1, name='simlist1'),
    path('similadest_view/list2/', views.simlist2, name='simlist2'),
    path('similadest_view/list3/', views.simlist3, name='simlist3'),
    path('similadest_view/list4/', views.simlist4, name='simlist4'),
    path('similadest_view/list5/', views.simlist5, name='simlist5'),

    path('destination_view/list1/', views.deslist1, name='deslist1'),
    path('destination_view/list2/', views.deslist2, name='deslist2'),
    path('destination_view/list3/', views.deslist3, name='deslist3'),
    path('destination_view/list4/', views.deslist4, name='deslist4'),
    path('destination_view/list5/', views.deslist5, name='deslist5'),

    path('surveydest_view/list1/', views.surveylist1, name='surveylist1'),
    path('surveydest_view/list2/', views.surveylist2, name='surveylist2'),
    path('surveydest_view/list3/', views.surveylist3, name='surveylist3'),
    # 상세정보 url 필요할듯
]