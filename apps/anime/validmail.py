

def valid_mail(mail: str):
    try:
        if mail.count("@") == 1 and mail[0] not in ' ,.><?$^%&#*_!_(@)#*(!<' and mail.count('.') > 0 and mail.rfind('.') > mail.rfind("@"):
            return mail
    except ValueError:
        pass
    else:
        return "ЕMAIL не корректен"


print(valid_mail("fsfjkls@gmail.com"))

print(valid_mail("fsfj@kls@gmail.com"))

print(valid_mail(".@gmail.com"))

print(valid_mail("hren.@gmail.com"))
