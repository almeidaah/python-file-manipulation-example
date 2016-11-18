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
print("Original James List")
print(james)
#printando a lista copiada dos dados originais, mantem a lista original
print("Sorted James List")
print(sorted(james))
#print("\n")
#print(julie)
#print(mikey)
#print(sorted(sarah))

def padronize(item):
    if '-' in item:
        splitter = '-'
    elif ':' in item:
        splitter = ':'
    else:
        return(item)
    (min,secs) = item.split(splitter)
    return (min + '.' + secs)

print("Lista Padronizada e sem duplicatas (set()) ")
print(sorted(set([padronize(item) for item in james])))

