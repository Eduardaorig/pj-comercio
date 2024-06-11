def cadastrarprodutos(condb,nome,descricao,preco, quantEstoque, nome_cat, descricao_cat):
    mycursor = condb.cursor()
    sql = "INSERT INTO produtos (nome, descricao, preco) VALUES (%s,%s,%s)"
    valores= (nome, descricao, preco)
    mycursor.execute(sql,valores)
    ID_Produto = mycursor.lastrowid

    sql1 = "INSERT INTO estoque (ID_Produto, Quantidade) VALUES (%s, %s)"
    val1 = (ID_Produto, quantEstoque)
    mycursor.execute(sql1, val1)
    if opc_cat == 's':
        sql3 = 'select ID_Categoria from categoriasprodutos where Nome = %s'
        mycursor.execute(sql3, (nome_cat,))
        id_categoria = mycursor.fetchone()[0]
        int(id_categoria)
        sql4 = 'update produtos set ID_Categoria = %s where ID_Produto = %s'
        val4 = (id_categoria, ID_Produto)
        mycursor.execute(sql, val4)
    else:
        sql2 = "INSERT INTO categoriasprodutos (ID_Categoria, Nome, Descricao) VALUES (%s, %s, %s) "
        val2 = (ID_Produto, nome_cat, descricao_cat)
        mycursor.execute(sql2, val2)
        ID_Categoria = mycursor.execute(sql2, val)
        sql8 = 'update produtos set ID_Categoria = %s where ID_Produto = %s'
        val8 = (ID_Categoria, ID_Produto) 
        mycursor.execute(sql8, val8)
    
    if opc_for== 's':
        sql5 = 'select ID_Fornecedor from fornecedores where Nome = %s'
        mycursor.execute(sql5,(nome_for,))
        id_fornecedor = mycursor.fetchone ()[0]
        int(id_fornecedor)
        sql6 = 'update produtos set ID_Fornecedor = %s where ID_Produto %s'
        val6 = (id_fornecedor, ID_Produto)
        mycursor.execute(sql6, val6)

    else: 
        sql7 = "insert into fornecedor (Nome, contato, endereco) VALUES (%s, %s, %s)"
        val7 = (nome_for, contato_for, endereco_for)
        mycursor.execute (sql7, val7) 
        ID_Fornecedor = mycursor.lastrowid
        sql9 = 'update produtos set ID_Fornecedor = %s where ID_Produto = %s'
        val9 = (id_fornecedor, ID_Produto)
        mycursor.execute (sql9, val9)

    condb.commit()         
    print ('produto cadastrado com sucesso')
    mycursor.close()

def cadastrarfornecedor  (condb, nome, contato, endereco):
    mycursor = condb.cursor()
    sql = "insert into fornecedores (nome, contato , endereco) VALUES (%s, %s, %s)"
    valores= (nome, contato, endereco)
    mycursor.execute(sql, valores)
    condb.commit()
    print ('fornecedor cadastrado com sucesso')
    mycursor.close()

def cadastrarfuncionario (condb, nome, cargo, departamento):
    mycursor = condb.cursor()
    sql = "insert into funcionarios (nome, cargo, departamento) VALUES (%s, %s, %s)"
    valores= (nome, cargo, departamento)
    mycursor.execute(sql, valores)
    condb.commit()
    print ('funcionario cadastrado com sucesso')
    mycursor.close()

def cadastrarclientes (condb, nome, sobrenome, endereco, cidade, codigopostal):
    mycursor = condb.cursor()
    sql = "insert into clientes (nome, sobrenome, endereco, cidade, codigopostal) VALUES (%s, %s, %s, %s, %s)"
    valores= (nome, sobrenome, endereco, cidade, codigopostal)
    mycursor.execute(sql, valores)
    condb.commit()
    print ('cliente cadastrado com sucesso')
    mycursor.close()

def cadastrarpromocoes (condb, nome, descricao, datainicio, datafim):
    mycursor = condb.cursor()
    sql = "insert into clientes (nome, descricao, datainicio, datafim) VALUES (%s, %s, %s, %s)"
    valores= (nome, descricao, datainicio, datafim)
    mycursor.execute(sql, valores)
    condb.commit()
    print ('ciente cadaastrado com sucesso')
    mycursor.close()

def atualizarprodutos (condb, nome, descricao, preco, id_produto):
    mycursor = condb.cursor()
    sql = "update produtos set Nome = %s, Descricao = %s, Preco = %s where ID_Produto = %s; "
    valores= (nome, descricao, preco, id_produto)
    mycursor.execute(sql, valores)
    condb.commit()
    print ('produto atualizado com sucesso')
    mycursor.close()

def atualizarfornecedor (condb, nome, contato, endereco, id_fornecedor):
    mycursor = condb.cursor()
    sql = "update fornecedores set Nome = %s, Contato = %s, Endereco = %s where ID_Fornecedor = %s; "
    valores= (nome, contato, endereco, id_fornecedor)
    mycursor.execute(sql, valores)
    condb.commit()
    print ('fornecedor atualizado com sucesso')
    mycursor.close()
    
def atualizarfuncionario (condb, nome, cargo, departamento, id_funcionario):
    mycursor = condb.cursor()
    sql = "update funcionarios set Nome = %s, Cargo = %s, Departamento = %s where ID_Funcionario = %s; "
    valores= (nome, cargo, departamento, id_funcionario)
    mycursor.execute(sql, valores)
    condb.commit()
    print ('funcionario atualizado com sucesso')
    mycursor.close()

