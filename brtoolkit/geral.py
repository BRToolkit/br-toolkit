from nltk import word_tokenize
import string
import collections
from re import compile
class Geral():

    def palavras(text):
        """ Método que remove a pontuação da frase
        para poder retornar um array com todas as
        palavras de forma limpa """

        regex = compile("\w+")
        saida = regex.findall(text)
        return " ".join(saida)

    def conta_palavras(text):
        """ Função que retorna a contagem de todas
        as palavras de um texto selecionado pelo
        usuário"""

        return(collections.Counter(
        Geral.palavras(text).split(" ")
        ))

    def diff_textos(texto1, texto2):
        """ Função que retorna o diferencial entre
        dois textos selecionados e inputados pelo
        usuario do BR-Toolkit """
        try:
            leitura1 = open(texto1, "r")
            leitura2 = open(texto2, "r")


        except Except:
            return "Houve um problema na leitura de um \
            dos seus arquivos"
