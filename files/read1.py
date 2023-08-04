from Pais import *
import csv
listaPaises=[]
with open('C:\\tercer_trimestre\\pais.csv') as csvDatapais:
    csvReader=csv.reader(csvDatapais)    
    for row in csvReader:
        ob=Pais(row[1],row[3],row[4],row[7])
        listaPaises.append(ob)
       
for p in listaPaises:
    print('El pais es:',p.getNombre())
    print('La poblacion es:',p.getPoblacion())
    print('La superficie es:',p.getSuperficie())
    print('La altura es:',p.getAltura())
    
    
if p %2==0:
        ind1=p//2
        ind2=p-1
        mediana=(listaPaises[ind1])
else:
        ind1=p//2
        mediana=listaPaises[ind1]
        #return mediana