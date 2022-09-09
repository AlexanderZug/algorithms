# id 70227497

class DeQueue:
    def __init__(self, max_size: int):
        self.queue = [None] * max_size
        self.size = 0
        self.front = - 1
        self.back = 0

    def push_back(self, value: str):
        self.back = self.push(self.back, 1, value)

    def pop_back(self):
        self.back, value = self.pop(self.back, 1)
        return value

    def push_front(self, value: str):
        self.front = self.push(self.front, -1, value)

    def pop_front(self):
        self.front, value = self.pop(self.front, -1)
        return value

    def push(self, index: int, index_change: int, value: str):
        if self.size < len(self.queue):
            self.queue[index] = value
            self.size += 1
            return (index + index_change) % len(self.queue)
        raise IndexError('Буфер заполнен')

    def pop(self, index: int, index_change: int):
        if self.size > 0:
            new_index = (index - index_change) % len(self.queue)
            self.size -= 1
            return new_index, self.queue[new_index]
        raise IndexError('Буфер пуст')


if __name__ == '__main__':
    commands_count = int(input())
    queue_size = DeQueue(int(input()))
    for _ in range(commands_count):
        command, *values = input().split()
        try:
            result = getattr(queue_size, command)(*values)
        except IndexError:
            result = 'error'
        if result:
            print(result)
