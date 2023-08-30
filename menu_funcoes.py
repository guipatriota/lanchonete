"""
Funções para açoes feitas pelo menu do sistema.
Toda nova funcionalidade do sistema deve ser colocada aqui e referenciada no menu.py
"""
from os import system, name
from datetime import datetime
from cliente import Cliente
from pedido import Pedido
from cardapio import Cardapio
from insumo import Insumo
from produto import Produto
from produto_insumo import ProdutoInsumo
from pedido_cardapio import PedidoCardapio

cliente = Cliente()
pedido = Pedido()
cardapio = Cardapio()
insumo = Insumo()
produto = Produto()
produto_insumo = ProdutoInsumo()
pedido_cardapio = PedidoCardapio()

# Funções para mostrar nome dos sub-menus:
def gerenciar_clientes():
    print("Gerenciando clientes...")
    return 0

def gerenciar_pedidos():
    print("Gerenciando pedidos...")
    return 0

def gerenciar_estoque():
    print("Gerenciando estoque...")
    return 0

# Funções de manipulação dos dados do sistema:
def adicionar_cliente():
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    print(f"\nCliente {nome} com endereço {endereco} será salvo no sistema.")
    conf = None
    while (conf not in ["y","n"]):
        conf = input("Deseja continuar ([Y]/n)? ").lower().strip()
        if conf == "y" or conf == "":
            cliente.inserir(nome, endereco)
            print(f"Cliente {nome} adicionado.")
            break
        if conf == "n":
            print("Salvamento cancelado")
            break
    input("\nPrecione enter para continuar")
    return 1

def listar_clientes():
    print("\n\nListando clientes...\n\n")
    print("Clientes:")
    clientes = cliente.listar()
    for item in clientes:
        print(item)
    input("\nPrecione enter para continuar")
    return 1

def adicionar_pedido():
    # Exibir as opções de status
    print("Escolha o status do pedido:")
    print("1. Em preparo")
    print("2. Pronto para retirada")
    print("3. Entregue")
    print("4. Cancelado")

    # Ler a escolha do usuário
    escolha = input("Digite o número correspondente ao status desejado: ")

    # Mapear a escolha para um status
    if escolha == "1":
        status = "Em preparo"
    elif escolha == "2":
        status = "Pronto para retirada"
    elif escolha == "3":
        status = "Entregue"
    elif escolha == "4":
        status = "Cancelado"
    else:
        print("Opção inválida. Definindo status como 'Indefinido'.")
        status = "Indefinido"
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_cliente = int(input("Digite o ID do cliente: "))
    print(f"\nO pedido com status {status}, hora {data_hora} do cliente {id_cliente} será salvo no sistema.")
    conf = None
    while (conf not in ["y","n"]):
        conf = input("Deseja continuar ([Y]/n)? ").lower().strip()
        if conf == "y" or conf == "":
            pedido.inserir(status, data_hora, id_cliente)
            id_pedido = pedido.get_last_insert_id()
            print(f"Pedido adicionado com ID {id_pedido}.")
            while True:
                if input("Se você deseja buscar o ID e nome dos itens no cardápio, digite 1: ") == "1":
                    cardapio.listar()
                id_cardapio = cardapio.get_id_por_nome(input("Digite o Nome do item do cardápio que você deseja adicionar ao pedido: "))[0]
                quantidade = int(input(f"Digite a quantidade para o item {produto.listar_nome_por_id(id_cardapio)[0]}: "))
                
                # Adiciona o item à tabela PedidoCardapio
                pedido_cardapio.adicionar(id_pedido, id_cardapio, quantidade)
                print(f"Produto {id_cardapio} com quantidade {quantidade} adicionado ao pedido {id_pedido}.")

                # Pergunta se deseja adicionar mais itens
                add_more = input("Deseja adicionar mais itens ao pedido? (y/n): ").strip().lower()
                if add_more != 'y':
                    break
        if conf == "n":
            print("Salvamento cancelado")
            break
    input("\nPrecione enter para continuar")
    return 1

def listar_pedidos():
    print("Pedidos:")
    pedidos = pedido.listar()
    for item in pedidos:
        print(item)
    input("\nPrecione enter para continuar")
    return 1

def listar_pedido_por_status():
    print("Para encontrar o ID do pedido, escolha um status:")
    print("1. Em preparo")
    print("2. Pronto para retirada")
    print("3. Entregue")
    print("4. Cancelado")

    # Ler a escolha do usuário para consulta
    escolha = input("Digite o número correspondente ao status que deseja consultar: ")

    # Mapear a escolha para um status para consulta
    status_para_consulta = None
    if escolha == "1":
        status_para_consulta = "Em preparo"
    elif escolha == "2":
        status_para_consulta = "Pronto para retirada"
    elif escolha == "3":
        status_para_consulta = "Entregue"
    elif escolha == "4":
        status_para_consulta = "Cancelado"
    else:
        print("Opção inválida.")
        input("\nPrecione enter para retornar ao menu")
        return 1

    # Listar pedidos com o status escolhido
    pedidos = pedido.listar_por_status(status_para_consulta)
    if not pedidos:
        print(f"Nenhum pedido com status '{status_para_consulta}' encontrado.")
        input("\nPrecione enter para continuar")
        return 1

    print(f"Pedidos com status '{status_para_consulta}':")
    for p in pedidos:
        print(f"ID: {p[0]}, Data e Hora: {p[2]}, ID do Cliente: {p[3]}")
    input("\nPrecione enter para continuar")
    return 1

