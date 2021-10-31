import io
import logging
import time
from enum import Enum
from typing import Any, Callable, Dict, Tuple

import gym
import numpy as np
from gym import spaces
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class GeometryDash(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(GeometryDash, self).__init__()

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self._init_browser()

        self.action_space = spaces.Discrete(2) # Jump, No action
        self.observation_space = spaces.Box(
            low=0, 
            high=255, 
            shape=(476, 720, 1),
            dtype=np.uint8
            ) #Images

    def _init_browser(self) -> None:
        self.driver.set_window_size(720, 600)
        self.driver.get('https://games-online.io/game/Geometry_Jump/')
        try:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="loader"][contains(@style, "display: none")]'))
            )
        except:
            self.driver.quit()
            raise TimeoutError()

    def step(self, action: int) -> Tuple[np.array, float, bool, Dict[str, Any]]:
        pass
        # return observation, reward, done, info

    def reset(self) -> np.array:
        while not self.retry_clickable:
            time.sleep(0.35)
        ActionChains(self.driver)\
            .move_to_element_with_offset(self.driver.find_element(By.TAG_NAME, 'body'), 300, 350) \
            .click() \
            .perform()
        time.sleep(1.35)
        return self.observation

    def render(self, mode: str='human'):
        pass

    def close(self):
        self.driver.quit()
    
    def _jump(self) -> None:
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)
    
    @property
    def observation(self) -> np.array:
        return np.array(Image.open(io.BytesIO(self.driver.get_screenshot_as_png())).convert('L')).reshape(self.observation_space.shape)

    @property
    def done(self) -> bool:
        return not np.any(self.observation.squeeze(-1)[:,210:240] == 186)
    
    @property
    def retry_clickable(self) -> bool:
        return self.observation[200][300][0] == 255

    @property
    def is_flying(self) -> bool:
        return not np.any(self.observation.squeeze(-1)[:,210:240] == 218)