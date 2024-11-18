from datetime import datetime
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import jwt
from pydantic import ValidationError

SECRET_KEY = "123456@"
SECURITY_ALGORITHM = "HS256"

reuseable_oauth2 = HTTPBearer(
    scheme_name = 'Authorization'
)

def validate_token(http_authorization_credentials=Depends(reuseable_oauth2)) -> str:
    '''
        Decode JWT token to get username => return username
    '''
    try:
        payload = jwt.decode(http_authorization_credentials.credentials, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
        print(f"[xxxxxx]    payload.get('exp') is{payload.get('exp')}")
        print(f"[xxxxxx]    datetime.utcnow() is{datetime.utcnow()}")
        exp_timestamp = payload.get('exp')  # Unix timestamp
        if exp_timestamp is not None:
            exp_datetime = datetime.utcfromtimestamp(exp_timestamp)  # Chuyển sang datetime
            if exp_datetime < datetime.utcnow():
        # if payload.get('exp') < datetime.utcnow():
                raise HTTPException(status_code=403, detail='Token expired')
        return payload.get('username')
    except(jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code = 403,
            detail = "Could not validate credetials"
        )