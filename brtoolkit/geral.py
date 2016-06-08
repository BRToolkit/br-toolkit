import string
class Geral():

    def removedor_pontuacao(self, text):

        _txt = text.split(" ")
        _neotexto = []
        for _word in _txt:
            if _word not in string.punctuation:
                _neotexto.append(_word)


        return(_neotexto)
