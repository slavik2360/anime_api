# Python
import re



def validate_mail(mail: str):
    try:
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        
        if pattern.match(mail):
            return "GOOD"
        else: 
            return "BAD"
    except Exception as e:
        return f"Ошибка -> {e}"


