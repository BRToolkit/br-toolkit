from unittest import TestCase, main
from texto import Texto
from random import choice
from numeros import Cardinais, Ordinais

class Teste_card(TestCase):
    def test_unidade(self):
        cardinais = Cardinais()
        n_lista = [0,1,2,3,4,5]
        t_lista = ['zero','um','dois', 'três', 'quatro', 'cinco']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

    def test_dezena(self):
        cardinais = Cardinais()
        n_lista = [10,11,12,13,14,15,20,30]
        t_lista = ['dez','onze','doze', 'treze', 'quatorze', 'quinze', 'vinte', 'trinta']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

    def test_centena(self):
        cardinais = Cardinais()
        n_lista = [100,200,300,400,500,600,700,800,900]
        t_lista = ['cem','duzentos','trezentos', 'quatrocentos', 'quinhentos',
                    'seissentos', 'setessentos', 'oitocentos', 'novessentos']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

    def test_milhar(self):
        cardinais = Cardinais()
        n_lista = [1000,2000,3000,4000,5000,60000]
        t_lista = ['um mil','dois mil','três mil','quatro mil','cinco mil','sessenta mil']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

    def test_mix(self):
        cardinais = Cardinais()
        n_lista = [215, 550, 111, 1201, 1001, 101]
        t_lista = ['duzentos e quinze', 'quinhentos e cinquenta', 'cento e onze',
                    'um mil duzentos e um', 'um mil e um', 'cento e um']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

class Teste_texto(TestCase):
    def teste_emo(self):
        emo = Texto()
        _emo = choice(emo.emocoes)
        self.assertIsNotNone(_emo)

    def teste_nome(self):
        emo = Texto()
        nome = choice(emo.emocoes)
        self.assertIsNotNone(nome)

    def teste_stopwords(self):
        emo = Texto()
        nome = choice(emo.stopwords)
        self.assertIsNotNone(nome)        

class Teste_ord(TestCase):
    def test_unidade(self):
        ordinais = Ordinais()
        n_lista = [1,2,3,4,5]
        t_lista = ['primeiro','segundo','terceiro', 'quarto', 'quinto']

        for num, trans in zip(n_lista,t_lista):
            result = ordinais.transcrever(num)
            self.assertEqual(result, trans)

    def test_centena(self):
        ordinais = Ordinais()
        n_lista = [100,200,300,400,500,600,700,800,900]
        t_lista = ['centésimo','ducentésimo','trecentésimo', 'quadrigentésimo', 'quingentésimo',
                    'sexcentésimo', 'septigentésimo', 'octigentésimo', 'nongentésimo']

        for num, trans in zip(n_lista,t_lista):
            result = ordinais.transcrever(num)
            self.assertEqual(result, trans)


    def test_mix(self):
        ordinais = Ordinais()
        n_lista = [215, 550, 111]
        t_lista = ['ducentésimo decimo quinto', 'quingentésimo quinquagésimo', 'centésimo decimo primeiro']

        for num, trans in zip(n_lista,t_lista):
            result = ordinais.transcrever(num)
            self.assertEqual(result, trans)

if __name__ == '__main__':
    main()
