import uvicorn
from fastapi import Depends, FastAPI
from fastapi_users import FastAPIUsers

from auth.auth_cookie import auth_backend
from auth.database_db import User
from auth.manager import get_user_manager
from auth.schemas import UserCreate, UserRead

app = FastAPI(
    title='Trading App' # Название пилжения
) # Переменная, экземпляр FastApi
app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonim"

if __name__ == "__main__":
    uvicorn.run('main:app', host="10.230.4.225", port=8000, reload=True)