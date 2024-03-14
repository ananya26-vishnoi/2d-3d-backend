import plotly.graph_objects as go
import numpy as np
from PIL import Image
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
import sys
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt
@api_view(['POST'])
def generate_3d_plot(request):
    # Get the image from the request
    image = request.data['image']

    # Convert the image to grayscale
    image_data = np.array(Image.open(image).convert('L'))

    # Create a meshgrid for 3D plot
    x, y = np.meshgrid(np.arange(image_data.shape[1]), np.arange(image_data.shape[0]))

    # Create a 3D surface plot
    fig = go.Figure(data=[go.Surface(z=image_data, colorscale='Viridis')])

    # Set axis labels
    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

    # Save the plot to an HTML file (optional)
    fig.write_html('templates/plotly_output.html')
    return Response({'url': 'plotly'})

def plot_html(request):
    return render(request, 'plotly_output.html')