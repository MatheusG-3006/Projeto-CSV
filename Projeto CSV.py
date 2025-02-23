#-------------------- Importando Bibliotecas ------------
import csv
#-------------------- Declarar Funções ------------------
def getData (filename):
    file = open(filename, "r", encoding = "cp437")
    data = list(csv.reader(file,delimiter = ","))
    file.close ()
    return data

def showMenu (dictionary):
    for key, value in dictionary.items():
        print(key, "\t", value)
        
#--------------------------------------------------------


#---------------------------------------------------------------[Top 10 de um mês/ ano específico]-------------------------------------------------------------------------------------------------------------------

def top10monthyear(dados, year, month):

    monthstr = str(month).zfill(2) #usuário poderá digitar um número com apenas uma casa decimal, pois a função zFill irá adicionar um 0 antes da casas decimal digitada

    yearmth= f"{year}-{monthstr}" # definindo a função yearmth como uma string, exibindo tanto o ano como o mês

    fdata = [line for line in dados if line[0].startswith(yearmth)] #filtra os dados conforme a planilha na billboard começando do índice 0

    fdata.sort(key=lambda x: int(x[1])) #faz com que os dados sejam ordenados sempre com base no valor da posição, convertendo o valor para inteiro

    print(f"Top 10 de {month}/{year}:") #print do mês e ano desejado 

    for i, linha in enumerate(fdata[:10], 1): #listando todos os artistas do ano e mês desejados de 1 a 10
        print(f"{i}. {linha[0]} - 5{linha[3]} - {linha[2]}") #print dos resultados desejados
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------[Top 12 do ano (1º de cada mês)]------------------------------------------------------------------------------------------------------------------

def top12year(data, year): 

    year = str(year) #convertendo a variável "year" em string

    print(f"Top 12 do ano de {year}:") #print simples do ano escolhido pelo usuário

    for month in range(1, 13): #numerando os meses de 1 até 12

        monthstr = str(month).zfill(2) #usuário poderá digitar um número com apenas uma casa decimal, pois a função zFill irá adicionar um 0 antes da casas decimal digitada

        yearmth = f"{year}-{monthstr}" # definindo a função yearmth como uma string podendo exibir o resultado dentro do print

        fdata = [line for line in data if line[0].startswith(yearmth)]  #filtra os dados conforme a planilha na billboard começando do índice 0

        fdata.sort(key=lambda x: int(x[1]), reverse=True) #faz com que os dados sejam ordenados sempre com base no valor da posição, convertendo o valor para inteiro e reverse=True para ordenar em ordem descrescente

        if fdata:
            first_artist = fdata[0] #filtra o primeiro artista de cada mês
            print(f"{monthstr}/{year}: 1. {first_artist[0]} - {first_artist[3]} - {first_artist[2]}") #print dos resultados desejados
        else:
            print(f"{monthstr}/{year}: Sem dados disponíveis") #caso não tenha nenhum dado filtrado, essa mensagem aparece
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            


#------------------------------------------------------------------[Top 100 de um mês/ ano específico]-------------------------------------------------------------------------------------------------------------------

def top100monthyear(data, year, month):

    monthstr = str(month).zfill(2) #usuário poderá digitar um número com apenas uma casa decimal, pois a função zFill irá adicionar um 0 antes da casas decimal digitada

    yearmth= f"{year}-{monthstr}" # definindo a função yearmth como uma string, exibindo tanto o ano como o mês 

    fdata = [line for line in data if line[0].startswith(yearmth)] #filtra os dados conforme a planilha na billboard começando do índice 0

    fdata.sort(key=lambda x: int(x[1]))#utilizando o método lambda como uma chave anônima para o método sort

    print(f"Top 10 de {month}/{year}:") #print simples do mês e ano escolhido pelo usuário

    for i, linha in enumerate(fdata[:100], 1): #numerando os dados de 1 até 100
        print(f"{i}. {linha[0]} - {linha[3]} - {linha[2]}") #print dos resultados desejados
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------[Buscar Artista]------------------------------------------------------------------------------------------------------------------

