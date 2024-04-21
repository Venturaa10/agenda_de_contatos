# AGENDA DE CONTATOS
# Desenvolva um programa que permita ao usuário adicionar, visualizar e editar contatos em uma agenda virtual.
'''Importando a biblioteca os'''
import os

'''Dicionario contendo os contatos'''

contatos = []

def mensagem():
    print('''
=============== AGENDA VIRTUAL ================
            INFORME UMA DAS OPÇÕES ABAIXO:

[ 1 ] - ADICIONAR AOS CONTATOS  
[ 2 ] - VISUALIZAR LISTA DE COTATOS 
[ 3 ] - EDITAR CONTATOS
[ 0 ] - DESLOGAR                                                        
=================================================== ''')

def main():
    mensagem()

if __name__ == '__main__':
    main()