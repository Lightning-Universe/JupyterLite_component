<!---:lai-name: JupyterLite--->

<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to launch a JupyterLite instance
______________________________________________________________________

![Tests](https://github.com/Lightning-AI/LAI-jupyterlite-Component/actions/workflows/ci-testing.yml/badge.svg)

</div>

# About

This component lets you launch a JupyterLite instance, which provides a way to serve Jupyter Notebooks completely in the
browser.


----

## Use the component

<!---:lai-use:--->

```python
import lightning as L
from lit_jupyterlite import JupyterLite


class YourComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.jupyter_lite = JupyterLite()

    def run(self):
        self.jupyter_lite.run()


app = L.LightningApp(YourComponent())

```

## install

Use these instructions to install:

<!---:lai-install:--->

```bash
git clone https://github.com/Lightning-AI/LAI-jupyterlite-Component.git
cd LAI-jupyterlite-Component
pip install -r requirements.txt
pip install -e .
```
