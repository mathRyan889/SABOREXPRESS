import os
from modelos.restaurante import Restaurante
from modelos.cardapio import item_cardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobrema import Sobremesa

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
        
restaurante_praca = Restaurante('praça','Gourmet')
bebida_suco = Bebida('Suco de melancia',5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pao',2.00,'O melhor pão da cidade')
sorvete = Sobremesa('Sorvete de morango',12.00,'Gelado')
prato_pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(sorvete)



def main():
    '''titulo()
    exibir_opçoes()
    opcao_escolhida()'''
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
    