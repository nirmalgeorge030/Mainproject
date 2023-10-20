# Generated by Django 4.2.4 on 2023-09-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Result', models.FileField(blank=True, null=True, upload_to='upload_pdfs/')),
                ('Fullname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Course', models.CharField(choices=[('python', 'python'), ('oops', 'oops')], max_length=50)),
                ('Trainer', models.CharField(choices=[('Rohini', 'Rohini')], max_length=50)),
                ('Level', models.CharField(choices=[('exam1', 'exam1'), ('exam2', 'exam2'), ('exam3', 'exam3'), ('exam4', 'exam4'), ('exam5', 'exam5'), ('exam6', 'exam6'), ('exam7', 'exam7'), ('exam8', 'exam8'), ('exam9', 'exam9'), ('exam10', 'exam10'), ('exam11', 'exam11'), ('exam12', 'exam12'), ('exam13', 'exam13'), ('exam14', 'exam14'), ('exam15', 'exam15')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trainer', models.CharField(choices=[('Rohini', 'Rohini')], max_length=50)),
                ('Course', models.CharField(choices=[('python', 'python'), ('oops', 'oops')], max_length=50)),
                ('Level', models.CharField(choices=[('exam1', 'exam1'), ('exam2', 'exam2'), ('exam3', 'exam3'), ('exam4', 'exam4'), ('exam5', 'exam5'), ('exam6', 'exam6'), ('exam7', 'exam7'), ('exam8', 'exam8'), ('exam9', 'exam9'), ('exam10', 'exam10'), ('exam11', 'exam11'), ('exam12', 'exam12'), ('exam13', 'exam13'), ('exam14', 'exam14'), ('exam15', 'exam15')], max_length=20)),
            ],
        ),
    ]
