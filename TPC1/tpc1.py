## TPC 1 : ANÁLISE DE DADOS: DOENÇA CARDÍACA

#1: Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória

#Primeiro, é mais fácil trabalhar com o ficheiro se este estiver no formato txt, pelo que abrimos o ficheiro csv em reading mode e escrevemos no txt em writing mode
class TPC1():
    lisDoenca=[]
    lisEscalao= []
    lisColesterol= []
    def saveInfo(self,arrayInfo):
        with open('myheart.csv', 'r') as f_in, open('myheart.txt', 'w') as f_out:
                content = f_in.read()
                f_out.write(content)
        # agora já tenho um ficheiro txt com os dados fornecidos
        # o ficheiro contém os seguintes campos:
        # idade,sexo,tensão,colesterol,batimento,temDoença
        # vou guardar os dados num array de arrays, em que cada linha é um array
        with open('myheart.txt', 'r+') as fp: 
                lines = fp.readlines() 
                fp.seek(0)
                fp.truncate()
                fp.writelines(lines[1:])
        for line in lines: 
                #print (line)
                x = line.split(",") #separa os valores entre as virgulas
                arrayInfo.append(x)
        #print(arrayInfo) 

    #2: Crie uma função que calcula a distribuição da doença por sexo;
    def distrDoencaPorSexo(self,arrayInfo):
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
        newestList=[maledoentes,percMen,femdoentes,percFem]
        self.lisDoenca.append(newestList)
        
    #3: Crie uma função que calcula a distribuição da doença por escalões etários. Considere os seguintes escalões: [30-34], [35-39], [40-44], ...
    #só estou a contabilizar a idade entre 30 e 100
    def distrEscalãoAUX(self):
        #cria array entre 0 (idade minima) e 100 (idade máxima)
        lista= list(range(30,100))
        for i in range(0, len(lista),5):
           yield lista[i:i + 5]
       
    def distrEscalão(self,arrayInfo):
        listinha= list(self.distrEscalãoAUX()) #array com arrays de números em chunks de 4 (um escalão)
        #print(listinha)
        for a in listinha:
            a.append(0) #adiciono um inteiro no fim de cada array para contabilizar o número de doentes desse array(escalão)
        #print(listinha)
        for a in listinha:
           for line in arrayInfo:
                if line[5] == '1\n': #se for doente
                    if int(line[0]) in a: 
                        newValue = a[5]
                        newValue+=1
                        a[5]=newValue 
        for a in listinha:
            if len(a)==6:
                NRmin = a[0]
                NRmax= a[4]
                NRdoentes = a[5]
                print ("No escalão [",NRmin,",",NRmax,"] existem ", NRdoentes,"doentes.")
                triplinho =(NRmin,NRmax,NRdoentes)
                self.lisEscalao.append(triplinho)
        #4: Calcula a distribuição da doença por níveis de colesterol
    def minMaxlColesterol(self, arrayInfo):
        minNr = 3000000
        maxNr = -10
        for line in arrayInfo:
            if line[3]!= 'colesterol':
                nr = int (line[3])
                if nr>maxNr : maxNr= nr
                if nr<minNr : minNr = nr
        #print (minNr)
        #print (maxNr)
        return (minNr,maxNr)
    
    def getIntervalosColesterol(self):
        min=self.minMaxlColesterol[0]
        max=self.minMaxlColesterol[1]
        lista= list(range(min,max))
        for i in range(0, len(lista),10):
           yield lista[i:i + 10] 
           
    def nivelColesterol(self, arrayInfo):
        listinha= list(self.distrEscalãoAUX()) #array com arrays de números em chunks de 4 (um escalão)
        #print(listinha)
        level=0
        for a in listinha:
            a.append(0) #adiciono um inteiro no fim de cada array para contabilizar o número de doentes desse array(escalão)
            a.append(level)
            level+=1
        for a in listinha:
           for line in arrayInfo:
                if line[5] == '1\n': #se for doente
                    if int(line[0]) in a: 
                        newValue = a[5]
                        newValue+=1
                        a[5]=newValue 
        for a in listinha:
            if len(a)==7:
                nivel= a[6]
                NRdoentes = a[5]
                print ("No nível de colesterol",nivel,"existem ", NRdoentes,"doentes.")
                tuplinho= (nivel,NRdoentes)
                self.lisColesterol.append(tuplinho)
                
    
        #4: função que imprime na forma de uma tabela uma distribuição
    def createTable(self,arrayInfo,type):
        if type==1 : #tabela distribuição doença por sexo
            self.distrDoencaPorSexo(arrayInfo)
            for l in self.lisDoenca:
                homensDoentes = l[0]
                percentagemHomensDoentes = l[1]
                mulheresdoentes =l[2]
                percentagemMulheresDoentes = l[3]
                print("------------------------------------------------------------")
                print ("        Género      |   Total doentes   |   Percentagem")
                print("------------------------------------------------------------")
                print("        Homem       |    ", homensDoentes, "          | " ,percentagemHomensDoentes," ")
                print("------------------------------------------------------------")
                print("        Mulher      |    ", mulheresdoentes, "           | " , percentagemMulheresDoentes," ")
                print("------------------------------------------------------------")
            
        if type==2 : #tabela distribuiçãopor escalão
            self.distrEscalão(arrayInfo)
            print("----------------------------------------------")
            print ("       Escalão      |   Total doentes   ")
            for l in self.lisEscalao:
                min= l[0]
                max=l[1]
                doentes =l[2]
                print("----------------------------------------------")
                print(" [",min,",",max,"]        | " ,doentes," ")
                print("----------------------------------------------")
        
        if type==3 : #tabela distribuição nível colesterol
            self.nivelColesterol(arrayInfo)
            print("----------------------------------------------")
            print ("      Nível Colesterol      |   Total doentes   ")
            for l in self.lisColesterol:
                nivel=l[0]
                doentes=l[1]
                print("----------------------------------------------")
                print(" ",nivel,"                        | " ,doentes," ")
                print("----------------------------------------------")
               
             


    