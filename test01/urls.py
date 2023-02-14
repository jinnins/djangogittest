from django.urls import path
from . import views

urlpatterns = [
    path('test01datas/', views.getTestDatas, name="test01datas"),
    path('test01data/<str:name>', views.getTestData, name="test01data"),
    path('postMember/', views.postMember, name="postMember"),
    path('putMember/<str:pk>', views.putMember, name="putMember"),
]