# Generated by Django 4.1.1 on 2022-09-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_alter_learningfacilitators_students_scores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningfacilitators',
            name='students_scores',
            field=models.CharField(choices=[('very unsatisfied', '-2'), ('unsatisfied', '-1'), ('nuetral', '0'), ('satisfied', '1'), ('very satisfied', '2')], max_length=20, null=True),
        ),
    ]