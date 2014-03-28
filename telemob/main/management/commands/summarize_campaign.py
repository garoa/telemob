import collections

from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count
from localflavor.br.br_states import STATE_CHOICES

from telemob.main.models import Campaign, Politician, Contact

class Command(BaseCommand):
    args = 'campaign_id'
    help = 'Exports summary campaign data for analysis'

    def handle(self, *args, **options):
        wr = self.stdout.write
        try:
            campaign_id = args[0]
        except IndexError:
            wr('Please provide the campaign_id as argument.')
            return
        try:
            campaign = Campaign.objects.get(pk=campaign_id)
        except Campaign.DoesNotExist:
            wr('No campaign with id %s found.' % campaign_id)
            return
        wr('# campaign name: ' + campaign.name)

        qry = Politician.objects.values('uf').order_by('uf').annotate(
            Count('uf'))
        politicians_per_state = collections.Counter(
            {r['uf']:r['uf__count'] for r in qry})

        contacted = collections.Counter({uf:0 for uf, name in STATE_CHOICES})
        for pol in Politician.objects.all():
            if pol.contact_set.count():
                contacted[pol.uf] += 1

        wr('# state\tpoliticians\tcontacted\tpct_contacted')
        for uf, name in sorted(STATE_CHOICES):
            lin = [uf, '%2d' % politicians_per_state[uf], '%2d' % contacted[uf],
                '%5.1f%%' % (float(contacted[uf])/politicians_per_state[uf]*100)]
            wr('\t'.join(lin)+'\n')


        wr('# contact results')
        results = {}
        for group, options in Contact.RESULT_CHOICES:
            for value, label in options:
                results[value] = group + '\t'+ label

        qry = Contact.objects.values('result').order_by('result').annotate(
            Count('result'))
        for res in qry:
            text = results.get(res['result'], 'n/a')
            wr('%3d\t%s\n' % (res['result__count'], text))




"""
        for contact in campaign.contact_set.all():
            pol = contact.politician
            columns = [str(contact.pk), pol.uf, pol.political_party,
                contact.contacted_by, contact.result, str(contact.date_created),
                pol.parliamentary_name]

            self.stdout.write('\t'.join(columns))
"""


