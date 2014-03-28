from django.core.management.base import BaseCommand, CommandError
from telemob.main.models import Campaign

class Command(BaseCommand):
    args = 'campaign_id'
    help = 'Exports denormalized campaign data for analysis'

    def handle(self, *args, **options):
        try:
            campaign_id = args[0]
        except IndexError:
            self.stdout.write('Please provide the campaign_id as argument.')
            return
        try:
            campaign = Campaign.objects.get(pk=campaign_id)
        except Campaign.DoesNotExist:
            self.stdout.write('No campaign with id %s found.' % campaign_id)
            return
        self.stdout.write('# campaign name: ' + campaign.name)
        for contact in campaign.contact_set.all():
            pol = contact.politician
            columns = [str(contact.pk), pol.uf, pol.political_party,
                contact.contacted_by, contact.result, str(contact.date_created),
                pol.parliamentary_name]

            self.stdout.write('\t'.join(columns))



"""
        for poll_id in args:
            try:
                poll = Poll.objects.get(pk=int(poll_id))
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write('Successfully closed poll "%s"' % poll_id)
"""
