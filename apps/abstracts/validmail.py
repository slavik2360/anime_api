import re

def valid_mail(mail: str):
    try:
        if mail.count("@") == 1 \
            and mail[0] not in ' ,.><?$^%&#*_!_(@)#*(!<' \
            and mail.count('.') > 0 \
            and mail.rfind('.') > mail.rfind("@"):
            return "GOOD"
        else: 
            return "BAD"
    except Exception as e:
        return f"Ошибка -> {e}"
        

def validate_mail(mail: str):
    try:
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        
        if pattern.match(mail):
            return "GOOD"
        else: 
            return "BAD"
    except Exception as e:
        return f"Ошибка -> {e}"

print(valid_mail("fsfjkls@gmail.com"))

print(valid_mail("fsfj@kls@gmail.com"))

print(valid_mail(".@gmail.com"))

print(valid_mail("hren_hren@gmail.com"))

print(valid_mail(123))

print(30 * '**')

print(validate_mail("fsfj@kls@gmail.com"))
print(validate_mail("fsfjkls@gmail.com"))
print(validate_mail(".@gmail.com"))
print(validate_mail("hren_hren@gmail.com"))