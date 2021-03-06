# Generated by Django 3.2.7 on 2021-09-30 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('Username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('Userimage', models.ImageField(upload_to='uploads/')),
                ('Useremail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_photo', models.ImageField(upload_to='uploadcriminal/')),
                ('c_name', models.CharField(max_length=50)),
                ('c_aliases', models.CharField(max_length=50)),
                ('c_height', models.IntegerField()),
                ('c_weight', models.IntegerField()),
                ('c_hair_color', models.CharField(choices=[('black', 'black'), ('grey', 'grey'), ('white', 'white'), ('bald', 'bald')], max_length=50)),
                ('c_eye_color', models.CharField(choices=[('black', 'black'), ('blue', 'blue'), ('red', 'red')], max_length=50)),
                ('c_scars', models.CharField(max_length=50)),
                ('c_arrestdate', models.DateField()),
                ('c_nationality', models.CharField(max_length=50)),
                ('c_city', models.CharField(max_length=50)),
                ('c_arrested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.userauth')),
            ],
        ),
        migrations.CreateModel(
            name='Crimereport',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_date', models.DateField()),
                ('r_time', models.TimeField()),
                ('r_summary', models.IntegerField()),
                ('r_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.userauth')),
            ],
        ),
    ]
