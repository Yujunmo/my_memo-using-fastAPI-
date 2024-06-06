from api.common import *
from schema.loginSchema import *
from database.orm import User, Memo
from common_function.login_function import get_hashed_pw, verify_password

@router.post("/signup")
async def signup(signup_data:RequestSchema_Signup, session:AsyncSession = Depends(get_db)):
    result = await session.execute(select(User).where(User.username==signup_data.username))
    db_user = result.scalars().first()
    if db_user:
        raise HTTPException(status_code=400, detail="invalid ID : already Exists !")
    
    hashed_pw = get_hashed_pw(signup_data.password)
    new_user = User(username = signup_data.username, email = signup_data.email, hashed_password = hashed_pw)
    session.add(new_user)
    
    try:
        await session.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="signup failure")
    await session.refresh(new_user)

    return {"message":"successfully signed up"}

@router.post("/login")
async def login(request:Request, signin_data:RequestSchema_Login, session:AsyncSession = Depends(get_db)):
    result = await session.execute(select(User).where(User.username==signin_data.username))
    db_user = result.scalars().first()
    if not db_user:
        raise HTTPException(status_code = 404, detail = "no data found : id doesn't exist")
    
    if not verify_password(signin_data.password, db_user.hashed_password):
        raise HTTPException(status_code = 401, detail = "unauthorized")
    
    request.session['username'] = signin_data.username
    return {"message":"successful login"}

@router.post("/logout")
async def logout(request:Request):
    request.session.pop("username",None)
    return {"message":"logged out successfully"}
