# #Tipo de seguro
# dtatual = datetime.datetime.now()
# cont = 0
# opcao = 0
# seg1 = '1- Para ciclistas que pedalam na rua'
# seg2 = '2- Para ciclistas de maratona'
# seg3 = '3- Para ciclistas que pedalam em montanhas'
# seg4 = '4- Para ciclistas que pedalam em pedras e rochas'
# seg5 = '5- Para ciclistas que pedalam em terra e mato'
# seg6 = '6- Para ciclistas por hobbie'
# seg7 = '7- Para ciclistas que viajam com a bike'
# opcSeguro = 0

# # #Dados do cliente
# # nome = 0
# # email = 0
# # rg = 0
# # cnh = 0
# # cpf = 0
# # telefone = 0
# # endereco = 0
# # cep = 0
# # bairro = ''
# # numresidencia = 0
# # complemento = ""
# # cidade = ""
# # estado = ""
# # pais = ""
# # cadastro = 0
# # confCli = 0

# #Bike
# numserie = 0
# modelo = 0
# valorbike = 0
# cor = 0
# ntfiscal = 0
# acessorios = 0
# registro = 0

# #Vistoria
# aprovado = 0
# reprovado = 0
# emAnalise = True
# faltandoDocs = 0

# #Feedback
# fbescolha = 0
# fbtempo = 0
# fbservicos = 0
# fbproblemas = 0
# fbatendimentos = 0
# fbduvidas = 0

# #Relatório
# cadastro = 0
# registro_bike = 0

#Para o cliente confirmar se o que informou está correto
def Confirmacao():
    print('\nAs informações estão corretas? \n1 - Sim \n2 - Não')
    confirm = int(input('\nSelecione uma opção: '))
    return confirm

#Mostrar os tipos de seguro
def TipoSeguro():
        print('\nEssas são as opções de seguro disponibilizadas pela nossa empresa')
        print("\n1- Para ciclistas que pedalam na rua"
                    + "\n2- Para ciclistas de maratona"
                    + "\n3- Para ciclistas que pedalam em montanhas"
                    + "\n4- Para ciclistas que pedalam em pedras e rochas"
                    + "\n5- Para ciclistas que pedalam em terra e mato"
                    + "\n6- Para ciclistas por hobbie"
                    +"\n7- Para ciclistas que viajam com a bike")
        
#Para escolher um tipo de seguro        
def RegistroSeguro():
    confirma = 2
    while confirma != 1:
        print('\nEssas são as opções de seguro disponibilizadas pela nossa empresa')
        print("\n1- Para ciclistas que pedalam na rua"
                    + "\n2- Para ciclistas de maratona"
                    + "\n3- Para ciclistas que pedalam em montanhas"
                    + "\n4- Para ciclistas que pedalam em pedras e rochas"
                    + "\n5- Para ciclistas que pedalam em terra e mato"
                    + "\n6- Para ciclistas por hobbie"
                    +"\n7- Para ciclistas que viajam com a bike")
        
        try:
            seguro = int(input('\nQual dessas opções combina mais com seu estilo?: '))
            if seguro < 1 or seguro > 7:
                print("\nDigite um número válido!")
            confirma = Confirmacao()
            if confirma == 1:
                print('\nSeguro selecionado')
            elif confirma == 2:
                print('\nEscolha novamente o seguro!')    
                seguro = 0
        except ValueError:
            print("Digite um número válido!")
            seguro = 0 
    return confirma

