# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render



class UserViewSet(viewsets.ModelViewSet):
  '''
  API endpoint that allows users to be viewed or edited  
  '''
  queryset = User.objects.all().order_by('-date_joined')
  print queryset
  serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

  '''
  API endpoint that allows group to be viewed or edited  
  '''
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
