from django.shortcuts import render
from .models import Text
from .forms import textForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
import pdb

@login_required
def main(request):
    texty = Text.objects.all()
    return render(request, 'main/index.html', {'texty': texty})

def main_pages(request, page):
    form = textForm()
    if request.method == 'POST':
        form = textForm(request.POST)
        data = request.POST
        delete = request.POST.get('delete','n/a')
        if not delete == 'n/a':
            tid = data[u'Textid']
            textDel = Text.objects.get(id=tid)
            textDel.delete() 
        else:        
            if data[u'Textid']:
                tid = data[u'Textid']
                textUpd = Text.objects.get(id=tid)
                textUpd.nazovTextu = request.POST.get('nazovTextu','n/a')
                textUpd.kapitola = data[u'kapitola']
                textUpd.strana = data[u'strana']
                textUpd.riadok = data[u'riadok']
                textUpd.origText = data[u'origText']
                textUpd.otLanguage = data[u'otLanguage']
                textUpd.translatedText = data[u'translatedText']
                textUpd.ttLanguage = data[u'ttLanguage']
                textUpd.save(force_update=True)  

            if form.is_valid():                                       
                textNew = form.save(commit=False)
                textNew.nazovTextu = data[u'nazovTextu']
                textNew.kapitola = data[u'kapitola']
                textNew.strana = data[u'strana']
                textNew.riadok = data[u'riadok']
                textNew.origText = data[u'origText']
                textNew.otLanguage = data[u'otLanguage']
                textNew.translatedText = data[u'translatedText']
                textNew.ttLanguage = data[u'ttLanguage']
                textNew.save()                                                        
    texty = Text.objects.filter(strana=page)
    return render(request, 'main/index.html', {'texty': texty, 'form': form })
        
                