def atualizar_pedido():
    if input("Se você deseja buscar o ID do pedido antes de atualizar os status, digite 1: ") == "1":
        listar_pedido_por_status()
    id_pedido = int(input("Digite o ID do pedido que você deseja atualizar: "))

    # Exibir as opções de status
    print("Escolha o novo status do pedido:")
    print("1. Em preparo")
    print("2. Pronto para retirada")
    print("3. Entregue")
    print("4. Cancelado")

    # Ler a escolha do usuário
    escolha = input("Digite o número correspondente ao novo status desejado: ")

    # Mapear a escolha para um status
    if escolha == "1":
        novo_status = "Em preparo"
    elif escolha == "2":
        novo_status = "Pronto para retirada"
    elif escolha == "3":
        novo_status = "Entregue"
    elif escolha == "4":
        novo_status = "Cancelado"
    else:
        print("Opção inválida. Mantendo status atual.")
        input("\nPrecione enter para continuar")
        return 1  # Encerra a função
    
    print(f"\nO status do pedido {id_pedido} será atualizado para {novo_status}.")
    
    conf = None
    while (conf not in ["y", "n"]):
        conf = input("Deseja continuar ([Y]/n)? ").lower().strip()
        if conf == "y" or conf == "":
            pedido.atualizar_status(id_pedido, novo_status)  # chamando o método da classe Pedido
            print("Status do pedido atualizado.")
            break
        if conf == "n":
            print("Atualização cancelada.")
            break
    input("\nPrecione enter para continuar")
    return 1

def verificar_produto_insumo(nome):
    registros = produto_insumo.buscar_por_nome(nome)

    if registros:
        print(f"O produto {nome} já está cadastrado com os seguintes detalhes:")
        for registro in registros:
            print(f"IdProdutoInsumo: {registro[0]}, IdProduto: {registro[1]}, IdInsumo: {registro[2]}, Quantidade: {registro[3]}")
        return True
    else:
        print(f"O produto {nome} não está cadastrado na tabela ProdutoInsumo.")
        return False

def adicionar_produto_insumo(id_produto):
    insumos_adicionados = 0
    print("Cadastro de insumos necessários para produção de um produto.")
    while True:
        nome_insumo = input("Digite o nome do insumo necessário para este produto: ")
        id_insumo = insumo.buscar_por_nome(nome_insumo)

        if id_insumo:
            quantidade_insumo = float(input(f"Digite a quantidade do insumo {nome_insumo} necessário para fabricação de 1 unidade do produto: "))
            produto_insumo.adicionar(id_produto, id_insumo, quantidade_insumo)
            insumos_adicionados += 1
        else:
            print("Insumo não encontrado.")

        if insumos_adicionados == 0:
            print("É obrigatório adicionar pelo menos um insumo.")
        else:
            adiciona_mais = input("Deseja adicionar mais insumos? ([Y]/n): ").lower().strip()
            if adiciona_mais == 'n':
                break

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor = float(input("Digite o valor do produto: "))
    
    print("Escolha a unidade de medida do produto:")
    print("1. Litro")
    print("2. Quilograma")
    print("3. Unidade")
    print("4. Caixa")

    escolha = input("Digite o número correspondente à unidade de medida desejada: ")

    if escolha == "1":
        unidade_medida = "Litro"
    elif escolha == "2":
        unidade_medida = "Quilograma"
    elif escolha == "3":
        unidade_medida = "Unidade"
    elif escolha == "4":
        unidade_medida = "Caixa"
    else:
        print("Opção inválida. Definindo unidade de medida como 'Indefinida'.")
        unidade_medida = "Indefinida"

    print(f"\nO produto {nome} com quantidade {quantidade}, valor {valor} e unidade de medida {unidade_medida} será salvo no sistema.")
    conf = None
    while (conf not in ["y","n"]):
        conf = input("Deseja continuar ([Y]/n)? ").lower().strip()
        if conf == "y" or conf == "":
            produto.inserir(nome, quantidade, valor, unidade_medida)
            id_produto = produto.get_last_insert_id()
            if verificar_produto_insumo(nome):
                adicionar_produto_insumo(id_produto)
            print("Produto adicionado.")
            break
        if conf == "n":
            print("Salvamento cancelado")
            break
    input("\nPrecione enter para continuar")
    return 1

