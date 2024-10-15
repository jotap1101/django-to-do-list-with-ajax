from django.db import models

# Create your models here.
class Status(models.Model):
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    name = models.CharField(max_length=255, verbose_name='Nome')
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    title = models.CharField(max_length=255, verbose_name='Título')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, to_field='id', default=1, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    def __str__(self):
        return self.title