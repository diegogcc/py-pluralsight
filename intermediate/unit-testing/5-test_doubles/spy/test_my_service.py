from unittest.mock import Mock

from my_service import MyService
from my_service import Request
from single_sign_on import SingleSignOnRegistry
from single_sign_on import SSOToken

'''
Spies and Mocks are similar to Stubs:
    - have the same methods as the tested object
But:
    - have assertions

types of assertions:
    - return value
'''


def test_hello_name():
    service = MyService(None)                   # Dummy
    response = service.handle(Request("Emily"), SSOToken())
    assert response.text == "Hello Emily!"      # Return value assertion

def test_single_sign_on():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(spy_sso_registry)
    token = SSOToken()
    service.handle(Request("Emily"), token)
    spy_sso_registry.is_valid.assert_called_with(token)