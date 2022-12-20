import pickle
import streamlit as st
import numpy as np

model = pickle.load(open('breast_cancer.sav', 'rb'))

st.title('Prediksi Kanker Payudara Ganas atau Jinak')

col1, col2, col3 = st.columns(3)

with col1:
    radius_mean = st.number_input('Radius Mean', format='%.6f', min_value=0.0)
    texture_mean = st.number_input('Texture Mean', format='%.6f', min_value=0.0)
    perimeter_mean = st.number_input('Perimeter Mean', format='%.6f', min_value=0.0)
    area_mean = st.number_input('Area Mean', format='%.6f', min_value=0.0)
    smoothness_mean = st.number_input('Smoothness Mean', format='%.6f', min_value=0.0)
    compactness_mean = st.number_input('Compactness Mean', format='%.6f', min_value=0.0)
    concavity_mean = st.number_input('Concavity Mean', format='%.6f', min_value=0.0)
    concave_points_mean = st.number_input('Concave Points Mean', format='%.6f', min_value=0.0)
    symmetry_mean = st.number_input('Symmetry Mean', format='%.6f', min_value=0.0)
    fractal_dimension_mean = st.number_input('Fractal Dimension Mean', format='%.6f', min_value=0.0)

with col2:
    radius_se = st.number_input('Radius SE', format='%.6f', min_value=0.0)
    texture_se = st.number_input('Texture SE', format='%.6f', min_value=0.0)
    perimeter_se = st.number_input('Perimeter SE', format='%.6f', min_value=0.0)
    area_se = st.number_input('Area SE', format='%.6f', min_value=0.0)
    smoothness_se = st.number_input('Smoothness SE', format='%.6f', min_value=0.0)
    compactness_se = st.number_input('Compactness SE', format='%.6f', min_value=0.0)
    concavity_se = st.number_input('Concavity SE', format='%.6f', min_value=0.0)
    concave_points_se = st.number_input('Concave Points SE', format='%.6f', min_value=0.0)
    symmetry_se = st.number_input('Symmetry SE', format='%.6f', min_value=0.0)
    fractal_dimension_se = st.number_input('Fractal Dimension SE', format='%.6f', min_value=0.0)

with col3:
    radius_worst = st.number_input('Radius Worst', format='%.6f', min_value=0.0)
    texture_worst = st.number_input('Texture Worst', format='%.6f', min_value=0.0)
    perimeter_worst = st.number_input('Perimeter Worst', format='%.6f', min_value=0.0)
    area_worst = st.number_input('Area Worst', format='%.6f', min_value=0.0)
    smoothness_worst = st.number_input('Smoothness Worst', format='%.6f', min_value=0.0)
    compactness_worst = st.number_input('Compactness Worst', format='%.6f', min_value=0.0)
    concavity_worst = st.number_input('Concavity Worst', format='%.6f', min_value=0.0)
    concave_points_worst = st.number_input('Concave Points Worst', format='%.6f', min_value=0.0)
    symmetry_worst = st.number_input('Symmetry Worst', format='%.6f', min_value=0.0)
    fractal_dimension_worst = st.number_input('Fractal Dimension Worst', format='%.6f', min_value=0.0)

breast_cancer_diagnosis = ''

if st.button('Prediksi Kanker Payudara'):
    breast_cancer_prediction = model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])

    if (breast_cancer_prediction[0] == 1):
        breast_cancer_diagnosis = 'Pasien Terkena Kanker Payudara Ganas'
    else:
        breast_cancer_diagnosis = 'Pasien Terkena Kanker Payudara Jinak'
    
    st.success(breast_cancer_diagnosis)