#Para pegar as informações do cliente
def RegistroCliente():

    cdopcao4 = 0
    while cdopcao4 != 1:
        nome = input("\nDigite seu nome: ")
        email = input("\nInforme seu email: ")
        print("\n1 - RG")
        print("2 - CNH")
        cdopcao2 = int(input("\nSelecione uma opção: "))
        if cdopcao2 == 1:
                rg = input("\nDigite seu RG: ")
        elif cdopcao2 == 2: 
                cnh = int(input("\nDigite sua CNH: "))
        cpf = input("Digite seu CPF: ")
        pais = input("Informe o seu país: ")
        estado = input("Informe seu estado: ")
        cidade = input("Informe sua cidade: ")
        cep = int(input("Informe seu cep: "))
        bairro = input("Informe seu bairro: ")
        endereco = input("Informe sua rua: ")
        numresidencia = int(input("Informe o número da residência: "))
        
        print("\nÉ necessário complemento? \n1 - Sim \n2 - Não")
        cdopcao3 = int(input("\nSelecione uma opção: "))
        if cdopcao3 == 1:
            complemento = input("Informe o complemento: ")

        if cdopcao2 == 1:
                print(f" \nNome: {nome}")
                print(f"RG: {rg}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {endereco} {numresidencia}  {complemento}")
                cdopcao4 = Confirmacao()
                if cdopcao4 == 1:
                    print("Cadastro realizado.")
        if cdopcao2 == 2:
                print(f"Nome: {nome}")
                print(f"CNH: {cnh}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {endereco} {numresidencia}  {complemento}")
                cdopcao4 = Confirmacao()
                if cdopcao4 == 1:
                    print("\nCadastro realizado.")
                elif cdopcao4 == 2:
                    print("Faça novamente o cadastro.")
                else:
                    print("\nDigite um número válido!")
    return cdopcao4, cdopcao2
            
#Para pegar as informações do bike
def RegistroBike():

    rgopcao = 0
    while rgopcao != 1:
        modelo = input("\nInforme o modelo da bike: ")
        numserie = int(input("Digite o número de série: "))
        ntfiscal = int(input("Informe a nota fiscal: "))
        cor = input("Informe a cor: ")
        valorbike = float(input("Informe o valor da bike: R$"))
        print("\nSua bike possui acessórios? \n1 - Sim \n2 - Não")

        bikeopcao = int(input("\nSelecione uma opção: "))
        if bikeopcao == 1:
            acessorios = float(input("Informe o valor total dos acessórios: R$"))
            print(f"\nModelo: {modelo}")
            print(f"Número de série: {numserie}")
            print(f"Nota fiscal: {ntfiscal}")
            print(f"Cor: {cor}")
            print(f"Valor da bike: R${valorbike}")

            if acessorios != 0:
                print(f"Valor dos acessórios: R${acessorios}")
                print(f'Valor total: R${valorbike + acessorios}')

        if bikeopcao == 2:
            print(f"\nModelo: {modelo}")
            print(f"Número de série: {numserie}")
            print(f"Nota fiscal: {ntfiscal}")
            print(f"Cor: {cor}")
            print(f"Valor da bike: R${valorbike}")

        rgopcao = Confirmacao()

        if rgopcao == 1:
            print("\nRegistro realizado.")
        else:
            print("\nFaça novamente o registro.")
    return rgopcao

#Para enviar as fotos e vídeos para a vistoria
def MidiaVistoria():
        
        print("\nClique no x para adicionar a foto: ")
        
        print("\n x- Foto da bike inteira de lado")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto da bike inteira de lado")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")
            
        print("\n x- Foto do número de série")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x - Foto do número de série")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada")
        
        print("\n x- Foto da roda")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto da roda")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto dos freios")
        confirmFoto = Confirmacao()
        while confirmFoto == 2: 
            print("Repita o processo")
            print("\n x- Foto dos freios")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")
        
        print("\n x- Foto do guidão")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto do guidão")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto dos pedais")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto dos pedais")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")
        
        print("\n x- Foto da corrente")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto da corrente")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto sua com a bike")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto sua com a bike")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto da bike de frente")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto da bike de frente")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto dos acessórios (se for visível)")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto dos acessórios (se for visível)")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\nClique no x para adicionar os vídeos: ")

        print("\nx -Vídeo mostrando a bike completa")
        confirmFoto = Confirmacao()
        while confirmFoto == 2: 
            print("Repita o processo")
            print("\nx -Vídeo mostrando a bike completa")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nVídeo adicionado.")

        print("\nx -Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\nx -Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nVídeo adicionado.")

#Para mostrar o tipo de seguro escolhido no relatório
def TpSeguro_Relatorio(seg1, seg2, seg3, seg4, seg5, seg6, seg7):

    opcSeguro = 0

    match opcSeguro:
        case 1:
            print(f'Opção de Seguro: {seg1}')
        case 2:
            print(f'Opção de Seguro: {seg2}')
        case 3:
            print(f'Opção de Seguro: {seg3}')
        case 4:
            print(f'Opção de Seguro: {seg4}')
        case 5:
            print(f'Opção de Seguro: {seg5}')
        case 6:
            print(f'Opção de Seguro: {seg6}')
        case 7:
            print(f'Opção de Seguro: {seg7}')
        case 0:
            print("\nNenhum seguro foi adicionado.")

