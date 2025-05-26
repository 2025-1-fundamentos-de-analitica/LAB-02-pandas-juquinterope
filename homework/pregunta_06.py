"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    import pandas as pd
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).parent.parent
    DATA_PATH = PROJECT_ROOT / "files" / "input"
    # Cargar el archivo tbl1.csv
    tabla = pd.read_csv(DATA_PATH / 'tbl1.tsv', sep='\t')

    # Obtener los valores únicos de la columna 'c4', convertir a mayúsculas y ordenar alfabéticamente
    valores_unicos = sorted(tabla['c4'].map(lambda x: x.upper()).unique())

    return valores_unicos


if __name__ == "__main__":
    print(pregunta_06())
