import random
# se necesita:
# - un switch troncal => maneja el tráfico en las vlans
# - uno o varios switches que repliquen las vlans
# - Conocer el subnetting que se va a realizar
# (para este ejemplo se realizará un subnetting básico)
# utilizaremos la 192.168.10 y .20
# se crearán 2 switches** (conectar automático)

#           router troncal 
#     Router A             Router B
#   Host1  Host2         Host1   Host2 
# R.R.10.H R.R.20.H    R.R.10.H  R.R.20.H

#Se deben definir las vlan en función
#de que red se van a usar
# ejemplo
# vlan 10 => 192.168.10.0/24
# vlan 20 => 192.168.20.0/24


# Creamos la vlan en todos los switches asociados
switches=int(input("Digita la cantidad de switches > "))
cantidad_pc_por_router=int(input("Digita la cantidad de pcs por switch > "))
for iterator in range(0, switches):
  print(f"\n!Router {iterator+1}")
  # modo privilegiado
  print("enable")
  # modo configuración
  print("configure terminal")
  # creamos las vlans 
  print(f"vlan 10")
  print("name desarrollo")
  print(f"vlan 20")
  print("name produccion")
  print("!accediendo por una interfaz a una vlan determinada ")
  for pc_iterator in range (0,cantidad_pc_por_router):
    print(f"\n!configurando la interface para el pc {pc_iterator+1}")
    print(f"interface f0/{pc_iterator+2}")
    print(f"switchport access vlan {pc_iterator+1}0")
    print("!PARA SER TRUNK")
    print("switchport mode trunk")
    print(f"switchport trunk native vlan 1")
    
    print("!poner las IPs en los pcs")
    print(f"!ip_example")
    print(f"!PC{pc_iterator+1} = 192.168.{pc_iterator+1}0.{random.randint(2,254)}")
    print("exit")
  print("exit")
  print("copy running-config startup-config")

print("\n!Para el router principal o inicial")
print("enable")
print("configure terminal")
if switches>1:print(f"interface range f0/1-{switches}")
else:print(f"interface range f0/1")
print("switchport mode trunk")
print("switchport trunk native vlan 1")
print("exit")
print("exit")
print("copy running-config startup-config")

  
print("!Prueba haciendo ping de lado a lado :)")
print("!ANTES COMPRUEBA LAS IPS EN LOS PC's :)")
