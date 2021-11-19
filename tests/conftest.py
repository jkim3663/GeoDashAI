from pathlib import Path

import pytest

@pytest.fixture(scope='module')
def TEST_ROOT():
    return Path(__file__).resolve().parent