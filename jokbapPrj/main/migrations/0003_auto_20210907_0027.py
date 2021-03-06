# Generated by Django 3.2.7 on 2021-09-06 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_bob_comment_jok_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bob_post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_commentss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jok_comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='J_comments', to='main.jok_post'),
        ),
    ]
