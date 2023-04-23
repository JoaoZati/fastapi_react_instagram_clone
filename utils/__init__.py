from passlib.context import CryptContext

pwd_cst = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_bycrpt(password: str):
    return pwd_cst.hash(password)

def hash_verify(hashed_password, plain_password):
    return pwd_cst.verify(plain_password, hashed_password)
