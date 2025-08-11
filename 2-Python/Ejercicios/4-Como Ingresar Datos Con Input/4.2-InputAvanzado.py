def registrar_estudiante():
    print("===Registro de Estudiante===")

    #1.Nombre sea Obligatorio
    while True:
        nombre = input("Nombre: ").strip()
        if nombre:
            break
        print("El Nombre no pueda estar Vacio")
    #2. Edad sea un entero positivo
    while True:
        try:
            edad = int(input("Edad: "))
            if edad>0:
                break
            else:
                print("La Edad no puede estar vacia")
        except ValueError:
            print("Ingrese un numero valido para la edad")    
    #3 Ciudad por defecto 
    ciudad = input("Ciudad [Lima]:").strip() or "Lima"    
    #4 Cursos lista separada por comas
    cursos= input("Cursos Matriculados (Separados por coma) :").split(",")        
    cursos=[curso.strip().title() for curso in cursos if curso.strip()]

    #Mostrar Resumen


    print("\n=== Resumen del Registro ===")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Cursos: {', '.join(cursos) if cursos else 'Ninguno'}")

registrar_estudiante()
