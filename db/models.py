from sqlalchemy import Column, String, Text, DateTime
from db.sessions import Base
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(String, primary_key=True, index=True)
    youtube_url = Column(Text)
    status = Column(String, default = "pending")
    created_at = Column(DateTime, default= datetime.utcnow)