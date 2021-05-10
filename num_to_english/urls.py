from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from num_to_english import views

urlpatterns = [

    path('num_to_english/', views.num_to_english_view),
    path('num_to_english/<int:pk>/', views.numbers_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)