# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0004_add_per_queue_staff_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escalationexclusion',
            name='queues',
            field=models.ManyToManyField(blank=True, help_text='Leave blank for this exclusion to be applied to all queues, or select those queues you wish to exclude with this entry.', to='helpdesk.Queue'),
        ),
        migrations.AlterField(
            model_name='ignoreemail',
            name='queues',
            field=models.ManyToManyField(blank=True, help_text='Leave blank for this e-mail to be ignored on all queues, or select those queues you wish to ignore this e-mail for.', to='helpdesk.Queue'),
        ),
        migrations.AlterField(
            model_name='presetreply',
            name='queues',
            field=models.ManyToManyField(blank=True, help_text='Leave blank to allow this reply to be used for all queues, or select those queues you wish to limit this reply to.', to='helpdesk.Queue'),
        ),
        migrations.AlterField(
            model_name='queue',
            name='email_address',
            field=models.EmailField(blank=True, verbose_name='E-Mail Address', max_length=254, help_text='All outgoing e-mails for this queue will use this e-mail address. If you use IMAP or POP3, this should be the e-mail address for that mailbox.', null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='submitter_email',
            field=models.EmailField(blank=True, verbose_name='Submitter E-Mail', max_length=254, help_text='The submitter will receive an email for all public follow-ups left for this task.', null=True),
        ),
        migrations.AlterField(
            model_name='ticketcc',
            name='email',
            field=models.EmailField(blank=True, verbose_name='E-Mail Address', max_length=254, help_text='For non-user followers, enter their e-mail address', null=True),
        ),
    ]
