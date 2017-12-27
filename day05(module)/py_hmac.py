#!/usr/bin/env python3
# by ysan

'''
    散列消息鉴别码，简称HMAC，是一种基于消息鉴别码MAC（Message Authentication Code）的鉴别机制。
    内部对我们创建 key 和 内容 再进行处理然后再加密
    一般用于网络通信中消息加密，前提是双方先要约定好key,就像接头暗号一样，然后消息发送把用key把消息加密，
    接收方用key ＋ 消息明文再加密，拿加密后的值 跟 发送者的相对比是否相等，这样就能验证消息的真实性，及发送者的合法性了。
'''

import hmac

h = hmac.new(b'12345', '天王盖地虎，宝塔镇河妖'.encode('utf-8'))
print(h.hexdigest())
