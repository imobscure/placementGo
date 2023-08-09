from django.urls import path
from .views import HomeView, ProfileView, EasyView, MedView, DiffView, RelView, MarkView, DelView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('profile', ProfileView.as_view(), name="profile"),
    path('<int:problem_id>/easy', EasyView.as_view(), name="easy"),
    path('<int:problem_id>/medium', MedView.as_view(), name="medium"),
    path('<int:problem_id>/difficult', DiffView.as_view(), name="difficult"),
    path('<int:problem_id>/relevant', RelView.as_view(), name="relevant"),
    path('<int:problem_id>/mark', MarkView.as_view(), name="mark"),
    path('<int:problem_id>/del', DelView.as_view(), name="del"),
]
