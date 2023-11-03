from django.urls import path

from homeboardapp.views import family_sns, homeboard, start_work

app_name='homeboardapp'

urlpatterns = [
    path('start_work/', start_work, name='home'),
    path('family_sns/', family_sns, name='family_sns'),
    path('homeboard', homeboard, name='homeboard'),
    ]