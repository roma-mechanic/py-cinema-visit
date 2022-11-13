from typing import Callable


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> Callable:
        print(f'{self.name} is watching "{movie}".')
