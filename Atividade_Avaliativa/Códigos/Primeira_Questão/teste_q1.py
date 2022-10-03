arquivo_tratado = []

with open('/home/suporte/Documentos/Kevin/Atividade_Corrigidinha_Gostosinha-main/Atividade_Avaliativa/Códigos/Primeira_Questão/dados_usuario.csv', encoding = 'utf-8') as file:
    for linha in file:
        arquivo_tratado.append(linha.strip().split(','))

'''
def procuraNome(nome = ' '):
        """
        Documento lido: (dados_usuario.csv)

        Apresenta a quantidade e uma lista com os registros curja a culuna name do documento inicie com o valor do parâmetro nome.

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
                                lista.append(linhas)
                                contador += 1
                return contador, lista
        
        except ValueError:
                print('Valor inválido')
                
contador, lista = procuraNome('Samuel')
print(f'{contador}\n{lista}')



def quantidadeGender(ano, sexo):
        """
        Documento lido: (dados_usuario.csv)

        Dada uma quantidade de registros
        Apresenta:
        gender = Igual ao valor do parâmetro sexo
        year = Com o valor maior ou igual ao valor do parâmetro ano.

        Arguments:
                ano : Uma String
                sexo: Uma String. Utilizando o método .capitalize()

        Returns:
                Retorna
        """
        try:
                if type(sexo) != str: raise TypeError
                if ano < 0: raise ValueError
                lista = []
                contador = 0
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
                
contador, lista = quantidadeGender(2002, "F")
print(contador, lista)


def substringARG(arg = ' '):
        """
                Documento lido: (dados_usuario.csv)


                Arguments:
                        

                Returns:
                
        """
        try:
                lista = []
                contador = 0
                for linha in arquivo_tratado:
                        for argumento_do_arquivo in linha:
                                if str(arg) in argumento_do_arquivo:
                                        lista.append(linha)
                                        contador += 1
                return contador, lista
        except:
                print('Erro de tempo de execução ')
                
contador, lista = substringARG('muel')
print(f'{contador}\n{lista}')


def procuraNumero(numero):
        """
        Documento lido: (dados_usuario.csv)

                

        Arguments:
                

        Returns:
                
        """
        try:
                if int(numero) < 0: raise Exception("Valor inválido")
                lista = []
                contador = 0
                for linhas in arquivo_tratado:
                        if str(numero) == linhas[4]:
                                lista.append(linhas[0])
                                contador += 1
                return contador, lista
        except Exception as e:
                print(e)
                
contador, lista = procuraNumero(5)
print(f'{contador}')

'''

def novo_cadastro(nome, ano, sexo, numero):
        """
        Documento lido: (dados_usuario.csv)

        Arguments:
                

        Returns:
                
        """
        try:
            id = int(arquivo_tratado[-1][0])+1
            with open('C:\\Users\\kimli\\Desktop\\Atividade_Avaliativa\\dados_usuario.csv','a', encoding ='utf-8') as file:
                file.write(f'{id},{nome},{ano},{sexo},{numero}\n')
                
        except:
            print('Todos os valores são obrigatórios')

novo_cadastro('Kim','2002','M','01')

'''

#quantidadeGender()
substringARG()
procuraNumero()
novo_cadastro()
'''