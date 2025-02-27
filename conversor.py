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
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

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
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]


    #Função de interação com o usuário
def main():
    print("Conversor de Unidades")
    print("Escolha uma categoria")
    print("1. Comprimento")
    print("2. Massa")

    choice = int(input("digite o número da categoria: "))

    if choice == 1:
        value = float(input(" valor a ser convertido: "))
        from_unit = input("Digite a unidade de origem :")
        to_unit =input("digite a unidade de destino: ")
        print(f"{value} {from_unit} é igual a {convert_length(value, from_unit, to_unit)}")

# Chamar a função principal
if __name__ == "__main__":
    main()

"""
Dia 27/02/2025-finalizado
passos para os proximos dias
corrigir a conversão
Adicionar mais medidas
Mais valores 
Armazenar valores
Criar um Executavél
"""