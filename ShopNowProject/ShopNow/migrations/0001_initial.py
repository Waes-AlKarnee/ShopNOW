# Generated by Django 5.0.2 on 2024-02-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('describtion', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('card_image', models.ImageField(upload_to='shop_image')),
            ],
        ),
    ]