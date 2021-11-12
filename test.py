import base64
import re
import outlook

user="youer@email.com"
mima="youerpass"
mail = outlook.Outlook()
if_login=mail.login(user,mima)
# print(mail.unread())
# s=mail.getEmail('2')
# print(type(s._payload))
if if_login:
    try:
        mail.inbox()
        s=mail.unread()
        if s!=0:
            # payload是一种以JSON格式进行数据传输的一种方式。
            s=s._payload
            # s=b'suLK1A=='
            # s=base64.urlsafe_b64decode(s)
            print(s)
            # print(s.decode("gb18030"))
    except:
        pass
        
