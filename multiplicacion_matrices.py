a = []
b = []
try:
    filasA = int(input("Ingrese el número de filas de la matriz A: "))
    columnasA = int(input("Ingrese el número de columnas de la matriz A: "))

    for i in range(0,filasA):
        list = []
        for j in range(0,columnasA):
            num = float(input(f"Ingrese el valor de a[{i}][{j}]"))
            list.append(num)
        a.append(list)

    filasB = int(input("Ingrese el número de filas de la matriz B: "))
    columnasB = int(input("Ingrese el número de columnas de la matriz B: "))

    for i in range(0,filasB):
        list = []
        for j in range(0,columnasB):
            num = float(input(f"Ingrese el valor de b[{i}][{j}]"))
            list.append(num)
        b.append(list)

    print("Matriz A")
    for i in range(0,filasA):
        for j in range(0,columnasA):
            print(a[i][j], "  ", end = "")
        print()

    print("Matriz B")
    for i in range(0,filasB):
        for j in range(0,columnasB):
            print(b[i][j], "  ", end = "")
        print()

    if columnasA == filasB:

        for i in range(0,filasA):
            for j in range(0,columnasB):
                print(f"a[{i}][{j}]*b[{j}][{i}]:",a[i][j]*b[j][i], "+", end = "")
            print()
    else:
        print("El número de columnas de A debe ser igual al número de filas de B\nNo se puede multiplicar")
except ValueError:
    print("Error de ingreso de datos")

    """ (0 0 * 0 0) + (0 1 * 1 0) + (0 0 * 0 1) + (0 1 * 1 1) """