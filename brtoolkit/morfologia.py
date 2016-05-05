# Arquivo para definição de classes morfológicas!

class Pronome():
    
    def __init__(self):
        self.pronomesPessoais = ['eu', 'tu', 'ele', 'ela', 'nós','vós', 'eles', 'elas','Pronome Pessoal']
        self.pronomesObliquos = ['me', 'te', 'o', 'a', 'lhe', 'se', 'nos', 'vos', 'os', 'as', 'lhes', 'mim', 'ti', 'ele', 'ela', 'si', 'nós', 'vós', 'eles', 'elas', 'Pronome Oblíquo']
        self.pronomesDeTratamento = ['você','senhor', 'senhora', 'senhoria', 'excelência', 'eminência', 'alteza', 'santidade', 'reverendíssima', 'paternidade', 'magnificência', 'majestade', 'Pronomes de Tratamento']
        self.pronomesPossessivos = ['meu', 'minha', 'teu', 'tua', 'seu', 'sua', 'nosso', 'nossa', 'vosso', 'vossa', 'deles', 'delas', 'meus', 'minhas', 'teus', 'tuas', 'seus', 'suas', 'nossos', 'nossas', 'vossos', 'vossas', 'deles', 'delas', 'Pronome Possessivo']
        self.pronomesIndefinidos = ['alguém', 'ninguém', 'tudo', 'outrem', 'nada', 'quem', 'cada', 'algo', 'algum', 'nenhum', 'todo', 'outro', 'muito', 'pouco', 'certo', 'vários', 'tanto', 'quanto', 'qualquer', 'alguns', 'nenhuns', 'todos', 'outros', 'muitos', 'poucos', 'certos', 'vários', 'tantos', 'quantos', 'qualquer', 'Pronome Indefinido']
        self.pronomesInterrogativos = ['quem', 'quanto', 'quanta', 'quantos', 'quantas', 'qual', 'quais', 'Pronome Interrogativo']
        self.pronomesRelativos = ['o qual', 'cujo', 'quanto', 'os quais', 'cujos', 'quantos', 'a qual', 'cuja', 'quanta', 'as quais', 'Pronome Relativo']
        self.todosPronomes = [self.pronomesPessoais ,self.pronomesObliquos ,self.pronomesDeTratamento ,self.pronomesPossessivos ,self.pronomesIndefinidos ,self.pronomesInterrogativos ,self.pronomesRelativos]


    def classificar(self,pronome):
        _pron = str(pronome)
        for tipo in self.todosPronomes:
            if _pron in tipo:
                return(tipo[-1])
