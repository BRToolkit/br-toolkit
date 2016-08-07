from brtoolkit import palavras.Palavras


def separar_silabas_frase(frase, separador):
    lstpalavras = [item for item in frase.split(" ")]
    for palavra in lstpalavras:
        print(palavras.Palavras().separar_silabas(palavra, separador))
