from django.conf.urls import url
from views import TemperatureChart

urlpatterns = [
    url(r'^$', TemperatureChart.as_view(), name='temperature.index')
]


