class Cardinais:
    def __init__(self):
        """
        Define os dicionários para poderem ser implementados nas diferentes classes de Unidades, Dezenas e Centenas
        """
        self._unidade = {'0': "zero", '1': "um", '2': "dois",
                        '3': "três", '4': "quatro", '5': "cinco",
                        '6': "seis", '7': "sete", '8': "oito",
                        '9': "nove"}

        self._dezena = {'10': "dez", '11': "onze",
                       '12': "doze", '13': "treze", '14': "quatorze",
                       '15': "quinze", '16': "dezesseis", '17': "dezesete",
                       '18': "dezoito", '19': "dezenove" , '20': "vinte",
                       '30': "trinta", '40': "quarenta", '50': "cinquenta",
                       '60': "sessenta", '70': "setenta", '80': "oitenta",
                       '90': "noventa"}

        self._centena = {'100': "cento", '200': "duzentos",
                        '300': "trezentos", '400': "quatrocentos", '500': "quinhentos",
                        '600': "seissentos", '700': "setessentos", '800': "oitocentos",
                        '900': "novessentos"}

    def transcrever(self, num):
        """
        Função para definição da quantidade de casas e de qual tipo de número a string *num* se enquadra
        """
        _num = str(num)
        tam_num = len(_num)

        if tam_num == 1:
            return self.unidade(_num)
        elif tam_num == 2:
            return self.dezena(_num)
        elif tam_num == 3:
            return self.centena(_num)
        elif tam_num == 4 or tam_num < 7:
            return self.milhar(_num)
        elif tam_num == 7 or tam_num < 10:
            return self.milhoes(_num)

    def unidade(self, num):
        """
        Função destinada ao processamento da casa de unidades
        """
        return self._unidade[num]

    def dezena(self, num):
        if num not in self._dezena:
            unidade = self.unidade(num[1])
            dezena = self._dezena["{N}0".format(N=num[0])]
            return "{dez} e {uni}".format(dez=dezena, uni=unidade)
        else:
            return self._dezena[num]

    def centena(self, num):
        """
        Função que serve para a definição de números com casa máxima da centena
        """
        if num == '100':
            return 'cem'

        elif num not in self._centena:
            if int(num[1]) < 1:
                aux_num = self.unidade(num[2])
            else:
                aux_num = self.dezena(num[1:])

            if num[0] != '0':
                centena = self._centena["{N}00".format(N=num[0])]
                return "{cen} e {aux}".format(cen=centena, aux=aux_num)
            else:
                return "e {aux}".format(aux=aux_num)

        else:
            return self._centena[num]

    def milhar(self, num):
        """
        Função que serve para a definição de números com casa máxima dos milhares
        """
        *mil, cen,dez,uni = num #Define uma divisão de números que são utilizados

        aux_mil = self.transcrever("".join(mil)) #São pegos apenas os números que são da ordem dos milhares e são transcritos
        aux_num = "{c}{d}{u}".format(c=cen,d=dez,u=uni) # Todo o resto é separado

        # Aqui há a verificação dos números e a junção para a formatação da String
        if aux_num == '000':
            return "{m} mil".format(m=aux_mil) # Escreve apenas para o caso do número terminar em 000
        else:
            return "{m} mil {c}".format(m=aux_mil,c=self.centena(aux_num)) # Junta os valores pegos e os reescreve

    def milhoes(self, num):
        """
        Função para escrever os números da casa dos milhões
        """
        *milhoes, mil2, mil1, mil0, cen, dez, uni = num # Define uma nova divisão dos números
        aux_milhoes = self.transcrever("".join(milhoes)) # Junta-se os números e os processa
        # Aplica uma regressão para pegar os números a partir da casa dos milhares
        aux_num = "{m2}{m1}{m0}{c}{d}{u}".format(m2=mil2,m1=mil1,m0=mil0,c=cen,d=dez,u=uni)
        if aux_num == "000000":
            return(aux_milhoes + "milhões") # Escreve os números, caso seja 000000
        else:
            return("{mi} milhões e {m}").format(mi=aux_milhoes,m=self.milhar(aux_num)) # Escreve o número completo

class Ordinais:
    def __init__(self):
        self._unidade = {'1': "primeiro", '2': "segundo",'3': "terceiro",
                        '4': "quarto", '5': "quinto", '6': "sexto",
                        '7': "setimo", '8': "oitavo", '9': "novo"}

        self._dezena = {'10': "decimo" , '20': "vigésimo", '30': "trigésimo",
                        '40': "quadragésimo", '50': "quinquagésimo", '60': "sexagésimo",
                        '70': "septuagésimo", '80': "octogésimo", '90': "nonagésimo"}

        self._centena = {'100': "centésimo", '200': "ducentésimo", '300': "trecentésimo",
                        '400': "quadrigentésimo", '500': "quingentésimo", '600': "sexcentésimo",
                        '700': "septigentésimo", '800': "octigentésimo", '900': "nongentésimo"}

    def transcrever(self, num):
        _num = str(num)
        tam_num = len(_num)

        if tam_num == 1:
            return self.unidade(_num)
        elif tam_num == 2:
            return self.dezena(_num)
        elif tam_num == 3:
            return self.centena(_num)
        elif tam_num == 4 or tam_num < 7:
            return self.milhar(_num)

    def unidade(self, num):
        return self._unidade[num]

    def dezena(self, num):
        if num not in self._dezena:
            unidade = self.unidade(num[1])
            dezena = self._dezena["{N}0".format(N=num[0])]
            return "{dez} {uni}".format(dez=dezena, uni=unidade)
        else:
            return self._dezena[num]

    def centena(self, num):
        if num not in self._centena:
            if int(num[1]) < 1:
                aux_num = self.unidade(num[2])
            else:
                aux_num = self.dezena(num[1:])

            if num[0] != '0':
                centena = self._centena["{N}00".format(N=num[0])]
                return "{cen} {aux}".format(cen=centena, aux=aux_num)
            else:
                return "{aux}".format(aux=aux_num)

        else:
            return self._centena[num]

    def milhar(self, num):
        *mil, cen, dez, uni = num
        return(mil)
