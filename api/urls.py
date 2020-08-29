from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('member_all_data_api_view', views.member_all_data),
]

# 設定後贅詞，可以直接 Call .api or .json
# view.py 必須設定 format
urlpatterns = format_suffix_patterns(urlpatterns)
