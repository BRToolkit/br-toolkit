import string
import collections

class Geral():

    def removedor_pontuacao(self, text):

        _txt = text.split(" ")
        _neotexto = []
        for _word in _txt:
            for ponto in string.punctuation :
                _word = _word.replace(ponto, "")
            _neotexto.append(_word)

        return(_neotexto)

    def conta_palavras(self, text):
        texto = Geral().removedor_pontuacao(text)
        contas = collections.Counter(texto)
        return(contas)
