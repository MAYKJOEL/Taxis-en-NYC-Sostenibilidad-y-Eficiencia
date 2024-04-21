from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd

app = FastAPI()

# Diccionario para mapear los nombres de los días de la semana a números
dias_semana = {
    "domingo": 0,
    "lunes": 1,
    "martes": 2,
    "miércoles": 3,
    "jueves": 4,
    "viernes": 5,
    "sábado": 6
}

# Diccionario para mapear los nombres de los boroughs a números
boroughs = {
    "manhattan": 1,
    "queens": 2,
    "brooklyn": 3,
    "bronx": 4,
    "staten island": 5
}

# Cargar el modelo entrenado desde el archivo pickle
model_taxi = joblib.load('model_taxi.pkl')

@app.post("/predictDemanda")
def predict(dia_nombre: str, hora: int, servicio_nombre: str, distrito_nombre: str):
    """
    Endpoint para realizar predicciones de demanda de taxis.

    Permite realizar predicciones si es posible. Si no es posible, retornará uno mensaje de error.

    Parameters:
    - dia_nombre: Nombre del día de la semana (ej. "Lunes").

    - hora: Número entero que representa la hora del día. El valor debe estar entre 0 y 23.

    - servicio_nombre: Nombre del servicio de taxi: Verde o Amarillo.

    - distrito_nombre: Nombre del distrito de recogida. Distritos disponibles: Manhattan, Queens, Brooklyn, Bronx y Staten Island.

    Ejemplo:
    - dia_nombre: Martes

    - hora: 12

    - servicio_nombre: Verde
    
    - distrito_nombre: Queens
    """
    try:
        dia = dias_semana[dia_nombre.lower()]  # Convertir a minúsculas antes de buscar en el diccionario
        servicio = 1 if servicio_nombre.lower() == "amarillo" else 0  # Convertir a minúsculas antes de comparar
        distrito = boroughs[distrito_nombre.lower()]  # Convertir a minúsculas antes de buscar en el diccionario

        data = {
            'dayofweek': [dia],  # Ejemplo de valores de día
            'hora': [hora],  # Ejemplo de valores de hora
            'serviceID': [servicio],  # Ejemplo de valores de service_type2
            'borough2ID': [distrito]  # Ejemplo de valores de pickup_borough2
        }

        input_data = pd.DataFrame(data)

        # Realizar la predicción
        prediction = model_taxi.predict(input_data)
        prediction = round(prediction[0], 2)

        return {"Probabilidad de conseguir taxis": f"{prediction}%"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))