def searchArtist(data, artist):

    artist = f"{artist}"  #convertendo a variável year em string

    fdata = [linha for linha in data if linha[3].lower().startswith(artist)] #filtrando os dados apenas do índice 3, indice que está listado os artistas

    if not fdata:
        print(f"Nenhuma música encontrada para o artista {artist}.") #estrutura de decisão para verificar se o artista está na planilha
        return

    fdata.sort(key=lambda x: int(x[1]))#utilizando o método lambda como uma chave anônima para o método sort

    print(f"Artista procurado {artist.capitalize()}:") #caso o artista esteja na planilha esse print será executado

    for i, linha in enumerate(dadosf, 1): 
        print(f"{i}. {linha[0]} - {linha[2]} - {linha[3]} - {linha[4]}")#print do artista, ano de suas músicas e o rank das músicas
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------[Busca por posição na lista do mês/ano]------------------------------------------------------------------------------------------------------------------      

def searchPositioninList(data, rank):

    rank = str(rank)  # converte a variável rank em string

    print(f"Procurando por rank: {rank}") #procura pelo rank desejado

    fdata = [line for line in data if line[1].strip() == rank.strip()] #filtra os dados necessários dentro da billboard

    print(f"Número de entradas encontradas: {len(fdata)}") #aqui diz o número de entradas encontradas de acordo com o rank

    if not fdata: #estrutura de decisão, se caso o rank existir o código fará a impressão do rank, senão irá imprimir a mensagem de nenhuma entrada encontrada
        print(f"Nenhuma entrada encontrada para o rank {rank}.") 
        return
        print(f"Rank escolhido foi {rank}:")

    for i, line in enumerate(fdata, 1):
        print(f"{i}. {linha[0]} - {linha[4]} - {linha[2]}")#print dos resultados desejados
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------[Artista que ficou mais semanas no mês/ano]---------------------------------------------------------------------------------------------------------------------

def topArtistByMonthYear(data, year, month):

    monthstr = str(month).zfill(2)#usuário poderá digitar um número com apenas uma casa decimal, pois a função zFill irá adicionar um 0 antes da casas decimal digitada

    yearmth = f"{year}-{monthstr}" #converte a variável yearmth para uma f string, mostrando tanto o mês quanto o ano desejado

    artist_ranking = {} #dicionário vazio, armazenando o número de semanas em que um artista apareceu no rank 

    for line in data: #Nesse trecho o código percorre cada linha de dados fornecidos 

        if line[0].startswith(yearmth): #Nessa linha o código verifica se a linha dentro da billboard corresponde ao mês e ano desejado

            artist = line[3] #Nessa linha vemos que o índice 3 corresponde exatamente a "artist" dentro da billboard, fazendo com que o nome do artista seja obtido

            weeks_on_rank = int(line[6]) if line[6].isdigit() else 0 #Nessa linha obtemos o número de semanas que a música do artista ficou no rank

            if artist in artist_ranking: #Verificação do artista se está dentro do dicionário 
                artist_ranking[artist] += weeks_on_rank #Caso o artista estiver dentro do dicionário, adiciona o número de semanas da música do artista atual ou já existente

            else:
                artist_ranking[artist] = weeks_on_rank #Caso o artista não estiver dentro do dicionário, uma nova entrada se cria com o número de semanas da música atual

    if artist_ranking:
        most_weeks_artist = max(artist_ranking, key=artist_ranking.get) #Encontra o artista com mais semanas dentro da billboard. 

        weeks = artist_ranking[most_weeks_artist] #Aqui temos o número total de semanas, correspondente ao que foi adicionado no dicionário

        print(f"Artista que ficou mais semanas no ranking em {month}/{year}:") #print simples do ano e mês escolhidos

        print(f"{most_weeks_artist} - {weeks} semanas no ranking") #print simples do total de semanas e do artista 

    else:
        print(f"Nenhuma informação disponível para {month}/{year}.") #print simples, caso nenhuma informação for encontrada
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        


#-----------------------------------------------------------------[Artista que mais apareceu na lista]--------------------------------------------------------------------------------------------------------------------

