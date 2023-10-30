# Generated by Django 4.2.6 on 2023-10-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0002_pessoa_cpf_pessoa_date_added_pessoa_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='genero',
            field=models.CharField(blank=True, choices=[('FE', 'Feminino'), ('MA', 'Masculino'), ('AG', 'Agenero'), ('FL', 'Genero Fluido'), ('NB', 'Nao Binario'), ('OU', 'Outro')], default=True, max_length=2),
        ),
    ]
