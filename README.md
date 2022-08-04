<!---:lai-name: JupyterLite--->

<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to launch a JupyterLite instance
______________________________________________________________________

![Tests](https://github.com/Lightning-AI/LAI-jupyterlite-Component/actions/workflows/ci-testing.yml/badge.svg)

</div>

# About

This component lets you launch a [JupyterLite](https://jupyterlite.readthedocs.io/en/latest/) instance, which provides a
way to serve Jupyter Notebooks completely in the
browser.

## How is it different from Jupyter Lab?

JupyterLite runs completely in the browser but JupyterLab needs a server to launch and run.
> At this moment not all the usual features available in JupyterLab and the Classic Notebook will work with JupyterLite,
> but many already do!

To learn more about JupyterLite please visit the
official [JupyterLite documentation](https://jupyterlite.readthedocs.io/en/latest/).



----

## install

Use these instructions to install:

<!---:lai-install:--->

### Using Lightning CLI

``` bash
lightning install component lightning/jupyterlite
```

### Install from GitHub repository

```bash
git clone https://github.com/Lightning-AI/LAI-jupyterlite-Component.git
cd LAI-jupyterlite-Component
pip install -r requirements.txt
pip install -e .
```

## How to use the component

To launch a Jupyter Lite instance in your app, you need to create an object of `JupyterLite` class and call the run
method in the flow.

### Example

<!---:lai-use:--->

```python
import lightning as L
from lai_jupyterlite import JupyterLite


class YourApp(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.jupyter_lite = JupyterLite()

    def run(self):
        self.jupyter_lite.run()


app = L.LightningApp(YourApp())

```
