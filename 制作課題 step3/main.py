from moneycsv import MoneyCsv
run = MoneyCsv('balance.txt', 'history.csv')

while True:
    ope = input('残高と履歴の確認:1  入金:2  出金:3  終了:4 -->')
    if ope == '1':
        print(f'残高:{run.get_balance()}円')
        his = run.get_history()
        for i in range(len(his)):
            print('-' * 30)
            print(f'入金/出金:{his[i][0]}')
            print(f'科目:{his[i][1]}')
            print(f'金額:{his[i][2]}')
    elif ope == '2':
        sub = input('科目:')
        try:
            val = int(input('金額:'))
        except ValueError:
            print('金額は数字で入力してください')
        else:
            run.set_payment(sub, val)
    elif ope == '3':
        sub = input('科目:')
        try:
            val = int(input('金額:'))
        except:
            print('金額は数字で入力してください')
        else:
            if run.set_withdrawal(sub, val):
                pass
            else:
                print('残高が不足しています')
    elif ope == '4':
        run.save()
        print('終了します')
        break
    else:
        print('1~4で入力してください')