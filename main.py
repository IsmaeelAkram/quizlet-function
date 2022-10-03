import functions_framework
from flask import Request, Response


@functions_framework.http
def home(request: Request):
    text = "Quizlet function v1"
    return Response(text, mimetype="text/plain")