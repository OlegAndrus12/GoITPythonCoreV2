# polymorphism: same interface, different implementations
# duck typing: if it has .send() it works — no shared base class required


class EmailNotifier:
    def send(self, message):
        print(f"[Email] {message}")


class SlackNotifier:
    def __init__(self, channel):
        self.channel = channel

    def send(self, message):
        print(f"[Slack #{self.channel}] {message}")


class WebhookNotifier:
    def __init__(self, url):
        self.url = url

    def send(self, message):
        print(f"[Webhook → {self.url}] {message}")


# duck typing: any object with a .send() method works here
def notify_all(notifiers, message):
    for notifier in notifiers:
        notifier.send(message)


notifiers = [
    EmailNotifier(),
    SlackNotifier("deployments"),
    WebhookNotifier("https://hooks.example.com/xyz"),
]

notify_all(notifiers, "Deployment to production finished")

print("--------------------")

# polymorphism via inheritance — overriding a method
class BaseLogger:
    def log(self, message):
        print(f"[LOG] {message}")


class FileLogger(BaseLogger):
    def __init__(self, path):
        self.path = path

    def log(self, message):
        print(f"[FILE:{self.path}] {message}")


class SilentLogger(BaseLogger):
    def log(self, message):
        pass  # suppresses all output


loggers = [BaseLogger(), FileLogger("/var/log/app.log"), SilentLogger()]
for logger in loggers:
    logger.log("server started")
