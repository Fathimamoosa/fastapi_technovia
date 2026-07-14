from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
import app.schemas as schemas
import app.models as models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Project")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "FastAPI project running successfully"}


@app.post(
    "/user_profile",
    response_model=schemas.UserResponseSchema,
)
def create_user(
    user: schemas.UserFormSchema,
    db: Session = Depends(get_db),
):
    db_user = models.UserForms(
        name=user.name.strip(),
        email=user.email.lower().strip(),
        message=user.message.strip(),
    )

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Unable to save data",
        )