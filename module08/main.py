
# function is an object in python

# Pass function as an argument to another function +
# Function can be saved in variable or another data structure +
# Function can be returned as a result of another function


def upload_success():
    print("Post is finished")

def upload_failed():
    print("Smth went wrong")


def upload_post_to_instagram():
    return upload_failed


f = upload_post_to_instagram()
f()