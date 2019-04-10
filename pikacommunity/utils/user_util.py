from django.core.mail import send_mail
from random import Random
from users.models import EmailVerifyRecord
from pikacommunity.settings import EMAIL_FROM


def random_str(randomstrlength=8):
    str = ''
    char = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(char)-1
    random = Random()
    for i in range(randomstrlength):
        str += char[random.randint(0,length)]
    return str


def send_message(email,email_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(randomstrlength=30)
    email_record.code = code
    email_record.email = email
    email_record.send_type = email_type
    email_record.save()
    if email_type == 'register':
        email_title = '皮卡出社区账号激活链接'
        email_content = '点击下方链接激活您的账号哦 (*^▽^*) http://127.0.0.1:8000/users/active/{0}'.format(code)
        send_status = send_mail(email_title,email_content,EMAIL_FROM,[email])
        return send_status
