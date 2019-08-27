from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from celery.schedules import crontab
from kombu import Exchange, Queue

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tabops_api.settings')

app = Celery('tabops_api')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.update(
    CELERY_BEAT_SCHEDULE={
        'wtv-task': {
            'task': 'zabbix.tasks.refresh_port_wtv',
            'schedule':  crontab(minute=0, hour=1),
        },
        'bimsboot-task': {
            'task': 'zabbix.tasks.refresh_port_bimsboot',
            'schedule': crontab(minute=5, hour=1),
        },
        'bimspanel-task': {
            'task': 'zabbix.tasks.refresh_port_bimspanel',
            'schedule': crontab(minute=10, hour=1),
        },
        'tms-task': {
            'task': 'zabbix.tasks.refresh_port_tms',
            'schedule': crontab(minute=15, hour=1),
        },
        'epg-task': {
            'task': 'zabbix.tasks.refresh_port_epg',
            'schedule': crontab(minute=20, hour=1),
        },
        'search-task': {
            'task': 'zabbix.tasks.refresh_port_search',
            'schedule': crontab(minute=25, hour=1),
        },
        'pic-task': {
            'task': 'zabbix.tasks.refresh_port_pic',
            'schedule': crontab(minute=30, hour=1),
        },
        'ppl-task': {
            'task': 'zabbix.tasks.refresh_port_ppl',
            'schedule': crontab(minute=35, hour=1),
        },
        'cosepg-task': {
            'task': 'zabbix.tasks.refresh_port_cosepg',
            'schedule': crontab(minute=40, hour=1),
        },
        'uic-task': {
            'task': 'zabbix.tasks.refresh_port_uic',
            'schedule': crontab(minute=45, hour=1),
        },
        'mscreen-task': {
            'task': 'zabbix.tasks.refresh_port_mscreen',
            'schedule': crontab(minute=50, hour=1),
        },
        'dms2-task': {
            'task': 'zabbix.tasks.refresh_port_dms2',
            'schedule': crontab(minute=55, hour=1),
        },
        'xmpp-task': {
            'task': 'zabbix.tasks.refresh_port_xmpp',
            'schedule': crontab(minute=0, hour=2),
        },
        'ndms-task': {
            'task': 'zabbix.tasks.refresh_port_ndms',
            'schedule': crontab(minute=5, hour=2),
        },
    },
    CELERY_ROUTES={
        # task_A
        'zabbix.tasks.refresh_port_wtv': {"queue": "for_task_A", "routing_key": "for_task_A"},
        'zabbix.tasks.refresh_port_bimsboot': {"queue": "for_task_A", "routing_key": "for_task_A"},
        'zabbix.tasks.refresh_port_bimspanel': {"queue": "for_task_A", "routing_key": "for_task_A"},
        'zabbix.tasks.refresh_port_tms': {"queue": "for_task_A", "routing_key": "for_task_A"},
        # task_B
        'zabbix.tasks.refresh_port_epg': {"queue": "for_task_B", "routing_key": "for_task_B"},
        'zabbix.tasks.refresh_port_search': {"queue": "for_task_B", "routing_key": "for_task_B"},
        'zabbix.tasks.refresh_port_pic': {"queue": "for_task_B", "routing_key": "for_task_B"},
        'zabbix.tasks.refresh_port_ppl': {"queue": "for_task_B", "routing_key": "for_task_B"},
        # task_C
        'zabbix.tasks.refresh_port_cosepg': {"queue": "for_task_C", "routing_key": "for_task_C"},
        'zabbix.tasks.refresh_port_uic': {"queue": "for_task_C", "routing_key": "for_task_C"},
        'zabbix.tasks.refresh_port_mscreen': {"queue": "for_task_C", "routing_key": "for_task_C"},
        'zabbix.tasks.refresh_port_dms2': {"queue": "for_task_C", "routing_key": "for_task_C"},
        # task_D
        'zabbix.tasks.refresh_port_xmpp': {"queue": "for_task_D", "routing_key": "for_task_D"},
        'zabbix.tasks.refresh_port_ndms': {"queue": "for_task_D", "routing_key": "for_task_D"},
    },
    CELERY_QUEUES=(
        # Queue("default", Exchange("default"), routing_key="default"),
        Queue("for_task_A", Exchange("for_task_A"), routing_key="for_task_A"),
        Queue("for_task_B", Exchange("for_task_B"), routing_key="for_task_B"),
        Queue("for_task_C", Exchange("for_task_C"), routing_key="for_task_C"),
        Queue("for_task_D", Exchange("for_task_D"), routing_key="for_task_D")
    )
)

# 允许root 用户运行celery
platforms.C_FORCE_ROOT = True


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
