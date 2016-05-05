# BR-toolkit
Caixa de ferramentas para português brasileiro em python3


#### Números Cardinais:

```python

from numeros import Cardinais

card = Cardinais()

assert(card.transcrever(5), 'cinco') #True
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
