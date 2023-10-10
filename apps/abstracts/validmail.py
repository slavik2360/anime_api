# import re

# def valid_mail(mail: str):
#     try:
#         if mail.count("@") == 1 \
#             and mail[0] not in ' ,.><?$^%&#*_!_(@)#*(!<' \
#             and mail.count('.') > 0 \
#             and mail.rfind('.') > mail.rfind("@"):
#             return "GOOD"
#         else: 
#             return "BAD"
#     except Exception as e:
#         return f"Ошибка -> {e}"
        

# def validate_mail(mail: str):
#     try:
#         pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        
#         if pattern.match(mail):
#             return "GOOD"
#         else: 
#             return "BAD"
#     except Exception as e:
#         return f"Ошибка -> {e}"

# print(valid_mail("fsfjkls@gmail.com"))

# print(valid_mail("fsfj@kls@gmail.com"))

# print(valid_mail(".@gmail.com"))

# print(valid_mail("hren_hren@gmail.com"))

# print(valid_mail(123))

# print(30 * '**')

# print(validate_mail("fsfj@kls@gmail.com"))
# print(validate_mail("fsfjkls@gmail.com"))
# print(validate_mail(".@gmail.com"))
# print(validate_mail("hren_hren@gmail.com"))


# from AnilistPython import Anilist
# anilist = Anilist()
# for i in range(10000, 12000):
#     try:
#         print(i)
#         name = anilist.get_anime_with_id(i)
#         print(name['name_romaji'])
#     except Exception as e:
#         pass

# print(anilist.get_anime("Owari no Seraph"))        
# print(anilist.get_anime_id("ReZero"))      
# print(anilist.print_anime_info("Madoka Magica"))
import random
# from string import ascii_letters

# name = ''.join((random.choice(ascii_letters) for x in range(20)))
# rate: float = random.uniform(2,10)

import requests

for _ in range(10):
    rand = random.randint(1,200)
    url = "https://myanimelist.p.rapidapi.com/anime/1535".format(rand)

    headers = {
        "X-RapidAPI-Key": "174bea933bmshcb2bd16a2bf0700p1cc5d6jsn819ca52ca990",
        "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json()['alternative_titles'].get('english'))

print(rand)