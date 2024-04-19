import pytest
import requests

# TODOS
# - Switch endpoints to post responses up to AlwaysON
# - handle calling endpoint multiple times
# - handle the hashing of a request...maybe? This actually might not been needed

def test_get_endpoint_static_path():
  # arrange
  # TODO figure out how to post the configuration at this point.

  # act
  actual = requests.get('http://localhost:8000/health')

  # assert
  assert 200 == actual.status_code
  assert { 'status': 'healthy' } == actual.json()


def test_get_endpoint_with_parameter():
  # arrange

  # act
  actual = requests.get('http://localhost:8000/health/13471337')

  # assert
  assert 200 == actual.status_code
  assert { 'status': 'healthy', 'params': ['13471337'] } == actual.json()


def test_get_endpoint_with_multiple_parameters():
  # arrange

  # act
  actual = requests.get('http://localhost:8000/responses/1347/health/1337')

  # assert
  assert 200 == actual.status_code
  assert { 'status': 'healthy', 'params': ['1347', '1337'] } == actual.json()


def test_get_endpoint_500():
  # arrange

  # act
  actual = requests.get('http://localhost:8000/responses/500')

  # assert
  assert 500 == actual.status_code
  assert { 'message': 'AlwaysON is OFF' } == actual.json()


def test_get_endpoint_400():
  # arrange

  # act
  actual = requests.get('http://localhost:8000/not-configured')

  # assert
  assert 400 == actual.status_code
  assert { 'message': '/not-configured has not been configured with a response'}


def test_get_endpoint_called_multiple_times():
  # arrange

  # act
  actual = requests.get('http://localhost:8000/multi-health')

  # assert
  assert 500 == actual.status_code
  assert { 'status': 'unhealthy' }

  # react
  actual = requests.get('http://localhost:8000/multi-health')

  # reassert
  assert 200 == actual.status_code
  assert { 'status': 'healthy' }
