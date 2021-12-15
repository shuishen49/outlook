#-*- coding: UTF-8 -*- 

class Config():
    def case1(self):                            # 第一种情况执行的函数
        self.imap_server = "imap.mail.ru"
        self.imap_port = 993
        self.smtp_server = "smtp.mail.ru"
        self.smtp_port = 587
    def case2(self):                            # 第二种情况执行的函数
        self.imap_server = "imap.mail.com"
        self.imap_port = 993
        self.smtp_server = "smtp.mail.com"
        self.smtp_port = 587
    def case3(self):                            # 第三种情况执行的函数
        self.imap_server = "imap.gmx.com"
        self.imap_port = 993
        self.smtp_server = "smtp.gmx.com"
        self.smtp_port = 587
    def case4(self):                            # 第三种情况执行的函数
        self.imap_server = "imap.163.com"
        self.imap_port = 993
        self.smtp_server = "smtp.163.com"
        self.smtp_port = 465
    def default(self):                          # 默认情况下执行的函数
        # for outlook.com
        if "outlook." in self.username or "live." in self.username or "hotmail." in self.username:
            self.imap_server = "imap-mail.outlook.com"
            self.imap_port = 993
            self.smtp_server = "smtp-mail.outlook.com"
            self.smtp_port = 587
        else:
            x = self.username.split("@")
            self.imap_server = "imap."+x[1]
            self.imap_port = 993
            self.smtp_server = "smtp."+x[1]
            self.smtp_port = 587
    def __init__(self,username):
        self.username=username
        switch = {'list.ru': self.case1,                # 注意此处不要加括号
          'mail.com':self.case2,
          'gmx.com': self.case3,
          '163.com': self.case4,
          }
        x = username.split("@")
        switch.get(x[1], self.default)()            # 执行对应的函数，如果没有就执行默认的函数
