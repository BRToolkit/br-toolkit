from nltk import word_tokenize
import string
import collections

class Geral():

    def removedor_pontuacao(text):
        """ Método que remove a pontuação da frase
        para poder retornar um array com todas as
        palavras de forma limpa """
        _txt = text.split(" ")
        _neotexto = []
        for _word in _txt:
            for ponto in string.punctuation :
                _word = _word.replace(ponto, "")
            _neotexto.append(_word)

        return(_neotexto)

    def conta_palavras(text):
        return(collections.Counter(Geral().removedor_pontuacao(text)))

    def diff_textos(texto1, texto2):
        try:
            leitura1 = open(texto1, "r")
            leitura2 = open(texto2, "r")


        except Except:
            return "Houve um problema na leitura de um dos seus arquivos"
