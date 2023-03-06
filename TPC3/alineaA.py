
class exA():
    #a) Calcula a frequência de processos por ano (primeiro elemento da data);
    def parserTextFile(self):
        dict={}
        lista = []
        myfile = open ('processos.txt','r')
        linhas = myfile.readlines()
        for linha in linhas:
            if linha.strip():
                arr2=linha.split("::")
                processo= arr2[1]
                data = processo.split("-")
                ano = int(data[0])
                lista.append(ano)
        return lista

    def dictFrequency(self,lista):
        freq={}
        for item in lista:
            if (item in freq):
                freq[item] +=1
            else:
                freq[item] =1   
        for key, value in freq.items():
            print ("% d : % d"%(key, value))
            
                    







