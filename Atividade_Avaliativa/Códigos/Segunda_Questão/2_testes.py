from funcoes_q2 import procuraPadrao,TestboolPadrao,frequenciaPadrao,naoPossuemPadrao,maximoPadrao,frequenciaMaximaPadrao
# 2 - a - fails:
cadeia = 'ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG'
restultado = procuraPadrao(cadeia,5)
print(restultado)

restultado = procuraPadrao(cadeia,True)
print(restultado)

restultado = procuraPadrao(cadeia,['ATG'])
print(restultado)

# 2 - a - sucess:

restultado = procuraPadrao(cadeia,'ATG')
print(restultado)

restultado = procuraPadrao(cadeia,'AT')
print(restultado)

restultado = procuraPadrao(cadeia,'A')
print(restultado)

restultado = procuraPadrao(cadeia,'atg')
print(restultado)

restultado = procuraPadrao(cadeia,'a')
print(restultado)

# 2 - b - fails:

restultado = TestboolPadrao(cadeia,5)
print(restultado)

restultado = TestboolPadrao(cadeia,True)
print(restultado)

restultado = TestboolPadrao(cadeia,['ATG'])
print(restultado)

# 2 - b - sucess:

restultado = TestboolPadrao(cadeia,'ATG')
print(restultado)

restultado = TestboolPadrao(cadeia,'AT')
print(restultado)

restultado = TestboolPadrao(cadeia,'A')
print(restultado)

restultado = TestboolPadrao(cadeia,'atg')
print(restultado)

restultado = TestboolPadrao(cadeia,'a')
print(restultado)

frequenciaPadrao()
naoPossuemPadrao()
maximoPadrao()
frequenciaMaximaPadrao()