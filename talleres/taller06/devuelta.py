def devolver(denominaciones : list, cantidad : int):
    denominaciones.sort(reverse = True)
    print("Su devuelta es de " + str(cantidad))
    for denominacion in denominaciones:
        numeroDeMonedas = cantidad // denominacion
        cantidad = cantidad % denominacion
        print(str(numeroDeMonedas) + " de " + str(denominacion))

def main():
  devolver([500,300,200],1900)
  print("-------------------------")
  devolver([1000,500,200,100,50],1004550)
  
main()