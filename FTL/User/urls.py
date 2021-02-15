from django.urls import path,include
from User import views

from rest_framework.routers import DefaultRouter
 
 
# router = DefaultRouter()
# router.register('CustomUser',views.UserInfo, basename='users')

urlpatterns = [
   
    # path('', views.userInfo,name = 'userInfo')
    # path('', include(router.urls)),
    path('userinfo/',views.GenericAPIView.as_view(),name = 'genericView')
]