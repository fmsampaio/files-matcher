from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/quadrados")

def quadrado( max: Optional[int] = 20):
    quadrados = []
    for i in range(0,max+1):
        quadrados.append(i*i)
    return { 
        "max" : max,
        "quadrados": quadrados 
        }
 
@app.get("/tabuada/{num}")

def tabuada(num: int, start: Optional[int] = 1, end: Optional[int] = 9):
    tabuada = []
    for i in range(start, end+1):
        numero = num*i
        tabuada.append(numero)

        
    return { 
        "num":num,
        "start":start,
        "end":end,
        "tabuada":tabuada
        }

class BhaskaraModel(BaseModel):
 a : float
 b : float
 c : float

@app.post("/bhaskara")

def bhaskara(bhaskara : BhaskaraModel):
    
    delta = (bhaskara.b ** 2) - 4 * bhaskara.a * bhaskara.c
    x1 = (-bhaskara.b + delta ** (1 / 2)) / (2 * bhaskara.a)
    x2 = (-bhaskara.b - delta ** (1 / 2)) / (2 * bhaskara.a)

    eq = f'{bhaskara.a}x² + {bhaskara.b}x + {bhaskara.c}'
        
    return { 
        "eq":eq,
        "x1":x1,
        "x2":x2
        }

class ContaModel(BaseModel):
    frase : str

@app.post("/conta")
def conta (Conta: ContaModel ):
    contV = 0
    contE=0
    outros=0
    for c in Conta.frase:
        if c == 'a':
            contV= contV + 1
        elif c == 'e':
            contV= contV + 1
        elif c == 'i':
            contV= contV + 1
        elif c == 'o':
            contV= contV + 1
        elif c == 'u':
            contV= contV + 1
        elif c == " ":
            contE= contE+1
        else:
            outros=outros+1


    return{
    "frase" : Conta.frase,
    "vogais": contV,
    "espaços":contE,
    "outros":outros
    
}