from django.http import HttpResponse
from django.template import Template, Context, loader

def inicio (request):
    return HttpResponse ("Fit 忍")

def home(request):
    # Abre el archivo utilizando 'with' para asegurarse de que se cierre adecuadamente
   """
    with open("C:/Users/macuo/Desktop/python/Proyecto/Proyecto1/Proyecto1/Plantillas/platilla1.html", encoding='utf-8') as home1:
        plantilla = Template(home1.read())

    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    """
   plantilla = loader.get_template("plantilla1.html")

   documento = plantilla.reder()
    return HttpResponse(documento)

