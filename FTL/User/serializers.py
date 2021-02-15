from rest_framework import serializers
from .models import CustomUser,UserActivity

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ('start_time','end_time')


class CustomUserSerializer(serializers.ModelSerializer):
    activity_periods = UserActivitySerializer(many = True,source = 'useractivity_set')
    class Meta:
        model = CustomUser
        fields = ('id','real_name','tz','activity_periods')
        # fields = '__all__'

