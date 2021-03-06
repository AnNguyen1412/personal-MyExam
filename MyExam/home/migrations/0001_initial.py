# Generated by Django 3.0.7 on 2020-06-11 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examName', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('name', models.CharField(default='', max_length=200)),
                ('day', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('month', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('year', models.DecimalField(decimal_places=0, default=0, max_digits=4)),
                ('phoneNumber', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(default='', max_length=254)),
                ('sex', models.BooleanField(default=False)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('key1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
                ('key2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Exam')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(default='')),
                ('isCorrect', models.BooleanField(default=False)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Exam')),
            ],
        ),
    ]
