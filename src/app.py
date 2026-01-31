from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.account_routes import router as account_router 
from routes.transaction_routes import router as transaction_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bank System API")

@app.get("/")
def root():
    return {"message": "Bank System API is running"}

app.include_router(user_router, prefix="/api")     
app.include_router(account_router, prefix="/api")
app.include_router(transaction_router, prefix="/api")