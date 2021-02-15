from django.shortcuts import render

from User.models import CustomUser, UserActivity
from User.serializers import CustomUserSerializer,UserActivitySerializer

from rest_framework import generics
from rest_framework import mixins

from rest_framework import viewsets




# class UserInfo(viewsets.ModelViewSet):
#     """
#         A viewset for viewing and editing article instances.
#         """

#     serializer_class = CustomUserSerializer
#     queryset = CustomUser.objects.all()







class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'id'


    def get(self, request, id = None):

        if id:
            return self.retrieve(request)

        else:
           return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

