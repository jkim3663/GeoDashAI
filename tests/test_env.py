import pytest
from geodashai.env import GeometryDash
from selenium.webdriver.common.by import By
import unittest

@pytest.fixture(scope='class')
def driver(request):
    request.cls.env = GeometryDash()
    yield
    request.cls.env.close()

@pytest.mark.usefixtures('driver')
class EnvTest(unittest.TestCase):
    def test_env_init(self):
        assert self.env.driver.current_url == 'https://games-online.io/game/Geometry_Jump/'
        assert self.env.driver.get_window_size()['width'] == 1024 and \
            self.env.driver.get_window_size()['height'] == 768
    
    def test_env_observation(self):
        assert self.env.observation.shape == self.env.observation_space.shape