import argparse

def suma(a,b):
    return a + b

def main():
    # Leer los argumentos
    parser = argparse.ArgumentParser(description="Calculadora simple por línea de comandos.")
    parser.add_argument("num1", type=float, help="Primer número")
    parser.add_argument("num2", type=float, help="Segundo número")
    parser.add_argument("--op", required=True, choices=["suma"], help="Operación a realizar")

    args = parser.parse_args()

    print(suma(args.num1, args.num2))

""" if __name__ == "__main__":
    main() """