import datetime
def datetime_decorator(func):
    def wrapper():
        print('time '+str(datetime.datetime.now()))
        func()
        print(datetime.datetime.now())
    return  wrapper

@datetime_decorator
def logger_login():
    print("Hello universe")
logger_login()

deco_func=datetime_decorator(logger_login)
deco_func()