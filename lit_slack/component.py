import lightning as L

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackMessenger(L.LightningFlow):
    def __init__(self, token, channel_id) -> None:
        """
        Sends a message to a specific slack channel.
        To enable this:
        1. visit https://api.slack.com/apps
        2. create an app
        3. install the app in your workspace

        Example:

        .. code:: python

            import lightning as L
            from lit_slack import SlackMessenger

            class YourComponent(L.LightningFlow):
                def __init__(self):
                    super().__init__()
                    self.slack_messenger = SlackMessenger(token='a-long-token', channel_id='A03CB4A6AK7')

                def run(self):
                    self.slack_messenger.run('hello from ⚡ lit slack ⚡')

        token: "Bot User OAuth Token" found at https://api.slack.com/apps/YOUR-APP_ID/install-on-team
        channel_id: Open slack > find channel > get channel details > copy channel ID at the bottom

        """
        super().__init__()
        self.channel_id = channel_id
        self.token = token


    def send_message(self, message):
        return self.run('send_message', message)


    def run(self, action: str, message: str):
        if action == 'send_message':
            return self._send_message(message)


    def _send_message(self, message):
        try:
            # Call the conversations.list method using the WebClient
            client = WebClient(token=self.token)
            result = client.chat_postMessage(
                channel=self.channel_id,
                text=message
            )
            return result

        except SlackApiError as e:
            print(f"Error: {e}")
