def obter_simbolos():
    print("Selecione 3 valores dentre: 0, 11, 10, 20, 21, 22")
    simbolos = []
    valores_validos = {0, 11, 10, 20, 21, 22}

    while len(simbolos) < 3:
        try:
            escolha = int(input(f"Valor {len(simbolos) + 1}: "))
            if escolha in valores_validos:
                simbolos.append(escolha)
            else:
                print("Escolha um valor válido (0, 11, 10, 20, 21, 22).")
        except ValueError:
            print("Por favor, insira um número válido.")

    return simbolos

def calcular_equacoes(simbolos):
    x, y, z = simbolos

    eq1 = 2 * x + 11
    eq2 = (2 * z + y) - 5
    eq3 = (y + z) - x

    return eq1, eq2, eq3

def main():
    simbolos = obter_simbolos()
    resultados = calcular_equacoes(simbolos)
    print("\nResultados das equações:")
    print(f"1ª Equação: {resultados[0]}")
    print(f"2ª Equação: {resultados[1]}")
    print(f"3ª Equação: {resultados[2]}")

if __name__ == "__main__":
    main()