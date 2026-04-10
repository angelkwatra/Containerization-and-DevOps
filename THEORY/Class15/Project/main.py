from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"name": "Angel Kwatra", "location": "Dehradun"}

@app.get("/{data}")
def read_data(data):
    return {"msg": data}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)