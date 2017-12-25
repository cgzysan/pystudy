#!/usr/bin/env python3
# by ysan

from conf import settings
from core import accounts


def make_transaction(acc_data, trans_type, amount, log_obj, *args):
    '''
    deal all the user transaction
    :param acc_data:    user account data
    :param trans_type:  transaction type
    :param amount:      transaction amount
    :param log_obj:     log object
    :param others:      extra function
    :return:
    '''
    amount = float(amount)
    account_target = "".join(args)  # 当转账需要一个目标账户的时候会用到
    if trans_type in settings.TRANSACTION_TYPE:
        trans_dict = settings.TRANSACTION_TYPE[trans_type]
        interest = amount * trans_dict['interest']
        old_balance = acc_data['balance']
        if trans_dict['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif trans_dict['action'] == 'minus':
            new_balance = old_balance - amount - interest
            # check credit
            if new_balance < 0:
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s], your current balance is
                [%s]''' % (acc_data['credit'], (amount + interest), old_balance))
                return
        acc_data['balance'] = new_balance
        accounts.dump_update_account(acc_data)
        log_obj.info("account: %s   action: %s  amount: %s  interest: %s"
                     % (acc_data['id'], trans_type, amount, interest))

        if trans_type == 'transfer':
            account_target_data = accounts.load_current_balance(account_target)
            account_target_data['balance'] += amount
            accounts.dump_update_account(account_target_data)
            log_obj.info("account: %s   action: %s  amount: %s  interest: %s"
                         % (account_target_data['id'], trans_type, amount, interest))
        return acc_data
    else:
        print("\033[31;1mThis transaction type [%s] is not exist!\033[0m" % trans_type)
