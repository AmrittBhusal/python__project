# Generated by Django 5.0.6 on 2024-05-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movievarity',
            name='type',
            field=models.CharField(choices=[('KA', 'KARAN ARJUN'), ('BM', 'BATMAN'), ('SM', 'SUPPERMAN'), ('SM', 'SPIDERMAN')], default='KA', max_length=2),
        ),
    ]
