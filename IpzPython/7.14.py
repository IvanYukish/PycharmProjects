import re
def validate(email):
    match = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", email)
    if match:
        return 'Valid email.'
    else:
        return 'Invalid email.'


print(validate("ib@examle.com"))
