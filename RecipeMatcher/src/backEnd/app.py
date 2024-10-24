from fastapi import FastAPI
from routes import userHandling

app = FastAPI()

# From routes folder
app.include_router(userHandling.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe Matcher API"}