def listar_produtos():
    produtos = produto.listar()
    if not produtos:
        print("Nenhum produto foi encontrado.")
        input("\nPrecione enter para continuar")
        return 1

    print("Produtos disponíveis:")
    print("-" * 40)
    print(f"{'ID':<5}{'Nome':<15}{'Quantidade':<10}{'Valor':<10}{'Unidade de Medida':<10}")
    print("-" * 40)

    for prod in produtos:
        print(f"{prod[0]:<5}{prod[1]:<15}{prod[2]:<10}{prod[3]:<10}{prod[4]:<10}")

    print("-" * 40)
    input("\nPrecione enter para continuar")
    return 1

def adicionar_item_cardapio():
    nome = input("Digite o nome do item: ")
    descricao = input("Digite a descrição do item: ")
    categoria = input("Digite a categoria do item: ")
    valor = float(input("Digite o valor do item: "))
    disponibilidade = int(input("O item está disponível? (1 para sim, 0 para não): "))
    conf = None
    while (conf not in ["y", "n"]):
        conf = input("Deseja continuar ([Y]/n)? ").lower().strip()
        if conf == "y" or conf == "":
            cardapio.inserir(nome, descricao, categoria, valor, disponibilidade)
            print("Cardápio atualizado.")
            break
        if conf == "n":
            print("Atualização cancelada.")
            break
    
    input("\nPrecione enter para continuar")
    return 1

def listar_cardapio():
    print("Cardápio:")
    itens_cardapio = cardapio.listar()
    
    if not itens_cardapio:
        print("Nenhum item disponível no cardápio.")
        return
    
    print("Itens do cardápio:")
    print("-" * 40)
    for item in itens_cardapio:
        id_cardapio, nome, descricao, categoria, valor, disponibilidade = item
        print(f"ID: {id_cardapio}")
        print(f"Nome: {nome}")
        print(f"Descrição: {descricao}")
        print(f"Categoria: {categoria}")
        print(f"Valor: R$ {valor:.2f}")
        print(f"Disponibilidade: {'Sim' if disponibilidade else 'Não'}")
        print("-" * 40)

    input("Pressione Enter para continuar.")
    return 1

def adicionar_item_insumos():
    print("Adicionar item ao estoque...")
    nome = input("Digite o nome do insumo: ")

    # Exibir as categorias disponíveis
    print("Escolha a categoria do insumo:")
    print("1. Legume")
    print("2. Fruta")
    print("3. Grão")
    print("4. Laticínio")
    print("5. Padaria")
    print("6. Carne")
    print("6. Bebida")

    # Ler a escolha do usuário
    escolha = input("Digite o número correspondente à categoria desejada: ")

    # Mapear a escolha para uma categoria
    if escolha == "1":
        categoria = "Legume"
    elif escolha == "2":
        categoria = "Fruta"
    elif escolha == "3":
        categoria = "Grão"
    elif escolha == "4":
        categoria = "Laticínio"
    elif escolha == "5":
        categoria = "Padaria"
    elif escolha == "6":
        categoria = "Carne"
    elif escolha == "7":
        categoria = "Bebida"
    else:
        print("Opção inválida. Definindo categoria como 'Indefinido'.")
        categoria = "Indefinido"

    unidade_medida = input("Digite a unidade de medida (ex: kg, l, unidades): ")
    quantidade = float(input("Digite a quantidade disponível: "))
    preco = float(input("Digite o preço do insumo: "))

    print(f"\nO insumo {nome} com {quantidade} {unidade_medida} ao preço de {preco} será salvo no sistema.")
    
    conf = None
    while (conf not in ["y","n"]):
        conf = input("Deseja continuar ([Y]/n)? ").lower().strip()
        if conf == "y" or conf == "":
            insumo.inserir(nome, categoria, unidade_medida, quantidade, preco)
            print("Insumo adicionado.")
            break
        if conf == "n":
            print("Salvamento cancelado.")
            break
    input("\nPrecione enter para continuar")
    return 1

def listar_insumos():    
    # Obter a lista de insumos do banco de dados
    lista_insumos = insumo.listar()
    
    if not lista_insumos:
        print("Nenhum insumo cadastrado.")
        return 1
    
    # Cabeçalho
    print(f'{"ID":<5} {"Nome":<20} {"Categoria":<20} {"Unidade":<10} {"Quantidade":<12} {"Preço":<10}')
    
    # Iterar sobre cada linha na lista de insumos e imprimi-los formatados
    for row in lista_insumos:
        id_insumo, nome, categoria, unidade_medida, quantidade, preco = row
        print(f'{id_insumo:<5} {nome:<20} {categoria:<20} {unidade_medida:<10} {quantidade:<12} {preco:<10}')
    input("\nPrecione enter para continuar")
    return 1

def clear():
    # para Windows
    if name == 'nt':
        _ = system('cls')

    # Para Mac e Linux
    else:
        _ = system('clear')
