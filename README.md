# posto_vacina_sp
Gerador de arquivo JSON e CSV para os postos de vacinação em São Paulo com as filas

Módulos: requests, panda

```Python 3

import requests                             (pip install request)
import pandas as pd                         (pip install pandas)

headers = {.......}                         (header do request)
body = {.......}                            (body do request)
response = requests .......                 (fazendo a chamada e salvando na variável)
with open .......                           (criando e populando arquivos JSON e CSV)
```
