import pytest
from geodashai.env import GeometryDash
from selenium.webdriver.common.by import By

@pytest.fixture
def env():
    return GeometryDash()

def test_env_init(env):
    assert env.driver.current_url == 'https://games-online.io/game/Geometry_Jump/'