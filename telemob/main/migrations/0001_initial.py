# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='Nome da Campanha')),
                ('description', models.TextField(verbose_name='Descri\xe7\xe3o da Campanha')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('last_updated', models.DateField(auto_now=True, verbose_name='\xdaltima atualiza\xe7\xe3o em')),
            ],
            options={
                'verbose_name': 'Campanha',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacted_by', models.CharField(max_length=10, verbose_name='Contato via', choices=[('tel', 'Telefone'), ('telegram', 'Telegrama via Web'), ('fax', 'Fax'), ('email', 'E-mail')])),
                ('result', models.CharField(blank=True, max_length=10, null=True, verbose_name='Resultado do contato', choices=[('Telefonei', (('10', 'Falei com o(a) Deputado(a) em pessoa.'), ('11', 'Falei com outra pessoa.'), ('12', 'Deixei recado em uma m\xe1quina.'), ('13', 'Fone: n\xfamero ocupado'), ('14', 'Fone: ningu\xe9m atendeu.'), ('15', 'Fone: n\xfamero inexistente ou outra falha.'))), ('Enviei telegrama', (('20', 'Nada a reportar: correio vai entregar no gabinete!'),)), ('Enviei fax', (('30', 'Fax: transmiss\xe3o bem sucedida.'), ('31', 'Fax: n\xfamero ocupado.'), ('32', 'Fax: n\xe3o atendeu.'), ('33', 'Fax: n\xfamero inexistente ou outra falha.'))), ('Enviei e-mail', (('40', 'E-mail enviado e n\xe3o voltou, tomara que leiam.'), ('41', 'E-mail voltou com erro.')))])),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('campaign', models.ForeignKey(verbose_name='Campanha', to='main.Campaign')),
            ],
            options={
                'verbose_name': 'Contato',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HelpText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='Nome da Ajuda')),
                ('description', models.TextField(verbose_name='Texto de Ajuda')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('last_updated', models.DateField(auto_now=True, verbose_name='\xdaltima atualiza\xe7\xe3o em')),
                ('campaign', models.ForeignKey(verbose_name='Texto de ajuda para a campanha', to='main.Campaign')),
            ],
            options={
                'verbose_name': 'Texto de Ajuda',
                'verbose_name_plural': 'Textos de Ajuda',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('parliamentary_name', models.CharField(max_length=150, verbose_name='Nome Parlamentar')),
                ('political_party', models.CharField(max_length=10, verbose_name='Partido', choices=[('PMDB', 'PMDB - Partido Do Movimento Democr\xe1tico Brasileiro'), ('PTB', 'PTB - Partido Trabalhista Brasileiro'), ('PDT', 'PDT - Partido Democr\xe1tico Trabalhista'), ('PT', 'PT - Partido Dos Trabalhadores'), ('DEM', 'DEM - Democratas'), ('PCdoB', 'PCdoB - Partido Comunista Do Brasil'), ('PSB', 'PSB - Partido Socialista Brasileiro'), ('PSDB', 'PSDB - Partido Da Social Democracia Brasileira'), ('PTC', 'PTC - Partido Trabalhista Crist\xe3o'), ('PSC', 'PSC - Partido Social Crist\xe3o'), ('PMN', 'PMN - Partido Da Mobiliza\xe7\xe3o Nacional'), ('PRP', 'PRP - Partido Republicano Progressista'), ('PPS', 'PPS - Partido Popular Socialista'), ('PV', 'PV - Partido Verde'), ('PTdoB', 'PTdoB - Partido Trabalhista Do Brasil'), ('PP', 'PP - Partido Progressista'), ('PSTU', 'PSTU - Partido Socialista Dos Trabalhadores Unificado'), ('PCB', 'PCB - Partido Comunista Brasileiro'), ('PRTB', 'PRTB - Partido Renovador Trabalhista Brasileiro'), ('PHS', 'PHS - Partido Humanista Da Solidariedade'), ('PSDC', 'PSDC - Partido Social Democrata Crist\xe3o'), ('PCO', 'PCO - Partido Da Causa Oper\xe1ria'), ('PTN', 'PTN - Partido Trabalhista Nacional'), ('PSL', 'PSL - Partido Social Liberal'), ('PRB', 'PRB - Partido Republicano Brasileiro'), ('PSOL', 'PSOL - Partido Socialismo E Liberdade'), ('PR', 'PR - Partido Da Rep\xfablica'), ('PSD', 'PSD - Partido Social Democr\xe1tico'), ('PPL', 'PPL - Partido P\xe1tria Livre'), ('PEN', 'PEN - Partido Ecol\xf3gico Nacional'), ('PROS', 'PROS - Partido Republicano Da Ordem Social'), ('SDD\xa0', 'SDD - Solidariedade')])),
                ('uf', models.CharField(max_length=10, verbose_name='UF', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('category', models.CharField(max_length=20, verbose_name='Categoria', choices=[('T', 'Titular'), ('S', 'Suplente'), ('E', 'Efetivo')])),
                ('annex', models.IntegerField(null=True, verbose_name='Anexo', blank=True)),
                ('chamber', models.IntegerField(null=True, verbose_name='Gabinete', blank=True)),
                ('tel', models.CharField(max_length=20, verbose_name='Telefone')),
                ('fax', models.CharField(max_length=20, verbose_name='Fax')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('last_updated', models.DateField(auto_now=True, verbose_name='\xdaltima atualiza\xe7\xe3o em')),
            ],
            options={
                'verbose_name': 'Pol\xedtico',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='politician',
            field=models.ForeignKey(verbose_name='Pol\xedtico', to='main.Politician'),
            preserve_default=True,
        ),
    ]
