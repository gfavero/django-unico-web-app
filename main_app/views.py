from django.shortcuts import render, redirect
from .models import (Content_table, In_table, Five_w_table, Totem_table,Theme_table,
                    Principal_table,Conjunto_table,  Base_table_new,Sub_base_table,
                    Status_table,Base_table_new,Sub_base_table,Turma_table)
from .forms import ContentForm, PrincipalForm, ConjuntoForm,BaseForm,SubBaseForm,TurmaForm
from django.contrib import messages
from django.contrib.auth.models import User, Group
from datetime import date
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


def turma_content(request):
    me = request.user
    try:
        turma_data = Turma_table.objects.filter(author=me.id)
        turma_data_key = Turma_table.objects.get(pk=turma_data[0].id)
    except:
        turma_data_key = None
    if not turma_data_key:
        turma_table = Turma_table(turma_name = '',
                                turma_genero = '',
                                turma_idade = '',
                                turma_renda = '',
                                turma_status = '',
                                turma_o_que_querem = '',
                                turma_lista_de_problemas = '',
                                turma_em_relacao_ao_PRR = '',
                                turma_quando = '',
                                turma_como = '',
                                turma_onde = '',
                                turma_o_que = '',
                                turma_quem = '',
                                turma_por_que = '',
                                turma_dreams_list = '',
                                turma_stucks_list = '',
                                author=me)
        turma_table.save()

    turma_data = Turma_table.objects.filter(author=me.id)
    turma_data_key = Turma_table.objects.get(pk=turma_data[0].id)
    form = TurmaForm(request.POST or None, instance= turma_data_key)

    if form.is_valid() :
        form.save()
    context = {'turma_data': turma_data[0],
                'form':form, }
    return render(request, 'turma_content.html', context)

# def turma_content(request):
#     content = {}
#     return render(request, 'turma_content.html', content)

def edit_conjunto_table(request, conjunto_id):
    conjunto = Conjunto_table.objects.get(pk= conjunto_id)
    form = ConjuntoForm(request.POST or None, instance=conjunto)
    if form.is_valid():        
        form.save()
        return redirect('banco-de-assunto')
    return render(request, 'edit_conjunto.html', {'form':form})



def delete_sub_base_table(request, sub_base_id):
    conjunto = Sub_base_table.objects.get(pk=sub_base_id)
    conjunto.delete()
    messages.success(request, ("Sub Base Deletada!"))
    return redirect('banco-de-assunto')

def delete_base_table(request, base_id):
    conjunto = Base_table_new.objects.get(pk=base_id)
    conjunto.delete()
    messages.success(request, ("Base Deletada!"))
    return redirect('banco-de-assunto')


def add_sub_base_table(request,base_id):
    if request.method == "POST": 
        form = SubBaseForm(request.POST)  
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author_user = request.user
            form_instance.content_base =  Base_table_new.objects.get(pk= base_id)
            form_instance.content_sub_base =  request.POST.get('content_sub_base')
            form_instance.save()
            return redirect('banco-de-assunto')
    else:
        form = SubBaseForm()
    return render(request, 'add_sub_base.html', {'form': form})


def add_base_table(request,conjunto_id):
    if request.method == "POST": 
        form = BaseForm(request.POST)  
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author_user = request.user
            form_instance.content_conjunto =  Conjunto_table.objects.get(pk= conjunto_id)
            form_instance.content_base =  request.POST.get('content_base')
            form_instance.save()
            return redirect('banco-de-assunto')
    else:
        form = BaseForm()
    return render(request, 'add_base.html', {'form': form})

def add_conjunto_table(request):
    if request.method == "POST": 
        form = ConjuntoForm(request.POST)  
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form_instance.content_conjunto =  request.POST.get('content_conjunto')
            form_instance.save()
            return redirect('banco-de-assunto')
    else:
        form = ConjuntoForm()
    return render(request, 'add_conjunto.html', {'form': form})


def delete_conjunto_table(request, content_id):
    conjunto = Conjunto_table.objects.get(pk=content_id)
    conjunto.delete()
    messages.success(request, ("Conjunto Deletado!"))
    return redirect('banco-de-assunto')


# banco-de-assunto
def banco_de_assunto(request):
    me = request.user
    try:
        principal_data = Principal_table.objects.filter(author=me.id)
        principal_data_key = Principal_table.objects.get(pk=principal_data[0].id)
    except:
        principal_data_key = None
    if not principal_data_key:
        principal_table = Principal_table(content_principal='Principal',author=me)
        principal_table.save()

    principal_data = Principal_table.objects.filter(author=me.id)
    principal_data_key = Principal_table.objects.get(pk=principal_data[0].id)
    form = PrincipalForm(request.POST or None, instance= principal_data_key)
    conjunto_data = Conjunto_table.objects.filter(author=me.id).order_by('id')
    base_data = Base_table_new.objects.filter(author_user=me.id).order_by('id')
    sub_base_data = Sub_base_table.objects.filter(author_user=me.id).order_by('id')

    if form.is_valid() :
        form.save()
    context = {'principal_data': principal_data[0],
                'form':form,
                'conjunto_data': conjunto_data,
                'base_data':base_data,
                'sub_base_data':sub_base_data}
    return render(request, 'banco_de_assunto.html', context)


