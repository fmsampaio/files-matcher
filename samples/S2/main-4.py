# Implemente um endpoint que calcule os quadrados perfeitos
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/quadrados")
def quadrados_perfeitos(Max : Optional[int] = 5):
    quadrados = []
    for i in range(1, Max+1):
        quadrados.append(i ** 2)
    return {
        "Max" : Max,
        "quadrados" : quadrados
    }


# Implemente um endpoint que calcule a tabuada de um número 
@app.get("/tabuada/{numero}")
def tabuada(numero : int, start: Optional[int] = 1, end: Optional[int] = 10):
    tabuada = []
    for i in range (start, end+1):
        tabuada.append( i * numero)

    return {
        "num" : numero,
        "start" : start,
        "end" : end,
        "tabuada" : tabuada
    }



#Implemente um endpoint que calcule as raízes reais de uma equação de segundo grau, utilizando a fórmula de Bhaskara
class bhaskaraModel (BaseModel):
    a: float
    b: float
    c: float

@app.post("/Bhaskara")
def Bhaskara(a:float, b:float, c:float) :
    delta = (b * 2 -4 *a *c)
    x1 = (((-1)*b) + ((delta)**1/2))/(2*a),
    x2 = (((-1)*b) - ((delta)**1/2))/(2*a)
        
    return{
        "equation": f'{a} x^2 + {b} x + {c}',
        "x1" : x1,
        "x2" : x2
    }


    
# Implemente um endpoint que conte a ocorrência de caracteres de uma frase
class ContaModel(BaseModel):
    frase: str

@app.post("/conta")
def conta(texto : ContaModel):
    tamanho = len(texto.frase)
    vogais = ["a","e","i","o","u"]
    espacos = [' ']
    cont_vogais = 0
    cont_espacos = 0
    cont_outros = 0
    contfrase = (texto.frase).lower()
    
    for i in range(0, tamanho , 1):
        contagem = contfrase[i]

        if contagem in vogais:
            cont_vogais = cont_vogais +1
        if contagem in espacos:
            cont_espacos = cont_espacos +1
        elif contagem not in vogais and espacos:
            cont_outros = cont_outros +1 

    return {
        "teste" : texto.frase,
        "vogais" : cont_vogais,
        "espacos" : cont_espacos,
        "outros" : cont_outros
    }