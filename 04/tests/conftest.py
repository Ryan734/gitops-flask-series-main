from pytest import fixture

def pytest_addoption(parser):
    parser.addoption(
        "--endpoint",
        action="store"
    )

@fixture()
def endpoint(request):
    return request.config.getoption("--endpoint")
