class config():
    def __init__(self,username):
        result = ".ru" in username
        if result:
            self.imap_server = "imap.mail.ru"
            self.imap_port = 993
            self.smtp_server = "smtp.mail.ru"
            self.smtp_port = 587
        else:
            # for outlook.com
            self.imap_server = "imap-mail.outlook.com"
            self.imap_port = 993
            self.smtp_server = "smtp-mail.outlook.com"
            self.smtp_port = 587
        # print(self.imap_server)
