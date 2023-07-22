from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
import requests
from bs4 import BeautifulSoup
import redis
import json
import time
from threading import Thread

app = FastAPI()
redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


data_fetch_thread = Thread(target=fetch_data)
data_fetch_thread.daemon = True
data_fetch_thread.start()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    data = redis_instance.get('nifty50_data')
    
    data = fetch_data()
    if data:
        data = json.loads(data)
    return {"data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