def artistMostAppearances(data):
    artist_count = {} #dicionário criado para armazenar o único artista que mais apareceu na lista 

    for line in data: #Nesse trecho o código percorre todas as linhas dos dados fornecidos 

        artist = line[3] #Nessa linha vemos que o índice 3 corresponde exatamente a "artist" dentro da billboard, fazendo com que o nome do artista seja obtido

        if artist in artist_count: #Estrutura de decisão, caso o artista tenha aparecido mais vezes, o contador acrescenta mais 1
            artist_count[artist] += 1

        else:
            artist_count[artist] = 1 #Caso contrário, o contador será igual a 1

    most_appearances_artist = max(artist_count, key=artist_count.get) #Encontra o artista que mais apareceu dentro da billboard. 
    appearances = artist_count[most_appearances_artist] #Variável para contabilizar o total de vezes em que o artista apareceu.

    print(f"Artista que mais apareceu na lista: {most_appearances_artist} com o total de({appearances} vezes)") #print simples do artitsa que mais apreceu e o total de vezes
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------[Executar Menu]-------------------------------------------------------------------------------------------------------------------
def executeMenu(option):

    if option == "1":

        print("-" * 80)
        year = int(input("Digite o ano no formato YYYY: "))
        month = int(input("Digite o mês que deseja: "))

        if year < 1958 or year > 2021:
            print("Ano inválido, por favor digite um ano entre 1958 e 2021")

        elif month < 1 or month > 12:
            print("Mês inválido, por favor digite um mês entre 01 e 12")

        else:
            print("-" * 80)
        top10monthyear(billboard, year, month)
        print("-" * 80)



    elif option == "2":

        print("-" * 80)
        year = int(input("Digite o ano que deseja no formato YYYY: "))

        if year < 1958 or year > 2021:
            print("Ano inválido, por favor digite um ano entre 1958 e 2021")
        else:
            top12year (billboard, year)
        print("-" * 80)

    elif option == "3":

        print("-" * 80)
        year = int(input("Digite o ano que deseja no formato YYYY: "))
        month = int(input("Digite o mês que deseja: "))
        if year < 1958 or year > 2021:
            print("Ano inválido, por favor digite um ano entre 1958 e 2021")

        elif month < 1 or month > 12:
            print("Mês inválido, por favor digite um mês entre 01 e 12")

        else:
            print("-" * 80)
        top100monthyear(billboard, year, month)
        print("-" * 80)


    elif option == "4":
        print("-" * 80 )
        artist = str(input("Digite o nome do artisa que deseja procurar: "))
        searchArtist(billboard,artist)
        print("-" * 80)


    elif option == "5":
        print("-" * 80 )
        rank = int(input("Digite a posição que deseja buscar: "))
        if rank < 0 and rank > 330088:
            print("Digite um rank Válido")
        else:
            searchPositioninList (billboard, rank)
        print("-" * 80)


    elif option == "6":
        print("-" * 80)
        year = int(input("Digite o ano que deseja no formato YYYY: "))
        if year < 1958 and year > 2021:
            print("Digite um ano entre 1958 e 2021")

        month = int(input("Digite o mês que deseja: "))
        if month < 0  and month  > 12:
            print("Digite um mês entre 1 e 12")
        if year < 1958 and year > 2021:
            print("Digite um ano entre 1958 até 2021")

        else:
            topArtistByMonthYear (billboard, year, month)
        print("-" * 80)
        

    elif option == "7":
        print("-" * 80)
        artistMostAppearances (billboard)
        print("-" * 80)



    elif option == "8":
        print("Sair do programa")

        #---------------------- Variáveis -------------------
billboard = getData ("billboard.csv")

options = {"1" : "Top 10 de um mês/ano específico",
           "2" : "Top 12 do ano (1º de cada mês) ",
           "3" : "Top 100 de um mês/ ano específico",
           "4" : "Busca por Artista",
           "5" : "Busca por posição na lista do mês/ano",
           "6" : "Artista que ficou mais semanas no mês/ano",
           "7" : "Artista que mais apareceu na lista",
           "8" : "Sair do Programa"}

#-------------------------- Fluxo Principal -------------------------------

selected = ""

while selected != "8":
    showMenu (options)
    print("-" * 80)
    selected = input("Selecione uma opção: ")
    executeMenu (selected)
