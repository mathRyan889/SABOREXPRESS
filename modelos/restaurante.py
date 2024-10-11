from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    
    def __init__(self,nome,categoria):
        self._nome = nome.capitalize()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'NOME'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'AVALIAÇÕES'.ljust(25)} | {'STATUS'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}| {restaurante.ativo}')
    
    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'inativo'

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente,nota):
        if 0 <nota <=5:
            avaliacao = Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
   
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'CARDAPIO DO RESTAURANTE {self._nome}\n')
        for i,item in enumerate(self._cardapio,start= 1):     
            if hasattr(item,'descricao')  :
                   mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                   print(mensagem_prato) 
            elif hasattr(item,'tipo'):
                mensagem_sobremesa = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tipo: {item.tipo}'
                print(mensagem_sobremesa)
            else:
                mensagem_bebia = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.tamanho}'
                print(mensagem_bebia)
                
    
    

