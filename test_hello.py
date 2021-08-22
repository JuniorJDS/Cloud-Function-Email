from unittest.mock import Mock

import main


def test_hello__print_name_receiving_from_request__expected_string():
    name = 'test'
    data = {'name': name}

    req = Mock(
        get_json = Mock(return_value=data),
        args = data,
        )
    
    assert main.hello(req) == f'Hello, {name}'

def test_hello__print_hello_world_from_request__expected_string():
    data = {}

    req = Mock(
        get_json = Mock(return_value=data),
        args = data,
        )

    assert main.hello(req) == f'Hello, World!'