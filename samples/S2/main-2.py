from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import math
app = FastAPI()

@app.get("/quadrado")
def quadrado(max: Optional[int] = 1):
    arrayResults = []
    for i in range(1, max + 1):
        arrayResults.append(i * i)
    return {
        "max": max,
        "quadrados": arrayResults,
    }

@app.get("/tabuada/{num}")
def tabuada(num: int, start: Optional[int] = 1, end: Optional[int] = 10):
    arrayResults = []
    for i in range(start, end + 1):
        arrayResults.append(i * num)
    return {
        "num": num,
        "start": start,
        "end": end,
        "tabuada": arrayResults,
    }

class bhaskaraClass(BaseModel):
    a : int
    b : int
    c : int

@app.post("/bhaskara")
def bhaskara(bhaskara : bhaskaraClass):
    delta = (bhaskara.b * bhaskara.b) - (4 * (bhaskara.a * bhaskara.c))
    x1 = (- bhaskara.b + math.sqrt(delta)) / (2 * bhaskara.a)
    x2 = (- bhaskara.b - math.sqrt(delta)) / (2 * bhaskara.a)
    return {
        "eq":  str(bhaskara.a) + 'x²' + ' ' + str(bhaskara.b) + 'x'+ ' ' + str(bhaskara.c),
        "x1": x1,
        "x2": x2,
    }


class fraseClass(BaseModel):
    frase: str


@app.post("/conta")
def bhaskara(frase : fraseClass):
   vogais = 0
   espacos = 0
   outros = 0

   for caractere in frase.frase:
        if(caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u"):
            vogais = vogais + 1
        elif(caractere == " "):
            espacos = espacos + 1
        else:
            outros = outros + 1

    return {
        "frase" : frase,
        "vogais" : vogais,
        "espaços" : espacos,
        "outros" : outros
    }