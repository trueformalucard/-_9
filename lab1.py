class Russian:
    @staticmethod
    def greet():
        return "Привет"

class English:
    @staticmethod
    def greet():
        return "Hello"

def show_greeting(language):
    print(f"На этом языке говорят: {language.greet()}")

russian = Russian()
english = English()

show_greeting(russian)
show_greeting(english)