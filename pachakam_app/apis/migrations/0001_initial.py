# Generated by Django 2.0.1 on 2018-01-06 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('total_time', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('category', models.IntegerField(choices=[(0, 'vegeterian'), (1, 'non-vegeterian'), (2, 'eggiterian')], default=0)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Dishes',
                'verbose_name': 'Dish',
            },
        ),
        migrations.CreateModel(
            name='Ingridient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Dish')),
            ],
            options={
                'verbose_name_plural': 'Ingridients',
                'verbose_name': 'Ingridient',
            },
        ),
        migrations.CreateModel(
            name='step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_name', models.CharField(max_length=150)),
                ('time', models.FloatField()),
                ('description', models.TextField(default=None, null=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Dish')),
            ],
        ),
    ]
