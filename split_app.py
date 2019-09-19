def main():
    amount = int(input("金額を入力してください[円] : "))
    number_of_people = int(input("人数を入力してください[人] : "))


    pay = amount//number_of_people
    remainder = amount-(pay*number_of_people)
    print(f'{amount}円{number_of_people}人　→　1人あたり{pay}円です。端数は{remainder}円です。')

if __name__ == '__main__':
    main()