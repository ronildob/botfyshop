from django import forms

class ContactForm(forms.Form):
    nome_completo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Seu nome completo"
                }
            )
        )
    email     = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email"
                }
            )
        )
    mensagem   = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
        )
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com")
        return email