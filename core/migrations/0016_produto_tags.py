# Generated by Django 3.2 on 2022-09-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_produto_postagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tags',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