def atualizarcliente (condb, nome, sobrenome, endereco, cidade, codigopostal, id_cliente):
    mycursor = condb.cursor()
    sql = "update clientes set Nome = %s, Sobrenome = %s, Endereco = %s, Cidade = %s, Codigopostal = %s where ID_Cliente = %s; "
    valores= (nome, sobrenome, endereco, cidade, codigopostal, id_cliente)
    mycursor.execute(sql, valores)
    condb.commit()
    print ('cliente atualizado com sucesso')
    mycursor.close()

def atualizarpromocoes (condb, nome, descricao, datainicio, datafim, id_promocoes):
    mycursor = condb.cursor()
    sql = "update clientes set Nome = %s, Descricao = %s, DataInicio = %s, DataFim = %s where ID_promocao = %s; "
    valores = (nome, descricao, datainicio, datafim, id_promocoes)
    mycursor.execute(sql, valores)
    condb.commit()
    print ('promocoes atualizado com sucesso')
    mycursor.close()

def deletarprodutos (condb, id_produto):
    mycursor = condb.cursor()
    sql = "delete from produtos where ID_Produto = %s "
    valores = (id_produto, )
    mycursor.execute(sql,valores)
    condb.commit()
    print ('produto deletado com sucesso')
    mycursor.close()

def deletarfornecedores (condb, id_fornecedor):
    mycursor = condb.cursor()
    sql = "delete from fornecedores where ID_Fornecedor = %s "
    valores = (id_fornecedor, )
    mycursor.execute(sql,valores)
    condb.commit()
    print ('fornecedor deletado com sucesso')
    mycursor.close()

def deletarfuncionarios (condb, id_funcionario):
    mycursor = condb.cursor()
    sql = "delete from funcionarios where ID_Funcionario = %s "
    valores = (id_funcionario, )
    mycursor.execute(sql, valores)
    condb.commit()
    print ('fornecedor deletado com sucesso')
    mycursor.close()

def deletarclientes (condb, id_cliente):
    mycursor = condb.cursor()
    sql = "delete from clientes where ID_Cliente = %s "
    valores = (id_cliente, )
    mycursor.execute(sql, valores)
    condb.commit()
    print ('cliente deletado com sucesso')
    mycursor.close()

def deletarpromocoes (condb, id_promocoes):
    mycursor = condb.cursor()
    sql = "delete from promocoes where ID_Promocoes = %s "
    valores = (id_promocoes, )
    mycursor.execute(sql, valores)
    condb.commit()
    print ('promoçao deletado com sucesso')
    mycursor.close()

def listarprodutos (condb):
    mycursor = condb.cursor()
    sql = "select * from produtos"
    mycursor.execute(sql)
    produtos = mycursor.fetchall()
    for produto in produtos:
        print(f'{produto[1]}, {produto[2]}, {produto[3]}')

def listarfornecedor (condb):
    mycursor = condb.cursor()
    sql = "select * from fornecedores"
    mycursor.execute(sql)
    fornecedores = mycursor.fetchall()
    for fornecedor in fornecedores:
        print(f'{fornecedor[1]}, {fornecedor[2]}, {fornecedor[3]}')
    
def listarfuncionarios (condb):
    mycursor = condb.cursor()
    sql = "select * from funcionarios"
    mycursor.execute(sql)
    funcionarios = mycursor.fetchall()
    for funcionario in funcionarios:
        print(f'{funcionarios[1]}, {funcionarios[2]}, {funcionarios[3]}')

def listarclientes (condb):
    mycursor = condb.cursor()
    sql = "select * from clientes"
    mycursor.execute(sql)
    clientes = mycursor.fetchall()
    for cliente in clientes:
        print(f'{clientes[1]}, {clientes[2]}, {clientes[3]}, {clientes[4]}')

def listarpromocoes (condb):
    mycursor =  condb.cursor()
    sql = "select * from promocoes"
    mycursor.execute(sql)
    promocoes = mycursor.fetchall()
    for promocao in promocoes:
        print(f'{promocoes[1]}, {promocoes[2]}, {promocoes[3]}, {promocoes[4]}')

def obterProdutoID(condb, nome):
    try:
        with mycondb.cursor() as cursor:
            sql = 'SELECT ID_Produto FROM produtos WHERE Nome = %s'
            mycursor.execute(sql, (nome,))
            resultado = mycursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                print(f"Produto com nome '{nome}' não encontrado.")
                return None
    except Error as e:
        print(f"Ocorreu um erro ao obter o ID do produto: {e}")
        return None


def deletarProduto(condb, nome_produto):
    try:
        produto_id = obterProdutoID(condb, nome_produto)
        if not produto_id:
            return

        condb.start_transaction()
        with conbd.cursor() as cursor:
            sql_detalhes_pedido = 'DELETE FROM detalhespedido WHERE ID_Produto = %s'
            mycursor.execute(sql_detalhes_pedido, (produto_id,))
    
        with condb.cursor() as cursor:
            sql_estoque = 'DELETE FROM estoque WHERE ID_Produto = %s'
            mycursor.execute(sql_estoque, (produto_id,))
        
        with condb.cursor() as cursor:
            sql_produto = 'DELETE FROM produtos WHERE ID_Produto = %s'
            mycursor.execute(sql_produto, (produto_id,))
        condb.commit()
        print("Produto e suas referências deletadas com sucesso")

    except Error as e:
        conbd.rollback()
        print(f"Ocorreu um erro ao deletar o produto: {e}")

    finally:
        condb.close()

def 

