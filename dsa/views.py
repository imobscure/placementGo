from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DsaSerializer, TagSerializer, VoteSerializer
from authapi.serializers import UserSerializer
from authapi.models import User
from authapi.views import UserView
from django.http import HttpRequest
from .models import Dsa
from rest_framework.renderers import TemplateHTMLRenderer
import requests, jwt
from django.contrib.auth.decorators import login_required

class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dsa/home.html'

    def get(self, request):
        dsa = Dsa.objects.all()
        serializer = DsaSerializer(dsa, many=True)

        token = request.COOKIES.get('jwt')
        if not token :
            return redirect('register')
        try:
            payload = jwt.decode(token, 'lFOPP9ja00OfHYF0Vv7MV_Q2nkOx6HqVvZOrhV71U9tYa4MCrq_qZn0UvXn0pbxj', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return redirect('register')
        user = User.objects.filter(id=payload['id']).first()
        usr = UserSerializer(user)

        data = serializer.data
        return Response({'data': data, 'user': usr.data})


class ProfileView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dsa/profile.html'

    def get(self, request):
        dsa = Dsa.objects.all()
        serializer = DsaSerializer(dsa, many=True)

        token = request.COOKIES.get('jwt')
        if not token :
            return redirect('register')
        try:
            payload = jwt.decode(token, 'lFOPP9ja00OfHYF0Vv7MV_Q2nkOx6HqVvZOrhV71U9tYa4MCrq_qZn0UvXn0pbxj', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return redirect('register')
        user = User.objects.filter(id=payload['id']).first()
        usr = UserSerializer(user)
        Data = serializer.data

        personal = []
        for data in Data:
            if data['name'] == 'Watermelon':
                personal.append(data)

        print(personal)
        print(Data)
        return Response({'data': personal, 'user': usr.data})
