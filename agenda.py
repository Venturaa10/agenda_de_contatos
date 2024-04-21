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
    for nome in nome_contato:
        lista_contatos.append(nome)
    
    print(f'O Contato {nome_contato} foi adicionado(a) a sua agenda.\n')
    input('ENTER para voltar ao menu: ')

    return executa_opcoes()

def executa_opcoes():
    limpa_terminal()
    mensagem()
    opcao = int(input('Digite o número da opção que deseja: '))
    if opcao == 1:
        adiciona_contato(opcao)

    return opcao
def main():
    limpa_terminal()
    mensagem()
    executa_opcoes()

if __name__ == '__main__':
    main()