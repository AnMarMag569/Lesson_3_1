calls = 0
def count_colls ():
    global calls
    calls = calls +1
def string_info (string):
    k=len(string)
    print(k,string.upper(), string.lower())

def is_contains (string, list_to_search):
    f = False
    for i in list_to_search:
        if string.casefold() in i.casefold():
            f = True
        continue
    print(f)


string_info("Capybara")
count_colls()
string_info("Armageddon")
count_colls()
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
count_colls()
is_contains('cycle', ['recycling', 'cyclic'])
count_colls()
print(calls)
