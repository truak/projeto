# Generated by Django 5.0 on 2024-01-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0003_alter_curso_carga_horaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]
