from django.http import JsonResponse

def hola(request):
    return JsonResponse({"mensaje": "hola"})
