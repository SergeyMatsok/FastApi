from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (AuthenticationBackend,
                                          CookieTransport, JWTStrategy)

from auth.manager import get_user_manager
from config import SECRET
from auth.models import User

cookie_transport = CookieTransport(cookie_name='money', cookie_domain='localhost', cookie_max_age=3600)

# SECRET = "SECRET" # Нужно задать длинную сточку и поместить ее в .env и импортировать 

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

