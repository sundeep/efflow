from datetime import datetime
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.db.base import SessionLocal
from api.db.models import FlowDB

# Add CORS Middleware
app = FastAPI()

# You can adjust the origins list to contain the list of allowed origins.
# For development purposes, I'm setting it to ["*"], which allows all origins.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# SCHEMAS
class FlowCreate(BaseModel):
    content: str


class Flow(BaseModel):
    id: int
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# CRUD operations
def create_flow_in_db(db: Session, flow: FlowCreate) -> FlowDB:
    db_flow = FlowDB(content=flow.content)
    db.add(db_flow)
    db.commit()
    db.refresh(db_flow)
    return db_flow


def get_flows_from_db(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FlowDB).offset(skip).limit(limit).all()


def get_flow_from_db(db: Session, flow_id: int):
    return db.query(FlowDB).filter(FlowDB.id == flow_id).first()


# Routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/flows/", response_model=Flow)
def create_flow(flow: FlowCreate, db: Session = Depends(get_db)):
    return create_flow_in_db(db, flow)


@app.get("/flows/", response_model=List[Flow])
def read_flows(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_flows_from_db(db, skip=skip, limit=limit)


@app.get("/flows/{flow_id}", response_model=Flow)
def read_flow(flow_id: int, db: Session = Depends(get_db)):
    db_flow = get_flow_from_db(db, flow_id=flow_id)
    if db_flow is None:
        raise HTTPException(status_code=404, detail="Flow not found")
    return db_flow
