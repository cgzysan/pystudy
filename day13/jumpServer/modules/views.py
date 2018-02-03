#!/usr/bin/env python3
'''
  * @time: Created on 2018/02/02 17:09
  * @author: by Ysan
'''
from models import models
from modules.db_conn import engine, session
from modules.utils import print_err, yaml_parser
from modules import common_filters


def start_session(argv):
    '''
    going to start session
    :param argv:
    :return:
    '''
    print("going to start session")


def stop_server(argv):
    pass


def syncdb(argv):
    '''
    生成数据表结构
    :param argv:
    :return:
    '''
    print("Syncing DB....")
    models.Base.metadata.create_all(engine)  # 创建所有表结构


def create_users(argv):
    '''
    create jumpserver access user
    :param argv:
    :return:
    '''
    if '-f' in argv:
        user_file = argv[argv.index('-f') + 1]
    else:
        print_err("invalid usage, should be:\ncreateusers -f <the new users file>", quit=True)

    source = yaml_parser(user_file)
    if source:
        print(source)
        for key, val in source.items():
            print(key, val)
            obj = models.UserProfile(username=key, password=val.get('password'))
            if val.get('groups'):
                host_groups = session.query(models.HostGroup).filter(models.HostGroup.name.in_(val.get('groups'))).all()
                if not host_groups:
                    print_err("none of [%s] exist in group table." % val.get('groups'), quit=True)
                obj.host_groups = host_groups
            if val.get('bind_hosts'):
                bind_hosts = common_filters.bind_hosts_filter(val)
                obj.bind_hosts = bind_hosts
            session.add(obj)
        session.commit()


def create_groups(argv):
    '''
    create groups
    :param argv:
    :return:
    '''
    if '-f' in argv:
        group_file = argv[argv.index('-f') + 1]
    else:
        print_err("Invalid usage, should be:\ncreate group -f <the new group file>", quit=True)
    source = yaml_parser(group_file)
    if source:
        print(source)
        for key, val in source.items():
            print(key, val)
            obj = models.HostGroup(name=key)
            if val.get('bind_host'):
                bind_hosts = common_filters.bind_hosts_filter()
                obj.bind_hosts = bind_hosts
            if val.get('user_profiles'):
                user_profiles = common_filters
                obj.user_profiles = user_profiles
            session.add(obj)
        session.commit()


def create_hosts(argv):
    '''
    create hosts
    :param argv:
    :return:
    '''
    if '-f' in argv:
        host_file = argv[argv.index('-f') + 1]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new hosts file>", quit=True)
    source = yaml_parser(host_file)
    if source:
        print(source)
        for key, val in source:
            obj = models.Host(hostname=key, ip=val.get('ip'), port=val.get('port') or 22)
            session.add(obj)
        session.commit()


def create_bindhosts(argv):
    '''
    create bind hosts
    :param argv:
    :return:
    '''
    if '-f' in argv:
        bindhost_file = argv[argv.index('-f') + 1]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new bindhosts file>", quit=True)
    source = yaml_parser(bindhost_file)
    if source:
        print(source)
        for key, val in source:
            host_obj = session.query(models.Host).filter(models.Host.hostname == val.get('hostname'))
            assert host_obj
            for item in val['remote_users']:
                assert item.get('auth_type')
                if item.get('auth_type') == 'ssh-passwd':
                    remoteuser_obj = session.query(models.RemoteUser).filter(
                        models.RemoteUser.username == item.get('username'),
                        models.RemoteUser.password == item.get('password'),
                    ).first()
                else:
                    remoteuser_obj = session.query(models.RemoteUser).filter(
                        models.RemoteUser.username == item.get('username'),
                        models.RemoteUser.auth_type == item.get('auth_type'),
                    ).first()
            if not remoteuser_obj:
                print_err("RemoteUser obj %s does not exist." % item, quit=True)
            bindhost_obj = models.BindHost(host_id=host_obj.id, remoteuser_id=remoteuser_obj.id)
            session.add(bindhost_obj)
            if source[key].get('groups'):
                group_obj = session.query(models.HostGroup).filter(models.HostGroup.name.in_(source[key].get('groups'))).all()
                assert group_obj
                bindhost_obj.host_groups = group_obj
            if source[key].get('user_profiles'):
                userprofile_obj = session.query(models.UserProfile).filter(models.UserProfile.username.in_(
                    source[key].get('user_profiles')
                )).all()
                assert userprofile_obj
                bindhost_obj.user_profiles = userprofile_obj
        session.commit()


def create_remoteusers(argv):
    '''
    create remoteuser
    :param argv:
    :return:
    '''
    if '-f' in argv:
        remoteuser_file = argv[argv.index('-f') + 1]
    else:
        print_err("invalid usage, should be:\ncreate_remoteusers -f <the new remoteusers file>", quit=True)
    source = yaml_parser(remoteuser_file)
    if source:
        for key, val in source:
            obj = models.RemoteUser(username=val.get('username'), auth_type=val.get('auth_type'), password=val.get('password'))
            session.add(obj)
        session.commit()
