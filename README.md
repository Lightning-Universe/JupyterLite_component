<!---:lai-name: Slack Messenger--->

<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to send a message on Slack
______________________________________________________________________

![Tests](https://github.com/PyTorchLightning/LAI-slack-messenger/actions/workflows/ci-testing.yml/badge.svg)

</div>

# About
This component lets you send a message on Slack from a Lightning app.


----

## Use the component

<!---:lai-use:--->
```python
import lightning as L
from lit_slack import SlackMessenger

class YourComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.slack_messenger = SlackMessenger(
            token='a-long-token', 
            channel_id='A03CB4A6AK7'
        )

    def run(self):
        self.slack_messenger.send_message('hello from ⚡ lit slack ⚡')
        
app = L.LightningApp(YourComponent())

```

## install
Use these instructions to install:

<!---:lai-install:--->
```bash
git clone https://github.com/PyTorchLightning/LAI-slack-messenger.git
cd LAI-slack-messenger
pip install -r requirements.txt
pip install -e .
```
