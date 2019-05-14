from bs4 import BeautifulSoup

my_int = 4_354_354_353_555_550_000_000_000_000
my_weight = 69.4
my_name = 'soongon'
my_bool = True     # False

print(f'제 이름은 {my_name}이고, 몸무게는 {my_weight}kg입니다.')

soup = BeautifulSoup('abc', 'html.parser')

print(type(soup))

print(my_int + 23_453_453)