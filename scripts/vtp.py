switches=int(input("Escribe el número de switches > "))
hosts=int(input("Escribe el número de hosts > "))
names=[]

for i in range(switches):
  names.append(input(f"Escribe el nombre de la vlan {i+1} > "))

print("\n!sur le premiere router\n")
print("enable")
print("configure terminal")
print("vtp mode server")
print("vtp domain juferoga.tk")
print("vtp password 20181020158")
print(f"interface range f0/1-{switches}")
print("switchport mode trunk")

for i in range(switches):
  print(f"vlan {i+1}0")
  print(f"name {names[i]}")

print("exit")
print("exit")
print("copy running-config startup-config")


print("\n!Dans les outers routers\n")
for i in  range(switches):
  print(f"\n!Router {i+1}\n")
  print("enable")
  print("configure terminal")
  print("vtp mode client")
  print("vtp domain juferoga.tk")
  print("vtp password 20181020158")

  print("interface f0/1")
  print("switchport mode trunk\n")

  print("!(config) las interfaces")
  for j in range(hosts):
    print(f"interface f0/{j+2}")
    print("switchport mode access")
    print(f"switchport access vlan {j+1}0")
    print("exit")
  print("exit")
  print("copy running-config startup-config")
  
print("!COMPRUEBA LAS IPS EN LOS PC's o activa el DHCP")
print("!Prueba haciendo ping de lado a lado :)")

# Comandos útiles
# (config) do sh vlan
