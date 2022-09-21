from typing import List


def hello(name: str = None) -> str:
    return 'Hello!' if not name else f'Hello, {name}!'


def int_to_roman(num: int) -> str:
    translator = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                  'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    ans = ''
    for rom_num, int_num in translator.items():
        count = num // int_num
        ans += count * rom_num
        num -= count * int_num
    return ans


def longest_common_prefix(strs_input: List[str]) -> str:
    if not len(strs_input):
        return ''
    ans = ''
    first_word = strs_input[0].lstrip(' \n\t')
    for i in range(1, len(first_word) + 1):
        temp = first_word.lstrip(' \n\t')[:i]
        for next_str in strs_input[1:]:
            if i > len(next_str) or not next_str.lstrip(' \n\t')[:i] == temp:
                return ans
        ans = temp
    return ans


def primes() -> int:
    def is_prime(num):
        for i in range(2, num):
            if not num % i:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = -1):
        self.balance_limit = balance_limit
        self.total_sum = total_sum

    def __call__(self, sum_spent):
        if sum_spent > self.total_sum:
            print('Not enough money to spend sum_spent dollars.')
            raise ValueError
        self.total_sum -= sum_spent
        print(f'You spent {sum_spent} dollars.')

    def __str__(self):
        return 'To learn the balance call balance.'

    def __add__(self, other):
        return BankCard(self.total_sum + other.total_sum,
                        max(self.balance_limit, other.balance_limit))

    @property
    def balance(self):
        if self.balance_limit == 0:
            print('Balance check limits exceeded.')
            raise ValueError()
        self.balance_limit -= 1
        return self.total_sum

    def put(self, sum_put):
        self.total_sum += sum_put
        print(f'You put {sum_put} dollars.')
