# arr = ['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']  # foo
#
# def find_uniq(arr):
#     for i in arr:
#         s = i
#         for v in i:
#             for e in s[-1]:
#                 print(v, i, s)
#                 if v == e:
#                     print(v, i, s)
#             else:
#                 print(v, i, '**************')
        # for z in i:
        #     z


# print(find_uniq(arr))


# m, p, n = 120, 25, 4
# m, p, n = int(input()), int(input()), int(input())
# m, p, n = 100, 25, 1
#
# for i in range(1, n+1):
#     if n == 1:
#         print(i, m)
#     else:
#         if i == 1:
#             print(i, float(m))
#         else:
#             m = float(m) * (p / 100 + 1)
#             print(i, m)

#
# for i in range(1, n+1):
#     print(i, m)
#     m = m + m * p * 0.01

# c = b
# b = a
# a = c
#
# a = int(input())
# b = int(input())
# if a > b:
#     for i in range(a, b-1, -1):
#         print(i)
# else:
#     for i in range(a, b+1):
#         print(i)

# put your python code here
# for i in range(10):
#     n = int(input())
#     if n == 0:
#       print('зеленый')
#     elif n >= 1 and n <= 10:
#       if n % 2 == 0:
#         print('черный')
#       else:
#         print('красный')
#     elif n >= 11 and n <= 18:
#       if n % 2 == 0:
#         print('красный')
#       else:
#         print('черный')
#     elif n >= 19 and n <= 28:
#       if n % 2 == 0:
#         print('черный')
#       else:
#         print('красный')
#     elif n >= 29 and n <= 36:
#       if n % 2 == 0:
#         print('красный')
#       else:
#         print('черный')
#     else:
#         print('ошибка ввода')


# < a
#
#
# class ="item_news_2" href="{% url 'news-detail' id2 %}" >
#
# < h3 > {{title2}} < / h3 >
# < p > {{price2}}$ < / p >
# < p > {{date2}} < / p >
# < / a >
# < a
#
#
# class ="item_news_3" href="{% url 'news-detail' id3 %}" >
#
# < h3 > {{title3}} < / h3 >
# < p > {{price3}}$ < / p >
# < p > {{date3}} < / p >
# < / a >