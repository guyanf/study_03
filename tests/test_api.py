
# _*_ coding: utf-8 _*_
# /usr/bin/env python

"""
Author: Thomas Chen
Email: guyanf@gmail.com
Company: Thomas

date: 2025/3/29 09:59
desc:
"""

import requests
import pytest
from requests.auth import HTTPBasicAuth

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def sample_data():
    """ 预设测试数据 """
    return {
        "title": "Test Title",
        "body": "Test body content.",
        "userId": 1
    }

def test_get_posts():
    """ 测试 GET 请求 """
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert "title" in response.json()

def test_create_post(sample_data):
    """ 测试 POST 请求 """
    response = requests.post(f"{BASE_URL}/posts", json=sample_data)
    assert response.status_code == 201
    assert response.json()["title"] == sample_data["title"]

def test_update_post(sample_data):
    """ 测试 PUT 请求 """
    response = requests.put(f"{BASE_URL}/posts/1", json=sample_data)
    assert response.status_code == 200
    assert response.json()["title"] == sample_data["title"]

def test_delete_post():
    """ 测试 DELETE 请求 """
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_multiple_posts(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id


def test_mock_get_post(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "userId": 1,
        "id": 1,
        "title": "Mocked title",
        "body": "This is a mocked post body."
    }

    # Mock requests.get 方法
    mocker.patch("requests.get", return_value=mock_response)

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Mocked title"



def test_api_timeout():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url, timeout=2)  # 设置超时 2 秒
        assert response.status_code == 200
    except requests.exceptions.Timeout:
        assert False, "API request timed out!"


def test_api_with_basic_auth():
    url = "https://httpbin.org/basic-auth/user/pass"
    response = requests.get(url, auth=HTTPBasicAuth("user", "pass"))

    assert response.status_code == 200


def test_api_404():
    url = "https://jsonplaceholder.typicode.com/posts/9999"
    response = requests.get(url)

    assert response.status_code == 404


def test_api_request_exception():
    url = "https://invalid-url.com"

    try:
        response = requests.get(url)
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        assert False, f"API request failed: {e}"
