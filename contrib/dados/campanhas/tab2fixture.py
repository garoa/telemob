"""
{
  "pk": 14,
  "model": "main.contact",
  "fields": {
    "contacted_by": "tel",
    "politician": 14,
    "result": "11",
    "campaign": 1,
    "date_created": "2014-03-18"
  }
}

main_contact (id, politician_id, campaign_id, contacted_by, date_created, result)
"""

import io
import json

NOMES_CAMPOS = set('politician campaign contacted_by date_created result'.split())

contatos = []
with io.open('marco-civil-2014-03.txt', encoding='utf-8') as entrada:
    for lin in entrada:
        lin = lin.rstrip()
        if lin.startswith('#') or not lin:
            continue
        pk, politician, campaign, contacted_by, date_created, result = lin.split('\t')
        pk = int(pk)
        campaign = int(campaign)
        politician = int(politician)
        campos = {}
        campos.update(locals())
        nao_campos = set(campos) - NOMES_CAMPOS
        for chave in nao_campos:
            del campos[chave]
        reg = dict(pk=pk, model='main.contact', fields=campos)
        contatos.append(reg)

print(json.dumps(contatos, indent=2))
