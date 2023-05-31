import ast
import threading
import time as ti
from os import remove
from players import *
from tkinter import *
from tkinter.font import *
from tkinter import messagebox
from tkinter import ttk
from selenium import webdriver
from random_word import RandomWords
from datetime import date, time, datetime
from colorama import init,Fore,Back,Style
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options=Options()
options.add_argument('--headless')

init(convert=True)

def creaCookiesPT1(driver,usuario): #FUNCION PARA LA CREACION DE LAS COOKIES (PRIMERA PARTE, PREVIO A LA COMPROBACION ANTI-BOT)
    
    try:
        driver.find_element(By.XPATH,"//*[@id='login-form']/form/div[1]/input").send_keys(usuario)
        driver.find_element(By.NAME,'password').send_keys(passGeneral)
        iframes1=driver.find_elements(By.TAG_NAME,'iframe')
        ti.sleep(1)
        driver.switch_to.frame(iframes1[0]) #FOCO EN FRAME DONDE ESTA EL CAPTCHA 
        driver.find_element(By.ID,'checkbox').click()
        ti.sleep(1)
    except:
        driver.find_element(By.XPATH,"//*[@id='login-form']/form/div[1]/input").send_keys(usuario)
        driver.find_element(By.NAME,'password').send_keys(passGeneral)
        iframes1=driver.find_elements(By.TAG_NAME,'iframe')
        ti.sleep(1)
        driver.switch_to.frame(iframes1[0]) #FOCO EN FRAME DONDE ESTA EL CAPTCHA
        driver.find_element(By.ID,'checkbox').click()
        ti.sleep(10)

def creaCookiesPT2(driver,nombre):#SEGUNDA PARTE DE LA CREACION DE LAS COOKIES (POSTERIOR A COMPLETAR CAPTCHA)
    
    print(Fore.CYAN+"Cargando las cookies...")
    print(Fore.BLACK)

    nombrearchivo="Cookies/"+str(nombre)+".html" #CREACION DE COOKIE ALMACENADA EN ARCHIVO HTML
            
    driver.switch_to.default_content() #VUELTA DE FOCO EN PRINCIPAL
    driver.find_element(By.XPATH,"//*[@id='login-form']/form/div[3]/div[3]/button").click() #CLICK EN LOGIN
    ti.sleep(3)
    driver.get("https://www.presearch.com")
    ti.sleep(5)
            
    cookies=driver.get_cookies() #SE OBTIENEN LAS COOKIES
    
    try:
        archivo=open(nombrearchivo)
        print(Fore.RED+"El archivo ya existe,se reemplazara por uno nuevo")
        print(Fore.BLACK)
        remove(nombrearchivo)
        archivo=open(nombrearchivo,"w")
        print(Fore.GREEN+"Archivo creado")
        print(Fore.BLACK)
    except:
        print(Fore.GREEN+"Creando archivo nuevo: "+str(nombrearchivo))
        print(Fore.BLACK)
        archivo=open(nombrearchivo,"w")
    
    archivo.write(str(cookies)) #SE ALMACENAN EN EL ARCHIVO
    archivo.close()
    
    print(Fore.GREEN+"Las cookies han sido almacenadas.Cerrando Proceso...")
    print(Fore.BLACK)
    driver.close()

def cargaCookies(driver,nombre): #FUNCION PARA LA APERTURA DE ARCHIVO DE COOKIES, PARSEO Y CARGA EN EL NAVEGADOR
    
    driver.get("http://www.presearch.com")
    nombre_archivo="Cookies/"+str(nombre)+".html" #CARGA ARCHIVO
    archivo=open(nombre_archivo,"r")
    texto=archivo.read()
    archivo.close()
    texto=texto.replace("[","")
    texto=texto.replace("]","")
    cookies=list(texto.split("}")) #CONVIERTE ARCHIVO EN UNA LISTA
    contador=1    
    for i in range(6):
        cookies[contador]=cookies[contador].replace(", {","{") #LIMPIEZA DE CARACTERES
        cookies[contador]=cookies[contador]+"}"
        contador+=1
    cookies[0]=cookies[0]+"}"
    largo=len(cookies)
    for cookie in cookies:
        print(cookie)
    contador=0    
    for i in range(largo-1):
        cookieN=ast.literal_eval(cookies[contador])
        driver.add_cookie(cookieN) #AQUI SE CARGAN LAS COOKIES AL NAVEGADOR
        contador+=1

    driver.refresh()

    print(Fore.GREEN+"Todas las cookies han sido cargadas.")
    ti.sleep(5)
    
    try:
        nuevoSaldo=driver.find_element(By.XPATH,"//*[@id='Home']/div[1]/div[2]/div/div[2]/div[1]/div[1]/span[1]")
        print(Fore.CYAN+"Saldo en la sesion: "+str(nuevoSaldo.text)) #EN CASO DE QUE LA CARGA HAYA SIDO CORRECTA Y LAS COOKIES ESTEN ACTUALIZADAS SE MOSTRARA EL SALDO ACTUALIZADO
    except:
        print("No se ha podido cargar el nuevo saldo")
    
    print(Fore.BLACK)

