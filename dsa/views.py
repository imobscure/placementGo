from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DsaSerializer, TagSerializer, MarkSerializer
from authapi.serializers import UserSerializer
from authapi.models import User
from authapi.views import UserView
from django.http import HttpRequest
from .models import Dsa, Mark
from rest_framework.renderers import TemplateHTMLRenderer
import requests, jwt
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
        mark = Mark.objects.all()
        mars = MarkSerializer(mark, many=True)
        token = request.COOKIES.get('jwt')
        if not token :
            return redirect('register')
        try:
            payload = jwt.decode(token, 'lFOPP9ja00OfHYF0Vv7MV_Q2nkOx6HqVvZOrhV71U9tYa4MCrq_qZn0UvXn0pbxj', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return redirect('register')
        user = User.objects.filter(id=payload['id']).first()
        usr = UserSerializer(user)

        hash = {-1}
        for data in mars.data:
            if data['username'] == usr.data['email']:
                hash.add(data['pid'])
        dsa = Dsa.objects.all()
        serializer = DsaSerializer(dsa, many=True)
        personal = []
        for data in serializer.data:
            if data['id'] in hash:
                personal.append(data)
        print(personal)
        return Response({'data': personal, 'user': usr.data})

class EasyView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dsa/home.html'

    def post(self, request, problem_id):
        dsa = get_object_or_404(Dsa, pk=problem_id)
        dsa.evote += 1
        dsa.save()
        return redirect('home')

class MedView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dsa/home.html'

    def post(self, request, problem_id):
        dsa = get_object_or_404(Dsa, pk=problem_id)
        dsa.mvote += 1
        dsa.save()
        return redirect('home')

class DiffView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dsa/home.html'

    def post(self, request, problem_id):
        dsa = get_object_or_404(Dsa, pk=problem_id)
        dsa.dvote += 1
        dsa.save()
        return redirect('home')

class RelView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dsa/home.html'

    def post(self, request, problem_id):
        dsa = get_object_or_404(Dsa, pk=problem_id)
        dsa.ivote += 1
        dsa.save()
        return redirect('home')

class MarkView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dsa/home.html'

    def post(self, request, problem_id):
        token = request.COOKIES.get('jwt')
        if not token :
            return redirect('register')
        try:
            payload = jwt.decode(token, 'lFOPP9ja00OfHYF0Vv7MV_Q2nkOx6HqVvZOrhV71U9tYa4MCrq_qZn0UvXn0pbxj', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return redirect('register')
        user = User.objects.filter(id=payload['id']).first()
        usr = UserSerializer(user)
        if Mark.objects.filter(username = usr.data['email']).exists():
            print("already:(")
            redirect('home')
        mark = Mark()
        mark.date = timezone.datetime.now()
        mark.pid = problem_id
        mark.username = usr.data['email']
        mark.save()
        return redirect('home')

class DelView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dsa/profile.html'

    def post(self, request, problem_id):
        token = request.COOKIES.get('jwt')
        if not token :
            return redirect('register')
        try:
            payload = jwt.decode(token, 'lFOPP9ja00OfHYF0Vv7MV_Q2nkOx6HqVvZOrhV71U9tYa4MCrq_qZn0UvXn0pbxj', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return redirect('register')
        user = User.objects.filter(id=payload['id']).first()
        usr = UserSerializer(user)
        prb = Mark.objects.get(username=usr.data['email'], pid=problem_id)
        prb.delete()
        return redirect('profile')
