from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "http://localhost:63342/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "https://kvandendijck.github.io/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    username: str

user = object


@app.post("/user")
async def post_user(item: User):
    global user
    headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAEyujQEAAAAAJ0Pcc2iUwHFq3tE5QXmkGZpM3qs%3Ddp0Tq4kSkqMeXGF8lNENr9apXGa6Mf6BGdAMLbajecB0EtIBXE"}
    r = requests.get("https://api.twitter.com/2/users/by/username/" + item.username, headers=headers)
    user = r.json()
    return user


@app.get("/getNumberOfTweets")
async def get_NumberOfTweets():
    global user
    id = user["data"]["id"]
    headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAEyujQEAAAAAJ0Pcc2iUwHFq3tE5QXmkGZpM3qs%3Ddp0Tq4kSkqMeXGF8lNENr9apXGa6Mf6BGdAMLbajecB0EtIBXE"}
    r = requests.get("https://api.twitter.com/2/users/"+id+"?user.fields=public_metrics", headers=headers)
    data = r.json()
    nrOfTweets = data["data"]["public_metrics"]["tweet_count"]
    return nrOfTweets


@app.get("/gettweet")
async def get_tweet():
    global user
    id = user["data"]["id"]
    headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAEyujQEAAAAAJ0Pcc2iUwHFq3tE5QXmkGZpM3qs%3Ddp0Tq4kSkqMeXGF8lNENr9apXGa6Mf6BGdAMLbajecB0EtIBXE"}
    r = requests.get("https://api.twitter.com/2/users/"+id+"/tweets?max_results=5", headers=headers)
    d = r.json()
    return d
