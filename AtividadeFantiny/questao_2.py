def qtd_padrao_in_cadeia(cadeia, padrao):
    '''
    Conta quantas vezes padrao aparece em cadeia.

    Arguments:
        cadeia: uma string.
        padrao: uma string.
    
    Returns:
        Quantidade de vezes que "padrao" aparece em "cadeia".
    '''

    try:
        contador = 0

        if type(padrao) != str and type(cadeia) != str:
            raise Exception('Valor inválido: padrão ou cadeia não é uma string')

        elif len(padrao) > len(cadeia):
            raise Exception('Tamanho inválido: padrão é maior que cadeia.')
        
        else:
            for indice in range(len(cadeia)):
                if cadeia[indice:len(padrao)+indice] == padrao.upper():
                    contador += 1
    except Exception as erro:
        print(erro)
    
    else:
        return contador

def padrao_in_cadeia(cadeia, padrao):
    '''
    Verifica se padrao é substring de cadeia.

    Arguments:
        cadeia: uma string.
        padrao: uma string.
    
    Returns:
        Valor booleano da verificação se padrão é substring de cadeia.
    '''
    try:
        if type(padrao) != str and type(cadeia) != str:
            raise Exception('Valor inválido: padrão ou cadeia não é uma string')

        elif len(padrao) > len(cadeia):
            raise Exception('Tamanho inválido: padrão é maior que cadeia.')
        
        else:
            if padrao.upper() in cadeia:
                return True

    except Exception as erro:
        print(erro)
    
    else:
        return False

def registro_dna():
    '''
    Acrecenta as colunas FREQ_ATGCCA e TEM_ ATGCCA com os
    seus respectivos dados no arquivo 'dados_DNA.txt'.

    Arguments:
        Sem argumentos.
    
    Returns:
        Sem retorno.
    '''
    
    try:
        with open('dados_DNA.txt', 'r', encoding='utf-8') as file:
            linhas = file.readlines()
        
        with open('dados_DNA.txt', 'w', encoding='utf-8') as file:
            file.write('sequence,FREQ_ATGCCA,TEM_ ATGCCA\n')
            for linha in linhas[1:]:
                qtd = qtd_padrao_in_cadeia(linha, 'ATGCCA')
                tem = padrao_in_cadeia(linha, 'ATGCCA')
                file.write(f'{linha[:-1]},{qtd},{tem}\n')

    except (FileNotFoundError, FileExistsError):
        print('Arquivo não encontrado ou inexistente.')
    
    else:
        print('Arquivo dados_DNA.txt atualizado com sucesso. :)')

def arquivo_dados_dna():
    '''
    Guarda cada coluna do arquivo "dados_DNA.txt"
    em uma posição de uma lista.

    Arguments:
        Não recebe argumentos.
    
    Returns:
        Lista com as listas das colunas
        do arquivo "dados_DNA.txt".
    '''

    try:
        lista_file = []

        with open('dados_DNA.txt', encoding= 'utf-8') as file:
            for linha_file in file:
                lista_file.append(linha_file.strip().split(','))

    except (FileNotFoundError, FileExistsError):
        return None
    
    else:
        return lista_file

def qtd_sequence_false():
    '''
    Verifica a quantidade de sequências que não possuem o padrão ATGCCA.

    Arguments:
        Sem argumentos.
    
    Returns:
        Quantidade de False na coluna TEM_ATGCCA.
    '''

    try:
        lista_file = arquivo_dados_dna()
        qtd_false = 0
        
        for linha in lista_file:
            if linha[2] == 'False':
                qtd_false += 1
        
    except TypeError:
        print('Erro na leitura do arquivo dados_DNA.TXT')
    
    else:
        return qtd_false

def freq_max():
    '''
    Verifica a qual a frequência máxima que padrão
    ATGCCA aparece no arquivo "dados_DNA.txt".

    Arguments:
        Sem argumentos.
    
    Returns:
        Frquência máxima do padrão ATGCCA.
    '''

    try:
        lista_file = arquivo_dados_dna()
        lista_freq = []
        
        for linha in lista_file[1:]:
            lista_freq.append(int(linha[1]))
    
        return max(lista_freq)
        
    except (TypeError, ValueError):
        print('Erro na leitura do arquivo dados_DNA.TXT')

def indices_freq_max():
    '''
    Verifica quais os índices do arquivo
    possuem a frequência máxima.

    Arguments:
        Sem argumentos.
    
    Returns:
        Indice(s) que possuem a frequência máxima.
    '''

    try:
        lista_file = arquivo_dados_dna()
        freq_max_result = freq_max()
        indices_lista = []
        
        if type(freq_max_result) != int:
            raise Exception('Valor inválido: frequência máxima não é um inteiro.')
        
        else:
            for linhas in lista_file[1:]:
                if int(linhas[1]) == freq_max_result:
                    indices_lista.append(lista_file.index(linhas)+1)
    
    except Exception as erro:
        print(erro)
    
    else:
        return indices_lista
