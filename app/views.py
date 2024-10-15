from app.forms import *
from app.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import dateformat, timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Create your views here.
@login_required(login_url='/admin/login/?next=/')
def index(request):
    tasks = Task.objects.all()
    status = Status.objects.all()
    create_task_form = CreateTaskForm()
    update_task_form = UpdateTaskForm()

    context = {
        'user': request.user,
        'tasks': tasks,
        'status': status,
        'create_task_form': create_task_form,
        'update_task_form': update_task_form,
    }

    return render(request, 'pages/index.html', context)

def create_task(request):
    if request.method == 'POST':
        task_form = CreateTaskForm(request.POST)

        if task_form.is_valid():
            task = task_form.save()

            response = {
                'status': 'success',
                'message': 'Tarefa criada com sucesso!',
                'task': {
                    'id': task.id,
                    'title': task.title,
                    'status': task.status.name,
                    'created_at': dateformat.format(timezone.localtime(task.created_at), 'd \d\e F \d\e Y \à\s H:i'),
                    'updated_at': dateformat.format(timezone.localtime(task.updated_at), 'd \d\e F \d\e Y \à\s H:i'),
                }
            }

            return JsonResponse(response, status=201)
        else:
            response = {
                'status': 'error',
                'message': 'Erro ao criar tarefa!',
                'errors': task_form.errors
            }

            return JsonResponse(response, status=400)
    else:
        response = {
            'status': 'error',
            'message': 'Método não permitido!'
        }

        return JsonResponse(response, status=405)
    
def read_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    try:
        response = {
            'status': 'success',
            'message': 'Tarefa encontrada com sucesso!',
            'task': {
                'id': task.id,
                'title': task.title,
                'status_id': task.status.id,
                'status_name': task.status.name,
                'created_at': dateformat.format(timezone.localtime(task.created_at), 'd \d\e F \d\e Y \à\s H:i'),
                'updated_at': dateformat.format(timezone.localtime(task.updated_at), 'd \d\e F \d\e Y \à\s H:i'),
            }
        }

        return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e)
        }

        return JsonResponse(response, status=404)

@csrf_exempt
@require_http_methods(['PUT'])
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))
            update_task_form = UpdateTaskForm(data, instance=task)
        except json.JSONDecodeError:
            response = {
                'status': 'error',
                'message': 'JSON inválido!'
            }

            return JsonResponse(response, status=400)

        if update_task_form.is_valid():
            task = update_task_form.save()

            response = {
                'status': 'success',
                'message': 'Tarefa atualizada com sucesso!',
                'task': {
                    'id': task.id,
                    'title': task.title,
                    'status': task.status.name,
                    'created_at': dateformat.format(timezone.localtime(task.created_at), 'd \d\e F \d\e Y \à\s H:i'),
                    'updated_at': dateformat.format(timezone.localtime(task.updated_at), 'd \d\e F \d\e Y \à\s H:i'),
                }
            }

            return JsonResponse(response, status=200)
        else:
            response = {
                'status': 'error',
                'message': 'Erro ao atualizar tarefa!',
                'errors': update_task_form.errors
            }

            return JsonResponse(response, status=400)
    else:
        response = {
            'status': 'error',
            'message': 'Método não permitido!'
        }

        return JsonResponse(response, status=405)
    
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'DELETE':
        task.delete()

        response = {
            'status': 'success',
            'message': 'Tarefa deletada com sucesso!'
        }

        return JsonResponse(response, status=200)
    else:
        response = {
            'status': 'error',
            'message': 'Método não permitido!'
        }

        return JsonResponse(response, status=405)
    
def filter_task(request):
    tasks = Task.objects.all()  # Obtem todas as tarefas

    # Filtra por status se o parâmetro de status estiver presente
    if 'status' in request.GET and request.GET['status']:
        tasks = tasks.filter(status_id=request.GET['status'])

    # Filtra por título se o parâmetro de pesquisa estiver presente
    if 'task' in request.GET and request.GET['task']:
        tasks = tasks.filter(title__icontains=request.GET['task'])

    # Prepara a lista de tarefas para a resposta
    task_list = []

    for task in tasks:
        task_list.append({
            'id': task.id,
            'title': task.title,
            'status_id': task.status.id,
            'status': task.status.name,
            'created_at': dateformat.format(timezone.localtime(task.created_at), 'd \d\e F \d\e Y \à\s H:i'),
            'updated_at': dateformat.format(timezone.localtime(task.updated_at), 'd \d\e F \d\e Y \à\s	H:i'),
        })

    return JsonResponse({'tasks': task_list}, status=200)