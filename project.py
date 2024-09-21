import itertools

# Pedimos al usuario que ingrese la ecuación lógica
# El usuario puede ingresar algo como: "not ((A and B) and ((A and B) ^ C))"
equation = input("Ingresa la ecuación lógica usando las variables A, B, y C: ")

# Identificamos las variables de entrada
variables = ['A', 'B', 'C']

# Generamos todas las combinaciones de valores posibles (0 y 1)
combinations = list(itertools.product([0, 1], repeat=len(variables)))

# Imprimimos la cabecera de la tabla de verdad
print(f"{'A':^3} {'B':^3} {'C':^3} {'Output':^7}")
print("-" * 20)

# Evaluamos la ecuación lógica para cada combinación
for combo in combinations:
    # Asignamos los valores de la combinación a las variables A, B, C
    A, B, C = combo
    # Usamos eval() para evaluar la ecuación lógica ingresada por el usuario
    try:
        result = eval(equation)
    except Exception as e:
        print(f"Error en la ecuación: {e}")
        break
    # Imprimimos la combinación y el resultado
    print(f"{A:^3} {B:^3} {C:^3} {result:^7}")
