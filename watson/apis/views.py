from django.shortcuts import render
from watson import settings
import json
from watson_developer_cloud import LanguageTranslatorV2
from watson.apis.forms import TranslateForm

def discover(request):
    
    context = {}
    
    form = TranslateForm(request.POST or None)

    if request.method == "POST":
        
        if form.is_valid():
            language_translator  = LanguageTranslatorV2(
                username=settings.DISCOVERY_USERNAME,
                password=settings.DISCOVERY_PASSWORD,            
            )

            context['languages'] = language_translator.identify(request.POST['texto'])    
        
    context['form'] = form

    return render(request, 'discover.html', context or None)


def translate(request):
    
    context = {}
    
    form = TranslateForm(request.POST or None)

    if request.method == "POST":
        
        if form.is_valid():
            language_translator  = LanguageTranslatorV2(
                username=settings.DISCOVERY_USERNAME,
                password=settings.DISCOVERY_PASSWORD,            
            )

            context['success'] = True
            context['tranlate_pt_en'] = language_translator.translate(request.POST['texto'], source='pt', target='en')
            context['tranlate_en_es'] = language_translator.translate(context['tranlate_pt_en'], source='en', target='es')
            context['tranlate_en_fr'] = language_translator.translate(context['tranlate_pt_en'], source='en', target='fr')                
        
    context['form'] = form

    return render(request, 'translate.html', context or None)