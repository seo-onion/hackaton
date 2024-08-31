def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception:
        return "Error: Invalid input."

def main():
    print("Calculadora de línea de comandos")
    print("Escribe una operación completa y presiona Enter (por ejemplo, 2 + 2).")
    print("Presiona 'c' para borrar la operación escrita y comenzar de nuevo.")
    print("Escribe 'exit' para salir de la calculadora.")
    
    while True:
        user_input = input(">> ")
        
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'c':
            print("Operación borrada.")
            continue
        
        result = calculate(user_input)
        print(result)

if __name__ == "_main_":
    main()