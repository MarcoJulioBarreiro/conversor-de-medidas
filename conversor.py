'''
Projeto Python conversor de medidas
Autor: Marco Julio De Sousa Barreiro
'''
def convert_length(value, from_unit, to_unit):
    # Conversão entre as unidades de comprimento
    conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Unidade inválida!"
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])

def convert_mass(value, from_unit , to_unit):
    #conversão de unidades de medida de masssa
    conversion_factors = {
        'grams': 1,
        'kilograms': 1000,
        'milligrams': 0.001,
        'pounds': 453.592,
        'ounces': 28.3495,
        'lbs': 0.453592,
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
      return "Unidade inválida!"
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])


def convert_volume (value, from_unit, to_unit):
    #conversão de unidades de medida de volume
    conversion_factors = {
        'liters': 1,
        'milliliters': 0.001,
        'gallons': 3.78541,
        'cups': 0.236588,
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
      return "Unidade inválida!"
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])

def convert_temperature (value , from_unit, to_unit):
    #conversão de unidades de temperatura
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    else:
        return "Erro: Unidades inválidas. Use 'Celsius', 'Fahrenheit' ou 'Kelvin'."

def convert_area(value, from_unit, to_unit):
    # Conversão entre unidades de área
    conversion_factors = {
        'square_meters': 1,
        'square_kilometers': 1000000,
        'square_inches': 0.00064516,
        'square_feet': 0.092903
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
      return "Unidade inválida!"
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])

    #Função de interação com o usuário
def main():
    print("Conversor de Unidades")
    print("Escolha uma categoria:")
    print("1. Comprimento")
    print("2. Massa")
    print("3. Volume")
    print("4. Temperatura")
    print("5. Área")
    
    try:
        choice = int(input("Digite o número da categoria: "))

        # Comprimento
        if choice == 1:
            value = float(input("Valor a ser convertido: "))
            from_unit = input("Digite a unidade de origem: ")
            to_unit = input("Digite a unidade de destino: ")
            print(f"{value} {from_unit} é igual a {convert_length(value, from_unit, to_unit)}")

        # Massa
        elif choice == 2:
            value = float(input("Valor a ser convertido: "))
            from_unit = input("Digite a unidade de origem: ")
            to_unit = input("Digite a unidade de destino: ")
            print(f"{value} {from_unit} é igual a {convert_mass(value, from_unit, to_unit)}")

        # Volume
        elif choice == 3:
            value = float(input("Valor a ser convertido: "))
            from_unit = input("Digite a unidade de origem: ")
            to_unit = input("Digite a unidade de destino: ")
            print(f"{value} {from_unit} é igual a {convert_volume(value, from_unit, to_unit)}")

        # Temperatura
        elif choice == 4:
            value = float(input("Digite o valor da temperatura: "))
            from_unit = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ").capitalize()
            to_unit = input("Digite a unidade de destino (Celsius, Fahrenheit, Kelvin): ").capitalize()

            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit} é igual a {result} {to_unit}")

        # Área
        elif choice == 5:
            value = float(input("Valor a ser convertido: "))
            from_unit = input("Digite a unidade de origem: ")
            to_unit = input("Digite a unidade de destino: ")
            print(f"{value} {from_unit} é igual a {convert_area(value, from_unit, to_unit)}")

        else:
            print("Erro: Categoria inválida. Escolha um número entre 1 e 5.")

    except ValueError:
        print("Erro: Insira um valor numérico válido.")
# Chamar a função principal
if __name__ == "__main__":
    main()

"""
Dia 28/03/2025
Futuros Updates:
adcionar Velocidade e Tempo
criar uma janela e utilizar botões
Adicionar mais medidas
Mais valores 
Criar um Executavél
"""
