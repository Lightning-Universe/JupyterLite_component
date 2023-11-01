import logging
import os.path
import subprocess
from typing import Optional

from lightning.app import LightningWork

logger = logging.getLogger(__name__)


class JupyterLite(LightningWork):
    """This component will launch JupyterLab instance that runs entirely in the browser.

    https://jupyterlite.readthedocs.io/en/latest/

    contents: Folder location to be copied while building jupyter lite. The provided folder will be visible in the
    Jupyter file browser.
    """

    def __init__(self, contents: Optional[str] = None, **kwargs):
        super().__init__(parallel=True, **kwargs)
        contents = contents or os.getcwd()
        assert os.path.exists(contents), f"{contents} not exist at {os.getcwd()}"
        self.contents = contents

    def run(self):
        cmd = "jupyter lite init"
        subprocess.run(cmd, shell=True)

        cmd = "jupyter lite build"
        subprocess.run(cmd, shell=True)

        cmd = f"jupyter lite serve --contents {self.contents} --port {self.port}"
        subprocess.run(cmd, shell=True)
