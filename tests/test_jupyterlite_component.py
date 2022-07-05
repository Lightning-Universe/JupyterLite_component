from threading import Thread
from time import sleep

import requests

from lit_jupyterlite.component import JupyterLite


def test_run():
    jupyter = JupyterLite(port=8080)
    thread = Thread(target=jupyter.run, daemon=True)
    thread.start()
    sleep(5)
    assert requests.get("http://localhost:8080").status_code == 200
