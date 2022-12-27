import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
output = "json"
page = 1


def get_tistory_name(access_token):
    blog_info = f"https://www.tistory.com/apis/blog/info?\
      access_token={access_token}\
      &output={output}"

    r = requests.get(blog_info)
    blog_name = r.json()["tistory"]["item"]["blogs"][0]["name"]

    return blog_name

def get_post_list(access_token):

    post_list = (
                "https://www.tistory.com/apis/post/list?"
                f"access_token={access_token}"
                f"&output=json"
                f"&blogName=devmi"
                f"&page={page}"
            )

    r = requests.get(post_list)
    posts = r.json()["tistory"]["item"]["posts"]

    return posts

