from django import forms
from .models import Content_table,Principal_table,Conjunto_table,Base_table_new,Sub_base_table, Turma_table
from django.contrib.auth.models import User
from django.forms  import ModelForm


# create a content page input
class ContentForm(ModelForm):
    class Meta:
        model = Content_table
        # fields = "__all__"
        fields = (  'content_subject', 
                    'content_reference', 
                    'content_in',
                    'content_five_w',
                    'content_totem', 
                    'content_theme',                     
                    'content_comment_01', 
                    'content_comment_02',
                    'content_comment_03',
                    'content_status',
                    )
        labels = {
            'content_subject': 'Assunto',
            'content_reference':  'Referência',
            'content_in':  'PdA',
            'content_five_w':  'WHN',
            'content_totem':  'Tópico',
            'content_theme':  'Tema',            
            'content_comment_01':  'Headline',
            'content_comment_02':  'Desenvolvimento',
            'content_comment_03':  'CTA',
            'content_status': 'Status',
        }

        widgets = {
            'content_subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'assunto'}),
            'content_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'content_reference'}),
            'content_five_w': forms.Select(attrs={'class': 'form-select', 'placeholder': 'content_five_w'}),
            'content_totem': forms.Select(attrs={'class': 'form-select', 'placeholder': 'content_totem'}),
            'content_theme': forms.Select(attrs={'class': 'form-select', 'placeholder': 'content_theme'}),
            'content_in': forms.Select(attrs={'class': 'form-select', 'placeholder': 'in3'}),
            'content_comment_01': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cê não sabe, nem te conto!'}),
            'content_comment_02': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Conteúdo'}),
            'content_comment_03': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Chamada para ação'}),
            'content_status': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Completo ou Rascunho'}),
                       

        }

class PrincipalForm(ModelForm):
    class Meta:
        model = Principal_table
        fields = ('content_principal',)
        widgets = {'content_principal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'assunto'}),}
    def __init__(self, *args, **kwargs):
        super(PrincipalForm, self).__init__(*args, **kwargs)
        self.fields['content_principal'].label = ''



class ConjuntoForm(ModelForm):
    class Meta:
        model = Conjunto_table
        fields = ('content_conjunto',)
        widgets = {'content_conjunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar conjunto'}),}
    def __init__(self, *args, **kwargs):
        super(ConjuntoForm, self).__init__(*args, **kwargs)
        self.fields['content_conjunto'].label = 'Adicionar Conjunto'

class BaseForm(ModelForm):
    class Meta:
        model = Base_table_new
        fields = ('content_base',)
        widgets = {'content_base': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar base'}),}
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.fields['content_base'].label = 'Adicionar Base'

class SubBaseForm(ModelForm):
    class Meta:
        model = Sub_base_table
        fields = ('content_sub_base',)
        widgets = {'content_sub_base': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar sub base'}),}
    def __init__(self, *args, **kwargs):
        super(SubBaseForm, self).__init__(*args, **kwargs)
        self.fields['content_sub_base'].label = 'Adicionar Sub Base'


class TurmaForm(ModelForm):
    class Meta:
        model = Turma_table

        fields = (  'turma_name',
                    'turma_genero',
                    'turma_idade',
                    'turma_renda',
                    'turma_status',
                    'turma_o_que_querem',
                    'turma_lista_de_problemas',
                    'turma_em_relacao_ao_PRR',
                    'turma_quando',
                    'turma_como',
                    'turma_onde',
                    'turma_o_que',
                    'turma_quem',
                    'turma_por_que',
                    'turma_dreams_list',
                    'turma_stucks_list',)

        widgets = {
                    'turma_name': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'turma nome'}),
                    'turma_genero': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'genero'}),
                    'turma_idade': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'idade'}),
                    'turma_renda': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'renda'}),
                    'turma_status': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'status'}),
                    'turma_o_que_querem': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_lista_de_problemas': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_em_relacao_ao_PRR': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_quando': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_como': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_onde': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_o_que': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_quem': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_por_que': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_dreams_list': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),
                    'turma_stucks_list': forms.TextInput(attrs={'class': 'form-control','placeholder' : ''}),                      

        }