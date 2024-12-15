from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializers import ExamenSerializer, PrediccionSerializer
from .models import Examen, Paciente, Prediccion
import numpy as np
import pandas as pd
from joblib import load
import os

COLUMN_NAMES = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
    "compactness_mean", "concavity_mean", "concave points_mean", "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se", "compactness_se",
    "concavity_se", "concave points_se", "symmetry_se", "fractal_dimension_se", "radius_worst",
    "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst", "compactness_worst",
    "concavity_worst", "concave points_worst", "symmetry_worst", "fractal_dimension_worst"
]

MODEL_PATH = os.path.join('breastcancer', 'mlmodels')

model = load(os.path.join(MODEL_PATH, 'logistic_regression_model.pkl'))
scaler = load(os.path.join(MODEL_PATH, 'scaler.pkl'))

def predict_diagnosis(data):
    data = np.array(data).reshape(1, -1)
    data_df = pd.DataFrame(data, columns=COLUMN_NAMES)
    data_scaled = scaler.transform(data_df)
    prediction = model.predict(data_scaled)
    return 'Maligno' if prediction[0] == 1 else 'Benigno'

def diagnosis_view(request):
    if request.method == "POST":
        data = request.POST.getlist('data[]')
        data = [float(i) for i in data]
        diagnosis = predict_diagnosis(data)
        return JsonResponse({"diagnosis": diagnosis})
    context = {'column_names': COLUMN_NAMES}
    return render(request, "breastcancer/diagnosis_form.html", context)

def home(request):
    return render(request, 'index.html')

def dashboard_view(request):
    # Aquí puedes agregar lógica para obtener datos necesarios para el dashboard
    context = {
        'total_pacientes': Paciente.objects.count(),
        # Agrega más datos al contexto según sea necesario
    }
    return render(request, 'breastcancer/dashboard.html', context)
  
