from unittest.mock import Mock

from my_service import MyService
from my_service import Request
from single_sign_on import SingleSignOnRegistry
from single_sign_on import SSOToken

'''
Spies are similar to Stubs:
    - have the same methods as the tested object
    - records the method calls it receives, so you can assert they were correct
    - used when you want to make sure that interactions between two objects 
        are happening correctly
        
But:
    - have assertions

types of assertions:
    - return value (or an exception)
        'assert converted_text == "quote: &#x27;<br />"'
    - state change (use an API to query the new state)
        'assert not alarm.is_alarm_on'
    - method call (did a specific method get called on a collaborator)
        'spy_sso_registry.is_valid.assert_called_with(token)'
'''


def test_hello_name():
    stub_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(stub_sso_registry)      # Dummy
    response = service.handle(Request("Emily"), SSOToken())
    assert response.text == "Hello Emily!"      # Return value assertion

def test_single_sign_on():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(spy_sso_registry)
    token = SSOToken()
    service.handle(Request("Emily"), token)
    spy_sso_registry.is_valid.assert_called_with(token)

def test_single_sign_on_with_invalid_token():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    spy_sso_registry.is_valid.return_value = False
    service = MyService(spy_sso_registry)
    token = SSOToken()
    response = service.handle(Request("Emily"), token)
    spy_sso_registry.is_valid.assert_called_with(token)
    assert response.text == "Please sign in"