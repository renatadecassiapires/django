from django import template

register = template.Library()

@register.filter(name = 'teste')
def teste(v1):
    if v1 == 8: 
        return f'Usuário master do sistema {v1}'
    else: 
        return v1