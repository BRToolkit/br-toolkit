# Arquivo para definição de classes para palavras

class Palavras():

    def separar_silabas(palavra, separador):
        """
        Função que separa silabas da palavra indicada na chamada da função. O
        usuário ainda pode escolher que tipo de separador ele deseja para poder
        ficar mais amigável ao seu código.
        """
        #TODO: Implementar função nativamente para processamento de sílabas
        from pyphen import Pyphen
        _palavra_sep = palavra.lower()
        dic = Pyphen(lang="pt_BR")
        _palavra_sep = dic.inserted(_palavra_sep)
        if separador == "-":
            return _palavra_sep
        _palavra_sep = str(_palavra_sep).replace("-", separador)
        return _palavra_sep


class Pronome():

    def __init__(self):
        """
        Todas as classes pronominais para consulta do toolkit
        """
        #TODO: Remover as palavras do arquivo e criar um json próprio para elas
        self.pronomesPessoais = ['eu', 'tu', 'ele', 'ela', 'nós','vós', 'eles', 'elas','Pronome Pessoal']
        self.pronomesObliquos = ['me', 'te', 'o', 'a', 'lhe', 'se', 'nos', 'vos', 'os', 'as', 'lhes', 'mim', 'ti', 'ele', 'ela', 'si', 'nós', 'vós', 'eles', 'elas', 'Pronome Oblíquo']
        self.pronomesDeTratamento = ['você','senhor', 'senhora', 'senhoria', 'excelência', 'eminência', 'alteza', 'santidade', 'reverendíssima', 'paternidade', 'magnificência', 'majestade', 'Pronomes de Tratamento']
        self.pronomesPossessivos = ['meu', 'minha', 'teu', 'tua', 'seu', 'sua', 'nosso', 'nossa', 'vosso', 'vossa', 'deles', 'delas', 'meus', 'minhas', 'teus', 'tuas', 'seus', 'suas', 'nossos', 'nossas', 'vossos', 'vossas', 'deles', 'delas', 'Pronome Possessivo']
        self.pronomesIndefinidos = ['alguém', 'ninguém', 'tudo', 'outrem', 'nada', 'quem', 'cada', 'algo', 'algum', 'nenhum', 'todo', 'outro', 'muito', 'pouco', 'certo', 'vários', 'tanto', 'quanto', 'qualquer', 'alguns', 'nenhuns', 'todos', 'outros', 'muitos', 'poucos', 'certos', 'vários', 'tantos', 'quantos', 'qualquer']
        self.pronomesInterrogativos = ['quem', 'quanto', 'quanta', 'quantos', 'quantas', 'qual', 'quais', 'Pronome Interrogativo']
        self.pronomesRelativos = ['o qual', 'cujo', 'quanto', 'os quais', 'cujos', 'quantos', 'a qual', 'cuja', 'quanta', 'as quais', 'Pronome Relativo']
        self.todosPronomes = [self.pronomesPessoais ,self.pronomesObliquos ,self.pronomesDeTratamento ,self.pronomesPossessivos ,self.pronomesIndefinidos ,self.pronomesInterrogativos ,self.pronomesRelativos]


    def classificar(self,pronome):
        """
        Função tem como o objetivo a classificação do pronome especificado na
        chamada da função.
        """
        _pron = str(pronome)
        for tipo in self.todosPronomes:
            if _pron in tipo:
                return(tipo[-1])

#TODO: Criação de arquivos para armazenar os pronomes e outras classes morfológicas
