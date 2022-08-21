import re  # new
import pytest
import requests


def test_index(endpoint):
    result = requests.get(f'http://{endpoint}/')
    assert b'hello' in result.content


# new
def test_cluster(endpoint):
    result = requests.get(f'http://{endpoint}/cluster')
    data = result.content.decode()
    assert re.match(r'This is (\w+) in cluster (\w+)', data)
