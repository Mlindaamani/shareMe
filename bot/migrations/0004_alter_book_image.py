# Generated by Django 5.0.4 on 2024-05-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_author_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='book.jpg', upload_to='books'),
        ),
    ]