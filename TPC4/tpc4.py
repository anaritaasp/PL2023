import csv,json,re,statistics,math

# Function to convert a CSV to JSON
# Takes the file paths as arguments
class TPC4():
    def make_json(self,csvFilePath, jsonFilePath):
        
        jsonArray = []
      
        #read csv file
        with open(csvFilePath,'r') as csvf: 
            #load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf) 
            #convert each csv row into python dict
            for row in csvReader: 
                for key,value in row.items() :
                #add this python dict to json array
                    betweenValues = re.search(r'{(\d+),?(\d+)?}', str(value))
                    if betweenValues:
                                if betweenValues.group(2):
                                        min= int(betweenValues.group(1)) #obtem o menor valor do intervalo 
                                        max = int(betweenValues.group(2)) #obtem o maior valor do intervalo
                                else:
                                        min = int(betweenValues.group(1)) #neste caso é quando temos N= x , assim min = n
                operação = re.search(r'(?<=(::))\w+', str(value)) 
                if operação:value = operação.group(0)
                if betweenValues:
                        listinha=[]
                        new= key+max
                        for n in row[new]: listinha.append(int(n))
                        if value == "sum":
                            row[value] = sum(listinha)
                        if value == "media":
                            row[value] = statistics.mean(listinha)
                        if value == "prod":
                            row[value] = math.prod(listinha)  
                        else:
                            row[value.split('{')[0]] = listinha
                else:
                        row[value] = row[key]
                jsonArray.append(row)
    
        #convert python jsonArray to JSON String and write to file
        with open(jsonFilePath, 'w') as jsonf: 
            jsonString = json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)
        
       