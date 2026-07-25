def recursive(n):
    #caso base
    if n<=0:
        return "Done"
    else:
        print(n-1)
        return recursive(n-1)

def fibonacci(n):
    if (n== 0) or (n==1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n * factorial(n-1)

def multiplicacion_recursive(n,m):
    if m == 0:
        return 0
    else:
        return n + multiplicacion_recursive(n,m-1)

def division_entera_recursiva(dividendo, divisor):
    if dividendo - divisor < 0:
        return 0
    else:
        return division_entera_recursiva(dividendo-divisor, divisor)+1

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente-1)

def serie_collatz(n):
    if n == 1:
        print(1)
        return "END!"
    elif n % 2 == 0:
        print(n//2)
        return serie_collatz(n//2)
    else:
        print(3*n+1)
        return serie_collatz(3*n + 1)

def aplanar_json(diccionario, clave_padre='', separador='.'):
    """
    Aplana un JSON (dict anidado) en un dict de un solo nivel.
    Soporta diccionarios anidados y listas.
    """
    elementos = {}
    for key, value in diccionario.items():
        nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else key

        if isinstance(value, dict):
            elementos.update(aplanar_json(value, nueva_llave, separador))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                llave_lista = f"{nueva_llave}{separador}{i}"
                if isinstance(item, dict):
                    elementos.update(aplanar_json(item, llave_lista, separador))
                else:
                    elementos[llave_lista] = item
        else:
            elementos[nueva_llave] = value
    return elementos


if __name__ == "__main__":
    json_prueba = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    },
    "f": [1, 2, 3],
    "g": [
        {"h": 4},
        {"i": 5}
    ],
    "j": {
        "k": [6, 7, {"l": 8}]
    },
    "m": None,
    "n": True,
    "o": []
}

    print("--- recursive(5) ---")
    print(recursive(5))

    print("\n--- fibonacci(10) ---")
    print(fibonacci(10))

    print("\n--- factorial(5) ---")
    print(factorial(5))

    print("\n--- multiplicacion_recursive(3,4) ---")
    print(multiplicacion_recursive(3, 4))

    print("\n--- division_entera_recursiva(17,5) ---")
    print(division_entera_recursiva(17, 5))

    print("\n--- potencia_recursiva(2,5) ---")
    print(potencia_recursiva(2, 5))

    print("\n--- serie_collatz(6) ---")
    print(serie_collatz(6))

    print("\n--- aplanar_json ---")
    print(aplanar_json(json_prueba))
