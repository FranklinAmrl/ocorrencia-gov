# Generated by Django 4.0.1 on 2022-04-29 05:40

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import ocorrencia.models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('coordenadaX', models.CharField(max_length=255, verbose_name='Coordenadas X')),
                ('coordenadaY', models.CharField(max_length=255, verbose_name='Coordenadas Y')),
                ('centro', models.CharField(choices=[('Almoxarifa-do-central', 'Almoxarifado Central'), ('Arquealogia', 'Arquealogia'), ('Apoio-pista-de-cooper', 'Apaio Pista de Cooper'), ('Biblioteca-central', 'Biblioteca Central'), ('Bloco-compartilhado-ccb', 'Bloco CoSSmpartilhado-CCB'), ('Bloco-compartilhados-outros', 'Bloco Compartilhado-CFCH/CE/CCSA')], max_length=255, verbose_name='Centro')),
                ('referencia', models.CharField(max_length=255, null=True, verbose_name='Local de referência')),
                ('data', models.DateTimeField(verbose_name='Data e hora')),
                ('tipo', models.CharField(choices=[('Agressao', 'Agressão'), ('Roubo', 'Roubo'), ('Furto', 'Furto')], max_length=255, verbose_name='Tipo da ocorrência')),
                ('descricao', models.TextField(max_length=255, null=True, verbose_name='Descrição da ocorrência')),
                ('envolvidoNome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do envolvido')),
                ('tipoEnvolvido', models.CharField(blank=True, choices=[('Suspeito', 'Suspeito'), ('Vitima', 'Vitima')], max_length=255, null=True, verbose_name='Tipo do envolvido')),
                ('genero', models.CharField(blank=True, choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outros', 'Outros')], max_length=255, null=True, verbose_name='Gênero do envolvido')),
                ('cpf', models.IntegerField(blank=True, null=True, verbose_name='CPF do envolvido')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email do envolvido')),
                ('fone', models.CharField(blank=True, max_length=14, null=True, verbose_name='Telefone do envolvido')),
                ('imagem', stdimage.models.StdImageField(blank=True, null=True, upload_to=ocorrencia.models.get_file_path, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Ocorrência',
                'verbose_name_plural': 'Ocorrências',
            },
        ),
        migrations.CreateModel(
            name='PassagemPlatao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('data', models.DateTimeField(verbose_name='Data e hora')),
                ('descricao', models.TextField(max_length=255, null=True, verbose_name='Descrição da plantão')),
            ],
            options={
                'verbose_name': 'Passagem de Plantão',
                'verbose_name_plural': 'Passagens de Plantão',
            },
        ),
        migrations.CreateModel(
            name='CustomUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('fone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Membro da equipe')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
