from fastapi import FastAPI

app = FastAPI()


@app.get("/hola")
def read_hola():
    return {"hola": "hola yoharis"}
    
@app.get("/mundo")
def read_mundo():
    return {"hola": "hola migue"}

@app.get("/realizar_flexiones/")
def realizar_flexiones ():
    # iniciar_flexiones = False

    #entradas
    # a.identificar accion para iniciar las flexiones
    iniciar_flexiones = True #boolean

    # b. cantidad de flexiones
    flexiones_a_realizar = 20
    
    if iniciar_flexiones is True:
        #procesamiento
        #contador iniciando en cero
        contador_de_flexiones = 0

        # B. aumentar en 1 el acumulador por cada flexion realizada
        while contador_de_flexiones < 20:
            contador_de_flexiones += 1
            print(f"flexion numero: {contador_de_flexiones}")

    elif iniciar_flexiones is False: #tambien se puede usar el else
        return {"mensaje": f"descansar"} 
        
    #salida
    return {"mensaje":f"{flexiones_a_realizar}Flexiones realizadas"}