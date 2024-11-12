""" 
整数の引数を2つ受け取って足し算する関数、同様に引き算、掛け算、割り算、余り算
をする関数をラムダ式を用いて定義しなさい。
それらの関数を利用してユーザが入力した2つの整数の足し算、引き算、掛け算、割り算、余り算
の結果を以下の実行例を参考に画面に表示するプログラムを作成しなさい。
【実行例】
整数を入力してください: 7
整数を入力してください: 3
7 + 3 = 10
7 - 3 = 4
7 * 3 = 21
7 / 3 = 2
7 % 3 = 1
"""
#整数値の入力
num1 = int(input('整数を入力してください: '))
num2 = int(input('整数を入力してください: '))

#四則演算の関数
add = lambda num1, num2: num1 + num2
sub = lambda num1, num2: num1 - num2
mul = lambda num1, num2: num1 * num2
div = lambda num1, num2: num1 // num2
rem = lambda num1, num2: num1 % num2

#結果の表示
print(f'{num1} + {num2} = {add(num1, num2)}')
print(f'{num1} - {num2} = {sub(num1, num2)}')
print(f'{num1} * {num2} = {mul(num1, num2)}')
print(f'{num1} / {num2} = {div(num1, num2)}')
print(f'{num1} % {num2} = {rem(num1, num2)}')

