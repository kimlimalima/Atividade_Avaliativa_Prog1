# primeiroNumero = int(input('Primeiro Número: '))
# segundoNumero  = int(input('Segundo Número:  '))

def testeBoolPrimosEntreSi(primeiroNumero = int, segundoNumero = int):
        """

        Dada a atribuíção de dois números inteiros maiores que zero:
        Calcula-se e apresenta o resultado booleano se os mesmos são primos entre si
                        

        Arguments:
                        primeiroNumero: Inteiro, maior que zero. Atribuído pelo usuário
                        SegundoNumero: Inteiro, maior que zero. Atribuído pelo usuário

        Returns:
                Retorna o valor booleano do teste se os números atribuídos são primos entre si.
                        
        """
        try:
            if primeiroNumero <= 0 or segundoNumero <=0 : Exception('Valor <= 0 é inválido')
            if type(primeiroNumero) != int or type(segundoNumero) != int : Exception('Tipo do valor é inválido')
            maior = segundoNumero
            menor = primeiroNumero

            if primeiroNumero > segundoNumero:
                    maior = primeiroNumero
                    menor = segundoNumero
            for i in range(2, menor):
                    if menor%i==0 and maior%i==0:
                            return False
            return True
        except Exception as e:
            print(e)

resultado = testeBoolPrimosEntreSi(primeiroNumero, segundoNumero)
print(resultado)


from random import randrange
localArquivo = 'C:\\Users\\washi\\OneDrive\\Documentos\\aval\\Atividade_Avaliativa\\Códigos\\Terceira_Questão\\primos_entre_si.txt'

def sorteioPrimos():
        """
        Dada o sorteio de dois números inteiros maiores que zero:

        Ocorre 1000 sorteios de dois números gerados aleatóriamente no intervalo de 1-100 em seguida:
        Escreve em um arquivo {primos_entre_si.txt} SIM se a função {testeBoolPrimosEntreSi} retornar True e NÃO caso o contrário
        Após isso é efetuado o cálculo da porcentagem referente a quantidade de aparições de numeros primos entre si

        Arguments:
                        

        Returns:
                Retorna a porcentagem equivalente a quantidade de valores iguais a 'SIM' contidas no arquivo {primos_entre_si.txt}
                        
        """
        with open(localArquivo, 'a', encoding='utf-8') as file:
                        
                for resultado in range(0,1000):

                        primeiroSorteado = randrange(1,100)
                        segundoSorteado = randrange(1,100)

                        resultado = testeBoolPrimosEntreSi(primeiroSorteado, segundoSorteado)
                        # print(resultado)


                        if resultado == True:
                                file.write('SIM \n')
                        else:
                                file.write('NÃO \n')
                                
        with open(localArquivo,'r', encoding='utf-8') as file:
                percent = 0
                for linha in file:               
                        if 'SIM' in linha:
                                percent += 1
                        porcentagem = (percent/1000)*100

        return porcentagem

porcentagem = sorteioPrimos()
print(porcentagem)
