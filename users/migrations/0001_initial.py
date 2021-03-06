# Generated by Django 4.0.4 on 2022-06-16 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='users')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