#Para fazer um feedback
def FB_Relatorio(fbtempo, fbservicos, fbproblemas, fbatendimentos, fbduvidas):

    match opcaofb:
        case 1:
            print(fbtempo)
        case 2:
            print(fbservicos)
        case 3:
            print(fbproblemas)
        case 4:
            print(fbatendimentos)
        case 5:
            print(fbduvidas)

#Para mostrar o status da vistoria
def Apolice():
    aprovado = False
    reprovado = False
    emAnalise = True
    faltandoDocs = False

    if aprovado == True:
        print("A apólice foi enviada para o seu email. No seu email, foram enviadas instruções de como assinar a apólice e como enviar ela de volta para empresa.")
    elif reprovado == True:
        print("Sua apólice não foi emitida pois sua vistoria não foi aprovada.")
    elif emAnalise == True:
        print("Sua vistoria ainda está em análise.")
    elif faltandoDocs == True:
        print("Há arquivos reprovados. Confira quais são e reenvie eles.")

#Para emitir a apólice
def EmitirApolice():

    #pegar todos os dados do cliente, dados da bike, assinatura do cliente
    print(f'Eu, {nome}, portador do rg nº {rg} e cpf nº{cpf}, morador do enedreço {endereco}  {numresidencia}  {complemento}, cep: {cep}' 
          +f'afirmo que escolhi o tipo de seguro {TpSeguro_Relatorio} e que os dados da bike modelo: {modelo}, cor: {cor}, valor total: R${valorbike + acessorios}, número de série: {numserie}, nota fiscal: {ntfiscal}, são verdadeiros. Tenho ciência da veracidade e da importância da prestação de informações corretas.'
          + 'Visto isso, eu concordo com a realização dessa vistoria e do seguro adquirido por mim')
    print('__ (assinatura do cliente) __ (assinatura da empresa) __(data)')
      
#Para perguntar a nota do fedback
def Nota():
    nota = int(input("Qual a sua nota para esse serviço? (0 - 10): "))
    return nota
def Vistoria():
    registro = 2
    confSeguro = 2
    confCli = 2

    aprovado = False
    reprovado = False
    emAnalise = True
    faltandoDocs = False

    # while confSeguro == 2:
    confSeguro = RegistroSeguro()
    # while confCli == 2:
    confCli, rgcpf = RegistroCliente()
    confCli = ''
    rgcpf = ''
    # while registro == 2:
    registro = RegistroBike()
    registro_bike = 1 
    print("\nPara finalizar a vistoria é necessário que sejam tiradas: "+ 
            "\n-Foto da bike inteira de lado"
            + "\n-Foto do número de série"
            + "\n-Foto da roda"
            + "\n-Foto dos freios"
            + "\n-Foto do guidão"
            + "\n-Foto dos pedais"
            + "\n-Foto da corrente"
            + "\n-Foto sua com a bike"
            + "\n-Foto da bike de frente"
            + "\n-Foto dos acessórios (se for visível)"
            + "\n-Vídeo mostrando a bike completa"
            + "\n-Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto")
    print("\nObservação: neste momento, como ainda não é possível enviar fotos e vídeos, esta parte não é totalmente funcional")
    
    MidiaVistoria()
    print("\nOs seus dados foram enviados para vistoria. Você pode acompanhar o atual status da análise pelo seu e-mail ou aqui pelo site.")
    print("\nDeseja conferir o status da análise da vistoria?")
    confirmVistoria = int(input("\n1 - Sim \n2 - Não \nSelecione uma opção: "))
    if confirmVistoria == 1: 
        if aprovado == True:
            print("\nSeus dados foram aprovados! Agora assine a apólice.")
        elif reprovado == True:
            print("\nSeus dados foram reprovados. Refaça o processo de vistoria.")
        elif emAnalise == True:
            print("\nSeus dados estão em análise. Confira novamente mais tarde.")
        elif faltandoDocs == True:
            print("\nEstá faltando documentos para realizar a vistoria. Revise seus dados.")
    else:
        print("Ok. Acompanhe no seu email ou nessa tela o atual status da sua vistoria para saber as informações de como prosseguir.")

