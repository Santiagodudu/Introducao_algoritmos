import random
import urllib.request
'''
def iniciaPalavras():
    with open("palavras.txt", "r") as arquivo:
        texto = arquivo.read()
        return texto.split()

def retornaPalavra(palavras):
    return random.choice(palavras)

palavras = iniciaPalavras()
p = retornaPalavra(palavras)

print(palavras, p)
'''
    
url = "http://pudim.com.br/"

with urllib.request.urlopen(url) as pudim:
    pudimHTML = pudim.read()
    print(pudimHTML)
