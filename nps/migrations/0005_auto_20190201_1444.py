# Generated by Django 2.1.5 on 2019-02-01 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nps', '0004_auto_20190128_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_answer_text', models.CharField(max_length=200)),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nps.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_question_text', models.CharField(max_length=200)),
                ('visibility', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='QnA',
        ),
        migrations.AddField(
            model_name='extraanswer',
            name='extra_question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nps.ExtraQuestion'),
        ),
    ]
