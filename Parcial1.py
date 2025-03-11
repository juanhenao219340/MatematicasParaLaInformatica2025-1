class Student:
    def __init__(self, gender, program, grades=None, age=None):
        self.gender = gender
        self.program = program
        self.grades = grades if grades is not None else []
        self.age = age

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

def endOfSemester():
    students = []
    numStudents = int(input("Ingrese el número de estudiantes: "))

    for _ in range(numStudents):
        print("-------------------------------------------------------------------")
        print(f"Información para el estudiante {len(students) + 1}")

        while True:
            program = input("Ingrese el programa académico (Sistemas/Telecomunicaciones): ").strip().lower()
            if program in ("sistemas", "telecomunicaciones"):
                break
            print("Entrada no válida. Por favor, ingrese 'Sistemas' o 'Telecomunicaciones'.")

        while True:
            gender = input("Ingrese el género del estudiante (M/F): ").strip().lower()
            if gender in ("m", "f"):
                break
            print("Entrada no válida. Por favor, ingrese 'M' o 'F'.")

        grades = []

        for i in range(5):
            while True:
                try:
                    grade = float(input(f"Ingrese la calificación {i+1}: "))
                    if 0 <= grade <= 5:  # Verifica que el valor esté entre 0 y 5
                        grades.append(grade)
                        break  # Salir del bucle si la calificación es válida
                    else:
                        print("La calificación debe estar entre 0 y 5. Intente nuevamente.")
                except ValueError:
                    print("Error: Ingrese un número válido.")

        student = Student(gender, program, grades)
        students.append(student)

    systemsMen = systemsWomen = telecomMen = telecomWomen = 0
    sumGradesSystems = sumGradesTelecom = 0

    for student in students:
        average = student.average_grade()
        if student.program == "sistemas":
            sumGradesSystems += average
            if student.gender == "m":
                systemsMen += 1
            elif student.gender == "f":
                systemsWomen += 1
        elif student.program == "telecomunicaciones":
            sumGradesTelecom += average
            if student.gender == "m":
                telecomMen += 1
            elif student.gender == "f":
                telecomWomen += 1

    totalSystems = systemsMen + systemsWomen
    totalTelecom = telecomMen + telecomWomen

    result = f"""
    ****************************************
    *          Resultado del Reporte      *
    ****************************************
    Sistemas - Hombres: {systemsMen}, Mujeres: {systemsWomen}, Promedio: {sumGradesSystems / totalSystems if totalSystems > 0 else 0}
    Telecomunicaciones - Hombres: {telecomMen}, Mujeres: {telecomWomen}, Promedio: {sumGradesTelecom / totalTelecom if totalTelecom > 0 else 0}
    ****************************************
    """
    print(result)

def admissionProcess():
    students = []

    while True:
        
        while True:
            try:
                age = int(input("Ingrese la edad del estudiante: "))
                if 0 < age:
                    break
                else:
                    print("La edad del estudiante debe ser mayor que 0. Intente nuevamente.")
            except ValueError:
                print("Error: Ingrese un número válido.")
            

        while True:
            gender = input("Ingrese el género del estudiante (M/F): ").strip().lower()
            if gender in ("m", "f"):
                break
            print("Entrada no válida. Por favor, ingrese 'M' o 'F'.")

        student = Student(gender, None, age=age)
        students.append(student)

        enroll = None
        while True:
            enroll = input("¿Desea inscribir un nuevo estudiante? (Y/N): ").strip().lower()
            if enroll in ("y", "n"):
                break
            print("Respuesta no válida. Por favor ingrese 'Y' para sí o 'N' para no.")

        if enroll == 'n':
            break

    totalStudents = len(students)
    men = sum(1 for student in students if student.gender == "m")
    women = sum(1 for student in students if student.gender == "f")
    sumAges = sum(student.age for student in students)

    averageAge = sumAges / totalStudents if totalStudents > 0 else 0


    result = f"""
    ****************************************
    *          Resultado del Reporte      *
    ****************************************
    Total de estudiantes inscritos: {totalStudents}
    Edad promedio de los estudiantes inscritos: {averageAge}
    Edad promedio de los estudiantes inscritos (redondeada): {round(averageAge)}
    Hombres inscritos: {men}
    Mujeres inscritas: {women}
    ****************************************
    """
    print(result)

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Proceso de admisión")
        print("2. Fin de semestre")
        print("3. Salir")
        choice = input("Ingrese el número de la opción deseada: ").strip()

        if choice == "1":
            admissionProcess()
        elif choice == "2":
            endOfSemester()
        elif choice == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

main()