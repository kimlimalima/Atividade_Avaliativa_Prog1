from funcoes_q1 import procuraNome, quantidadeGender, substringARG, procuraNumero, novo_cadastro
# 1 - a - fails:
contador, lista = procuraNome(5)
print(f'{contador}\n{lista}')

contador, lista = procuraNome(True)
print(f'{contador}\n{lista}')

contador, lista = procuraNome(["sam", 'kev'])
print(f'{contador}\n{lista}')

# 1 - a - succes:
contador, lista = procuraNome('kim kev')
print(f'{contador}\n{lista}')

contador, lista = procuraNome("kim")
print(f'{contador}\n{lista}')

contador, lista = procuraNome("sam")
print(f'{contador}\n{lista}')

contador, lista = procuraNome("False")
print(f'{contador}\n{lista}')

contador, lista = procuraNome("56")
print(f'{contador}\n{lista}')

# 1 - b - fails:

contador, lista = quantidadeGender(-2002, "F")
print(contador, lista)

contador, lista = quantidadeGender(2002, 8)
print(contador, lista)

contador, lista = quantidadeGender(2001, "Test")
print(contador, lista)

# 1 - b - succes:

contador, lista = quantidadeGender(2000, "F")
print(contador, lista)

contador, lista = quantidadeGender(2015, "m")
print(contador, lista)

contador, lista = quantidadeGender(2022, "M")
print(contador, lista)

contador, lista = quantidadeGender(2010, "M")
print(contador, lista)

contador, lista = quantidadeGender(2022, "F")
print(contador, lista)

# 1 - c - fails:

contador, lista = substringARG(True)
print(f'{contador}\n{lista}')

contador, lista = substringARG(5)
print(f'{contador}\n{lista}')

contador, lista = substringARG(['True'])
print(f'{contador}\n{lista}')

# 1 - c - succes:

contador, lista = substringARG('samuel')
print(f'{contador}\n{lista}')

contador, lista = substringARG('uel')
print(f'{contador}\n{lista}')

contador, lista = substringARG('True')
print(f'{contador}\n{lista}')

contador, lista = substringARG('')
print(f'{contador}\n{lista}')

contador, lista = substringARG('kim')
print(f'{contador}\n{lista}')

# 1 - d - fails:
contador, lista = procuraNumero(True)
print(f'{contador}/n {lista}')

contador, lista = procuraNumero(0)
print(f'{contador}/n {lista}')

contador, lista = procuraNumero(-5)
print(f'{contador}/n {lista}')

# 1 - d - succes:

contador, lista = procuraNumero(1)
print(f'{contador}/n {lista}')

contador, lista = procuraNumero(5)
print(f'{contador}/n {lista}')

contador, lista = procuraNumero('1')
print(f'{contador}/n {lista}')

contador, lista = procuraNumero('5')
print(f'{contador}/n {lista}')

contador, lista = procuraNumero('556465')
print(f'{contador}/n {lista}')

#1 - d - fails:

novo_cadastro(True,'2002','M', 5)

novo_cadastro('True',-2002,'M', 5)

novo_cadastro('True',2002,'M', -5)

# 1 - e - succes:

novo_cadastro("Kevin", 2003, "M", 3)

novo_cadastro("Kevin", '2003', "M", 3)

novo_cadastro("Kevin", '2003', "M", '3')

novo_cadastro("", '2000', "", 3)

novo_cadastro("Kevin", '2003', "m", '3')