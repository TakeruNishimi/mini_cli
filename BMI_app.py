def main():
    height = float(input("身長を入力してください[cm] : "))
    weight = float(input("体重を入力してください[kg] : "))
    bmi = round((weight / (height / 100) ** 2), 2)
    print("BMIは ",bmi)



if __name__ == '__main__':
    main()
