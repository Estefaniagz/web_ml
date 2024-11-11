from pickle import load
import streamlit as st

model = load(open('/workspaces/web_ml/models/decission_tree_classifier_42.sav', 'rb'))

st.title('Predicción de notas')


horas_estudio = st.slider('Horas de estudio', min_value=0, max_value=14, step=1)
asistencia = st.slider('Asistencia', min_value=60, max_value=100, step=1)
horas_sueño = st.slider('Horas de sueño', min_value=4, max_value=10, step=1)
nota_previa = st.slider('Nota previa', min_value=50, max_value=100, step=5)
tutoria = st.slider('Sesiones de tutoria', min_value=0, max_value=8, step=1)
act_extra = st.toggle('Actividades extracurriculares')
env_parental = st.radio(
    "Involucamiento parental", 
    ['Bajo', 'Medio', 'Alto'],
    index=None)
tipo_escuela= st.radio(
    "Tipo de escuela", 
    ['Publica', 'Privada'],
    index=None)
niv_edc_padres = st.radio(
    "Nivel de educacion de los padres", 
    ['Media', 'Bachillerato', 'Universitaria', 'Ninguna'],
    index=None)
influencia = st.radio(
    "Influencia de los pares", 
    ['Positiva', 'Negativa', 'Neutral'],
    index=None)
Family_Income_num = 0
Distance_from_Home_num = 0
Access_to_Resources_num = 0
Teacher_Quality_num = 0
Motivation_Level_num = 0
Gender_num = 0
Internet_Access_num =0
School_Type_num = 0
Extracurricular_Activities_num=0

env_parental_dict= {"Bajo": 0,
                    "Medio": 1,
                    "Alto":2}
act_extra= int(act_extra)
tipo_escuela_dict = {"Publica": 0, "Privada":1}
niv_edc_padres_dic= {'Media': 0, 'Bachillerato': 1, 'Universitaria': 2, 'Ninguna': -1}
influencia_dic = {'Positiva': 0, 'Negativa':1, 'Neutral': 2}

if st.button('Predecir'):
    prediccion = model.predict([[horas_estudio, asistencia, horas_sueño, nota_previa, tutoria, act_extra, env_parental_dict[env_parental], tipo_escuela_dict[tipo_escuela], niv_edc_padres_dic[niv_edc_padres], influencia_dic[influencia], 0, 0, 0, 0, 0, 0, 0, 0,0]])
    st.write('Nota predecida:', prediccion)

