import unittest
from pathlib import Path
from typing import Optional, Union

import numpy as np
import pytest
from geodashai.env import GeometryDash
from PIL import Image

def image_to_numpy(path: Union[Path, str]) -> np.array:
    return np.array(Image.open(path).convert('L'))[..., np.newaxis]

@pytest.fixture(scope='class')
def driver(request):
    request.cls.env = GeometryDash(headless=True)
    yield
    request.cls.env.close()

@pytest.mark.usefixtures('driver')
class EnvTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _request_test_root(self, TEST_ROOT):
        self._test_root = TEST_ROOT

    def test_env_init(self):
        assert self.env.driver.current_url == 'https://games-online.io/game/Geometry_Jump/'
    
    def test_env_observation(self):
        assert self.env.observation.shape[0] == self.env.observation_space.shape[0] and \
            self.env.observation.shape[1] == self.env.observation_space.shape[1]
    
    def test_env_done(self):
        path_done = list(self._test_root.glob('images/done*'))
        path_not_done = list(self._test_root.glob('images/not_done*'))
        for path in path_done:
            assert self.env.done(image_to_numpy(path)) == True
        for path in path_not_done:
            assert self.env.done(image_to_numpy(path)) == False

    def test_env_clickable(self):
        path = self._test_root / 'images'
        assert self.env.retry_clickable(image_to_numpy(path / 'retry_clickable.png')) == True
        assert self.env.retry_clickable(image_to_numpy(path / 'retry_not_clickable.png')) == False

    def test_env_is_flying(self):
        path_is_flying = list(self._test_root.glob('images/is_flying*'))
        path_not_done = list(self._test_root.glob('images/not_done*'))
        for path in path_is_flying:
            assert self.env.is_flying(image_to_numpy(path)) ==  True
        for path in path_not_done:
            assert self.env.is_flying(image_to_numpy(path)) ==  False
