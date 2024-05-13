class ChatRoomMediator:
    """
    @brief Klasa mediatora czatu.

    Klasa ChatRoomMediator zarządza komunikacją między użytkownikami
    czatu.
    """
    def __init__(self):
        """Inicjalizuje pustą listę uczestników czatu."""
        self.users = []

    def add_user(self, user):
        """Dodaje użytkownika do czatu."""
        self.users.append(user)

    def send_message(self, sender, message):
        """Wysyła wiadomość do wszystkich użytkowników czatu."""
        for user in self.users:
            if user != sender:
                user.receive_message(message)


class User:
    """
    @brief Klasa reprezentująca użytkownika czatu.

    Klasa User reprezentuje użytkownika czatu, który może wysyłać i odbierać
    wiadomości za pośrednictwem mediatora czatu.
    """
    def __init__(self, mediator, name):
        """Inicjalizuje użytkownika z podanym mediatorem i imieniem."""
        self.mediator = mediator
        self.name = name

    def send_message(self, message):
        """Wysyła wiadomość do wszystkich użytkowników czatu."""
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(self, message)

    def receive_message(self, message):
        """Odbiera wiadomość od innego użytkownika czatu."""
        print(f"{self.name} receives: {message}")


if name == "main":
    # Tworzenie mediatora czatu
    chat_mediator = ChatRoomMediator()

    # Tworzenie użytkowników czatu
    user1 = User(chat_mediator, "Eryk")
    user2 = User(chat_mediator, "Paweł")
    user3 = User(chat_mediator, "Aleksanda")
    user4 = User(chat_mediator, "Marceliana")
    user5 = User(chat_mediator, "Fizyka techniczka")

    # Dodawanie użytkowników do czatu
    chat_mediator.add_user(user1)
    chat_mediator.add_user(user2)
    chat_mediator.add_user(user3)
    chat_mediator.add_user(user4)

    # Wysyłanie wiadomości przez użytkownika
    user1.send_message("\nHej, wszystkim!\n")
    user2.send_message("\nPorozmawiajmy o naszym projekcie\n")
    user3.send_message("\nOto nasz Mediator ...\n")
    user4.send_message("\nJak ocenacie nasz projekt?\n")
    user5.send_message("\n5.0\n")