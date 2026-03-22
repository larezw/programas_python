import calculadora

def main():
    a = 10
    b = 5

    # Uso de la función sumar
    print(f"Suma: {a} + {b} = {calculadora.sumar(a, b)}")

    # Uso de la función restar
    print(f"Resta: {a} - {b} = {calculadora.restar(a, b)}")

    # Uso de la función multiplicar
    print(f"Multiplicación: {a} * {b} = {calculadora.multiplicar(a, b)}")

    # Uso de la función dividir
    try:
        print(f"División: {a} / {b} = {calculadora.dividir(a, b)}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

    # Ejemplo de manejo de error (división por cero)
    try:
        calculadora.dividir(a, 0)
    except ZeroDivisionError as e:
        print(f"Prueba de error: {e}")

if __name__ == "__main__":
    main()