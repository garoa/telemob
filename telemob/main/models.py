# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Campaign(models.Model):
    name = models.CharField('Nome da Campanha', max_length=150)
    description = models.TextField('Descrição da Campanha')
    date_created = models.DateField('Criado em', auto_now_add=True)
    last_updated = models.DateField('Última atualização em', auto_now=True)

    def __unicode__(self):
        return self.name


class Politician(models.Model):
    PARTY_CHOICES = (
        ('PMDB', 'PMDB - Partido Do Movimento Democrático Brasileiro'),
        ('PTB', 'PTB - Partido Trabalhista Brasileiro'),
        ('PDT', 'PDT - Partido Democrático Trabalhista'),
        ('PT', 'PT - Partido Dos Trabalhadores'),
        ('DEM', 'DEM - Democratas'),
        ('PCdoB', 'PCdoB - Partido Comunista Do Brasil'),
        ('PSB', 'PSB - Partido Socialista Brasileiro'),
        ('PSDB', 'PSDB - Partido Da Social Democracia Brasileira'),
        ('PTC', 'PTC - Partido Trabalhista Cristão'),
        ('PSC', 'PSC - Partido Social Cristão'),
        ('PMN', 'PMN - Partido Da Mobilização Nacional'),
        ('PRP', 'PRP - Partido Republicano Progressista'),
        ('PPS', 'PPS - Partido Popular Socialista'),
        ('PV',  'PV - Partido Verde'),
        ('PTdoB','PTdoB - Partido Trabalhista Do Brasil'),
        ('PP',  'PP - Partido Progressista'),
        ('PSTU', 'PSTU - Partido Socialista Dos Trabalhadores Unificado'),
        ('PCB', 'PCB - Partido Comunista Brasileiro'),
        ('PRTB', 'PRTB - Partido Renovador Trabalhista Brasileiro'),
        ('PHS', 'PHS - Partido Humanista Da Solidariedade'),
        ('PSDC', 'PSDC - Partido Social Democrata Cristão'),
        ('PCO', 'PCO - Partido Da Causa Operária'),
        ('PTN', 'PTN - Partido Trabalhista Nacional'),
        ('PSL', 'PSL - Partido Social Liberal'),
        ('PRB', 'PRB - Partido Republicano Brasileiro'),
        ('PSOL', 'PSOL - Partido Socialismo E Liberdade'),
        ('PR',  'PR - Partido Da República'),
        ('PSD', 'PSD - Partido Social Democrático'),
        ('PPL', 'PPL - Partido Pátria Livre'),
        ('PEN', 'PEN - Partido Ecológico Nacional'),
        ('PROS', 'PROS - Partido Republicano Da Ordem Social'),
        ('SDD ', 'SDD - Solidariedade'),
    )

    name = models.CharField('Nome', max_length=150)
    tel = models.CharField('Telefone', max_length=20)
    email = models.EmailField('Email', max_length=100)
    uf = models.CharField(choices=STATE_CHOICES, max_length=10)
    political_party = models.CharField(choices=PARTY_CHOICES, max_length=10)
    date_created = models.DateField('Criado em', auto_now_add=True)
    last_updated = models.DateField('Última atualização em', auto_now=True)


class Contact(models.Model):

    CONTACT_CHOICES = (
        ('tel', 'Telefone'),
        ('email', 'E-mail')
    )

    politician = models.OneToOneField(Politician)
    campaign = models.OneToOneField(Campaign)
    contacted_by = models.CharField(choices=CONTACT_CHOICES, max_length=10)
    date_created = models.DateField('Criado em', auto_now_add=True)