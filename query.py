from fastapi import HTTPException, status
from database import get_db
import model




def search(id: int):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No blog with {id} is present in database")
    return blog