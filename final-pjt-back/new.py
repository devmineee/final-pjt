import json
with open('final-pjt-back/country.json', mode='r', encoding='utf-8' ) as country:
    loaded = json.loads(country.read())

#  {
#     "iso_3166_1": "ZW",
#     "english_name": "Zimbabwe",
#     "native_name": "Zimbabwe"
#   }

for country in loaded:

    # 동아시아
    if country["iso_3166_1"] in ["KR","CN","JP","TW","HK"]:
        country["area"] = 1

    # 동남아시아
    elif country["iso_3166_1"] in ["TH", "VN", "SG", "PH", "ID"]:
        country["area"] = 2

    # 중앙아시아
    elif country["iso_3166_1"] in ["MN","KZ","UZ"]:
        country["area"] = 3

    # 남아시아
    elif country["iso_3166_1"] in ["IN","PK"]:
        country["area"] = 4

    # 중동
    elif country["iso_3166_1"] in ["IL","EG","TR","IR","SA"]:
        country["area"] = 5

    # 북미
    elif country["iso_3166_1"] in ["US", "CA"]:
        country["area"] = 6

    # 남미
    elif country["iso_3166_1"] in ["MX","BR","AR","CL","CO"]:
        country["area"] = 7

    # 유럽
    elif country["iso_3166_1"] in ["GB","FR","DE","ES","IT","CZ","SE"]:
        country["area"] = 8

    # 오세아니아
    elif country["iso_3166_1"] in ["NZ","AU"]:
        country["area"] = 9

    # 아프리카
    elif country["iso_3166_1"] in ["NG","ET","CD","ZA","TZ"]:
        country["area"] = 10
