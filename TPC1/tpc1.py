## TPC 1 : ANÁLISE DE DADOS: DOENÇA CARDÍACA

#1: Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória

#Primeiro, é mais fácil trabalhar com o ficheiro se este estiver no formato txt, pelo que abrimos o ficheiro csv em reading mode e escrevemos no txt em writing mode
class TPC1():
    def saveInfo(arrayInfo):
        with open('myheart.csv', 'r') as f_in, open('myheart.txt', 'w') as f_out:
                content = f_in.read()
                f_out.write(content)
        # agora já tenho um ficheiro txt com os dados fornecidos
        # o ficheiro contém os seguintes campos:
        # idade,sexo,tensão,colesterol,batimento,temDoença
        # vou guardar os dados num array de arrays, em que cada linha é um array
        with open('myheart.txt', 'r') as f: 
                lines = f.readlines() 
        for line in lines: 
                #print (line)
                x = line.split(",") #separa os valores entre as virgulas
                arrayInfo.append(x)
        #print(arrayInfo) 

    #2: Crie uma função que calcula a distribuição da doença por sexo;
    def distrDoencaPorSexo(arrayInfo):
        male= 0
        maledoentes = 0
        fem = 0
        femdoentes = 0
        for line in arrayInfo:
            if line[1] == 'M':
                male +=1
                if line[5] == '1\n': maledoentes +=1
            if line[1] == 'F' :
                fem+=1
                if line[5] == '1\n': femdoentes +=1  
        percMen = (maledoentes/male)*100
        percFem = (femdoentes /fem)*100   
        print ("Num total de",male, "homens exitem", maledoentes, "homens doentes, correspondendo à seguinte percentagem:",percMen, "%")
        print ("Num total de",fem, "mulheres exitem", femdoentes, "mulheres doentes correspondendo à seguinte percentagem:", percFem,"%")
                        
    arrayInfo = []
    saveInfo(arrayInfo)
    distrDoencaPorSexo(arrayInfo)
            
