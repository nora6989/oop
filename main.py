from Calc import Calc
def main():             # 전역함수 
    calc = Calc(int(input("첫번째 수")),int(input("두번째 수")))       
                    # 생성자.  input은 숫자를 넣어도 문자로 인식하기 때문에  int를 줘야 
    print(calc.first)
    print(calc.second)
    print("{}+{}={}".format(calc.first, calc.second, calc.sum()))
    print("{}-{}={}".format(calc.first, calc.second, calc.sub()))
    print("{}*{}={}".format(calc.first, calc.second, calc.mul()))
    print("{}/{}={}".format(calc.first, calc.second, calc.div()))

"""
OOP에서는 
선언(declaration)과 실행(execution)이 구분된다.
"""

if __name__ == "__main__":
    main()



