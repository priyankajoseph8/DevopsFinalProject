# Generated by Django 2.1.7 on 2019-05-29 11:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190528_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Progress', 'In Progress'), ('Done', 'Done')], max_length=8)),
                ('priority', models.IntegerField(default=1)),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date submitted')),
                ('description', models.TextField(default='description is not defined.', max_length=800)),
            ],
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='title',
            new_name='issue_title',
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(default='description is not defined.', max_length=800),
        ),
        migrations.AlterField(
            model_name='issue',
            name='objective',
            field=models.TextField(default='Objective is not defined.', max_length=400),
        ),
        migrations.AddField(
            model_name='task',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Issue'),
        ),
    ]