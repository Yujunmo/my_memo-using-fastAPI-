from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

def get_hashed_pw(password:str):
    return pwd_context.hash(password)

def verify_password(plain_pw, hashed_pw):
    return pwd_context.verify(plain_pw,hashed_pw)
