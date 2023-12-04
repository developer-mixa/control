from abc import ABC, abstractmethod

class Figure(ABC):
    _pool = {}
    _instance = None

    @abstractmethod
    def __init__(self, sides) -> None:
        self.__sides = sides

    @property
    def sides(self):
        return self.__sides
    
    @sides.setter
    def sides(self, new_value):
        
        if not isinstance(new_value, list[int|float]):
            raise TypeError('The type must be <list[int]>')

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
    

sq = Square([12,12,12,12])
sq2 = Square([12,12,12,12])
print(sq, sq2)
