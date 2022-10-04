from questao_2 import qtd_padrao_in_cadeia,padrao_in_cadeia,registro_dna,arquivo_dados_dna,qtd_sequence_false,freq_max,indices_freq_max

# 2 - a - fails:
cadeia = 'ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG'
restultado = qtd_padrao_in_cadeia(cadeia,5)
print(restultado)

restultado = qtd_padrao_in_cadeia(cadeia,True)
print(restultado)

restultado = qtd_padrao_in_cadeia(cadeia,['ATG'])
print(restultado)

# 2 - a - sucess:

restultado = qtd_padrao_in_cadeia(cadeia,'ATG')
print(restultado)

restultado = qtd_padrao_in_cadeia(cadeia,'AT')
print(restultado)

restultado = qtd_padrao_in_cadeia(cadeia,'A')
print(restultado)

restultado = qtd_padrao_in_cadeia(cadeia,'atg')
print(restultado)

restultado = qtd_padrao_in_cadeia(cadeia,'a')
print(restultado)

# 2 - b - fails:

restultado = padrao_in_cadeia(cadeia,5)
print(restultado)

restultado = padrao_in_cadeia(cadeia,True)
print(restultado)

restultado = padrao_in_cadeia(cadeia,['ATG'])
print(restultado)

# 2 - b - sucess:

restultado = padrao_in_cadeia(cadeia,'ATG')
print(restultado)

restultado = padrao_in_cadeia(cadeia,'AT')
print(restultado)

restultado = padrao_in_cadeia(cadeia,'A')
print(restultado)

restultado = padrao_in_cadeia(cadeia,'atg')
print(restultado)

restultado = padrao_in_cadeia(cadeia,'a')
print(restultado)


registro_dna()
arquivo_dados_dna()
qtd_sequence_false()
freq_max()
indices_freq_max()