# Generated by Django 4.0.3 on 2022-03-31 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('photo', models.ImageField(blank=True, upload_to='user/%Y/%m/%d/')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('record_type', models.CharField(choices=[('photo', 'Фотосессия'), ('obj_shoot', 'Предметная съёмка'), ('make_up', 'Макияж')], default='photo', max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]