from abc import ABC, abstractmethod

class Figure(ABC):
    _pool = {}

    @abstractmethod
    def __init__(self, sides: list[int|float]) -> None:
        self.sides = sides

    @property
    def sides(self):
        return self.__sides
    
    @sides.setter
    def sides(self, new_value):
        print(new_value)
        if not isinstance(new_value, list):
            raise TypeError('The type must be <list[int]>')
        
        for value in new_value:
            if not isinstance(value, int|float):
                print(type(value))
                raise TypeError('The type must be <int>')
        
        if len(new_value) == 0:
            raise ValueError("SIze == 0")

        self.__sides = new_value

    @abstractmethod
    def perimetr(self) -> int | float:
        pass

    @abstractmethod
    def square(self) -> int | float:
        pass

    def __new__(cls, *args, **kwargs) :
        args_key = '_'.join([str(arg) for arg in args])
        kwargs_key = '_'.join([f'{key}-{value}' for key, value in kwargs.items()])
        key = args_key + kwargs_key
        if key in cls._pool.keys():
            return cls._pool[key]
        else:
            instance = super().__new__(cls)
            cls._pool[key] = instance
            return instance
        
class Square(Figure):
    def __init__(self, sides) -> None:
        super().__init__(sides)

    def perimetr(self) -> int | float:
        return sum([side for side in self.sides])
    
    def square(self) -> int | float:
        return self.sides[0]  ** 2
    

