from fastapi import FastAPI, Depends, HTTPException, status
import model
import schema
from sqlalchemy.orm import Session
from database import Base, engine, get_db
app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/blog")
def create_blog(blog: schema.Blog, db: Session = Depends(get_db)):
    new_blog = model.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/Blog", response_model=list[schema.BlogShow])
def all_blog(db: Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No blogs are present in database")
    return blogs


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No blog with {id} is present in database")
    db.delete(blog)
    db.commit()
    return "Deleted"


@app.get("/blog/{id}", response_model=schema.BlogShow)
def get_blog_byid(id, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No blog with {id} is present in database")
    return blog

@app.put("/blog/{id}")
def update(id, request: schema.Blog, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No blog with {id} is present in database")
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return "updated"
