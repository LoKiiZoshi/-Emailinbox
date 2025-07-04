# Generated by Django 5.2.3 on 2025-06-26 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('imap_server', models.CharField(default='imap.gmail.com', max_length=100)),
                ('imap_port', models.IntegerField(default=993)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=500)),
                ('sender', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(blank=True, max_length=200)),
                ('recipient', models.EmailField(max_length=254)),
                ('date_received', models.DateTimeField()),
                ('body_text', models.TextField(blank=True)),
                ('body_html', models.TextField(blank=True)),
                ('is_read', models.BooleanField(default=False)),
                ('message_id', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='inboxapp.emailaccount')),
            ],
            options={
                'ordering': ['-date_received'],
            },
        ),
        migrations.CreateModel(
            name='EmailAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('file_path', models.FileField(upload_to='attachments/')),
                ('file_size', models.IntegerField()),
                ('content_type', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='inboxapp.email')),
            ],
        ),
    ]
