from fastapi import FastAPI

from src.routes import contacts, users, auth

app = FastAPI()

app.include_router(contacts.router, prefix='/api')
app.include_router(users.router, prefix='/api')
app.include_router(auth.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI!"}
