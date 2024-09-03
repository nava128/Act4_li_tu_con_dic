

# ejemplo de uso de listas
misnovias=["Agripina", "Anastacia", "Maria"]
misNumeros=[666, 77, 10]
# Mostrando mis novias
print(misnovias)
# Mostrando mis numeros raros
print(misNumeros)
print("---accediento a los elementos de la lista---")
print(misnovias[-2])
if "Ana" in misnovias:
  print("si, 'Ana esta en la lista de mis novias")
else:
  print("Chale no eres mi novia")
print("Numeros de novias")
Nnovias=len(misnovias)
print(f"Numero de novias = {Nnovias}")
print("ciclo for en listas")
posicion=0
for medianaranja in misnovias:
  print(posicion," ",medianaranja)
  posicion=posicion+1