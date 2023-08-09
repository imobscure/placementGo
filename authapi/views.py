from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render, redirect

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'authapi/register.html'

    def get(self, request):
        return Response({'hello': 'hello'})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return redirect('home')
        except:
            return render(request, 'authapi/register.html', {'error': 'Registration Failed! Try again.'})


class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'authapi/register.html'

    def get(self, request):
        return Response({'hello': 'hello'})

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        #print(user.username)
        if user is None:
            return render(request, 'authapi/register.html', {'Lerror': 'User not found!'})

        if not user.check_password(password):
            return render(request, 'authapi/register.html', {'Lerror': 'Incorrect Password!'})

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'lFOPP9ja00OfHYF0Vv7MV_Q2nkOx6HqVvZOrhV71U9tYa4MCrq_qZn0UvXn0pbxj', algorithm='HS256')

        response = redirect('home')

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):

        token = request.COOKIES.get('jwt')

        if not token :
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'lFOPP9ja00OfHYF0Vv7MV_Q2nkOx6HqVvZOrhV71U9tYa4MCrq_qZn0UvXn0pbxj', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return redirect('register')
