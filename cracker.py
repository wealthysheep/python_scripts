import hashlib

users = {
    "admin" : hashlib.sha256("admin".encode()).hexdigest(),
    "user1" : hashlib.sha256("password".encode()).hexdigest(),
    "guest" : hashlib.sha256("1234".encode()).hexdigest(),
    "user2" : hashlib.sha256("12345".encode()).hexdigest(),
}

common_pw = ["admin", "password", "1234", "securepassword", "qwerty123456"]

def brute_force(us):
    if us not in users:
        print("User not found!")
        return
    
    stored_hash = users[us]
    
    for pw in common_pw:
        hash_common_pw = hashlib.sha256(pw.encode()).hexdigest()
        if hash_common_pw == stored_hash:
            print("Password for " + us + " is " + pw)
            return

    print("No password found.")
    return

us = input("username: ")
brute_force(us)

# How it was tested:
# I inputed all the users and a user that doesn't exist.
