from django.db.models import Count
from localflavor.br.br_states import STATE_CHOICES
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .forms import ContactForm
from .models import Campaign, Politician, Contact


def index(request):
    campaign = get_object_or_404(Campaign, id=1)
    contacts = Contact.objects.filter(campaign=campaign.pk).count()

    return render(
        request,
        'index.html',
        {'campaign': campaign, 'uf_list': STATE_CHOICES, 'count_contacts': contacts},
    )


def politician_list(request, campaign_id, uf=None):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    if uf:
        politician_list = Politician.objects.filter(uf__iexact=uf)
    else:
        politician_list = Politician.objects.all()

    politician_list = politician_list.annotate(contacts=Count('contact')).order_by(
        'contacts', 'parliamentary_name'
    )

    return render(
        request,
        'politician_list.html',
        {
            'politician_list': politician_list,
            'campaign': campaign,
            'uf_list': STATE_CHOICES,
        },
    )


def report_contact(request, campaign_id, politician_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    politician = get_object_or_404(Politician, id=politician_id)

    contact = Contact(campaign=campaign, politician=politician)
    form = ContactForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        msg = (
            'Seu contato foi registrado, grato por participar! '
            'Se tiver tempo, aproveite para contatar outro '
            'parlamentar agora mesmo.'
        )
        messages.success(request, msg)
        return redirect('politician_list', campaign_id=campaign.pk, uf=politician.uf)

    return render(
        request,
        'contact_add.html',
        {'form': form, 'politician': politician, 'campaign': campaign},
    )
