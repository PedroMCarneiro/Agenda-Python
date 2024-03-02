
agenda={}


def inluirContato(nome,telefone):
    agenda[nome]=telefone
def buscarContatos():
    if len(agenda)==0:
        print("Agenda vazia!!")
    else:
        for i in agenda.items():
            print(i)        
def buscarContato(nome):
    if nome in agenda:
        print(nome, " - ", agenda[nome])
def alterarContato(nome):
    pass
def excluirContato(nome):
    if nome in agenda:
        agenda.pop(nome)
    else:
        print("Contato não encontrado!")
def limparAgenda():
    agenda.clear()

sair = False

while sair!=True:
   
    opcao = int(input("Escolha uma opção: \n 1 - Adicionar contato; \n 2 - Alterar contato; \n 3 - Mostrar todos os contatos; \n 4 - Buscar contato; \n 5 - Excluir contato; \n 6 - Limpar agenda; \n 0 - Sair; \n"))   
    
    if opcao==1:
        nome = input("Informe o nome: ")
        telefone = input("Informe o telefone: ")
        
        inluirContato(nome,telefone)
    elif opcao==2:
        nome = input("Informe o nome: ")
        telefone = input("Informe um novo telefone telefone: ")
        alterarContato(nome,telefone)
    elif opcao==3:
        buscarContatos()
    elif opcao==4:
        nome = input("Informe o nome: ")
        buscarContato(nome)
    elif opcao==5:
        nome = input("Informe o nome: ")
        excluirContato(nome)
    elif opcao==6:
        limparAgenda()
    elif opcao==0:
        sair=True
    else:
        print("Opção inválida!!")