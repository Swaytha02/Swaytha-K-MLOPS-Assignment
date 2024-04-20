from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import React
from .serializers import ReactSerializer
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

class ReactView(APIView):
    def get(self, request):
        try:
            # Load the data
            data = pd.read_csv(r"F:\React-Django-20240420T103539Z-001\React-Django\data.csv")
            # Preprocess the data
            data["number_courses"] = pd.to_numeric(data["number_courses"], errors='coerce')
            data["time_study"] = pd.to_numeric(data["time_study"], errors='coerce')
            data.dropna(inplace=True)
            # Prepare input features (X) and target variable (y)
            X = data[["number_courses", "time_study"]]
            y = data.iloc[:, -1]
            # Train the model
            model = LinearRegression()
            model.fit(X, y)
            # Get input from request query parameters
            number_courses_str = request.query_params.get("number_courses")
            time_study_str = request.query_params.get("time_study")
            # Validate input parameters
            if number_courses_str is None or time_study_str is None:
                return Response({"error": "Both 'number_courses' and 'time_study' are required as query parameters."}, status=400)
            number_courses = float(number_courses_str)
            time_study = float(time_study_str)
            # Prepare input array for prediction
            input_array = np.array([[number_courses, time_study]])
            # Impute missing values if any
            imputer = SimpleImputer(strategy='mean')
            input_array_imputed = imputer.fit_transform(input_array)
            # Make prediction
            output = model.predict(input_array_imputed)
            return Response({"prediction": output.tolist()})
        except Exception as e:
            return Response({"error": str(e)}, status=400)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
