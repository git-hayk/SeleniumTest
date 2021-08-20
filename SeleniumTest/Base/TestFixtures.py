import pytest
from WebDriver    import WebDriver

class TestFixtures:
    @pytest.fixture()
    def RunStopDriver(self):
        WebDriver().createDriver()
        yield
        WebDriver().closeDriver()
