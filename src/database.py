import time
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não definida no ambiente")

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        engine.connect()
        print("✅ Conectado ao banco!")
        break
    except Exception as e:
        print(f"⏳ Banco não disponível ainda, tentativa {i+1}/10...")
        time.sleep(3)
else:
    raise RuntimeError("❌ Não foi possível conectar ao banco após 10 tentativas")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()