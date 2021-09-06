# Generated by Django 3.2.7 on 2021-09-06 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20210907_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bob_post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
