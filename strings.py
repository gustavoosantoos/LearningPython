str1 = "Hello"
str2 = "World"

# Concatenações são normais
print(str1 + str2)

# Por que dá pra multiplicar uma string em Python? Só deus sabe... 
num1 = 10
print(str1 * num1)

# Não há cast automático para string, a linha de baixo ocasiona erro
# print(str1 + num1) 

# Cast para int de string
print(str1 + str(num1))

# Obter chars através do index
print(str1[0])

# Obter chars através de ranges
print(str1[0:3])
print(str1[3:5])

# Obter tamanho da string
print(len(str1))

# Trim 
print("      teste 3    ".strip())

# Outros métodos
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.replace("l", "r"))

# Split
x = str1.split('l')
print(x)