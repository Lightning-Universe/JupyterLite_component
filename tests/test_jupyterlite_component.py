from threading import Thread
from time import sleep

import requests

from lai_jupyterlite.component import JupyterLite


def test_run(tmp_path):
    jupyter = JupyterLite(port=8080, contents=str(tmp_path))
    thread = Thread(target=jupyter.run, daemon=True)
    thread.start()
    sleep(10)
    assert requests.get("http://0.0.0.0:8080").status_code == 200
