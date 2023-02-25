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
# vlan 10 => 193.168.10.0/24
# vlan 20 => 193.168.20.0/24


# Creamos la vlan en todos los switches asociados
switches=input("digita la cantidad de switches")
for iterator in range(0, switches):
  print("enable !modo privilegiado")
  print("configure terminal !modo privilegiado")
  # creamos las vlans 
  print(f"vlan 10")
  print("name desarrollo")
  print(f"vlan 20")
  print("name produccion")
  print("exit")
  print("!accediendo por una interfaz a una vlan determinada ")
  print("interface f0/2")
  print("switchport access vlan 10")
  print("!poner las IPs en los pcs")
  
