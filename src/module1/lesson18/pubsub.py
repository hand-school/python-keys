from abc import abstractmethod, ABC


class Email:

    def __init__(self, from_publisher, message) -> None:
        self.from_publisher = from_publisher
        self.message = message

    def print(self):
        print(f'Publisher: {self.from_publisher} \nMessage: {self.message}')


class EmailSubscriber(ABC):

    @abstractmethod
    def update(self, email: Email) -> None:
        """
        Получить обновление от публикатора.
        """
        pass


class EmailPublisher(ABC):

    @abstractmethod
    def attach(self, observer: EmailSubscriber) -> None:
        """
        Присоединяет наблюдателя к издателю.
        """
        pass

    @abstractmethod
    def detach(self, observer: EmailSubscriber) -> None:
        """
        Отсоединяет наблюдателя от издателя.
        """
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Уведомляет всех наблюдателей о событии.
        """
        pass


class BBCNews(EmailPublisher):
    subscribers = set()

    def attach(self, subscriber: EmailSubscriber) -> None:
        self.subscribers.add(subscriber)

    def detach(self, subscriber: EmailSubscriber) -> None:
        self.subscribers.remove(subscriber)

    def notify(self, message: str) -> None:
        for subscriber in self.subscribers:
            subscriber.update(Email("BBCNews", message))


class MailClient(EmailSubscriber):

    def __init__(self, username: str) -> None:
        super().__init__()
        self.username = username

    def update(self, email: Email) -> None:
        print("_____________________")
        print(f"MailClient <{self.username}> get update")
        email.print()
        print("=====================")


news = BBCNews()
client1 = MailClient("lexcorp")
client2 = MailClient("volkodav")

news.attach(client1)
news.attach(client2)

news.notify("Hello everyone!")

news.detach(client1)

news.notify("Bye-bye!")
