from players import *
from tools import *

root=Tk()
root.title("PRE.")
root.geometry("230x120")

nombre=StringVar()

def inicioIndividual(): #ESTA FUNCION INICIA SOLAMENTE LA SESION SELECCIONADA EN EL COMBOBOX
    jugador=nombre.get()
    inicia(jugador)
    print("El juego de: "+str(jugador)+" ha finalizado")

def iniciaTodos(lista): #INICIO DE TODAS LAS SESIONES DEL GRUPO, RECIBE COMO PARAMETRO LA LISTA DE PLAYERS
    contador=0
    for i in range(len(lista)):
        inicia(lista[contador].nombre)
        contador+=1
    print("Todas las busquedas han sido realizadas")

def creaCookiesMain(lista,pos): #ESTA FUNCION ES DE NEXO ENTRE LOS PARAMETROS QUE SE RECIBIRAN PARA LA CREACION DE COOKIES SEGUN EL GRUPO Y LA FUNCION CREACOOKIES DE TOOLS
    
    for i in lista:
        driver=webdriver.Chrome()
        driver.set_window_size(500,619)
        driver.set_window_position(x=int(pos),y=0,windowHandle='current')
        driver.get("https://account.presearch.com/external-login?") #PAGINA DE LOGUEO
        
        creaCookiesPT1(driver,i.user)
        messagebox.showinfo("PRESEARCH","Presiona cuando hayas resuelto los captcha")
        creaCookiesPT2(driver,i.nombre)

def cookiesG1(): #SE ABREN HILOS POR GRUPO DE PLAYERS Y SE LES ASGINAN UNA POSICION EN LA PANTALLA 
    hilo1=threading.Thread(target=creaCookiesMain,args=(listaPlayers1,0))
    hilo2=threading.Thread(target=creaCookiesMain,args=(listaPlayers2,640))
    hilo3=threading.Thread(target=creaCookiesMain,args=(listaPlayers3,1280))
    hilo1.start()
    ti.sleep(3)
    hilo2.start()
    ti.sleep(3)
    hilo3.start()

def cookiesG2():
    hilo1=threading.Thread(target=creaCookiesMain,args=(listaPlayers4,0))
    hilo2=threading.Thread(target=creaCookiesMain,args=(listaPlayers5,640))
    hilo3=threading.Thread(target=creaCookiesMain,args=(listaPlayers6,1280))
    hilo4=threading.Thread(target=creaCookiesMain,args=(listaPlayers7,1920)) #AL TENER DOS MONITORES EN MI SETUP ESTA VENTANA SE VERIA EN EL SEGUNDO MONITOR
    hilo1.start()
    ti.sleep(3)
    hilo2.start()
    ti.sleep(3)
    hilo3.start()
    ti.sleep(3)
    hilo4.start()
        
#DETALLES DE VENTANA:

frame1=Frame(root)
frame1.grid(row=0,column=0)
Button(frame1,text="Iniciar",command=inicioIndividual).grid(row=0,column=0,)
Button(frame1,text="Iniciar G1",command=lambda: iniciaTodos(listaJuega1)).grid(row=1,column=0,)
listanombres=[]

for player in listaJuega1:
    listanombres.append(player.nombre)
combobox=ttk.Combobox(frame1,values=listanombres,textvariable=nombre)
combobox.grid(row=0,column=1)
Button(frame1,text="Crear",command=cookiesG1).grid(row=1,column=1)


frame2=Frame(root)
frame2.grid(row=1,column=0,pady=10)
Button(frame2,text="Iniciar",command=inicioIndividual).grid(row=0,column=0,)
Button(frame2,text="Iniciar G2",command=lambda: iniciaTodos(listaJuega2)).grid(row=1,column=0,)
listanombres=[]
for player in listaJuega2:
    listanombres.append(player.nombre)
combobox=ttk.Combobox(frame2,values=listanombres,textvariable=nombre)
combobox.grid(row=0,column=1)
Button(frame2,text="Crear",command=cookiesG2).grid(row=1,column=1)


root.mainloop()