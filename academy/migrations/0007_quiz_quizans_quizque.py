# Generated by Django 3.1 on 2020-10-18 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_auto_20201017_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_status', models.CharField(max_length=100)),
                ('quiz_name', models.CharField(max_length=300)),
                ('quiz_cat', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='QuizQue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='academy.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuizAns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1000)),
                ('ques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='academy.quizque')),
            ],
        ),
    ]
