cadeia = 'ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG'
def procuraPadrao(cadeia, padrao):
        """
        Documento lido: (dados_usuario.csv)

                        

        Arguments:
                        

        Returns:
                        
        """
        try:
                tamanho = len(padrao)
                contador = 0
                for i in range(len(cadeia)):
                        if cadeia[i:tamanho+i] == padrao:
                                contador += 1
                return contador
        except:
                print('EEEROUUUUUUUUUUUUUUUUUUUUUUU')
restultado = procuraPadrao(cadeia,'ATG')
print(restultado)



cadeia = 'ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG'

def TestboolPadrao(cadeia, padrao):
        """
        Documento lido: (dados_usuario.csv)

                        

        Arguments:
                        

        Returns:
                        
        """
        
        if padrao in cadeia:
                return True
        else:
                return False

resultado = TestboolPadrao(cadeia, 'ATG')
print(resultado)

def frequenciaPadrao():
    """
        Documento lido: (dados_usuario.csv)

                        

        Arguments:
                        

        Returns:
                        
    """

    with open('C:\\Users\\kimli\\Desktop\\Atividade_Avaliativa\\dados_DNA.txt',encoding='utf-8') as file:
        linhas = file.readlines()

    with open('C:\\Users\\kimli\\Desktop\\Atividade_Avaliativa\\dados_DNA.txt','w', encoding='utf-8') as file:
        file.write('sequence,FREQ_ATGCCA,TEM_ATGCCA\n')
        for cadeia in linhas[1:]:
            freq = procuraPadrao(cadeia, 'ATGCCA')
            tem = TestboolPadrao(cadeia, 'ATGCCA')
            file.write(f'{cadeia[:-1]},{freq},{tem}\n')

frequenciaPadrao()


arquivo_tratado = []

with open('C:\\Users\\kimli\\Desktop\\Atividade_Avaliativa\\dados_DNA.txt', encoding = 'utf-8') as file:
    for linha in file:
        arquivo_tratado.append(linha.strip().split(','))


def naoPossuemPadrao():
    """
        Documento lido: (dados_usuario.csv)

                        

        Arguments:
                        

        Returns:
                        
    """
    contador = 0
    for linha in arquivo_tratado:
        if linha[2] == 'False':
            contador += 1
    return contador
naoPossuemPadrao()

def maximoPadrao():
    """
        Documento lido: (dados_DNA.txt)

                        

        Arguments:
                        

        Returns:
                        
    """

    valorMaior = []
    for linha in arquivo_tratado[1:]:
        valorTeste = int(linha[1])
        if valorTeste > 0 :
            valorMaior.append(valorTeste)
    maior = max(valorMaior)

    return maior

maximoPadrao()


def frequenciaMaximaPadrao():
    """
        Documento lido: (dados_DNA.txt)

                        

        Arguments:
                        

        Returns:
              
    """
    with open('C:\\Users\\kimli\\Desktop\\Atividade_Avaliativa\\dados_DNA.txt', encoding='utf-8') as file:
        linhas_arquivo = file.readlines()[1:]

        lista_index = []
        frequencia_maxima = maximoPadrao()

        for indices in range(len(linhas_arquivo)):
            frequencia = int(linhas_arquivo[indices].split(',')[1])
            
            if frequencia == frequencia_maxima:
                lista_index.append(indices)
    return lista_index
frequenciaMaximaPadrao()

