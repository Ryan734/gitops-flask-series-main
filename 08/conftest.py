from pytest import fixture

def pytest_addoption(parser):
    parser.addoption(
        "--endpoint",
        action="store"
    )

    parser.addoption(
        "--context",
        action="store"
    )

@fixture()
def endpoint(request):
    return request.config.getoption("--endpoint")

def pytest_configure(config):
    global option
    option = config.option
