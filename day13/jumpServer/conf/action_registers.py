#!/usr/bin/env python3
'''
  * @time: Created on 2018/02/03 09:01
  * @author: by Ysan
'''

from modules import views

action = {
    'start_session': views.start_session,
    'stop': views.stop_server,
    'syncdb': views.syncdb,
    'create_users': views.create_users,
    'create_groups': views.create_groups,
    'create_hosts': views.create_hosts,
    'create_bindhosts': views.create_bindhosts,
    'create_remoteusers': views.create_remoteusers,
}