def busqueda(driver,nombre): #FUNCION DE BUSQUEDA, SE LE PASA COMO PARAMETRO EL DRIVER PREVIAMENTE ABIERTO, Y EL NOMBRE DE SESION ASIGNADA
    nuevoContador=0
    while nuevoContador <26:
        try:
            try:
                palabraN=RandomWords().get_random_word() #OBTIENE PALABRA ALEATORIA
                ti.sleep(1)
                palabraN=palabraN.replace(" ","+")
                urlBusqueda="https://presearch.com/search?q="+str(palabraN) #BUSCA LA PALABRA VIA URL
                driver.get(urlBusqueda)
                actual=datetime.now()                   
                print(Fore.GREEN+"Busqueda "+str(int(nuevoContador+1))+" de "+str(nombre)+" a las: "+str(actual.hour)+":"+str(actual.minute)+":"+str(actual.second)) #DEVUELVE INFORME DE BUSQUEDA CORRECTA
                print(Fore.RESET)
                ti.sleep(20)
                try:
                    nuevoSaldo=driver.find_element(By.XPATH,"//*[@id='Home']/div[1]/div[2]/div/div[2]/div[1]/div[1]/span[1]")
                    print(Fore.CYAN+"Saldo en la sesion: "+str(nuevoSaldo.text))
                except:
                    pass
                print(Fore.BLACK)                    
            except:
                palabraN=RandomWords().get_random_word()
                ti.sleep(1)
                palabraN=palabraN.replace(" ","+")
                urlBusqueda="https://presearch.com/search?q="+str(palabraN)
                driver.get(urlBusqueda)
                actual=datetime.now()
                print(Fore.GREEN+"Busqueda "+str(int(nuevoContador+1))+" de "+str(nombre)+" a las: "+str(actual.hour)+":"+str(actual.minute)+":"+str(actual.second))
                print(Fore.RESET)
                ti.sleep(20)
                try:
                    nuevoSaldo=driver.find_element(By.XPATH,"//*[@id='Home']/div[1]/div[2]/div/div[2]/div[1]/div[1]/span[1]")
                    print(Fore.CYAN+"Saldo en la sesion: "+str(nuevoSaldo.text))
                except:
                    pass
                print(Fore.BLACK)     
            nuevoContador+=1
        except:
            driver.refresh()
            ti.sleep(1)
            pass
    ti.sleep(3)
    try:
        nuevoSaldo=driver.find_element(By.XPATH,"//*[@id='Home']/div[1]/div[2]/div/div[2]/div[1]/div[1]/span[1]")
        print(Fore.GREEN+"Busquedas realizadas con exito en "+str(nombre)+" A las: "+str(actual.hour)+":"+str(actual.minute)+":"+str(actual.second)+" .Saldo final: "+str(nuevoSaldo.text))
        print(Fore.RESET)
    except:
        print(Fore.GREEN+"Busquedas finalizadas")

def inicia(nombre): #SECUENCIA COMPLETA DE BUSQUEDA
    
    driver=webdriver.Chrome(options=options) #INICIA DRIVER
    driver.set_window_size(500,619)
    cargaCookies(driver,nombre) #CARGA LAS COOKIES
    busqueda(driver,nombre) #REALIZA LAS BUSQUEDAS
    driver.close() #CIERRA DRIVER