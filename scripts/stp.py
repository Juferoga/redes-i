# elimina bucles de capa 2
# evita la sobrecarga en la difusión
# evita que no se permita la enviar nuevos paquetes

## PAra definir el root se tiene en cuenta por defecto la prioridad y en segunda instancia la MAC

## TEner en cuenta que la vlan 1 esta creada por defecto podemos crear otras aparte

switches=3
switches=int(input("Digita la cantidad de switches (min. 2 a parte del principal) \n > "))

print("\n!En el router principal\n")
print("enable")
print("configure terminal")
print("spanning-tree vlan 1 root primary")
print("exit")
print("enable")
print("show spa")
print("copy running-config startup-config")

print("\n!En los otros\n")
for i in range(switches):
  print(f"\n!ROUTER {i+1}")
  print("enable")
  print("configure terminal")
  print("spanning-tree vlan 1 root secondary")
  print("exit")
  print("show spa")
  print("copy running-config startup-config")
