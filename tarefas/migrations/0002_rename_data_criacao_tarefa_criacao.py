# Generated by Django 4.0.4 on 2022-05-05 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='data_criacao',
            new_name='criacao',
        ),
    ]
