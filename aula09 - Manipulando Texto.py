#Fatiamento
frase = '   Curso em vídeo Python   '
print(frase[9:14])
print(frase[9:14:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Analise
print(len(frase))
print(frase.count('o')) # conta quantos 'o' tem na frase
print(frase.count('o', 0, 13))#conta con fatiamento
print(frase.find('deo')) #encotra na string o valor informado
print(frase.find('Android')) # retorna -1 caso não econtre o valor da string
print('Curso' in frase) # retorna true caso encontre

#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip()) #remove os espaços do final e inicio da string
print(frase.rstrip())
print(frase.lstrip())
print(frase.strip())

#Junção

print('-'.join(frase))
