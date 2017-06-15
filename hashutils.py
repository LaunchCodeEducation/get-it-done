import hashlib


def make_pw_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_pw_hash(password, hash):
    if make_pw_hash(password) == hash:
        return True

    return False
