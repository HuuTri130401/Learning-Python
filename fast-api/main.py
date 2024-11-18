from datetime import datetime, timedelta
from typing import Union
import jwt
from pydantic import BaseModel
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from security import reuseable_oauth2, validate_token

SECRET_KEY = "123456@"
SECURITY_ALGORITHM = "HS256"

app = FastAPI(
    title='Learning Python', openapi_url='/openapi.json', docs_url='/docs', description='Learning Python Syntax'
)

class LoginRequest(BaseModel): # BaseModel of Pydantic
    username: str
    password: str

def verify_password(username: str, password:str):
    if username == 'admin' and password == '123':
        return True
    return False

def generate_token(username: Union[str, any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds= 60 * 60 * 24 * 3 #Expired after 3 days
    )
    to_encode = {
        'exp': expire, 'username': username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt
     
@app.post('/login')
def login(request: LoginRequest):
    print(f"[x] request_data: {request.__dict__}") # __dict__ là dictionary chứa tất cả thuộc tính và giá trị đối tượng
    if verify_password(username=request.username, password=request.password):
        token = generate_token(username=request.username)
        return {
            "message": "Login Success",
            "token": token
            }
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/books", dependencies=[Depends(validate_token)])
def list_books():
    return {'data': ["AAA", "BBB", "CCC"]}

if __name__ == '__main__':
    uvicorn.run(app, host='0,0,0,0', port=8000)