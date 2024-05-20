import sys
import os

# 親ディレクトリをsys.pathに追加してmainをインポート
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from app import app
import pytest
import json

def test_index_route():
    response = app.test_client().get('/fib?n=5')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['result'] == 5
