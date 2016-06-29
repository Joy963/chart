from django.views.generic import TemplateView


class TemperatureChart(TemplateView):
    template_name = 'temperature.html'

