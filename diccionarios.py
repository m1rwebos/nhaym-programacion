# #un conjunto de PARES de datos


# dic={
#     "nombre":"Jhon Marshton",
#     "numero": 945453443,
#     "casado": True,
# }
# print(dic)

# #****************
# # for key,value in dic.items():
# #     print(key,value)

# #sabe cual es key y value por el orden 

# dic ["ciudad"]="Talca"
# for key,value in dic.items():
#     print(key,value)

# dic["casado"]=False
# for key,value in dic.items():
#     print(key,value)



# frutas={
#      "sandia": 3000,
#      "manzanas": 1500,
#      "naranjas": 1000
# }
# print(frutas)
# fruta=input("ingrese una fruta")
# precio=int(input("ingrese el precio"))

# frutas[fruta]=precio



frutas={
     "guanabana": 3000,
     "mango": 1500,
     "mandarinas": 1000
}


while True:
    print(''' 
     1.-ingresar fruta y precio
     2.-actuaizar precio
     3.-borrar frutas y precios
     4.-
     5.-
     6.-       
     ''')
    op=int(input("elija una opcion")) 
    match op:
         case 1:
              fruta=input("ingrese una fruta")
              precio=int(input("ingrese el precio"))
              frutas[fruta]=precio
            
         case 2:
              
              frutas.update 

    