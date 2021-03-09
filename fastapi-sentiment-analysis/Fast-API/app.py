import uvicorn
from fastapi import FastAPI

# init app
app = FastAPI()

# Routes


@app.get('/')
def index():
    return {'text': 'Hello from FastAPI'}


@app.get('/')
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
