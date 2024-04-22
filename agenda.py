# AGENDA DE CONTATOS
# Desenvolva um programa que permita ao usuário adicionar, visualizar e editar contatos em uma agenda virtual.
'''Importando a biblioteca os'''
import os

'''Lista contendo os contatos'''
lista_contatos = ['João','Vinicius','Michelle']

def limpa_terminal():
    '''Função responsavél por limpar o terminal'''
    os.system('cls')

def continuar(opcao):    
    input('ENTER para continuar: ')

def pula_linha():
    '''Apenas pula linha'''
    print()

def opcao_invalida():
    input('\nOpção Invalída!')


def voltar():
    '''Função responsavél por retornar ao menu'''
    return escolhe_opcao()    

def mensagem():
    '''Função responsavél por exibir a mensagem com as opções possiveis na agenda'''
    print('''
=============== AGENDA VIRTUAL ================
            INFORME UMA DAS OPÇÕES ABAIXO:

[ 1 ] - ADICIONAR AOS CONTATOS  
[ 2 ] - VISUALIZAR LISTA DE COTATOS 
[ 3 ] - EDITAR CONTATOS
[ 0 ] - DESLOGAR                                                        
=================================================== ''')
    pula_linha()

def adiciona_contato(opcao):
    '''Função responsavél por adicionar um contato a agenda do usuario'''
    print('0 -> Para voltar ao menu!\n')
    nome_contato = input('Nome do contato: ').capitalize().strip()

    if nome_contato == '0':
        voltar()

    if len(nome_contato) < 0 or len(nome_contato) < 2:
        print('CONTATO NÃO ADICIONADO A LISTA\n')
        print('Deve conter no minimo 2 caracteres!')
        continuar(opcao)
        limpa_terminal()
        return adiciona_contato(opcao)

    if nome_contato in lista_contatos:
        print(f'O contato {nome_contato} já existe na sua agenda\n')
        continuar(opcao)
        limpa_terminal()
        return adiciona_contato(opcao)

    else:
        lista_contatos.append(nome_contato)
        print(f'O Contato {nome_contato} foi adicionado(a) a sua agenda.\n')
        continuar(opcao)  
        limpa_terminal()
        return escolhe_opcao()       
def apenas_exibi_a_lista():
    '''Função resposanvél por apenas exibir a lista de contatos'''
    print('LISTA DE CONTATOS')
    '''Arrumei a exibição da lista de contatos, porém tenho que fazer um tratamento quando o usuario buscar o contato pelo número.'''
    for indice, i in enumerate(lista_contatos):
        print(f'{indice} - {i}')   

def visualizar_lista(opcao):
    '''Função resposanvél por exibir a lista de contato e voltar ao menu'''
    print('LISTA DE CONTATOS')
    '''Arrumei a exibição da lista de contatos, porém tenho que fazer um tratamento quando o usuario buscar o contato pelo número.'''
    for indice, i in enumerate(lista_contatos):
        print(f'{indice} - {i}')   

    pula_linha()
    continuar(opcao)
    return escolhe_opcao()

def editar_contato(opcao):
    '''Função responsavél por editar o nome do contato'''
    limpa_terminal()
    print('FAZER A LOGICA PARA EDITAR')
    print('0 -> Para voltar ao menu!\n')
    apenas_exibi_a_lista()

    try:
        editar = int(input('\nNúmero do contato a editar: '))
    except:
        opcao_invalida()
        return editar_contato(opcao)   
        
    if editar == 0:
        return escolhe_opcao()

def excluir_contato(opcao):
    '''Função responsavél por excluir o contato'''
    limpa_terminal()
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
    try:
        contato_excluido = lista_contatos.pop(excluir)
    except:
        pula_linha()
        input(f'O contato número {excluir} não existe, tente novamente!')
        return excluir_contato(opcao)
    
    print(f'O contato {contato_excluido} foi excluído!')        
    print(lista_contatos)
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
    '''Função responsavél pela execução da função que o usuario desejar fazer'''
    limpa_terminal()
    mensagem()
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
    mensagem()
    escolhe_opcao()

if __name__ == '__main__':
    main()