import streamlit as st
import joblib
import pandas as pd

# Diccionario para mapear los nombres de los días de la semana a números
dias_semana = {
    "Domingo": 0,
    "Lunes": 1,
    "Martes": 2,
    "Miércoles": 3,
    "Jueves": 4,
    "Viernes": 5,
    "Sábado": 6
}

# Diccionario para mapear los nombres de los boroughs a números
boroughs = {
    "Manhattan": 1,
    "Queens": 2,
    "Brooklyn": 3,
    "Bronx": 4,
    "Staten Island": 5
}

# Cargar el modelo entrenado desde el archivo pickle
model_taxi = joblib.load('model_taxi.pkl')

def predict(data):
    try:
        # Crear DataFrame de nuevos datos
        input_data = pd.DataFrame(data)

        # Convertir la hora a formato de cadena de texto y extraer la hora
        hora_str = str(input_data['hora'].iloc[0]) + ":00"

        # Realizar la predicción
        prediction = model_taxi.predict(input_data)

        # Devolver la predicción
        return prediction

    except Exception as e:
        st.error(f"Error: {e}")

# Configuración de la interfaz de usuario con Streamlit
st.title('Predicción de Taxi')
st.write('Este es un formulario para predecir el número de taxis.')

# Recolección de datos de entrada del usuario
dia_nombre = st.selectbox("Selecciona un día de la semana:", options=list(dias_semana.keys()))
dia = dias_semana[dia_nombre]  # Convertir el nombre del día a su correspondiente número

hora = st.number_input("Ingresa una hora del día (0 al 23)", min_value=0, max_value=23, step=1)
service = st.selectbox("Selecciona el tipo de servicio:", options=["Verde", "Amarillo"])
borough_nombre = st.selectbox("Selecciona un borough:", options=list(boroughs.keys()))
borough = boroughs[borough_nombre]  # Convertir el nombre del borough a su correspondiente número


# Convertir el tipo de servicio a un valor numérico
service_id = 1 if service == "Amarillo" else 0

# Suponiendo que tienes algunos datos para hacer predicciones
data = {
    'dayofweek': [dia],  # Ejemplo de valores de día
    'hora': [hora],  # Ejemplo de valores de hora
    'serviceID': [service_id],  # Ejemplo de valores de service_type2
    'borough2ID': [borough]  # Ejemplo de valores de pickup_borough2
}

if st.button('Predecir'):
    prediction = predict(data)
    st.success(f'La predicción es: {prediction}')