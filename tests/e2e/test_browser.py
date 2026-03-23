import subprocess
import time
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def server():
    proc = subprocess.Popen(
        ["uvicorn", "app.main:app", "--port", "8000"]
    )
    time.sleep(2)
    yield
    proc.terminate()
    proc.wait()

@pytest.mark.e2e
def test_docs_page_loads(server):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000/docs")
        assert "Swagger" in page.title() or page.locator("h2").count() > 0
        browser.close()