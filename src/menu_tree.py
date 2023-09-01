'''
Criação da estrutura de dados para montagem do menu.
Estrutura baseada em árvore de dados, onde cada nó é um item ou subitem de menu.
Os nós folha são responsáveis por executar alguma função do software.
Sempre que uma função é executada e retorna 0 é entendido como nó não folha.
Sempre que uma função é executada e retorna 1 é entendido como nó folha.
'''
from time import sleep
from funcoes_apoio import clear
from menu_funcoes import (cliente,

                          adicionar_cliente,
                          gerenciar_clientes,
                          listar_clientes,

                          adicionar_item_cardapio,
                          listar_cardapio,

                          gerenciar_estoque,

                          adicionar_pedido,
                          gerenciar_pedidos,
                          listar_pedidos,

                          adicionar_item_insumos,
                          listar_insumos,

                          adicionar_produto,
                          listar_produtos)

class NoMenu:
    '''
    Classe NoMenu define a estrutura de um nó da árvore de menu.
    Cada objeto do tipo nó (NoMenu) é composto do seguinte:
    ATRIBUTOS:
    - String: self.descrição  - Informação de sua descrição para 
                                aparecer como texto no menu
    - Function: self.funcao   - Uma função definida em menu_funcoes.py 
                                que ou mostra um título de sub-menu 
                                (retorna 0) ou realiza alguma função
                                dentro do sistema (retorna 1)
    - Dictionary: self.filhos - Dicionário com as chaves sendo o número
                                a da opção do item no menu e o valor sendo
                                o texto a ser mostrado no menu como descrição
                                do item de menu.
    - NoMenu: self.pai        - Objeto do tipo NoMenu que é o nível superior do
                                menu com relação à um determinado sub-item.
                                Caso self.pai seja None, o nó atual é o raiz
                                (menu principal).
    MÉTODOS:
    - None: self.adicionar-filho(
                                opção numérica:string, 
                                NoMenu:no_filho
                                ) - Método de adição de nós abaixo do nó atual.
    - dictionary: self.executar() - Método que executa a função cadastrada no 
                                    nó, caso exista, e retorna um dicionário 
                                    com todos os filhos do nó atual.
    '''
    def __init__(self, descricao, funcao=None):
        self.descricao = descricao
        self.funcao = funcao
        self.filhos = {}
        self.pai = None

    def adicionar_filho(self, opcao, no_filho):
        '''Adiciona nó filho no dicionário filhos'''
        no_filho.pai = self
        self.filhos[opcao] = no_filho

    def executar(self):
        '''
        Executa a função associada ao nó, se houver.
        Retorna um dicionário de filhos.
        '''
        if self.funcao:
            if self.funcao() == 1:
                sleep(1)
        return self.filhos

class ArvoreMenu:
    '''
    Classe ArvoreMenu define a estrutura de um árvore de menu com nó raiz e
    controla qual o nó atual na navegação do usuário.
    O sistema possuirá apenas um objeto do tipo árvore (ArvoreMenu), que é 
    estruturado conforme abaixo.
    ATRIBUTOS:
    - NoMenu: self.raiz     - Objeto do tipo NoMenu que é o nível superior do
                              menu com relação à todos os demais sub-itens.
                              (menu principal).
    - NoMenu: self.no_atual - Objeto do tipo NoMenu que é o nível atual do
                              menu que o usuário se encontra.
    MÉTODOS:
    - None: self.navegar()  - Loop infinito de apresentação do menu.
                              Controla a lógica de funcionamento dos menus
                              e sua estratégia de desligamento do software.
    '''
    def __init__(self, raiz):
        self.raiz = raiz
        self.no_atual = raiz

    def navegar(self):
        '''
        Método de criação e controle do menu e estratégia 
        de desligamento do software
        '''
        while True:
            clear()
            filhos = self.no_atual.executar()
            if filhos == {}:
                self.no_atual = self.no_atual.pai
                clear()
                filhos = self.no_atual.executar()
            if self.no_atual == self.raiz:
                print("=== Menu da Lanchonete ===")

            print("\nOpções:")
            for opcao, filho in filhos.items():
                print(f"{opcao}. {filho.descricao}")
            if self.no_atual == self.raiz:
                print("0. Sair")
            else:
                print("0. Voltar")

            escolha = input("Escolha uma opção: ")

            if escolha in filhos:
                self.no_atual = filhos[escolha]
            elif escolha == '0':
                if self.no_atual == self.raiz:
                    print("Saindo...")
                    cliente.lanchonete_db.close()
                    break
                print("Retornando ao menu anterior...")
                sleep(1)
                self.no_atual = self.no_atual.pai

            else:
                print("Opção inválida.")

# Estrutura da árvore de menus apenas para testes. Não atualizar!
def main():
    '''
    Estrutura da árvore de menus apenas para testes. Não atualizar!
    '''
    raiz = NoMenu("Menu Principal")

    no_cliente = NoMenu("Gerenciar Clientes", gerenciar_clientes)
    no_pedido = NoMenu("Gerenciar Pedidos", gerenciar_pedidos)
    no_estoque = NoMenu("Gerenciar Insumos, Produtos e Cardápio", gerenciar_estoque)

    raiz.adicionar_filho("1", no_cliente)
    raiz.adicionar_filho("2", no_pedido)
    raiz.adicionar_filho("3", no_estoque)

    no_adicionar_cliente = NoMenu("Adicionar Cliente", adicionar_cliente)
    no_listar_clientes = NoMenu("Listar Clientes", listar_clientes)
    no_cliente.adicionar_filho("1", no_adicionar_cliente)
    no_cliente.adicionar_filho("2", no_listar_clientes)

    no_adicionar_pedido = NoMenu("Adicionar Pedido", adicionar_pedido)
    no_listar_pedidos = NoMenu("Listar Pedidos", listar_pedidos)
    no_pedido.adicionar_filho("1", no_adicionar_pedido)
    no_pedido.adicionar_filho("2", no_listar_pedidos)

    no_adicionar_item_insumo = NoMenu("Adicionar Item ao Insumo",
                                      adicionar_item_insumos)
    no_listar_itens_insumo = NoMenu("Listar Itens do Estoque de Insumos",
                                    listar_insumos)
    no_adicionar_produto = NoMenu("Adicionar Novo Produto",
                                  adicionar_produto)
    no_listar_produtos = NoMenu("Listar Produtos",
                                listar_produtos)
    no_adicionar_item_cardapio = NoMenu("Adicionar Item ao Cardápio",
                                        adicionar_item_cardapio)
    no_listar_itens_cardapio = NoMenu("Listar Itens do Cardápio",
                                      listar_cardapio)
    no_estoque.adicionar_filho("1", no_adicionar_item_insumo)
    no_estoque.adicionar_filho("2", no_listar_itens_insumo)
    no_estoque.adicionar_filho("3", no_adicionar_produto)
    no_estoque.adicionar_filho("4", no_listar_produtos)
    no_estoque.adicionar_filho("5", no_adicionar_item_cardapio)
    no_estoque.adicionar_filho("6", no_listar_itens_cardapio)

    menu_tree = ArvoreMenu(raiz)
    menu_tree.navegar()

if __name__ == "__main__":
    main()
