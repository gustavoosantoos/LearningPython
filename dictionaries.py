myDic = {
    "teste" : "valor 1",
    "teste2" : "valor 2",
    "teste3" : "valor 3"
}

print(myDic)
print(myDic["teste"])

for chave in myDic.keys():
    print(chave)

for valor in myDic.values():
    print(valor)