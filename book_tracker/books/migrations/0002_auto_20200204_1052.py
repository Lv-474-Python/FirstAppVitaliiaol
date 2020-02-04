# Generated by Django 3.0.2 on 2020-02-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('NF', 'Non-Fiction'), ('PT', 'Poetry'), ('NV', 'Novel'), ('AN', 'Anthology'), ('PL', 'Play')], max_length=2),
        ),
    ]
