# Generated by Django 3.2.4 on 2021-06-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]