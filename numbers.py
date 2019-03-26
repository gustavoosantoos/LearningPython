n1 = 10
n2 = 30
n3 = 1.0

# Operações básicas são padrão
y = n2 + n1
print(y)

# Operações básicas são padrão
y = n2 % n1
print(y)

# Operações básicas são padrão
y = n2 / n1
print(y)

# Suporte para números complexos
k = 3+10j

# Método para obter tipo de variável
print(type(y).__name__)
print(type(k))
print(type(n3))

# Cast de string para int
str = "12"
print(n1 + int(str))