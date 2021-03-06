# Generated by Django 2.2.5 on 2020-01-13 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '0002_auto_20200107_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Kirr_url', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='shortener.KirrURL')),
            ],
        ),
    ]
