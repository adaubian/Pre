class Player(object):
    def __init__(self,user,nombre):
        
        self.user=user
        self.nombre=nombre

passGeneral="aquiElpass"

#PARA LA PUBLICACION HAY UN SOLO USUARIO DISPONIBLE, Y LA CONTRASEÑA NO ES LA CORRECTA POR LO QUE NO SE PODRAN GENERAR COOKIES NUEVAS A MENOS QUE SE INGRESEN NOMBRES DE USUSARIO Y CONTRASEÑAS CORRECTAS
#ELIMINAR LA CANTIDAD DE PLAYERS PERTINENTES Y RESPETAR LA DISTRIBUCION DE LISTAS

p1=Player("elhijodecito1@hotmail.com","falsohijo")
p2=Player("elhijodecito1@hotmail.com","falsohijo")
p3=Player("elhijodecito1@hotmail.com","falsohijo")
p4=Player("elhijodecito1@hotmail.com","falsohijo")
p5=Player("elhijodecito1@hotmail.com","falsohijo")
p6=Player("elhijodecito1@hotmail.com","falsohijo")
p7=Player("elhijodecito1@hotmail.com","falsohijo")
p8=Player("elhijodecito1@hotmail.com","falsohijo")
p9=Player("elhijodecito1@hotmail.com","falsohijo")
p10=Player("elhijodecito1@hotmail.com","falsohijo")

p11=Player("elhijodecito1@hotmail.com","falsohijo")
p12=Player("elhijodecito1@hotmail.com","falsohijo")
p13=Player("elhijodecito1@hotmail.com","falsohijo")
p14=Player("elhijodecito1@hotmail.com","falsohijo")
p15=Player("elhijodecito1@hotmail.com","falsohijo")
p16=Player("elhijodecito1@hotmail.com","falsohijo")
p17=Player("elhijodecito1@hotmail.com","falsohijo")
p18=Player("elhijodecito1@hotmail.com","falsohijo")
p19=Player("elhijodecito1@hotmail.com","falsohijo")
p20=Player("elhijodecito1@hotmail.com","falsohijo")
p21=Player("elhijodecito1@hotmail.com","falsohijo")
p22=Player("elhijodecito1@hotmail.com","falsohijo")

#EN EL MAIN A ESTE GRUPO SE LO RECONOCE COMO G1 EN LO REFERIDO A LA CREACION DE COOKIES, ESTO ES ASI YA QUE ES NECESARIO PODER ABRIR MAS DE UN CANAL A LA VEZ, PERO NO TODOS JUNTOS
listaPlayers1=[p1,p2,p3]
listaPlayers2=[p4,p5,p6]
listaPlayers3=[p7,p8,p9]

#Y A ESTE COMO G2:
listaPlayers4=[p11,p12,p13]
listaPlayers5=[p14,p15,p16]
listaPlayers6=[p17,p18,p19]
listaPlayers7=[p20,p21,p22]

#ESTE GRUPO ES G1 AL MOMENTO DE JUGAR:
listaJuega1=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,]

#Y ESTE G2:
listaJuega2=[p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21]