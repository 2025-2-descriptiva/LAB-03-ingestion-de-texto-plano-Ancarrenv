"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requerimientos son los siguientes:
    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo espacio entre palabra y palabra.
    - La columna 'cluster' debe ser de tipo numérico.
    """

    # Leer archivo (ajusta skiprows si tu archivo tiene encabezado de texto)
    df = pd.read_fwf("files/input/clusters_report.txt", skiprows=4)

    # Asignar nombres correctos de columnas
    df.columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]
