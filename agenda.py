# Agenda de contatos virtual
# Desenvolvendo um programa que permite ao usuário adicionar, visualizar,excluir e editar contatos em uma agenda virtual.
'''Importando a biblioteca os'''
import os

'''Lista contendo os contatos'''
lista_contatos = []

def limpa_terminal():
    '''Função responsavél por limpar o terminal'''
    os.system('cls')

def continuar(opcao):    
    '''
    - Exibe um input para continuar o programa
    '''
    input('ENTER para continuar: ')

def msg_nome_invalido():
    print('Nome inválido')
    print('Deve conter no minímo 2 caracteres!')
    pula_linha()

def pula_linha():
    '''Apenas pula linha'''
    print()

def opcao_invalida():
    '''
    - Exibe um input com um tipo de mensagem de erro
    '''
    input('\nOpção Invalída!')

def voltar():
    '''Função responsavél por retornar ao menu'''
    return escolhe_opcao()    

def mensagem_menu():
    '''Função responsavél por exibir a mensagem com as opções possiveis na agenda'''
    print('''
        ================= AGENDA VIRTUAL ==================
            INFORME UMA DAS OPÇÕES ABAIXO:

                [ 1 ] - ADICIONAR AOS CONTATOS  
                [ 2 ] - VISUALIZAR LISTA DE COTATOS 
                [ 3 ] - EDITAR CONTATOS
                [ 0 ] - DESLOGAR                                                        
        ==================================================''')
    pula_linha()

def adiciona_contato(opcao):
    '''Função responsavél por adicionar um contato a agenda do usuario
    - Recebe o novo contato do usuario
    - Faz a validação da quantidade de caracteres e se o contato já existe
    - Armezana o novo contato do usuario na lista caso seja valido
    - Metodo capitalize -> Retorna a primeira letra da string maiuscula e o restante minusculo
    - Metodo strip -> Remove os espaços vazios do input, evitando os "espaços" do teclado do usuario
    '''
    print('0 -> Para voltar ao menu!\n')
    apenas_exibi_a_lista()
    pula_linha()
    nome_contato = input('Nome do contato: ').capitalize().strip()

    if nome_contato == '0':
        voltar()

    elif len(nome_contato) < 0 or len(nome_contato) < 2:
        msg_nome_invalido()
        continuar(opcao)
        limpa_terminal()
        return adiciona_contato(opcao)

    elif nome_contato in lista_contatos:
        print(f'O contato {nome_contato} já existe na sua agenda\n')
        continuar(opcao)
        limpa_terminal()
        return adiciona_contato(opcao)

    else:
        lista_contatos.append(nome_contato)
        print(f'O Contato {nome_contato} foi adicionado(a) a sua agenda.\n')
        continuar(opcao)  
        limpa_terminal()
        return adiciona_contato(opcao)       

def apenas_exibi_a_lista():
    '''Função resposanvél por apenas exibir a lista de contatos
    - Cria/Exibe uma lista com os contatos cadastrados pelo usuario
    - Tratei acrescentando +1 no indice, para exibir ao usuario os contatos numerados do 1 em diante, pois aparecer "0 - nome" não tem sentido
    - Fiz tratamentos na função de excluir para que seja excluído o contato correto de acordo com o seu indice
    '''
    print('LISTA DE CONTATOS')
    if len(lista_contatos) == 0:
        pula_linha()
        return print('-----> LISTA DE CONTATOS VAZIA! <-----')
    else:
        for indice, i in enumerate(lista_contatos):
            print(f'{indice + 1} - {i}')   

def visualizar_lista(opcao):
    '''Função resposanvél por exibir a lista de contato e voltar ao menu'''
    apenas_exibi_a_lista()
    pula_linha()
    continuar(opcao)
    return escolhe_opcao()

