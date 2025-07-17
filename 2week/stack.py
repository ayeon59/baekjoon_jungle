from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu',['푸시','팝','피크','검색','덤프','종료'])

def select_menu() -> Menu:

    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep=' ', end='')
        n = int(input(':' ))
        if 1<= n <= len(Menu):
            return Menu()
        
s = FixedStack(64)

while True : 
    print(f'현재 데이터의 개수 : {len(s)}/{s.capacity}')
    menu = select_menu()

 