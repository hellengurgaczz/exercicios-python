# Cabeçalho do arquivo ex4.py
"""
Exercício 4: "Banco de Dados" de dicionários.
"""

# Dicionário global para armazenar os usuários
banco_usuarios = []

def cadastrar_usuario(campos_obrigatorios):
    """
    Função para cadastrar um usuário de maneira flexível.

    Args:
    campos_obrigatorios (tuple): Uma tupla com os campos obrigatórios para cadastro.

    Returns:
    dict: O dicionário gerado com os dados do usuário.
    """
    usuario = {}
    print("Digite os dados do usuário:")
    
    for campo_obrigatorio in campos_obrigatorios:
        valor = input(f"{campo_obrigatorio}: ")
        usuario[campo_obrigatorio] = valor
    
    while True:
        campo_extra = input("Digite um campo extra (ou 'sair' para finalizar): ")
        if campo_extra.lower() == 'sair':
            break
        valor_extra = input(f"{campo_extra}: ")
        usuario[campo_extra] = valor_extra
    
    banco_usuarios.append(usuario)
    return usuario

def imprimir_usuarios(*args, **kwargs):
    """
    Função para imprimir os dados dos usuários de acordo com as opções especificadas.

    Args:
    *args: Argumentos posicionais que podem ser nomes de usuários.
    **kwargs: Argumentos nomeados que são campos e valores de filtro.

    Exemplos de chamada:
    - imprimir_usuarios() -> Imprime todos os usuários com todas as informações.
    - imprimir_usuarios("alberto", "joaquina", "enzo", "valentina") -> Imprime os dados dos usuários com os nomes especificados.
    - imprimir_usuarios(campo="endereço", valor="xv de novembro", campo2="idade", valor2="20") -> Imprime os dados dos usuários que satisfazem às condições especificadas.
    """
    if not args and not kwargs:
        for usuario in banco_usuarios:
            print(usuario)
    elif args and not kwargs:
        for nome in args:
            for usuario in banco_usuarios:
                if usuario['nome'] == nome:
                    print(usuario)
    elif not args and kwargs:
        for usuario in banco_usuarios:
            satisfaz_condicoes = True
            for campo, valor in kwargs.items():
                if campo not in usuario or usuario[campo] != valor:
                    satisfaz_condicoes = False
                    break
            if satisfaz_condicoes:
                print(usuario)
    elif args and kwargs:
        for nome in args:
            for usuario in banco_usuarios:
                if usuario['nome'] == nome:
                    satisfaz_condicoes = True
                    for campo, valor in kwargs.items():
                        if campo not in usuario or usuario[campo] != valor:
                            satisfaz_condicoes = False
                            break
                    if satisfaz_condicoes:
                        print(usuario)

# Menu principal
campos_obrigatorios = tuple(input("Digite os campos obrigatórios para cadastro (separados por vírgula): ").split(","))
while True:
    print("\nMenu:")
    print("1 - Cadastrar usuário")
    print("2 - Imprimir usuários")
    print("0 - Encerrar")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        usuario_cadastrado = cadastrar_usuario(campos_obrigatorios)
        print(f"Usuário cadastrado: {usuario_cadastrado}")
    elif opcao == '2':
        print("\nOpções de impressão:")
        print("1 - Imprimir todos")
        print("2 - Filtrar por nomes")
        print("3 - Filtrar por campos")
        print("4 - Filtrar por nomes e campos")
        sub_opcao = input("Digite a sub-opção: ")
        if sub_opcao == '1':
            imprimir_usuarios()
        elif sub_opcao == '2':
            nomes = input("Digite os nomes para filtro (separados por vírgula): ").split(",")
            imprimir_usuarios(*nomes)
        elif sub_opcao == '3':
            campos = input("Digite os campos para filtro (separados por vírgula): ").split(",")
            valores = input("Digite os valores correspondentes (separados por vírgula): ").split(",")
            filtro_kwargs = {}
            for i in range(len(campos)):
                filtro_kwargs[campos[i]] = valores[i]
            imprimir_usuarios(**filtro_kwargs)
        elif sub_opcao == '4':
            nomes = input("Digite os nomes para filtro (separados por vírgula): ").split(",")
            campos = input("Digite os campos para filtro (separados por vírgula): ").split(",")
            valores = input("Digite os valores correspondentes (separados por vírgula): ").split(",")
            filtro_kwargs = {}
            for i in range(len(campos)):
                filtro_kwargs[campos[i]] = valores[i]
            imprimir_usuarios(*nomes, **filtro_kwargs)
    elif opcao == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")
