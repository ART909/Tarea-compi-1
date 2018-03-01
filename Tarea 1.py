#Miguel Jimenez Torres 2014033122
#Jose Arturo Luna Izaguirre 2014110993

#Librerias

from PIL import Image
import pytesseract
from os import scandir
import re
import unicodedata
import sys

#variables globales
Lista_Horas = []
Lista_Paradas_HA = ["Ulatina","UCR","Estacion Atlantico","Colima","Santa Rosa","Miraflores","Estatcion Heredia","San Francisco","San Joaquin","Rio Segundo","Alajuela"]

#funciones de impresion

def printList(lista):
    for i in lista:
        print(i)

def printDic(diccionario):
    for i in diccionario:
        print(str(i)+ " : "+diccionario[i])

# abrir y cerrar archivos
def AbrirArchivo(nombre):
    try:
        archivo = open(nombre, "r")
        return archivo
    except:
        print("Error abriendo el archivo, " + str(sys.exc_info()[0]))
        return False

def CerrarArchivo(archivo):
    try:
        archivo.close();
        return True
    except:
        print("*ERROR: " +  sys.exc_info()[0])
        return False

#funcion encontrar hora
def EncontrarHora(directorio_archivo):
    #archivo = AbrirArchivo(directorio_archivo)
    consulta = r'[0-9]+[:][0-9]+'
    #texto = archivo.read().lower()
    cont = 0
    hora = 0
    for palabra in directorio_archivo:
        cont=cont+1 
        hora = re.findall(consulta, directorio_archivo)
    #CerrarArchivo(archivo)
    #print(cont/5)
    return hora

#Menu principal

def main():
    #directorio_general = r'C:\Users\yanira\Desktop\Compiladores trabajos\Prueba.txt'
    """im = Image.open("a.png")
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(EncontrarHora(text))"""
    im = Image.open("b.png")
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(EncontrarHora(text))
    """im = Image.open("d.png")
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(EncontrarHora(text))
    im = Image.open("e.png")
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(EncontrarHora(text))
    im = Image.open("f2.png")
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(EncontrarHora(text))
    im = Image.open("g.png")
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(EncontrarHora(text))"""


main()
