def procuraPadrao(cadeia, padrao):
        """
        Documento lido: (dados_DNA.txt)

        Dada a atríbuição múltipla de argumentos para os parâmetros {cadeia} e {padrao}
                        

        Arguments:
                cadeia : Um string. Passada de forma posicional pelo usuário
                padrao : Uma string. Passada de forma posiciojal pelo usuário
                        
        Returns:
                Retorna a quantidade de vezes em que ocorre a aparição de {padrao} em {cadeia}.
                        
        """
        try:
                if type(padrao) != str: raise Exception("Tipo de padrão inválido") 
                tamanho = len(padrao)
                contador = 0
                padrao = padrao.upper()
                for i in range(len(cadeia)):
                        if cadeia[i:tamanho+i] == padrao:
                                contador += 1
                return contador
        except Exception as e:
                print(e)




cadeia = 'ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG'

def TestboolPadrao(cadeia, padrao = ' '):
        """
        Documento lido: (dados_DNA.txt)

        Dada a atribuição múltipla e pocisional de argumentos para os parâmetros {cadeia} e {padrao} da função:
        Apresenta-se ao usuário o resultado de um teste booleano se possui ou não a string {padrao} na string {cadeia}

        Arguments:
                cadeia : Um string. Passada de forma posicional pelo usuário
                padrao : Uma string. Passada de forma posiciojal pelo usuário
        Returns:
                Retorna um resultado booleano do teste de {padrao} contém em {cadeia}
                        
        """
        try:
            if type(padrao) != str: raise Exception("Tipo de padrão inválido")
        
            if padrao in cadeia:
                return True
            else:
                return False
        except Exception as e:
                print(e)

def frequenciaPadrao():
    """
        Documento lido: (dados_DNA.txt)
            Dado o arquivo dados.DNA.txt:
            Executas-se uma estrutura de códigos que atríbui as colunas:
                cadeia : Refere-se a string {cadeia}
                fre

        Arguments:
                

        Returns:
                Retorna a criação das novas colunas {FREQ_ATGCCA} e {TEM_ATGCCA} assim como atribui as mesma valores referentes:
                A frequencia: Extráida com a função {procuraPadrao}
                O resultado booleano do teste feito pela função {TestboolPadrao}
    """

    with open('C:\\Users\\washi\\OneDrive\\Documentos\\aval\\Atividade_Avaliativa\\Códigos\\Segunda_Questão\\dados_DNA.txt',encoding='utf-8') as file:
        linhas = file.readlines()

    with open('C:\\Users\\washi\\OneDrive\\Documentos\\aval\\Atividade_Avaliativa\\Códigos\\Segunda_Questão\\dados_DNA.txt','w', encoding='utf-8') as file:
        file.write('sequence,FREQ_ATGCCA,TEM_ATGCCA\n')
        for cadeia in linhas[1:]:
            freq = procuraPadrao(cadeia, 'ATGCCA')
            tem = TestboolPadrao(cadeia, 'ATGCCA')
            file.write(f'{cadeia[:-1]},{freq},{tem}\n')




arquivo_tratado = []

with open('C:\\Users\\washi\\OneDrive\\Documentos\\aval\\Atividade_Avaliativa\\Códigos\\Segunda_Questão\\dados_DNA.txt', encoding = 'utf-8') as file:
    for linha in file:
        arquivo_tratado.append(linha.strip().split(','))


def naoPossuemPadrao():
    """
        Documento lido: (dados_DNA.txt)
        Dado o arquivo dados.DNA.txt:
        Apresenta-se a quantidade de sequências que não possuem o padrão {ATGCCA}
                        

        Arguments:
                        

        Returns:
        
        Retorna o a váriavel {contador} atualizada com a quantidade de vezes em que não ocorre o aparecimento do padrão {ATGCCA} no arquivo (dados_DNA.txt)
                        
    """
    contador = 0
    for linha in arquivo_tratado:
        if linha[2] == 'False':
            contador += 1
    return contador


def maximoPadrao():
    """
        Documento lido: (dados_DNA.txt)

        Dado o arquivo dados_DNA.txt já com a atualização de colunas:
        Apresenta-se a frequência máxima do padrão {ATGCCA} possui no conteúdo do arquivo {dados_DNA.txt}

        Arguments:
                        

        Returns:
        Retorna a aparição em que possui a frequência máxima do padrão {ATGCCA} no arquivo {dados_DNA.txt}
                        
    """

    valorMaior = []
    for linha in arquivo_tratado[1:]:
        valorTeste = int(linha[1])
        if valorTeste > 0 :
            valorMaior.append(valorTeste)
    maior = max(valorMaior)

    return maior




def frequenciaMaximaPadrao():
    """
        Documento lido: (dados_DNA.txt)

        Dado o arquivo dados_DNA.txt já com a atualização de colunas:
        Apresenta-se os índices das linhas que possuem frequencia igual ao valor máximo.
                        

        Arguments:
                        

        Returns:
        Retorna uma lista contendo os índices das linhas que possuem a frequência igual ao valor máximo
              
    """
    with open('C:\\Users\\washi\\OneDrive\\Documentos\\aval\\Atividade_Avaliativa\\Códigos\\Segunda_Questão\\dados_DNA.txt', encoding='utf-8') as file:
        linhas_arquivo = file.readlines()[1:]

        lista_index = []
        frequencia_maxima = maximoPadrao()

        for indices in range(len(linhas_arquivo)):
            frequencia = int(linhas_arquivo[indices].split(',')[1])
            
            if frequencia == frequencia_maxima:
                lista_index.append(indices)
    return lista_index