# Delete table content
def delete_content_table(request, content_id):
    conteudo = Content_table.objects.get(pk=content_id)
    conteudo.delete()
    messages.success(request, ("Conteudo Deletado!"))
    return redirect('content-list')

#Update table content
def update_content_table(request, content_id):
	content = Content_table.objects.get(pk=content_id)
	form = ContentForm(request.POST or None, instance=content)	
	me = request.user.id
	if content.author.id == me:
		if form.is_valid():        
			form.save()
			return redirect('content-list')
		return render(request, 'update_content_table.html', 
			{'form':form})
	else:
		messages.success(request, ("You do not have access to view this page!"))
		return redirect('content-list')

#Retrive data and diplay report for all records by user
def process_report(request):
    me = request.user.id
    process_data = Content_table.objects.filter(author=me).order_by('-content_creation_date')
    return render(request, 'process_report.html', {'process_data':process_data})

#Retrive data and diplay report for all records by user
def content_list(request):
    me = request.user.id
    process_data = Content_table.objects.filter(author=me).order_by('-content_creation_date')
    return render(request, 'content_list.html', {'process_data':process_data})

#Display all selected content information before saveing
def process_summary(request):
    if request.method == "POST":  
        form = ContentForm(request.POST or None)
        if form.is_valid():     
            process_summary = form.save(commit=False)
            process_summary.author = request.user
            process_summary.content_creation_date = date.today() 
            if request.POST.get('content_reference', None)[:4] == "http":
                process_summary.content_reference=  request.POST.get('content_reference', None)
            else:
                process_summary.content_reference= str("http://" + request.POST.get('content_reference', None))
            process_summary.save()
            messages.success(request, ("Processo salvo!"))
            return redirect('content-list')
    else:
             form = ContentForm()
    return render(request, 'process_summary.html', {'form': form})

#page to select the thema
def process_theme(request):
    context = {}
    context['theme_data'] = Theme_table.objects.all()
    context['ProjectName'] = request.POST.get('ProjectName',None)
    context['Reference'] = request.POST.get('Reference', None)
    context['content_in'] = request.POST.get('content_in', None)
    context['content_in_key'] = request.POST.get('content_in_key', None)
    context['content_five_w'] = request.POST.get('content_five_w', None)
    context['content_five_w_key'] = request.POST.get('content_five_w_key', None)
    context['content_totem'] = request.POST.get('content_totem', None).split('|')[0]
    context['content_totem_key'] = request.POST.get('content_totem', None).split('|')[1]
    return render(request, 'process_theme.html',context)

#page to select the totem
def process_totem(request):
    context = {}
    context['totem_data'] = Totem_table.objects.all()
    context['ProjectName'] = request.POST.get('ProjectName',None)
    context['Reference'] = request.POST.get('Reference', None)
    context['content_in'] = request.POST.get('content_in', None)
    context['content_in_key'] = request.POST.get('content_in_key', None)
    context['content_five_w'] = request.POST.get('content_five_w_key', None).split('|')[0]
    context['content_five_w_key'] = request.POST.get('content_five_w_key', None).split('|')[1]
    return render(request, 'process_totem.html',context)

#page to select the process five w
def process_5W(request):
    context = {}
    context['five_w_data'] = Five_w_table.objects.all()
    context['ProjectName'] = request.POST.get('ProjectName',None)
    context['Reference'] = request.POST.get('Reference', None)
    context['content_in'] = request.POST.get('content_in_key', None).split('|')[0]
    context['content_in_key'] = request.POST.get('content_in_key', None).split('|')[1]
    return render(request, 'process_5W.html', context, request.FILES or None)

#page to select the process in
def process_in(request):
    context = {}
    context['in_data'] = In_table.objects.all()
    context['ProjectName'] = request.POST.get('ProjectName',None)
    context['Reference'] = request.POST.get('Reference', None)
    return render(request, 'process_IN.html', context )

#page to stat creating the content process.
@csrf_exempt
def createContents(request,):
    context = {}
    context['ProjectName'] = request.POST.get('ProjectName',None)
    # context['ProjectName'] = "project test value"
    return render(request, 'create_contents.html', context)

#home page
def home(request,):
    name = "Unico Website"
    return render(request, 'home.html', {
        'name': name,
    })

#admin page
def admin(request):
    return render(request, 'admin')

