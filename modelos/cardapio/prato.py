from modelos.cardapio.item_cardapio import ItemCardapio #importar classe pai
class Prato(ItemCardapio): #referenciar que a nova classe recebe os metodos e atribudos do pai
    def __init__(self,nome,preco,descricao): #criar bloco construtor com as mesmas instancias do pai + adicional
        super().__init__(nome,preco) #Chamar o bloco construtor da classe pai
        self.descricao = descricao
        
    def __str__(self):
        return self.nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)