import json
import keyword


class Green:
    repr_color_code = 32


class Red:
    repr_color_code = 31


class ColorizeMixin:
    """
    A mixin class that provides a custom __repr__ method to colorize the output of the class.

    Methods:
        __repr__(): Returns a string representation of the object with colored output.
    """
    def __repr__(self):
        res = []
        for k, v in self.data.items():
            if isinstance(v, dict):
                res.append(repr(Advert(v, False)))
            elif k == 'price':
                res.append(f'{str(v)} ₽')
            else:
                res.append(str(v))

        s = ' | '.join(res)
        return f'\033[{self.repr_color_code}m{s}'


class Advert(ColorizeMixin, Red):
    """
    A class representing an advertisement.

    Attributes:
        data (dict): A dictionary containing the data for the advertisement.
        price (int): The price of the advertisement.

    Methods:
        __init__(data: dict, root: bool = True): Initializes an instance of the Advert class.
        __getattr__(item: str): Retrieves the value of the specified attribute.
        __setattr__(key, value): Sets the value of the specified attribute. (Only price is mutable)

    Raises:
        ValueError: If the 'title' attribute is missing in the data dictionary (when root is True).
        ValueError: If the 'price' attribute is less than 0.
    """
    def __init__(self, data: dict, root: bool = True):
        if root and 'title' not in data:
            raise ValueError('title is required')
        self.__dict__['data'] = data
        if 'price' not in data:
            self.__dict__['price'] = 0
        elif data['price'] < 0:
            raise ValueError('price must be >= 0')

    def __getattr__(self, item: str):
        if item.endswith('_') and item[:-1] in keyword.kwlist:
            item = item[:-1]

        if isinstance(self.data[item], dict):
            return Advert(self.data[item], False)
        else:
            return self.data[item]

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError('price must be >= 0')
        elif key == 'price':
            self.data[key] = value


if __name__ == '__main__':
    lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""

    lesson = json.loads(lesson_str)
    ad = Advert(lesson)
    print(ad.location.address)

    dog_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)

    print(dog_ad.price)

    dog_str2 = """{
    "title": "Вельш-корги",
    "class": "dogs"
    }"""
    dog2 = json.loads(dog_str2)
    dog_ad2 = Advert(dog2)

    print(ad)  # red output

    dog_ad.price = -5  # raise ValueError
