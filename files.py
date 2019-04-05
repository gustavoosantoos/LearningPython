
# criando arquivo 
try: 
    myFile = open("myTextFile.txt", "x")
    myFile.write("Testing de write of my file\n")
    myFile.write("Testing \t3\n")
except:
    print('O arquivo já foi criado, e por isso deu erro.')

# escrvendo conteúdo sem dar append
myFileWrite = open("myTextFile.txt", "w")
myFileWrite.write("Testing de write of my file\n")
myFileWrite.write("Testing \t3\n")
myFileWrite.flush()

myFileRead = open("myTextFile.txt", "r")
for line in myFileRead:
    print(line)


