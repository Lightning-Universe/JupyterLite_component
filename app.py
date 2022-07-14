import os

from lightning import LightningApp, LightningFlow

from lit_jupyterlite.component import JupyterLite


class Demo(LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        os.makedirs("jupyter-contents", exist_ok=True)
        self.lite = JupyterLite("jupyter-contents")

    def run(self):
        self.lite.run()

    def configure_layout(self):
        return [{"name": "lite", "content": self.lite.url}]


if __name__ == "__main__":
    app = LightningApp(Demo())
