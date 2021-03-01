# Generated by Django 3.1.7 on 2021-03-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('body', models.TextField(max_length=1500, verbose_name='Тело поста')),
                ('contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Контакты')),
                ('email', models.EmailField(max_length=50, verbose_name='Почта')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
