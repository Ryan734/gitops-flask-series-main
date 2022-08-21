import pytest
import requests

def test_index(endpoint):
    result = requests.get("http://{}/".format(endpoint))
    assert b'hello' in result.content
