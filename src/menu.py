'''
Apresenta os menus da aplicação
'''
from menu_tree import (NoMenu,
                       ArvoreMenu,
                       )
from menu_funcoes import (adicionar_cliente,
                          gerenciar_clientes,
                          listar_clientes,

                          adicionar_item_cardapio,
                          listar_cardapio,

                          gerenciar_estoque,

                          adicionar_pedido,
                          atualizar_pedido,
                          gerenciar_pedidos,
                          listar_pedidos,
                          listar_pedido_por_status,

                          adicionar_item_insumos,
                          listar_insumos,

                          adicionar_produto,
                          listar_produtos)

class Menu:
    '''Classe Menu cria todos os nós de menus em uma estrutura em árvore.

    Estrutura da Árvore de Menu:

    Menu Principal
    ├── 1: Gerenciar Clientes
    │   ├── 1: Adicionar Cliente
    │   └── 2: Listar Clientes
    │
    ├── 2: Gerenciar Pedidos
    │   ├── 1: Adicionar Pedido
    │   ├── 2: Listar Pedidos
    │   ├── 3: Atualizar Pedido
    │   └── 4: Listar Pedidos por Status
    │
    └── 3: Gerenciar Insumos, Produtos e Cardápio
        ├── 1: Adicionar Item ao Estoque de Insumos
        ├── 2: Listar Insumos
        ├── 3: Adicionar Item ao Estoque de Produtos
        ├── 4: Listar Produtos
        ├── 5: Adicionar Item ao Cardápio
        └── 6: Listar Itens do Cardápio

    Para usar o menu, siga as instruções na tela.
    '''
    def __init__(self):

        # Montagem do menu feito em estrutura de dados do tipo árvore
        # Menu Principal:
        self.raiz = NoMenu("Menu Principal")

        self.raiz.adicionar_filho(
                                 "1",
                                 NoMenu("Gerenciar Clientes",
                                        gerenciar_clientes)
                                 )
        self.raiz.adicionar_filho(
                                "2",
                                NoMenu("Gerenciar Pedidos",
                                        gerenciar_pedidos)
                                )
        self.raiz.adicionar_filho(
                                "3",
                                NoMenu("Gerenciar Insumos, Produtos e Cardápio",
                                        gerenciar_estoque)
                                )

        # Clientes (Opção 1 do menu principal):
        self.raiz.filhos["1"].adicionar_filho(
                                "1",
                                NoMenu("Adicionar Cliente",
                                       adicionar_cliente)
                                )
        self.raiz.filhos["1"].adicionar_filho(
                                "2",
                                NoMenu("Listar Clientes",
                                       listar_clientes)
                                )

        # Pedidos (Opção 2 do menu principal):
        self.raiz.filhos["2"].adicionar_filho(
                                "1",
                                NoMenu("Adicionar Pedido",
                                       adicionar_pedido)
                                )
        self.raiz.filhos["2"].adicionar_filho(
                                "2",
                                NoMenu("Listar Pedidos",
                                       listar_pedidos)
                                )
        self.raiz.filhos["2"].adicionar_filho(
                                "3",
                                NoMenu("Atualizar Pedido",
                                       atualizar_pedido)
                                )
        self.raiz.filhos["2"].adicionar_filho(
                                "4",
                                NoMenu("Listar Pedidos por Status",
                                       listar_pedido_por_status)
                                )

        # Insumos (Opção 3 do menu principal):
        self.raiz.filhos["3"].adicionar_filho(
                                "1",
                                NoMenu("Adicionar Item ao Estoque de Isumos",
                                       adicionar_item_insumos)
                                )
        self.raiz.filhos["3"].adicionar_filho(
                                "2",
                                NoMenu("Listar Insumos",
                                       listar_insumos)
                                )

        # Produtos (Opção 3 do menu principal):
        self.raiz.filhos["3"].adicionar_filho(
                                "3",
                                NoMenu("Adicionar Item ao Estoque de Produtos",
                                       adicionar_produto)
                                )
        self.raiz.filhos["3"].adicionar_filho(
                                "4",
                                NoMenu("Listar Produtos",
                                       listar_produtos)
                                )

        # Cardápio (Opção 3 do menu principal):
        self.raiz.filhos["3"].adicionar_filho(
                                "5",
                                NoMenu("Adicionar Item ao Cardápio",
                                       adicionar_item_cardapio)
                                )
        self.raiz.filhos["3"].adicionar_filho(
                                "6",
                                NoMenu("Listar Itens do Cardápio",
                                       listar_cardapio)
                                )

        self.menu_tree = ArvoreMenu(self.raiz)

    def exibir_menu(self):
        '''Método para iniciar a exibição do menu da aplicação.'''
        self.menu_tree.navegar()
