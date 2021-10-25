import logging
from typing import Callable, Tuple
from enum import Enum

import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

__all__ = ['Capture']

class Stage(Enum):
    STEREO_MADNESS = 0
    BACK_ON_TRACK = 1
    POLARGEIST = 2

class Capture:
    '''
    The Capture object captures game screen and sends keyboard signal.

    Parameters
    ----------
    
    Attributes
    ----------
    driver : webdriver.
        driver object remotes chrome browser.
    '''
    def __init__(self, *args, **kwargs) -> None:
        self.stage = kwargs.get('stage', Stage.STEREO_MADNESS)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scratch.mit.edu/projects/105500895/fullscreen/')
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'stage_green-flag-overlay_gNXnv'))
            )
        except:
            self.driver.quit()
        self.driver.find_element(By.CLASS_NAME, 'stage_green-flag-overlay_gNXnv').click()

        # Edit below
        pass

    def jump(self) -> None:
        '''Make character jump'''
        pass

    @property
    def is_game_started(self) -> bool:
        '''It returns whether the game has started or not

        Returns
        -------
        started
            True if game has started
        '''
        pass

    @property
    def is_done(self) -> bool:
        '''The function returns whether the game has ended or not
        
        Returns
        -------
        done: bool
            True if game has ended
        '''
        pass

    def get_screenshot(self, res: Tuple[int, int, int], preprocessor: Callable[[], np.array]) -> np.array:
        '''The function captures game screen and retuns as numpy array with specific shape
        
        Parameters
        ----------
        res: Tuple
            Shape of returned image
        preprocessor : Callable
            The callable function of preprocessor
        
        Returns
        -------
        img: np.array
            Captured image
        '''
        pass

    def reset(self) -> None:
        '''Reset the game (Same as clicking the green flag)'''
        pass