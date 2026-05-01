from calculadora.operaciones import sumar, restar, multiplicar, dividir

while True:
    print("\n====== CALCULADORA ======")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elegí una opción (1-5): ")

    if opcion == "5":
        print("Hasta Luego!")
        break

    try:
        a = int(input("Ingresá el primer número: "))
        b = int(input("Ingresá el segundo número: "))
    except ValueError:
        print("Error: ingresá números válidos")
        continue

    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        print("Resultado:", dividir(a, b))
    else:
        print("Opción inválida")