import pytest
from geodashai.capture import Capture
from selenium.webdriver.common.by import By

@pytest.fixture
def capture():
    return Capture()

def test_capture_init(capture):
    assert capture.driver.current_url == 'https://scratch.mit.edu/projects/105500895/fullscreen/'