from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from routers import pdf_router, query_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database for demo purposes
fake_db = {
    "users": [
        {"name": "Admin", "email": "admin@example.com", "password": "adminpassword", "role": "admin"},
        {"name": "User", "email": "user@example.com", "password": "userpassword", "role": "user"}
    ]
}

# SignUp route (if needed for adding more users later)
class UserSignup(BaseModel):
    name: str
    email: str
    password: str

@app.post("/signup")
def signup(user: UserSignup):
    # Check if user already exists
    if any(u['email'] == user.email for u in fake_db['users']):
        raise HTTPException(status_code=400, detail="Email already registered")

    # Add user directly to the database with 'user' role
    new_user = {"name": user.name, "email": user.email, "password": user.password, "role": "user"}
    fake_db['users'].append(new_user)
    return {"success": True, "message": "User registered."}

# SignIn route
class UserSignin(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: UserSignin):
    # Search for user in the database
    db_user = next((u for u in fake_db['users'] if u['email'] == user.username and u['password'] == user.password), None)

    # Validate user credentials
    if db_user:
        return {"message": f"Welcome {db_user['role']}!"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(pdf_router.router, prefix="/api/admin")
app.include_router(query_router.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "API is running successfully!"}
