
import pytest

@pytest.fixture()
def DataLoad1():
    print("I'll get executed from data load functions")
    yield
    print("I'm called at last or when all the test cases has been executed")

@pytest.fixture()
def dataload():
    print("called with data driven approach2")
    return ['amit','sumit','dev']


@pytest.fixture(params=["Chrome","FireFox","IE"])
def crossBrowser(request):
    return request.param
