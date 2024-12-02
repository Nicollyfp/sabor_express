import os

lista_de_restaurantes = [{'nome':'Praça', 'categoria':'japonesa', 'ativo':False },
                         {'nome':'Pizza suprema', 'categoria':'italiana', 'ativo':True},
                         {'nome':'Cantina', 'categoria':'Escolar', 'ativo':False }]

def exibir_nome():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def opcoes():
    print('1. Cadastrar restaurante')
    print('2. listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def voltar_menu():
    input('\nClique em uma tecla para voltar ao menu principal ')
    main()

def subtitulo(texto):
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    subtitulo('Cadrastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    lista_de_restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | Status')
    for restaurante in lista_de_restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurnate = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | - {categoria_restaurante.ljust(20)} | - {ativo_restaurnate.ljust(20)}')
    voltar_menu()

def altenar_estado_restaurante():
    subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in lista_de_restaurantes:

        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo']:
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso!')
            else:
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso!')
            break

    if not restaurante_encontrado:
        print('O restaurante não foi cadastrado, volte ao menu para cadastrar')
            
    voltar_menu()

def finalizar_app():
    subtitulo('Finalizando o app')

def opcao_invalida():
    subtitulo('OPÇÃO INVÁLIDA')
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            altenar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()