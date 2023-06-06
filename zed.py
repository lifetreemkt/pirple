nome = input("qual é o nome?\n")
print (f"o seu nome é {nome}")

Lugares = []
for i in range(5):
    local = input("Digite um lugar que vc quer conhecer:\n")
    Lugares.append(local)
print(Lugares)

ListaFerias = open ("locais","w")
for local in Lugares:
    ListaFerias.write(local + ",")
ListaFerias.close()

Lugares = open ("locais", "r")

ListaPronta = Lugares.read()
print(ListaPronta)
