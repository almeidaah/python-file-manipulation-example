#LE as parciais de tempo dos atletas atraves dos arquivos e calcula os 3 melhores tempos
print('===ReadFiles===')

with open('../files/james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('../files/julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('../files/mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('../files/sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

#print lista original
print(james)
#printando a lista copiada dos dados originais, mantem a lista original
print(sorted(james))
print("\n")
print(julie)
print(mikey)
print(sorted(sarah))



