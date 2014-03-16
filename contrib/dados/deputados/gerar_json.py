#!/usr/bin/env python3

# Python 3 porque lida melhor com encodings em CSV

import json
import csv

NOMES_CAMPOS = ('nome_parlamentar partido uf categoria '
                'anexo gabinete fone fax email nome_civil').split()

"""
[0   'ZOINHO',
 1   'PR',
 2   'RJ',
 3   'T',
 4   'C\xc3\xa2mara dos Deputados, Edif\xc3\xadcio Anexo',
 5   '4',
 6   ', gabinete n\xc2\xba',
 7   '619',
 8   'Bras\xc3\xadlia - DF - CEP 70160-900',
 9   '3215-5619',
10   '3215-2619',
11   '12',
12   '15',
13   'dep.zoinho@camara.leg.br',
14   'ZOINHO',
15   'Exmo. Senhor Deputado',
16   '(profissao)',
17   'JORGE DE OLIVEIRA'
"""

IGNORAR = set((4, 6, 8, 11, 12, 14, 15, 16))

with open('deputados.tab') as entrada:
    leitor = csv.reader(entrada, delimiter='\t')
    for lin in leitor:
        campos = [campo for i, campo in enumerate(lin) if i not in IGNORAR]
        print(dict(zip(NOMES_CAMPOS, campos)))
