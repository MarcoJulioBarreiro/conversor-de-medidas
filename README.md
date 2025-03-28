 Sobre o Projeto
==============================================================================================================================================================================================================================================================================
O Conversor de Medidas é um programa simples em Python que permite converter entre diferentes unidades de comprimento e massa. Ele é útil para estudantes, profissionais e qualquer pessoa que precise converter unidades de forma rápida e precisa.
==============================================================================================================================================================================================================================================================================
Tecnologias Utilizadas
==============================================================================================================================================================================================================================================================================
Python 3+
Git/GitHub (para versionamento)
==============================================================================================================================================================================================================================================================================
Estrutura do Projeto
conversor-de-medidas/
│── conversor.py  # Código principal do conversor
│── README.md      # Documentação do projeto
│── .gitignore     # Arquivos ignorados pelo Git
==============================================================================================================================================================================================================================================================================
Como Instalar e Executar
Pré-requisitos
Antes de começar, verifique se você tem o Python 3 instalado em seu sistema:
python --version
Se não estiver instalado, baixe e instale pelo site: python.org.
==============================================================================================================================================================================================================================================================================
Baixar o projeto
Clone este repositório para o seu computador:
git clone https://github.com/seu-usuario/conversor-de-medidas.git
Entre na pasta do projeto:
cd conversor-de-medidas
==============================================================================================================================================================================================================================================================================
Executar o código
Para rodar o conversor, utilize:
python conversor.py
==============================================================================================================================================================================================================================================================================
Update: 28/03/2025
Correção do try-except:

A parte de entrada do número da categoria agora está envolvida por um try-except. Isso impede que o programa trave caso o usuário insira um valor não numérico.

A exceção captura o erro de ValueError e exibe uma mensagem informando que o valor inserido é inválido, encerrando a função principal (main) se houver erro.

Correção no fluxo de execução:

A lógica de escolha das categorias foi ajustada para garantir que o programa só continue caso a entrada do usuário seja válida.

As verificações de unidades inválidas foram mantidas nas funções de conversão de unidades.
==============================================================================================================================================================================================================================================================================
Como Usar
Escolha a categoria:

1 para Comprimento

2 para Massa

Digite o valor que deseja converter.

Escolha a unidade de origem e a unidade de destino.

O programa exibirá o resultado da conversão.
==============================================================================================================================================================================================================================================================================
Exemplo de Conversão
Escolha uma categoria
1. Comprimento
2. Massa
digite o número da categoria: 1
Valor a ser convertido: 70
Digite a unidade de origem: meters
Digite a unidade de destino: kilometers
70.0 meters é igual a 0.07 kilometers
==============================================================================================================================================================================================================================================================================
Unidades Suportadas

Comprimento:

meters (metros)

kilometers (quilômetros)

centimeters (centímetros)

millimeters (milímetros)

miles (milhas)

yards (jardas)

feet (pés)

Massa:

grams (gramas)

kilograms (quilogramas)

milligrams (miligramas)

lbs (libras)
==============================================================================================================================================================================================================================================================================

Licença
Este projeto está sob a licença MIT. Você pode ver mais detalhes no arquivo LICENSE.

Feito por Marco Julio Barreiro
