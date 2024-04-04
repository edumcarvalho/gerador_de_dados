import random
import os

nomes = ['Eduardo','Angela','João','Júlia','Mary jane']
emails = ['teste1@gmail.com','teste1@yeahoo.com','teste1@hotmail.com','teste1@outlook.com','teste1@ig.com']
telefones = ['48-99998888, 98-77773333','65-99994444','45-99992222','32-66662222']
cidades = ['Curitiba', 'Laguna', 'São paulo', 'Fpolis', 'Palhoça']
estados = ['SC', 'RS', 'PR', 'SP', 'RJ']

def gravar_arquivo(texto):
    with open('dados.txt', 'a', encoding='utf-8', newline='') as arquivo:
            arquivo.write(texto+ os.linesep)     

while True:
    print('Bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa, digite "parar"')
    print('-'*50)
    print('Escolha uma ou mais opções abaixo a serem geradas aleatoriamente')
    print('[1] - Nome')
    print('[2] - E-mail')
    print('[3] - Telefone')
    print('[4] - Cidade')
    print('[5] - Estado')
    opcao = input('Digite uma(s) opções:')
    if opcao == 'parar':    
        print('Encerrando o programa.')
        break
    print('-'*50)
    gravar = input('Gostaria de salvar os dados em um arquivo de texto?(s/n)')
    print('-'*50)
    if opcao.find('1')>=0:
        print(random.choice(nomes))
        if gravar == 's':
             gravar_arquivo(random.choice(nomes))
    if opcao.find('2')>=0:
        print(random.choice(emails))
        if gravar == 's':
             gravar_arquivo(random.choice(emails))
    if opcao.find('3')>=0:
        print(random.choice(telefones))
        if gravar == 's':
             gravar_arquivo(random.choice(telefones))
    if opcao.find('4')>=0:
        print(random.choice(cidades))
        if gravar == 's':
             gravar_arquivo(random.choice(cidades))
    if opcao.find('5')>=0:
        print(random.choice(estados))
        if gravar == 's':
             gravar_arquivo(random.choice(estados))
    
    print('-'*50)
    
        