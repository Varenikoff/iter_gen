class FlatIterator:

    def __init__(self, nested_list):
        self.cursor = -1
        self.nested_list = nested_list
        self.incl_list = None

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        while True:
            if self.incl_list:
                yield from self.incl_list
                self.incl_list = None
            else:
                self.cursor += 1
                if self.cursor == len(self.nested_list):
                    break
                value = self.nested_list[self.cursor]
                if type(value) is list:
                    self.incl_list = FlatIterator(value)
                else:
                    yield value

def flat_generator(target: list):
    start = 0
    end = len(target)
    while start < end:
        value = target[start]
        if type(value) is list:
            yield from flat_generator(value)
        else:
            yield value
        start += 1


def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
        [[3, [4]], 5],
        [6, 7, True]
    ]
    print('Flat list in iterator:')
    for item in FlatIterator(nested_list):
        print(item)
    print('\n')
    flat_list = [item for item in FlatIterator(nested_list)]
    print('flat_list as list:')
    print(flat_list)
    print('\n')
    print('Flat list in generator:')
    for item in flat_generator(nested_list):
        print(item)


if __name__ == '__main__':
    main()