def Relatorio():
    seg1 = ''
    seg2 = ''
    seg3 = ''
    seg4 = ''
    seg5 = ''
    seg6 = ''
    seg7 = ''
    nome = ''
    rg = ''
    cnh = ''
    cpf = ''
    endereco = ''
    numresidencia = ''
    complemento = ''
    cep = 0
    modelo = ''
    numserie = 0
    ntfiscal = 0
    cor = ''
    valorbike = 0
    acessorios = 0
    fbescolha = 0
    fbtempo = 0
    fbservicos = 0
    fbproblemas = 0
    fbatendimentos = 0
    fbduvidas = 0

    print("\nRelatório dos dados adicionados: ")
    TpSeguro_Relatorio(seg1, seg2, seg3, seg4, seg5, seg6, seg7)
    confCli = 1
    rgcpf = 0
    registro = 1 
    
    if confCli == 1:
        print(f"Nome: {nome}")
        if rgcpf ==1:
            print(f"RG: {rg}")
        elif rgcpf == 2:
            print(f"CNH: {cnh}")
        print(f"CPF: {cpf}")
        print(f"Endereço: {endereco} {numresidencia}  {complemento}")
    else:
        print(f'\nNenhum dado foi adicionado.')

    if registro == 1:
        print(f"\nRelatório do registro da bike:  \nModelo: {modelo}")
        print(f"Número de série: {numserie}")
        print(f"Nota fiscal: {ntfiscal}")
        print(f"Cor: {cor}")
        if acessorios != 0:
            print(f"Valor dos acessórios: {acessorios}")
    else:
        print("\nNenhum registro foi adicionado.")
    
    if fbescolha == 1:
        print("FeedBack adicionado: ")
        FB_Relatorio(fbtempo, fbservicos, fbproblemas, fbatendimentos, fbduvidas)

def Status():
    faltandoDocs = False
    reprovado = False
    aprovado = False
    emAnalise = True
    print("Os seus dados foram enviados para vistoria. Você pode acompanhar o atual status da análise pelo seu email ou aqui pelo site.")
    print("Deseja conferir o status da análise da vistoria?")
    confirmVistoria = int(input("\n1 - Sim \n2 - Não \nSelecione uma opção: "))
    if confirmVistoria == 1: 
        if aprovado == True:
            print("Seus dados foram aprovados! Agora assine a apólice.")
        elif reprovado == True:
            print("Seus dados foram reprovados. Refaça o processo de vistoria.")
        elif emAnalise == True:
            print("Seus dados estão em análise. Confira novamente mais tarde.")
        elif faltandoDocs == True:
            print("\nEstá faltando documentos para realizar a vistoria. Revise seus dados.")
    else:
        print("\nOk. Acompanhe no seu email ou nessa tela o atual status da sua vistoria para saber as informações de como prosseguir.")
    return emAnalise



    
#Menu de opções
opcaomenu = 0
while opcaomenu != 7:
    print("\nOlá, em que a Technobike pode te ajudar hoje?")
    print("1 - Conheça os tipos de seguro para a bike")
    print("2 - Iniciar processo de vistoria")
    print("3 - Relatório")
    print("4 - Verificar status da vistoria")
    print("5 - Emissão da apólice")
    print("6 - Feedback")
    print("7 - Encerrar")
    opcaomenu = int(input("\nSelecione uma das opções acima: "))
    match opcaomenu:
        case 7:
          print("\nEncerrando, até a próxima!")
          break


#Tipo de seguro
        case 1: 
            # opcSeguro = 0
            # while opcSeguro < 1 or opcSeguro > 7:
            TipoSeguro()
                        

#Vistoria
        case 2:
           Vistoria()
        
#Relatório
        case 3:
            Relatorio()
            
#Status da vistoria
        case 4: 
           statusVistoria = Status()

#Apólice 
        case 5:
            Apolice()               
            
            
#Feedback
        case 6:
            opcaofb = [
                {"motivo": "Tempo para fazer vistoria", "nota": None},
                {"motivo": "Serviços fornecido", "nota": None},
                {"motivo": "Problemas", "nota": None},
                {"motivo": "Atendimento", "nota": None},
                {"motivo": "Resolução de dúvidas", "nota": None}
]           
            for feedback in opcaofb:
                motivo = feedback["motivo"]
                print(f"\n{motivo}")
                feedback["nota"] = Nota()
                print("Feedback enviado")
                print(f"Nota: {feedback['nota']}")
            