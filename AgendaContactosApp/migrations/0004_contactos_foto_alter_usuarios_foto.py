# Generated by Django 4.2.13 on 2024-06-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaContactosApp', '0003_usuarios_foto_alter_contactos_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactos',
            name='foto',
            field=models.ImageField(default='imagenes-web/foto_contactos/foto_contacto.png', upload_to='imagenes-web/foto_contactos'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='foto',
            field=models.ImageField(default='imagenes-web/foto_usuario/foto_perfil.png', upload_to='imagenes-web/foto_usuario'),
        ),
    ]
