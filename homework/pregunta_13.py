"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    import pandas as pd
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).parent.parent
    DATA_PATH = PROJECT_ROOT / "files" / "input"

    # Cargar los archivos tbl0.tsv y tbl2.tsv
    tbl0 = pd.read_csv(DATA_PATH / 'tbl0.tsv', sep='\t')
    tbl2 = pd.read_csv(DATA_PATH / 'tbl2.tsv', sep='\t')

    # Unir las tablas por la columna c0
    merged = pd.merge(tbl0, tbl2, on='c0')

    # Agrupar por c1 y sumar los valores de c5b
    result = merged.groupby('c1')['c5b'].sum()

    return result


if __name__ == "__main__":
    print(pregunta_13())
