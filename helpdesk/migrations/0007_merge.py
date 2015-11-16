# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_auto_20150628_2303'),
        ('helpdesk', '0006_email_maxlength'),
    ]

    operations = [
        migrations.AddField(
            model_name='Queue',
            name='socks_proxy_type',
            field=models.CharField(null=True, verbose_name='Socks Proxy Type', help_text='SOCKS4 or SOCKS5 allows you to proxy your connections through a SOCKS server.', blank=True, max_length=8, choices=[('socks4', 'SOCKS4'), ('socks5', 'SOCKS5')]),
        ),
        migrations.AddField(
            model_name='Queue',
            name='socks_proxy_host',
            field=models.GenericIPAddressField(null=True, verbose_name='Socks Proxy Host', help_text='Socks proxy IP address. Default: 127.0.0.1', blank=True),
        ),
        migrations.AddField(
            model_name='Queue',
            name='socks_proxy_port',
            field=models.IntegerField(null=True, verbose_name='Socks Proxy Port', blank=True, help_text='Socks proxy port number. Default: 9150 (default TOR port)'),
        ),
    ]
