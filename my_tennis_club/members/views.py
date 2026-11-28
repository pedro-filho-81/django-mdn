from django.http import HttpResponse
from django.template import loader
from .models import Member

# podemos executar essa visão chamando a visualização via uma URL.
def members(request):
    # variável recebe todos os valores do objeto MeMber
    # Cria um objeto com todos os valores do modelo.mymembersMember
    mymembers = Member.objects.all().values()
    # Carrega o template.all_members.html
    template = loader.get_template('all_members.html')
    # Cria um objeto contendo o objeto. mymembers
    context = {
        # Envia o objeto para o modelo.
        'mymembers': mymembers,
    }

    # renderiza para a pasta templates e procura o arquivo mymembers.html
    # Exibe o HTML que é renderizado pelo modelo.
    return HttpResponse(template.render(context, request))

# Chega como argumento.id
def details(request, id):
    # Usa o para localizar o registro correto 
    # na tabela de Membros.id
  mymember = Member.objects.get(id=id)
#   Carrega o modelo.details.html
  template = loader.get_template('details.html')
#   Cria um objeto contendo o membro.
  context = {
    #  Envia o objeto para o modelo.
    'mymember': mymember,
  }
# Exibe o HTML que é renderizado pelo modelo.
  return HttpResponse(template.render(context, request))


def main(request):
  # Carrega o modelo.main.html
  template = loader.get_template('main.html')
  # Carrega o modelo.main.html
  return HttpResponse(template.render())


'''
Adicionar Visualização
Comece adicionando uma visualização chamada "teste" no 
arquivo: views.py
'''
def testing(request):
  # variável recebe todos os valores da da classe member no arquivo models.py 
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  '''
  Criamos um objeto (DICIONÁRIO) chamado context, o preenchemos com dados e o enviamos como o primeiro parâmetro na função. (template.render())
  '''
  context = {
    # 'fruits': ['Apple', 'Banana', 'Cherry'],   
    # 'firstname': 'Linus',
  }
  return HttpResponse(template.render(context, request))
