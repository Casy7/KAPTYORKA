# Generated by Django 3.2.7 on 2021-11-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KaptyorkaApp', '0010_groupaccounting_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realMembers', models.IntegerField(default=0)),
                ('students', models.IntegerField(default=0)),
                ('newOnes', models.IntegerField(default=0)),
                ('others', models.IntegerField(default=0)),
            ],
        ),
    ]