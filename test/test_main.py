import sys
import os

# 親ディレクトリをsys.pathに追加してmainをインポート
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import app
import pytest
import json

def test_1():
    response = app.test_client().get('/fib?n=1')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['result'] == 1
    
def test_2():
    response = app.test_client().get('/fib?n=2')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['result'] == 1

def test_5():
    response = app.test_client().get('/fib?n=5')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['result'] == 5
    
def test_missing_parameter():
    response = app.test_client().get('/fib')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['message'] == 'Parameter n is missing'
    
def test_non_numeric_parameter():
    response = app.test_client().get('/fib?n=abc')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['message'] == 'Parameter n must be a number.'
    
def test_zero():
    response = app.test_client().get('/fib?n=0')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['message'] == 'Parameter n must be a positive integer.'