def editar_contato(opcao):
    '''Função responsavél por editar o nome do contato
    - A variavel "editar" recebe o número do contato que é exibido na lista a qual o usuario deseja editar
    - Tratamentos de erros nas variaveis "editar" e "novo_nome" caso receba valores inválidos ou número de contato inexistente na lista
    - Validação de caracteres do novo nome recebido pelo usuario
    - O -1 é para tratar e o programa pegar o indice do usuario correto, o contato do indice 0 é exibido com o número 1 na lista de contato para o usuario, assim em diante.
    - Metodo capitalize -> Retorna a primeira letra da string maiuscula e o restante minusculo
    - Metodo strip -> Remove os espaços vazios do input, evitando os "espaços" do teclado do usuario
    '''
    limpa_terminal()
    print('TELA PARA EDITAR O CONTATO!')
    pula_linha()
    print('0 -> Para voltar ao menu!\n')
    apenas_exibi_a_lista()

    try:
        editar = int(input('\nNúmero do contato a editar: '))
    except:
        opcao_invalida()
        return editar_contato(opcao)   
        
    if editar == 0:
        return escolhe_opcao()

    elif editar < 0:
        opcao_invalida()
        return editar_contato(opcao)
    
    try:
        novo_nome = input(f'Digite o novo nome do contato "{lista_contatos[editar - 1]}": ').capitalize().strip()

    except:
        pula_linha()
        input(f'O contato número {editar} não existe, tente novamente!')
        return editar_contato(opcao) 

    if len(novo_nome) < 0 or len(novo_nome) < 2:
        msg_nome_invalido()
        continuar(opcao)
        limpa_terminal()
        return editar_contato(opcao)
    else:
        print(f'O contato "{lista_contatos[editar - 1]}" foi alterado(a) para "{novo_nome}"')
        lista_contatos[editar - 1] = novo_nome
        
    pula_linha()
    continuar(opcao)
    return editar_contato(opcao)

def excluir_contato(opcao):
    '''Função responsavél por excluir o contato
    - Tratamento de erro em caso de valores invalidos no input "excluir"
    - Tratamento de erro na variavel "contato_excluido" em caso de indice/número do contato fornecido pelo usuario seja inexistente
    - Tratei a variavel "contato_excluido", pois caso o usuario queira excluir o contato de número 1, o indice desse contato é 0, devido ao tratamento que fiz ao exibir a lista de contatos ao usuario acrescentando +1 ao exibir o indice. Logo contato número 1 = indice 0, assim em diante
    - Mensagem exibindo o nome do contato excluído 
    - Return do contato excluido para atualizar a lista
    '''
    limpa_terminal()
    print('TELA PARA EXCLUIR O CONTATO!')
    pula_linha()
    print('0 -> Para voltar ao menu!\n')
    apenas_exibi_a_lista()
    pula_linha()
    try:
        excluir = int(input('Número do contato a excluir: '))
    except:
        opcao_invalida()
        return excluir_contato(opcao)
    
    if excluir == 0:
        return escolhe_opcao()
    elif excluir < 0:
        opcao_invalida()
        return excluir_contato(opcao)

    try:
        contato_excluido = lista_contatos.pop(excluir - 1)
    except:
        pula_linha()
        input(f'O contato número {excluir} não existe, tente novamente!')
        return excluir_contato(opcao)
    
    print(f'O contato "{contato_excluido}" foi excluído!')        
    # print(lista_contatos)
    pula_linha()
    continuar(opcao)
    return excluir_contato(opcao),contato_excluido

def editar_lista(opcao):
    '''Função responsavél por fazer alterações na lista de contatos, como editar ou excluir contato'''
    limpa_terminal()
    print('''
        5 - EDITAR
        6 - EXCLUIR
        0 - VOLTAR AO MENU
                    ''')
    try:
        opcao_editar = int(input('Número da opção desejada: ')) 
    except:
        opcao_invalida()
        return editar_lista(opcao)
    
    if opcao_editar == 5:
        '''Função editar aqui'''
        editar_contato(opcao)
     
    elif opcao_editar == 6:
        '''Função excluir aqui'''
        excluir_contato(opcao)
        
    elif opcao_editar == 0:
        voltar()

    else:
        opcao_invalida()
        return editar_lista(opcao)


def escolhe_opcao():
    '''Função responsavél pela execução da função que o usuario desejar fazer
    - Tratamento de erro no input "opcao"
    - Exibe o texto com as opções disponiveis e o número correspondente
    - Condicionais para executar a função de acordo com o número recebido pelo usuario
    '''
    limpa_terminal()
    mensagem_menu()
    try:
        opcao = int(input('Digite o número da opção que deseja: '))
    except:
        opcao_invalida()
        return escolhe_opcao()
    
    if opcao == 1:
        limpa_terminal()
        adiciona_contato(opcao)
    elif opcao == 2:
        limpa_terminal()
        visualizar_lista(opcao)

    elif opcao == 3:
        limpa_terminal()
        editar_lista(opcao)

    elif opcao == 0:
        deslogar()
        
    else:
        opcao_invalida()
        return escolhe_opcao()
        
    return opcao


def deslogar():
    '''Função responsavél por encerrar o programa'''
    limpa_terminal()
    print('DESLOGADO!')

def main():
    limpa_terminal()
    mensagem_menu()
    escolhe_opcao()

if __name__ == '__main__':
    main()