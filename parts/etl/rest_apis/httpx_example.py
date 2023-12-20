from typing import Any
import httpx
import icecream as ic
import pdb

BASE_URL = "http://httpbin.org"

def fetch_get() -> Any:
    r = httpx.get(f"{BASE_URL}/get").json()
    return r

def fetch_put() -> Any:
    r = httpx.put(f"{BASE_URL}/put").json()
    return r

def fetch_auth() -> Any:
    r = httpx.request(method="GET", url=f"{BASE_URL}/basic-auth/user/passwd", auth=("user", "passwd"))
    return r

def fetch_bearer() -> Any:
    r = httpx.request(method="GET", url=f"{BASE_URL}/bearer")

def main():
    #pdb.set_trace()
    print(fetch_bearer())

if __name__ == "__main__":
    main()