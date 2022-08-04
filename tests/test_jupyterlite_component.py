import random
from threading import Thread
from time import sleep

import requests

from lai_jupyterlite.component import JupyterLite


def test_run(tmp_path):
    port = int("80" + str(random.randrange(10, 99)))
    jupyter = JupyterLite(host="localhost", port=port, contents=str(tmp_path))
    thread = Thread(target=jupyter.run, daemon=True)
    thread.start()
    sleep(10)
    requests.get(f"http://localhost:{port}").raise_for_status()
