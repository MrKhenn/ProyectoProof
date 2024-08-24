## lista de contraseñas de los usuarios:
contraseñas: ["ken80b", "maximiliano401", "pepe1017"]

## este diccionario determina los usuarios registrados en la base de datos:
lista_Usuarios = {
  0 : "Will",
  1 : "Thomas",
  2 : "Kheynner",
}

def inicio():
  print("Bienvenido a tu agencia de viaje favorita, donde los precios se adaptan a tus necesidades")
  print("antes de continuar dime, ¿cual es tu solicitud el dia de hoy?")
  elecciones = [1,2,3,4]
  elecciones1_5 = ["agendar vuelo", "pedir alojamiento", "registro al sistema", "lineas de atencion"]
  elecciones2 = ["1.agendar vuelo", "2.pedir alojamiento", "3.registro al sistema", "4.lineas de atencion"]
  print(elecciones2[0])
  print(elecciones2[1])
  print(elecciones2[2])
  print(elecciones2[3])
  a = input("ingresa aqui tu solicitud: ")
  return a
