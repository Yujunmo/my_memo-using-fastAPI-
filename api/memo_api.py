from api.common import *
from fastapi import HTTPException
from database.orm import User,Memo
from schema.memoSchema import *
from schema.loginSchema import *

# api
@router.post("/memos",response_model=ResponseSchema_CreateMemo)
async def create_memo(request:Request, memo:RequestSchema_CreateMemo, session:AsyncSession = Depends(get_db)):
    user_name = request.session.get('username')
    if not user_name: 
        raise HTTPException(status_code=401, detail="unauthorized")
    
    result = await session.execute(select(User).where(User.username == user_name))
    db_user = result.scalars().first()

    if not db_user:
        raise HTTPException(status_code=404,detail="no data found")

    new_memo = Memo(user_id=db_user.id, title=memo.title, content = memo.content)
    session.add(new_memo)
    await session.commit()
    await session.refresh(new_memo)

    return new_memo 

@router.get("/memos")
async def get_memos(request:Request, session:AsyncSession = Depends(get_db)):
    
    username = request.session.get('username')
    if not username :
        raise HTTPException(status_code=401, detail="unauthorized")

    result = await session.execute(select(User).where(User.username==username))
    db_user = result.scalars().first()

    if not db_user:
        raise HTTPException(status_code=404,detail="no ID data found")

    result = await session.execute(select(Memo).where(Memo.user_id == db_user.id))
    memos = result.scalars().all()

    return templates.TemplateResponse("memos.html",{"request":request,"memos":memos,"username":username})


@router.get("/memos/{memo_id}",response_model=ResponseSchema_GetMemo)
async def get_memos(request:Request, memo_id:int, session:AsyncSession = Depends(get_db)):
    username = request.session.get('username')
    if not username:
        raise HTTPException(status_code=401,detail="unauthorized")
    
    result = await session.execute(select(User).where(User.username==username))
    db_user = result.scalars().first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="no ID data found")
    
    result = await session.execute(select(Memo).where(Memo.user_id == db_user.id, Memo.id == memo_id))
    memo = result.scalars().first()

    if not memo:
        raise HTTPException(status_code=404, detail="no memo data found")
    return memo

@router.put("/memos/{memo_id}", response_model=ResponseSchema_UpdateMemo)
async def update_memos(request:Request, memo_id:int, memo:RequestSchema_UpdateMemo, session:AsyncSession = Depends(get_db)):
    username = request.session.get("username")
    if not username :
        raise HTTPException(status_code=401, detail="unauthorized")
    
    result = await session.execute(select(User).where(User.username == username))
    db_user = result.scalars().first()

    if not db_user:
        raise HTTPException(status_code=404, detail="no  ID data found")
    
    result = await session.execute(select(Memo).where(Memo.user_id == db_user.id), Memo.id == memo_id)
    db_memo = result.scalars().first()

    if not db_memo:
        raise HTTPException(status_code=404, detail="no Memo data found")

    if memo.title:
        db_memo.title = memo.title
    if memo.content:
        db_memo.content = memo.content
   
    await session.commit()
    await session.refresh(db_memo)
    return memo


@router.delete("/memos/{memo_id}")
async def delete_memos(request:Request, memo_id:int,session:AsyncSession=Depends(get_db)):
    username = request.session.get("username")
    
    if not username :
        raise HTTPException(status_code=401, detail="unauthorized")
    
    result = await session.execute(select(User).where(User.username == username))
    db_user = result.scalars().first()

    if not db_user:
        raise HTTPException(status_code=404, detail="no ID data found")

    result = await session.execute(select(Memo).where(Memo.user_id==db_user.id,Memo.id == memo_id))
    db_memo = result.scalars().first()
    
    if not db_memo:
        raise HTTPException(status_code=404, detail="no Memo data found")
    
    await session.delete(db_memo)
    await session.commit()

    return {"message":"successfully deleted data"}
