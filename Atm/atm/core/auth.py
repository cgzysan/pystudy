# by ysan
#!/usr/bin/env python3


def acc_auth(account, password):
    '''
    account auth func
    :param account:     credit account number
    :param password:    credit card password
    :return:    if pass the authentication , return the account object, otherwise, return None
    '''
    


def acc_login(user_data, log_obj):
    '''
    account login func
    :param user_data:   user info data, only save in memory
    :param log_obj:     log file
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("\033[32;1macount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()