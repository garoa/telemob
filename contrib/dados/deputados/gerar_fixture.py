#!/usr/bin/env python3

# Python 3 porque lida melhor com encodings em CSV

"""
CSV:
 0   'ZOINHO',
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

import json
import csv

NOMES_CAMPOS = ('parliamentary_name political_party uf category '
                'annex chamber tel fax email name').split()

SAMPLE = {"pk": 1, "model": "main.politician", "fields":
{"category": "titular",
"fax": "2222-2222",
"political_party": "PMDB",
"tel": "1111-1111",
"name": "Fulano", "annex": 1,
"parliamentary_name": "",
"chamber": 234,
"date_created":
"2014-03-14", "uf": "AC",
"email": "e@mail.com",
"last_updated": "2014-03-14"}}


IGNORAR = set((4, 6, 8, 11, 12, 14, 15, 16))

with open('deputados.tab') as entrada:
    leitor = csv.reader(entrada, delimiter='\t')
    registros = []
    for idx, lin in enumerate(leitor):
        if idx == 0: continue # pular linha 1
        campos = [campo for i, campo in enumerate(lin) if i not in IGNORAR]
        campos = dict(zip(NOMES_CAMPOS, campos))
        campos['last_updated'] = campos['date_created'] = '2015-01-25'
        campos['annex'] = int(campos['annex'])
        campos['chamber'] = int(campos['chamber'])
        registro = dict(pk=idx, model='main.politician', fields=campos)
        registros.append(registro)

with open('deputados.json', 'wt', encoding='utf-8') as saida:
    json.dump(registros, saida)

print(idx, 'registros gerados')
