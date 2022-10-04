from shutil import ExecError


arquivo_tratado = []

with open('C:\\Users\\washi\\OneDrive\\Documentos\\aval\\Atividade_Avaliativa\\Códigos\\Primeira_Questão\\dados_usuario.csv', encoding = 'utf-8') as file:
    for linha in file:
        arquivo_tratado.append(linha.strip().split(','))


def procuraNome(nome = ' '):
        """
        Documento lido: (dados_usuario.csv)

        Apresenta a quantidade e uma lista com os registros cujo a culuna name do documento inicie com o valor do parâmetro nome.

        Arguments:
        nome : Uma string. Default valor = ' ' (string vazia)

        Returns:
        Retorna a quantidade de aparições de nome e uma lista com suas aparições.
        """
        try:
                lista = []
                contador = 0
                for linhas in arquivo_tratado:
                        if nome in linhas[3]:
                                print(linhas[3])
                                lista.append(linhas)
                                contador += 1
                return contador, lista
        
        except ValueError:
                print('Valor inválido')
        except TypeError:
                print('Tipo de variavel inválida')
                




def quantidadeGender(ano, sexo):
        """
        Documento lido: (dados_usuario.csv)

        Dada a passagem de argumentos para os parâmetros 'ano' e 'sexo' da função:
        Apresenta a quantidade de vezes que índices da coluna gender são iguais ao argumento passado para sexo e 
        year tem um valor maior ou igual ao parâmetro ano.
        
        Apresenta:
                gender = Igual ao valor do parâmetro sexo
                year = Com o valor maior ou igual ao valor do parâmetro ano.

        Arguments:
                ano : Uma String. Agumento passado pelo usuário
                sexo: Uma String. Argumento passado pelo usuário. Deve conter uma string maiúscula

        Returns:
                Retorna a quantidade e uma lista referente as aparições dos resultados que se adequam aos requisitos constados acima 
        """
        try:
                
                if type(sexo) != str: raise TypeError
                if ano < 0 and sexo != 'F' and sexo != "M": raise ValueError
                lista = []
                contador = 0
                sexo = sexo.capitalize()
                print(sexo)
                for linhas in arquivo_tratado:
                        if sexo in linhas[2]:
                                if str(ano) <= linhas[1]:
                                        lista.append(linhas)
                                        contador += 1
                return contador, lista
        except TypeError:
                print('Tipo de valor inválido')
        except ValueError: 
                print('Valor inválido')


def substringARG(arg = ' '):
        """
                Documento lido: (dados_usuario.csv)

                        Dada a passagem de um argumento para o parâmetro 'arg' da função:
                        Apresenta a quantidade e uma lista de aparecimentos da substring do mesmo.

                Arguments:
                        
                        arg : uma string. Passado pelo usuário
                        

                Returns:
                        Retorna a quantidade e uma lista de aparecimentos da substring do mesmo.
        """
        try:
                if type(arg) != str: raise Exception('Tipo de argumento inválido')
                lista = []
                contador = 0
                for linha in arquivo_tratado:
                        for argumento_do_arquivo in linha:
                                if arg in argumento_do_arquivo:
                                        lista.append(linha)
                                        contador += 1
                return contador, lista
        except Exception as e:
                print(e)
                

def procuraNumero(numero):
        """
        Documento lido: (dados_usuario.csv)

                Dada a passagem de um argumento para o parâmetro 'numero' da função:
                Apresenta uma lista de com os Ids dos registros que possuem a coluna {number} do arquivo com valores iguais ao parâmetro {numero}.

        Arguments:
                numero : Uma string. Atríbuida pelo usuário.

        Returns:
                Retorna uma lista com aparições de linhas com a coluna {number} iguais ao parâmetro passado.
                
        """
        try:
                if int(numero) < 0: raise Exception("Valor inválido")
                if type(numero) != int and type(numero) != str: raise Exception('Tipo de argumento inválido')
                lista = []
                contador = 0
                for linhas in arquivo_tratado:
                        if str(numero) == linhas[4]:
                                lista.append(linhas[0])
                                contador += 1
                return contador, lista
        except Exception as e:
                print(e)
                


def novo_cadastro(nome = ' ', ano = 0, sexo = ' ', numero =0):
        """
        Documento lido: (dados_usuario.csv)

        Dada a atríbuição múltipla de argumentos para os parâmetros {nome},{ano},{sexo} e {numero} da função:
        É feita uma atualização do arquivo dados_usuario.csv, realizando assim a adição de uma nova linha no arquivo.
        Assim que o código é executado com os parâmtros corretos, ocorre uma atualização do ID.

        Arguments:
            nome : Uma string. Atríbuida pelo usuário.
            ano : Uma string. Atríbuida pelo usuário.
            sexo : Uma string. Atríbuida pelo usuário.
            numero : Uma string. Atríbuida pelo usuário.

        Returns:
                
        """
        try:
                if int(ano) <= 0: raise Exception('Valor inválido')
                if type(ano) != int and type(ano) != str: raise Exception('Tipo de argumento inválido')
                if int(numero) <= 0: raise Exception('Valor inválido')
                if type(numero) != int and type(numero) != str: raise Exception('Tipo de argumento inválido')
                if type(sexo) != str: raise Exception('Tipo de argumento inválido')
                if type(nome) != str: raise Exception('Tipo de argumento inválido')
                id = int(arquivo_tratado[-1][0])+1
                with open('\\Users\\washi\\OneDrive\\Documentos\\aval\\Atividade_Avaliativa\\Códigos\\Primeira_Questão\\dados_usuario.csv','a', encoding ='utf-8') as file:
                        file.write(f'{id},{nome},{ano},{sexo},{numero}\n')
        
        except Exception as e :
                print(e)
            

