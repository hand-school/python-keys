# def logger(f):
#     # f - ссылка на функцию, которая декоррируется
#     def wrapper():
#         print("START")
#         result = f()
#         print(result)
#         print("STOP")
#         return result
#
#     return wrapper
#
# @logger
# def get_random_number():
#     import random
#     return random.randint(0, 100)
#
# a = get_random_number()


def datetime_logger(f):
    # f - ссылка на функцию, которая декоррируется
    def wrapper(arg1):
        print("DATETIME with arg: " + str(arg1))
        return f(arg1)

    return wrapper


@datetime_logger
def get_current_date_plus_days(days):
    from datetime import datetime, timedelta
    return datetime.now() + timedelta(days=days)


b = get_current_date_plus_days(3)
print(b)


# def fucker(fuck=False):
#     def decor(f):
#         # f - ссылка на функцию, которая декоррируется
#         def wrapper(arg1):
#             if fuck:
#                 return "Соси хуй"
#             else:
#                 return f(arg1)
#
#         return wrapper
#
#     return decor
#
#
# @fucker(fuck=True)
# def get_current_date_plus_days(days):
#     from datetime import datetime, timedelta
#     return datetime.now() + timedelta(days=days)
#
#
# c = get_current_date_plus_days(2)
# print(c)
