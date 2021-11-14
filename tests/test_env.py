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
    
    def test_env_observation(self):
        assert self.env.observation.shape[0] == self.env.observation_space.shape[0] and \
            self.env.observation.shape[1] == self.env.observation_space.shape[1]