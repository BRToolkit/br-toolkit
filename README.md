# BR-toolkit
Caixa de ferramentas/toolkit para processamento e análise de Português Brasileiro em Python 3


#### Números Cardinais:

```python

from numeros import Cardinais

card = Cardinais()

assert(card.transcrever(5), 'cinco') #True

# Os números cardinais são suportados até a casa dos milhões, a partir disto, todos os números não podem ser testados!
```



#### Números Ordinais:

```python

from numeros import Ordinais

_ord = Ordinais()

assert(_ord.transcrever(5), 'quinto') #True
```

#### Sentimentos randômicos:

```python

from texto import Texto
from random import choice

texto = Texto()

choice(texto.emocoes) #alegria
```

#### Nomes comuns no brasil:

```python

from texto import Texto
from random import choice

texto = Texto()

choice(texto.nome) #Eduardo
choice(texto.nome) #Sophia
choice(texto.nome) #Davi
```

#### Classificação de Pronomes:

```python

from brtoolkit.morfologia import Pronome
from random import choice

# Classificação de Pronomes
p = Pronome()
p.classificar("eu") # Pronome Pessoal

```
