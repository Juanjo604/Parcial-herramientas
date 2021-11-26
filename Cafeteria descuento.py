#Menu
menu = [["021","Gaseosa","6000"],
        ["022","Doritos","5000"],
        ["023","Salchipapa","4000"]]

#Profesor - estudiante
cedulaUsuario = input("Ingrese su # de indentificación:")
rolUsuario = input("Ingrese su rol (estudiante o profesor):")

cantidadDeProductosAComprar = int(input("¿Cuantos productos va a comprar? :"))

contadorProductos = 0
totalAPagar = 0

while contadorProductos < cantidadDeProductosAComprar:

  #Producto
  codigoProducto = input("Ingrese el codigo del producto:")
  cantidadProducto = int(input("Ingrese cantidad del producto:"))

  contadorProductoExiste = 0
  precioProducto = 0

  for i in range(len(menu)):

    for j in range(len(menu[i])):

      if j == 0:
        productoMenu = menu[i][j]
        if codigoProducto == productoMenu:

          precioProducto = int(menu[i][2])

          contadorProductoExiste = 1

  precioTotalConDescuento = 0

  if contadorProductoExiste == 1:
    #descuentos --> estudiantes 50%, profesores 20%
    precioTotalsinDescuento = float(precioProducto * cantidadProducto)

    if rolUsuario == "estudiante":
      precioTotalConDescuento = float(precioTotalsinDescuento - (precioTotalsinDescuento * 0.5))
    
    else:
      precioTotalConDescuento = float(precioTotalsinDescuento - (precioTotalsinDescuento * 0.2))

    print("\n")
    print('El ' + rolUsuario + ' con cedula ' +  cedulaUsuario + ' debe pagar $' + str(precioTotalConDescuento) + ' por el producto ' + codigoProducto)

    

  else:
    print("Codigo producto no registrado")

  totalAPagar = precioTotalConDescuento + totalAPagar


  contadorProductos += 1

print('\n')
print('Total a pagar por los productos: ' + str(totalAPagar))


