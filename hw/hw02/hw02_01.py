###수업중 나온 코드 완성하기
###홀수, 짝수 구분

def main():
    aaa = int(input("숫자 입력"))

    if aaa % 2 == 0:
        print(f"{aaa}은(는) 짝수입니다.")
    else:
        print(f"{aaa}은(는) 홀수입니다.")

if __name__ == "__main__":
    main()