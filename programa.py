
import operaciones

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Suma:", operaciones.suma(num1, num2))
    print("Resta:", operaciones.resta(num1, num2))
    print("Multiplicación:", operaciones.multiplicacion(num1, num2))
    print("División:", operaciones.division(num1, num2))

if __name__ == "__main__":
    main()
