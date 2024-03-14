# plotly_app/urls.py

from django.urls import path
from .views import generate_3d_plot, plot_html

urlpatterns = [
    path('generate', generate_3d_plot, name='generate_3d_plot'),
    path('plotly', plot_html, name='plotly'),    
]
