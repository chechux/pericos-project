import os

def limpiar_pantalla():

    limpiar = "clear"

    if os.name in ("nt","dos"):
        limpiar="cls"
    
    os.system(limpiar)