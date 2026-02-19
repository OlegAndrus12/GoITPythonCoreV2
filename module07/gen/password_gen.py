import string
import random

def generate_strong_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        password = ''.join(random.choice(alphabet) for _ in range(length))
        
        # Check constraints
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_spec  = any(c in string.punctuation for c in password)
        
        if has_lower and has_upper and has_digit and has_spec:
            break

    return password


def generate_strong_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        password = ''.join(random.choice(alphabet) for _ in range(length))
        
        # Check constraints
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_spec  = any(c in string.punctuation for c in password)
        
        if has_lower and has_upper and has_digit and has_spec:
            yield password


# always better
i = 0
for password in generate_strong_password():
    if i == 100:
        break
    print(password)
    i += 1


# then

# passwords = []
# for i in range(100):
#     passwords += generate_strong_password()

# for password in passwords:
#     pass