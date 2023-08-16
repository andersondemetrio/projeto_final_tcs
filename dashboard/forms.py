from django import forms
from dashboard.models import  GastosFixos,GastosVariaveis, Colaboradores,Cargos,Endereco,Empresa,HorasProdutivas,Insumos

class GastosFixosForm(forms.ModelForm):
    class Meta:
        model = GastosFixos
        fields = "__all__"

class GastosVariaveisForm(forms.ModelForm):
    class Meta:
        model = GastosVariaveis
        fields = "__all__"

class ColaboradoresForm(forms.ModelForm):
    class Meta:
        model = Colaboradores
        fields = "__all__"

class CargosForm(forms.ModelForm):
    class Meta:
        model = Cargos
        fields = "__all__"

class InsumosForm(forms.ModelForm):
    class Meta:
        model = Insumos
        fields = "__all__"

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"

class EmpresaForm():
    class Meta:
        model = Empresa
        fields = "__all__"

class HorasProdutivasForm(forms.ModelForm):
    class Meta:
        model = HorasProdutivas
        fields = "__all__"
        