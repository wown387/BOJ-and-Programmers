hash_li={}

def get_key(key):
    con_key=ord(key[0])
    return con_key%5

def store_key(con_key,value):
    hash_li[con_key]=value

def add(key,value):
    con_key=get_key(key)
    store_key(con_key,value)
def print_val(key):
    con_key=get_key(key)
    print(hash_li[con_key])


add("ANDY","010-5555-5555")
add("DADDY","010-7777-7777")

print_val("ANDY")
print_val("DADDY")

print(hash_li)




