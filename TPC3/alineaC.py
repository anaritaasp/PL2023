import re

class exC():
    #c) Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;
    
    def parseRRR(self):
        listaaa=[]
        myfile = open ('processos.txt','r')
        linhas = myfile.readlines()
        for linha in linhas:
            if linha.strip():
                getParentesco = re.compile(r',([\w ]+)\.')
                strPar= getParentesco.findall(linha)
                for elemento in strPar:
                   # print(strPar)
                    listaaa.append(elemento)
        return listaaa
                                
    def parentescoFrequency(self,lista):
        freq={}
        for item in lista:
            if (item in freq):
                freq[item] +=1
            else:
                freq[item] =1   
        for key, value in freq.items():
            print ("% a : % d"%(key, value))          