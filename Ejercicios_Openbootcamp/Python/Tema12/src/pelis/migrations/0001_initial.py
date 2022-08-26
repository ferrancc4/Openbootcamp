# Generated by Django 2.0.7 on 2022-08-25 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('nacimiento', models.DateField()),
                ('defuncion', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('sinopsis', models.TextField()),
                ('estreno', models.PositiveIntegerField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelis.Director')),
            ],
        ),
    ]
