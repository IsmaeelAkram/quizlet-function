import json
import flask
from flask import Flask, request, Response
from selenium import webdriver
from selenium.webdriver.common.by import By
import uuid
import time

app = Flask(__name__)
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(options=chrome_options)

# @functions_framework.http
@app.route("/", methods=["GET", "POST", "OPTIONS"])
def home():
    if request.method == "POST":
        body = request.get_json()

        newCards = []
    
        browser.get(url=body.get("url"))
        browser.execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
        time.sleep(1)
        terms = browser.find_elements_by_class_name("SetPageTerm-content")
        terms = browser.find_elements(By.CLASS_NAME, "SetPageTerm-content")
        for term in terms:
            definition = term.find_element(By.CLASS_NAME, "SetPageTerm-definitionText").text
            term = term.find_element(By.CLASS_NAME, "SetPageTerm-wordText").text
            if definition == "" or term == "":
                continue
            newCards.append({
                "id": str(uuid.uuid4()),
                "name": term,
                "content": definition,
            })

        return Response(
            json.dumps(newCards),
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Max-Age": "3600",
            },
        )
    elif request.method == "GET":
        text = "Quizlet downloader v1"
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