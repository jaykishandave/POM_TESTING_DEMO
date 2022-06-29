import pytest


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    print("\u001b[41m This is Base Test class \u001b[0m")
    pass
