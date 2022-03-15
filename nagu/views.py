from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.

#read
class GoodList(GenericAPIView,ListModelMixin):
    queryset=Good.objects.all()
    serializer_class=GoodSerializer
    def get(self,request):
        return self.list(request)

#create
class Goodcreate(GenericAPIView,CreateModelMixin):
    queryset=Good.objects.all()
    serializer_class=GoodSerializer
    def post(self,request):
        return self.create(request)

class Goodretrie(GenericAPIView,RetrieveModelMixin):
    queryset=Good.objects.all()
    serializer_class=GoodSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)



class Goodupdate(GenericAPIView,UpdateModelMixin):
    queryset=Good.objects.all()
    serializer_class=GoodSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)



class Gooddelete(GenericAPIView,DestroyModelMixin):
    queryset=Good.objects.all()
    serializer_class=GoodSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)






#read
class GoodListcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Good.objects.all()
    serializer_class=GoodSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)


class Goodretrieupde(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Good.objects.all()
    serializer_class=GoodSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
