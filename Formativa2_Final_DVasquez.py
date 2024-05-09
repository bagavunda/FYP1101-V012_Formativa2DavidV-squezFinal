#Formativa2
#Declaración de variables 

PikachuRoll = 4500
OtakuRoll = 5000
PulpoRoll = 5200
AnguilaRoll = 4800
AcumRolls = 0
menu = 1
totalProductos = 0
subTotal = 0
dcto = 0.90
total = 0
prgDcto = 0
codDcto = "soyotaku"
ingDcto = 0
volverDcto = 0

#Inicio Programa 
print ("¡Bienvenido a Kurapika Sushi!")
print ("A continuación le presentamos el menú de rolls disponibles. ")

while 0 < menu <= 4:
    seleccionMenu = int(input(f"Seleccione su opción: \n1) Pikachu Roll - $4500 \n2) Otaku Roll - $5000 \n3) Pulpo Venenoso Roll - $5200 \n4) Anguila Eléctrica Roll - $4800. \nPor favor, realice su selección presionando (1/2/3/4): "))
    
    if seleccionMenu == 1: 
        print (f"Has seleccionado Pikachu Roll.")
        AcumRolls = 4500
        
    elif seleccionMenu == 2:
        print (f"Has seleccionado OtakuRoll.") 
        AcumRolls = 5000
        
    elif seleccionMenu == 3: 
        print (f"Has seleccionado Pulpo Venenoso Roll.")
        AcumRolls = 5200
        
    elif seleccionMenu == 4:
        print (f"Has seleccionado Anguila Eléctrica Roll.")
        AcumRolls = 4800
    subTotal += AcumRolls
    
    AgregarRolls = int(input(f"¿Desea agregar más rolls? (1=si/2=no): "))
    if AgregarRolls == 1: 
        print (f"Subtotal: ${subTotal}")
        menu = 1
    if AgregarRolls == 2: 
        print (f"Subtotal: ${subTotal}")
        menu = 5
        #SubMenú Cupón de Descuento 
        prgDcto = int(input ("¿Tiene cupón de descuento? (1=si/2=no): "))
        while 0 < prgDcto < 3: 
            if prgDcto == 1: 
                ingDcto = input("Por favor, ingrese código de descuento: ")
                if ingDcto == codDcto: 
                    totalProductos = (subTotal * dcto)
                    print ("Código válido.")
                    print("Total pedido con descuento:", totalProductos)
                    prgDcto = 4
                else: 
                    print("Código de descuento no válido.")
                    volverDcto = (input("Para reingresar el código presione (A). Para volver al menú presione (X): "))
                    if volverDcto == "A": 
                        prgDcto = 1
                    elif volverDcto == "X":
                        prgDcto = 4 
                        menu = 1
                        
                
    elif prgDcto == 2: 
        totalProductos = {subTotal}
        print (totalProductos)


    