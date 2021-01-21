from prime.prime import Prime
import prime.constants as c
from email.email import Email
#Triggering the entire project
#Do this by python run.py

def run():
    p = Prime(start=c.START, finish=c.FINISH)
    prettier = p.prettify()
    print(prettier)
    new_mail = Email()
    new_mail.to = 'JohnDoe@email.com'
    new_mail.subject = f'Prime Numbers execution between {c.START} to {c.FINISH}'
    new_mail.body = prettier
    new_mail.send()

if __name__ == '__main__':
    run()