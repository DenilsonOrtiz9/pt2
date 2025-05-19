from proveedores import proveedor
from productos import producto
global Prov1,Prod1
Opcio=""
Prov1=proveedor()
Prod1= producto()

while(Opcio!=5):
    print("1. Agregar proveedor ")
    print("2. Crear producto")
    print("3. Agregar producto a proveedor")
    print("4. Listar productos")
    print("5. Salir")
    print("Ingrese la opcion que desea:")
    Opcio = int(input())

    if Opcio==1:
        apellidos=input("Ingrese apellidos:")
        nombre=input("Ingrese Nombre:")
        telefono=input("Ingrese telefono:")

        #Crear el proveedor
        Prov1.AgregarProveedor(apellidos,nombre,telefono)

    elif Opcio==2:
        
        #Pedir ingreso de productos
        codigo=int(input("Ingrese codigo del producto:"))
        NomProducto=input("Ingrese el nombre del producto:")
        Precio=int(input("Ingrese el precio del producto:"))

        #Crear producto
        Prod1.CrearProducto(codigo,NomProducto,Precio)

    elif Opcio==3:
        Prov1.AgregarProductos(Prod1)

    elif Opcio==4:
        Prod1.ListarProductos(Prod1)