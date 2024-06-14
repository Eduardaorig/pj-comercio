from ConexaoBD import conexao
from datetime import datetime, date
from bd import * 
from mysql.connector import Error

condb = conexao()



while True: 

    opc= int(input("0. sair\n1. cadastrar produto\n2. cadastrar fornecedor\n3. cadastrar funcionario\n4. cadastrar cliente\n5. cadastrar promocoes\n6. atualizar produtos\n7. atualizar fornecedores\n8. atualizar funcionarios\n9. atualizar clientes\n10. atualizar promocoes\n11. deletar produtos\n12. deletar fornecedores\n13. deletar funcionarios\n14. deletar clientes\n15. deletar promocoes\n16. listar produtos\n17. listar fornecedores\n18. listar funcionarios\n19. listar clientes\n20. listar promocoes\n21. fazer pedidos:  "))

    if opc == 0: break

    elif opc == 1:
        nproduto = input('digite nome: ')
        dproduto = input('digite a descrição: ')
        pproduto = float(input('digite o preço: '))
        quantEstoque = int(input('digite a quantidade do estoque: '))
        opc_cat = input ('a categoria já existe? s/n')
        if opc_cat == 's': 
            nome_cat = input('digite o nome da categoria: ')
            descricao_cat = '' 
        
        else: 
            nome_cat = input('digite o nome da categoria: ')
            descricao_cat = ('digite a descrição da categoria: ')
        
        opc_for = input('o fornecedor já existe? s/n')
        if opc_for == 's':
            nome_for = input('digite o nome do fornecedor: ')

        else:
            nome_for = input ('digite o nome do fornecedor: ')
            contato_for = input ('digite o contato do fornecedor: ')
            endereco_for = input ('digite o endereço do fornecedor: ')
        

        cadastrarprodutos (condb, nproduto, dproduto, pproduto, quantEstoque, nome_cat, descricao_cat, nome_for, contato_for, endereco_for, opc_cat, opc_for)
    

    elif opc == 2:

        nome = input('digite nome do fornecedor: ')
        contato = input('digite o contato: ')
        endereco = input('digite o endereço: ')


        cadastrarfornecedor (condb, nome, contato, endereco)


    elif opc == 3:

        nome = input('digite nome do funcionário: ')
        cargo = input('digite o cargo: ')
        departamento = input('digite o departamento: ')
        

        cadastrarfuncionario (condb, nome, cargo, departamento)


    elif opc == 4:
        nome = input('digite o nome do cliente: ')
        sobrenome = input('digite o sobrenome: ')
        endereco = input('digite o endereço: ')
        cidade = input('digite a cidade: ')
        codigopostal = input('digite o código postal: ') 


        cadastrarclientes (condb, nome, sobrenome, endereco, cidade, codigopostal)


    elif opc == 5:
        nome = input('digite o nome: ')
        descricao = input('digite a descricao: ')
        datainicio = input('digite a datainicio: ')
        datafim = input('digite a datafim: ')
        

        cadastrarpromocoes (condb, nome, descricao, datainicio, datafim)


    elif opc == 6:
        nproduto = input('digite nome do produto: ')
        dproduto = input('digite a descrição: ')
        pproduto = input('digite o produto: ')
        id_produto = int(input('digite o id do produto que deseja atualizar: '))


        atualizarprodutos (condb, nproduto, dproduto, pproduto, id_produto)
    

    elif opc == 7:

        nome = input('digite o nome do fornecedor: ')
        contato = input('digite o contato: ')
        endereco = input('digite o endereco: ')
        id_fornecedor = int(input('digite o id do fornecedor: '))


        atualizarfornecedor (condb, nome, contato, endereco, id_fornecedor)


    elif opc == 8:

        nome = input('digite o nome do funcionário: ')
        cargo = input('digite o cargo: ')
        departamento = input('digite o departamento: ')
        id_funcionario = int(input('digite o id do funcionário: '))


        atualizarfuncionario (condb, nome, cargo, departamento, id_funcionario)


    elif opc == 9:
        nome = input('digite o nome do cliente: ')
        sobrenome = input('digite o sobrenome: ')
        endereco = input('digite o endereço: ')
        cidade = input('digite a cidade: ')
        codigopostal = input('digite o código postal: ')
        id_cliente = int(input('digite o id do cliente: '))


        atualizarcliente (condb, nome, sobrenome, endereco, cidade, codigopostal, id_cliente)


    elif opc == 10:

        nome = input('digite o nome da promoção: ')
        descricao = input('digite a descrição: ')
        datainicio = input('digite a datainicio: ')
        datafim = input('digite a datafim: ')
        id_promocoes = int(input('digite o id de promocões: '))


        atualizarpromocoes (condb, nome, descricao, datainicio, datafim, id_promocoes)


    elif opc == 11:

        id_produto =int(input('digite o id do produto que deseja deletar: '))
        opc = input('deseja realmente deletar este produto? s/n ')
        if opc == 's':
           deletarprodutos(condb,id_produto)
        else: break

    elif opc == 12:

        id_fornecedor = int(input('digite o id do fornecedor que deseja deletar: '))
        opc = input('deseja realmente deletar este produto? s/n ')
        if opc == 's':
            deletarfornecedores(condb,id_fornecedor)
        else: break

    elif opc == 13:
        
        id_funcionario = int(input('digite o id do funcionário que deseja deletar: '))
        opc = input('deseja realmente deletar este funcionário? s/n ')
        if opc == 's':
            deletarfuncionarios(condb, id_funcionario)
        else: break
        
    elif opc == 14:
        id_cliente = int(input('digite o id do cliente que deseja deletar: '))
        opc = input('deseja realmente deletar este cliente? s/n ')
        if opc == 's':
            deletarclientes(condb, id_cliente)
        else: break

   
    elif opc == 15:
         id_promocoes = int(input('digite o id da promoção: '))
         opc = input('deseja realmente deletar esta promoção? s/n ')
         if opc == 's':
            deletarpromocoes(condb, id_promocoes)
         else: break
    
    
    elif opc == 16:
        listarprodutos (condb)

    
    elif opc == 17:
        listarfornecedor (condb)
        
    
    elif opc == 18:
        listarfuncionarios (condb)


    elif opc == 19:
        listarclientes (condb)

    elif opc == 20:
        listarpromocoes (condb)

    elif opc == 21:
        nome = input("digite o nome do cliente: ")
        produto = input("digite o nome do produto: ")
        quantProduto = int(input("digite a quantidade de produtos: "))
        data_atual = date.today()
        realizarPedido (condb, nome, data_atual, produto, quantProduto)
