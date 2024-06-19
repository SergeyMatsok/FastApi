import uvicorn
from fastapi import Depends, FastAPI


from auth.base_config import auth_backend
from auth.manager import User

from auth.schemas import UserCreate, UserRead
from auth.base_config import fastapi_users
app = FastAPI(
    title='Trading App' # Название пилжения
) # Переменная, экземпляр FastApi
# app = FastAPI()


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

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)