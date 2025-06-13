# waos

# autos=0

# def lavado():
#     print('''
#      1.- cursar pago de lavado
#      2.-ver ventas diarias
#      3.-salir
#     ''')
#     op=int(print("eliga su opcion"))
#     if op==1:
#         print('''eliga su opcion de lavado
#               1.- full 15.000
#               2.- estandar 10.000
#               3.- basico 7.000



# usuario1= None
# usuario2=None
# usuario3=None
# contraseña1= None
# contraseña2=None
# contraseña3= None


# def inicio_sesion():
#     if usuario1==None and usuario2==None and usuario3==None:
#         print("Debe tener al menos un usuario")
#     else:
#         user=input("ingrese su usuario")
#         passw=input("ingresa su contraseña")
#         if (user==usuario1 and passw==contraseña1) or (user==usuario2 and passw==contraseña2) or (user==usuario3 and passw==contraseña3):
#             op=int(input())
     

# Productos=0


# def Menu_ese():
#  while True:
#     print('''
#      elige la wea 
#      1.- Agregar un producto
#      2.-eliminar producto
#      3.-mostrar producto
#      4.-salir
#           ''')
# op=int

# nombres=[]
# apellidos=[]
# while True:
#     print('''
#          1.-Insertar Nombre y apelido
#          2.-Mostrar Nombres y apellidos 
#          3.-Buscar nombre
#          4.-Salir
#            ''')
#     op=int(input("seleccione una opcion"))
#     match op:
        
#         case 1:
#             nom=input("ingresar nombre:")
#             nombres.append(nom)
#             ape=input("ingrese un apellido :")
#             apellidos.append(ape)
#             print(apellidos)
#          case 2:
#             c=0
#             for n in nombres:
#                 print(nombres[c], apellidos [c])
#                 c+=1
#          case 3:


# productos=[]
# precios=[]
# carritoDeSuper=[]
# articulos=0


# while True:
#     print('''
#      1.- Ingresar productos     
#      2.- Comprar
#      3.- Crear boleta
#      4.- Salir     
#           ''')

#     op=int(input("seleccione una opcion"))
#     match op:
#         case 1:
#             nom=input("ingrese un productos")

notas=[7.0,4.6,4.9, 7.0,5.6]

while True :
    print('''
     1.- ingresar Nota
     2.- Borrar nota
     3.- Mostrar notas
     4.-Sacar promedio, nota mayor y norta menor
     5.- Limpiar las notas
     6.- salir

     ''')
    op=int(input("Seleccione una opcion : "))
    match op:
        case 1:
            nta=float(input("Ingrese notanota"))
            notas.append(nta)
        case 2:
            for i, nota in enumerate (notas) :
                print(i+1,".-", nota )
            borrar=int(input("seleccione la nota a borrar"))
            notas.pop(borrar-1)
        case 3:
             print(notas)
        case 4 :
            if (notas)==0:
              print("no hay notas para evaluar")
            else:
              promedio= sum (notas) / len(notas)
              print(f"el promedio de notas es:",promedio)
              print("la nota mayor es",max(notas))
              print("la nota menos es",min(notas))   
        case 5 :
           notas.clear()
        case 6 :
            print("xao")
            break
        case _:
            print("ingrea algo que este ahi , weon")










































