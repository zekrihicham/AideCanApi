from django.urls import path
from CaseApp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('cases/', views.CaseList.as_view()),
    path('cases/<int:pk>/', views.CaseDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)