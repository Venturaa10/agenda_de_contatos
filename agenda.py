# AGENDA DE CONTATOS
# Desenvolva um programa que permita ao usuário adicionar, visualizar e editar contatos em uma agenda virtual.
'''Importando a biblioteca os'''
import os

'''Dicionario contendo os contatos'''

lista_contatos = []

def limpa_terminal():
    os.system('cls')


def mensagem():
    print('''
=============== AGENDA VIRTUAL ================
            INFORME UMA DAS OPÇÕES ABAIXO:

[ 1 ] - ADICIONAR AOS CONTATOS  
[ 2 ] - VISUALIZAR LISTA DE COTATOS 
[ 3 ] - EDITAR CONTATOS
[ 0 ] - DESLOGAR                                                        
=================================================== ''')
    print() #Pula linha

def adiciona_contato(opcao):
    limpa_terminal()
    nome_contato = input('Nome do contato: ').capitalize()
    if nome_contato in lista_contatos:
        print(f'O contato {nome_contato} já existe na sua agenda\n')
        input('ENTER para voltar ao menu: ')        
    else:
        lista_contatos.append(nome_contato)
        print(f'O Contato {nome_contato} foi adicionado(a) a sua agenda.\n')
        input('ENTER para voltar ao menu: ')            

    return executa_opcoes()

def visualizar_lista():
    limpa_terminal()
    print('LISTA DE CONTATOS')
    '''A lista está sendo exibida de maneira incorreta'''
    for num in range(0,len(lista_contatos)):
        num = num + 1
        for c in lista_contatos:
            print(f'{num} - {c}')

def executa_opcoes():
    limpa_terminal()
    mensagem()
    opcao = int(input('Digite o número da opção que deseja: '))
    if opcao == 1:
        adiciona_contato(opcao)
    elif opcao == 2:
        visualizar_lista()

    return opcao
def main():
    limpa_terminal()
    mensagem()
    executa_opcoes()

if __name__ == '__main__':
    main()