import os
import socket
import psutil
from fastapi import FastAPI
from typing import Dict, List, Any
import redis
from fastapi.middleware.cors import CORSMiddleware

# uvicorn app:app --reload

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Initialize Redis connection
# Using environment variables with defaults for connection parameters
redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}


@app.get("/info")
async def info() -> Dict[str, Any]:

    print("Request received")
    print("Redis connection parameters:", redis_host, redis_port)

    # Get process ID
    pid = os.getpid()

    # Get hostname
    hostname = socket.gethostname()

    # Get all network interface IP addresses
    networks = []
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:  # IPv4
                networks.append(addr.address)

    # Get all environment variables
    envs = dict(os.environ)

    # Increment view count in Redis
    view_count_key = "app:view_count"
    try:
        view_count = redis_client.incr(view_count_key)
    except redis.exceptions.ConnectionError as e:
        print(f"Redis connection error: {e}")
        view_count = -1  # Indicate Redis connection issue

    return {
        "view_count": view_count,
        "pid": pid,
        "hostname": hostname,
        "networks": networks,
        "envs": envs,
    }
