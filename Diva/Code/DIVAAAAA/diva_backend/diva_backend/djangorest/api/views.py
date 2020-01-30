# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from django.views.generic import View
from django.db import transaction
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import Prefetch, Q, Max
import uuid
import copy
import datetime

from requests import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.exceptions import APIException
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from api import models as app_models
from api import serializers as app_serializers
from api import utils as app_utils
from django.http import JsonResponse
from api import build_team as bt
import pandas as pd

# Create your views here.
import pandas as pd

class Books(APIView):
    # template_name = "admin/books.html"


    def post(self, request, *args, **kwargs):
        print(request.data)
        book_objects = app_models.Book.objects.filter(is_deleted=False)
        print('dadadada')

        formation_4_3_3 = {
            'RW':{
                'left':120,
                'top':85
            },
            'ST': {
                'left': 35,
                'top': 85
            },
            'LW': {
                'left': 35,
                'top': 85
            }
            ,
            'LCM': {
                'left': 120,
                'top': 85
            },
            'CM': {
                'left': 35,
                'top': 85
            },
            'RCM': {
                'left': 35,
                'top': 85
            },
            'LB': {
                'left': 90,
                'top': 85
            }
            ,
            'LCB': {
                'left': 15,
                'top': 85
            },
            'RCB': {
                'left': 15,
                'top': 85
            },
            'RB': {
                'left': 15,
                'top': 85
            },
            'GK': {
                'left': 237,
                'top': 15
            }
        }

        formation_4_2_31A = {
            'ST': {
                'left': 237,
                'top': 35
            },
            'LAM': {
                'left': 120,
                'top': 25
            },
            'CAM': {
                'left': 35,
                'top': 25
            }
            ,
            'RAM': {
                'left': 35,
                'top': 25
            },
            'LCM': {
                'left': 176,
                'top': 40
            },
            'RCM': {
                'left': 35,
                'top': 40
            },
            'LB': {
                'left': 90,
                'top': 70
            }
            ,
            'LCB': {
                'left': 15,
                'top': 70
            },
            'RCB': {
                'left': 15,
                'top': 70
            },
            'RB': {
                'left': 15,
                'top': 70
            },
                    'GK': {
            'left': 237,
            'top': 20
        }

        }
        book_serializer_data = app_serializers.BucketlistSerializer(book_objects, many=True).data
        # return JsonResponse({'response':'redd'})
        # return HttpResponse(json.dumps({'response':'redd'}), content_type="application/json")
        return app_utils.response({'response':book_serializer_data})



class BuildTeam(APIView):
    # template_name = "admin/books.html"


    def post(self, request, *args, **kwargs):
        data = bt.data
        print(request.data)
        # data = pd.read_csv("data.csv")
        # data = data.dropna(subset=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
        #                            'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
        #                            'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'])

        # book_objects = app_models.Book.objects.filter(is_deleted=False)
        print('dadadada')
        # book_serializer_data = app_serializers.BucketlistSerializer(book_objects, many=True).data
        # return JsonResponse({'response':'redd'})
        # return HttpResponse(json.dumps({'response':'redd'}), content_type="application/json")

        if request.data["algo"] == "algo1":
            team = bt.greddy_team(data, request.data.get('formation'))
        else:
            team = bt.build_team(data,request.data.get('formation'))
        # print(team)
        return app_utils.response({'response':team})

class BuildBudgetTeam(APIView):
    # template_name = "admin/books.html"


    def post(self, request, *args, **kwargs):
        data = bt.data
        print(request.data)
        # data = pd.read_csv("data.csv")
        # data = data.dropna(subset=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
        #                            'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
        #                            'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'])

        # book_objects = app_models.Book.objects.filter(is_deleted=False)
        print('dadadada')
        # book_serializer_data = app_serializers.BucketlistSerializer(book_objects, many=True).data
        # return JsonResponse({'response':'redd'})
        # return HttpResponse(json.dumps({'response':'redd'}), content_type="application/json")
        team = bt.build_budget_team(data,request.data.get('formation'),request.data.get('budget'))
        # print(team)
        return app_utils.response({'response':team})


class ManageTeam(APIView):
    # template_name = "admin/books.html"


    def post(self, request, *args, **kwargs):
        print(request.data)
        # data = pd.read_csv("api/data.csv",encoding='latin1')
        data = bt.data

        # print(data.columns)
        # data = data.dropna(subset=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
        #                              'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
        #                              'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'])

        # data = data.fillna(0)
        # data = data.dropna(subset=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
        #                            'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
        #                            'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'])

        # book_objects = app_models.Book.objects.filter(is_deleted=False)
        print('dadadada')
        # book_serializer_data = app_serializers.BucketlistSerializer(book_objects, many=True).data
        # return JsonResponse({'response':'redd'})
        # return HttpResponse(json.dumps({'response':'redd'}), content_type="application/json")
        if request.data["algo"] == "algo1":
            team = bt.greddy_team(data,request.data.get('formation'),request.data.get('club'),request.data.get('nation'))
        else:
            team = bt.build_team(data, request.data.get('formation'), request.data.get('club'),
                                 request.data.get('nation'))
        # print(team)
        return app_utils.response({'response':team})




class SubstituteTeam(APIView):
    # template_name = "admin/books.html"


    def post(self, request, *args, **kwargs):
        # print(request.data['players'])
        # data = pd.read_csv("api/data.csv",encoding='latin1')
        data = bt.data

        # print(data.columns)
        # data = data.dropna(subset=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
        #                              'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
        #                              'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'])

        # data = data.fillna(0)
        # data = data.dropna(subset=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
        #                            'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
        #                            'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'])

        # book_objects = app_models.Book.objects.filter(is_deleted=False)
        print('dadadada')
        # book_serializer_data = app_serializers.BucketlistSerializer(book_objects, many=True).data
        # return JsonResponse({'response':'redd'})
        # return HttpResponse(json.dumps({'response':'redd'}), content_type="application/json")
        team = bt.subsitute_player(data,request.data.get('players'),request.data.get('club'),request.data.get('substitute'),request.data.get('formation'),request.data.get('nation'))
        # print(team)
        return app_utils.response({'response':team})


class Analytics(APIView):
    # template_name = "admin/books.html"


    def post(self, request, *args, **kwargs):
        # print(request.data['players'])
        # data = pd.read_csv("api/data.csv",encoding='latin1')
        # data = pd.read_csv("api/data.csv")

        if request.data['chartType'] == 'ov':
            data = bt.box_plot()
        # print(team)
        elif request.data['chartType'] == 'op':
            data=bt.percent_players()
        elif request.data['chartType'] == 'age':
            data=bt.bar_plot()
        elif request.data['chartType']=='att':
            data=bt.radar_plot('forwards')
        elif request.data['chartType']=='mid':
            data=bt.radar_plot('midfielders')
        elif request.data['chartType']=='def':
            data = bt.radar_plot('defenders')

        return app_utils.response({'response': data})


