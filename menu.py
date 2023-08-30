"""
Apresenta os menus da aplicação
"""
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
    def __init__(self):

        # Montagem do menu feito em estrutura de dados do tipo árvore:
        self.raiz = NoMenu("Menu Principal")

        no_cliente = NoMenu("Gerenciar Clientes", gerenciar_clientes)
        no_pedido = NoMenu("Gerenciar Pedidos", gerenciar_pedidos)
        no_estoque = NoMenu("Gerenciar Insumos, Produtos e Cardápio",
                            gerenciar_estoque)

        self.raiz.adicionar_filho("1", no_cliente)
        self.raiz.adicionar_filho("2", no_pedido)
        self.raiz.adicionar_filho("3", no_estoque)

        # Clientes:
        no_adicionar_cliente = NoMenu("Adicionar Cliente", adicionar_cliente)
        no_listar_cliente = NoMenu("Listar Clientes", listar_clientes)
        no_cliente.adicionar_filho("1", no_adicionar_cliente)
        no_cliente.adicionar_filho("2", no_listar_cliente)

        # Pedidos:
        no_adicionar_pedido = NoMenu("Adicionar Pedido", adicionar_pedido)
        no_listar_pedido = NoMenu("Listar Pedidos", listar_pedidos)
        no_atualizar_pedido = NoMenu("Atualizar Pedido", atualizar_pedido)
        no_listar_por_status = NoMenu("Listar Pedidos por Status",
                                      listar_pedido_por_status)
        no_pedido.adicionar_filho("1", no_adicionar_pedido)
        no_pedido.adicionar_filho("2", no_listar_pedido)
        no_pedido.adicionar_filho("3", no_atualizar_pedido)
        no_pedido.adicionar_filho("4", no_listar_por_status)

        # Insumos
        no_adicionar_insumo = NoMenu("Adicionar Item ao Estoque de Isumos",
                                    adicionar_item_insumos)
        no_listar_insumos = NoMenu("Listar Insumos", listar_insumos)
        no_estoque.adicionar_filho("1", no_adicionar_insumo)
        no_estoque.adicionar_filho("2", no_listar_insumos)

        # Produtos
        no_adicionar_produto = NoMenu("Adicionar Item ao Estoque de Produtos",
                                      adicionar_produto)
        no_listar_produtos = NoMenu("Listar Produtos", listar_produtos)
        no_estoque.adicionar_filho("3", no_adicionar_produto)
        no_estoque.adicionar_filho("4", no_listar_produtos)

        # Cardápio
        no_adicionar_item_cardapio = NoMenu("Adicionar Item ao Cardápio",
                                            adicionar_item_cardapio)
        no_listar_itens_cardapio = NoMenu("Listar Itens do Cardápio",
                                          listar_cardapio)
        no_estoque.adicionar_filho("5", no_adicionar_item_cardapio)
        no_estoque.adicionar_filho("6", no_listar_itens_cardapio)

        self.menu_tree = ArvoreMenu(self.raiz)

    def exibir_menu(self):
        self.menu_tree.navegar()
