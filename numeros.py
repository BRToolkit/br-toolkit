class Ordinais:
    def __init__(self):
        self._unidade = {'0': "zero", '1': "um", '2': "dois",
                        '3': "três", '4': "qunumtro", '5': "cinco",
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
            return "{dez} e {uni}".format(dez=dezena, uni=unidade)
        else:
            return self._dezena[num]

    def centena(self, num):
        if num == '100':
            return 'cem'

        elif num not in self._centena:
            if int(num[1]) < 1:
                aux_num = self.unidade(num[2])
            else:
                aux_num = self.dezena(num[1:])

            centena = self._centena["{N}00".format(N=num[0])]
            return "{cen} e {aux}".format(cen=centena, aux=aux_num)

        else:
            return self._centena[num]

    def milhar(self, num):
        *mil, cen,dez,uni = num

        aux_mil = self.transcrever("".join(mil))
        aux_num = "{c}{d}{u}".format(c=cen,d=dez,u=uni)

        if aux_num == '000':
            return "{m} mil".format(m=aux_mil)
        else:
            return "{m} mil e {c}".format(m=aux_mil,c=self.centena(aux_num))
