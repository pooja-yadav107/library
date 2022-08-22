# Generated by Django 3.2.7 on 2022-08-22 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_price',
        ),
        migrations.CreateModel(
            name='Book_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_price', models.CharField(default='', max_length=40)),
                ('bookname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.book')),
            ],
        ),
    ]
