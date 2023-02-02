from fastapi import FastAPI, Response, Request
import json

app = FastAPI()


def slice_domain(email):
    return email[email.index('@') + 1:]


@app.post("/check")
async def check(request: Request):
    request_data = await request.json()
    if not (request_data.get("email")):
        return {"message": "Provide required parameter email"}

    with open('list.json') as spam_list:
        data = json.load(spam_list)

    domain = slice_domain(request_data.get("email"))
    for i in data:
        if domain == i:
            return {"valid": False, "msg": "Provided email is not valid"}
            break

    return {"valid": True, "msg": "Success, provided email is valid"}


