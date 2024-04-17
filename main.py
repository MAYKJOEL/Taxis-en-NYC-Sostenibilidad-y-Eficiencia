"""
FUNCIONES CREADAS PARA EL PROYECTO FINAL DE DATA SCIENCE DE SOY HENRY
                               - NY TAXIS - 

FUNCIONES PARA ALIMENTAR LA API
"""

# Importamos las librerías necesarias
import pandas as pd
import joblib
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse

# Instanciamos la aplicación FastAPI
app = FastAPI()

# Ruta para la página de inicio
@app.get("/", response_class=HTMLResponse)
async def inicio():
    """
    Página de inicio de la API Taxis.

    Realice sus consultas.
    """
    template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>API Taxi</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>API de consultas predictivas sobre viajes en Taxi</h1>
            <p>Bienvenido a la API de Taxis. Utiliza la ruta <strong>/predict</strong> para realizar predicciones.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=template)

# Ruta para realizar predicciones
@app.post("/predictDemanda")
def predict(dia: int,hora: int, servicio: int, distrito: int):
    """
    Endpoint para realizar predicciones.

    Permite realizar predicciones si es posible. Si no es posible, retornará uno mensaje de error.

    Parameters:
    - dia: Número entero que representa el día de la semana. El valor debe ser 0 para Domingo y 6 para Sábado.
    - hora: Número entero que representa la hora del día. El valor debe estar entre 0 y 23.
    - servicio: Número entero que representa el servicio de taxi, 0 para Green y 1 para Yellow.
    - distrito: Número entero que representa el distrito de recogida. El valor debe estar entre 1 y 5.

    Returns:
        - JSON con el resultado de la predicción indicando la probabilidad de si es posible conseguir pasajeros, 
        o uno mensaje de error si no es posible hacer predicciones.
    """
    dia = dia
    hora = hora
    service = servicio
    borough = distrito

    data = {
        'dia': [dia],  # Ejemplo de valores de día
        'hora': [hora],  # Ejemplo de valores de hora
        'ervice_type2': [service],  # Ejemplo de valores de service_type2
        'pickup_borough2': [borough]}  # Ejemplo de valores de pickup_borough2

    try:
        model_taxi = joblib.load('model_taxi.pkl')

        input_data = pd.DataFrame(data)

        prediction = model_taxi.predict(input_data)

        return {"Probabilidad de conseguir taxis": prediction.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    # Ruta para realizar predicciones
@app.post("/predictEconomico")
def predict(dia: int, servicio: int, distrito: int):
    """
    Endpoint para realizar predicciones.

    Permite realizar predicciones si es posible. Si no es posible, retornará uno mensaje de error.

    Parameters:
    - dia: Número entero que representa el día de la semana. El valor debe ser 0 para Domingo y 6 para Sábado.
    - servicio: Número entero que representa el servicio de taxi, 0 para Green y 1 para Yellow.
    - distrito: Número entero que representa el distrito de recogida. El valor debe estar entre 1 y 5.

    Returns:
        - JSON con el resultado de la predicción indicando la probabilidad de si es posible conseguir pasajeros, 
        o uno mensaje de error si no es posible hacer predicciones.
    """
    dia = dia
    service = servicio
    borough = distrito

    data = {
    'dayofweek': [dia],  # Ejemplo de valores de día #'hora': ['17:00', '2:00', '21:00'],  # Ejemplo de valores de hora
    'serviceID': [service],  # Ejemplo de valores de service_type2
    'borough2ID': [borough]}  # Ejemplo de valores de pickup_borough2

    try:
        model_taxi = joblib.load('model_taxi_eco.pkl')

        input_data = pd.DataFrame(data)

        prediction = model_taxi.predict(input_data)

        return {"Cuanto es la ganancia del día": prediction.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    #uvicorn main:app --reload