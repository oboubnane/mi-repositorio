
#comentario2
print("Hello world!!!")
"""comentario 
en varias líneas"""

#variables
nombre="Omar"
edad=48
estatura=1.83
estudia=False
trabaja=True

print("tipo de variables:")
print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(estudia))

# Algunos operadores
print("texto "*3)
print("texto" != "caramelo")
print(6**2)
# comparar
print("T == S")
print ("T"=="S")
#built-in functions
print("S == S " + str("S"=="S"))
print(int(3.23))
print(float(5))
#print(help(int))

#lista [1,2,3,4] (ordenado, mutable, duplicados)
#tupla (1,2,3,4,5) (ordenado, no mutable, duplicados)
#diccionario {llave : valor} (no ordenado, mutable, no duplicados)
#set {elemento_unico1, elemento_unico2} (no ordenado, mutable, no duplicados)
print("listas")
lenguajes = ["python","Java","R"]
programacion = [lenguajes,True,1.0,"dedicación"]
extension = ["C","Javascript"]
valores = ["A","B","C","A"]
print(lenguajes [0])
print(lenguajes [0:2])
print(lenguajes [-1])
print(lenguajes [-2])
print(programacion [0][2])
programacion [0][2]= "Pascal"
print(programacion [0][2])
lenguajes.extend(extension)
programacion.append(valores)
print(programacion)
print("longitud " + str(len(programacion)))
#tuplas lo mismo que listas pero sin opción de cambiar los valores.
#diccionarios similar a json o hashmaps
Dic_lenguajes = {
    "nombre" : "python",
    "creador" : "Guido",
    "anio" : "1991",
    "Nombre" : "Curso PRogramación"
}
Dic_lenguajes["Nombre"] = "Curso Programación"
print (Dic_lenguajes)
Dic_lenguajes["características"]=["Sencillo","agil","genial"]
print(Dic_lenguajes.items())
print(Dic_lenguajes.keys())
print(Dic_lenguajes.values())
#set
set1 = {"amarillo", "rojo", "morado"}
set1.add ("amarillo")
set1.add ("azul")
print(set1)
set1.remove ("azul")
print(set1)
set1.discard("azul")
set1.update(["negro"])
print(set1)
set1.clear()
print(len(set1))

#bucles y condiciones
a=1
b=0

if a < b :
    print ("B")
elif a > b :
    print ("A")
else :
    print ("Iguales")

if a is not b:
    print ("diferente")
else:
    print ("lo mismo")

for element in range(0,9):
    if element>=len(lenguajes) :
       print("No encontrado")
       break
    elif lenguajes[element]=="C":
        print(element)
        break
    else:
        print("sigo buscando")

for element in lenguajes:
    print (element)

i = 0 
while i <= 5:
  print (lenguajes[i])
  i+=1
  if i==3:
    break
  else:
      continue
  
for llave, valor in Dic_lenguajes.items():
      print(llave,valor)

frutas = ["manzana", "naranja", "piña"]

for fruta in frutas:
    x = 0
    for letra in fruta:
        x += 1
    print("fruta: ", fruta)
    print("tiene: ", x, " letras")