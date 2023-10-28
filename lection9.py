# import json

# with open("city.list.json", "r",encoding="utf-8") as file:
#   data = json.load(file)


# ########################################
# #1. Определить количество городов в файле
# #print(len(data))

# ########################################
# #2. Создать словарь, где ключ — это код страны, а значение — количество городов.

# # def get_dict_country_with_count_cities(date: list) -> dict:
# #     list_of_country = []
# #     uniccountry = []
# #     dict_country = {}
# #     count = 0
    
# #     for x in date:
# #         list_of_country.append(x["country"])
# #     uniccountry = set(list_of_country)
# #     uniccountry = list(sorted(uniccountry))

# #     date = list(sorted(date,key = lambda x: x["country"]))

# #     for i in uniccountry:
# #         count = 0
# #         for x in date:
# #             if i == x["country"]:
# #                 count += 1
# #                 dict_country[i] = count


# #     return dict_country


# # c = get_dict_country_with_count_cities(data)

# # print(c)

# #######################################################################
# # 3. Подсчитать количество городов в северном полушарии и в южном.
 
# def get_enumenator_city(date:list):
#     n_city = []
#     s_city = []
#     for x in date:
#       if float(x["coord"]["lat"]) > 0 :
#         n_city.append(x)
#       else:
#         s_city.append(x)
#     c_n_city = len(n_city)
#     c_s_city = len(s_city)
#     stroka = "Количество городов в северном полушарии: " + str(c_n_city) +"  " + "Количество городов в южном полушарии: " + str(c_s_city)
#     return stroka
  

# c = get_enumenator_city(data)
# print(c)
