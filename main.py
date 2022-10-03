import json
import functions_framework
from flask import Request, Response

cards = [
    {
        "id": "1eaa989b-9cd1-4641-ae3d-03198519d73c",
        "name": "card 1",
        "content": "pfokweropfkpwe",
    },
    {
        "id": "939d3ea3-d506-4c19-a5c2-9b92f3eb7c1c",
        "name": "card 2 ",
        "content": "fg[plfp[welfwefewfwef",
    },
    {
        "id": "eba1c8ce-70ad-4fa9-a1b8-fe656377f11f",
        "name": "card 3",
        "content": "feiopwkfpwekfopfkwe",
    },
]


@functions_framework.http
def home(request: Request):
    if request.method == "POST":
        return Response(
            json.dumps(cards),
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Max-Age": "3600",
            },
        )
    elif request.method == "GET":
        text = "Please use POST method"
        return Response(
            text,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Max-Age": "3600",
            },
        )
    elif request.method == "OPTIONS":
        return Response(
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Max-Age": "3600",
            },
        )