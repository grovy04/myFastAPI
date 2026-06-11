from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS 설정 (React에서 접근 가능하도록 수정 완료)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # 모든 도메인(현재 웹 미리보기 포함) 허용
    allow_credentials=False,   # allow_origins가 ["*"]일 때는 반드시 False
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 데이터 모델
class LoginRequest(BaseModel):
    userid: str
    password: str

# 모크 데이터
MOCK_USER = {
    "userid": "user",
    "password": "1234"
}

@app.post("/login")
async def login(request: LoginRequest):
    if request.userid != MOCK_USER["userid"]:
        msg = '사용자 아이디가 틀렸습니다'
        raise HTTPException(status_code=401, detail=msg)
    
    if request.password != MOCK_USER["password"]:
        msg = '비밀번호가 틀렸습니다'
        raise HTTPException(status_code=401, detail=msg)
    
    return {"message": "로그인 성공"}