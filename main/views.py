from main import app
from flask import render_template, request
from query import get_results
from config import FREEZER_BASE_URL

results = get_results()

@app.route('/')
def index():
    page_title = 'Town Meeting Day 2017'
    page_url = FREEZER_BASE_URL.rstrip('/') + request.path

    return render_template('content.html',
        page_title=page_title,
        page_url=page_url,
        results=results)
