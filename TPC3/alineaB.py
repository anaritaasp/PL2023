import re
import operator

class exB():
    #a) Calcula a frequência de processos por ano (primeiro elemento da data);
    
    def parserNome(self,proprios,apelidos):
        myfile = open ('processos.txt','r')
        linhas = myfile.readlines()
        for linha in linhas:
            if linha.strip():
                #pegamos em tudo o que seja texto de cada linha
                strTexto =re.compile(r'(?:(?:[A-Z][a-z]+ )*(?:[A-Z][a-z]+)\.?)')
                #remove palavras de texto que acabem em . e que sejam constituidas por mais do que 1 nome
                nomesApenas = [x for x in strTexto.findall(linha) if x[-1:] != '.' and len(x.split(' ')) > 1]
                for name in nomesApenas:
                    strNome= name.split(" ")
                    tamanho= len(strNome)
                    proprio = strNome[0]
                    proprios.append(proprio)
                    apelido=strNome[tamanho-1]
                    apelidos.append(apelido)
    
    def NomeFrequency(self,lista):
        freq={}
        for item in lista:
            if (item in freq):
                freq[item] +=1
            else:
                freq[item] =1   
        newA = dict(sorted(freq.items(), key=operator.itemgetter(1), reverse=True)[:5])
        for key, value in newA.items():
            print ("% a : % d"%(key, value))
            
                    

            
        
                




