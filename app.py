import os
from modelos.restaurante import Restaurante

def titulo():
    print('=-'*30)
    print("\033[1;34m" + "           RESTAURANTE          " + "\033[m")
    print('=-'*30)

def cadastrar_novo_restaurantes():
    print('-='*20)
    nome = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria do seu restaurante: ')
    print('-='*20)
    
    novo_restaurante = Restaurante(nome,categoria)
    print(f'Restaurante {novo_restaurante._nome} cadastrado com sucesso!!! ')

def exibir_opçoes():
    print('''
          1. Cadastrar Restaurantes
          2. Exibir restaurantes
          3. Deixar uma avaliação
          4. Sair do app''')

def opcao_escolhida():
    opcao = int(input(': '))
    
    if opcao == 1:
        cadastrar_novo_restaurantes()
    elif opcao == 2:
        Restaurante.listar_restaurantes()
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    else:
        print('opção invalida...')
        
    

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

def main():
    titulo()
    exibir_opçoes()
    opcao_escolhida()


if __name__ == '__main__':
    main()
    