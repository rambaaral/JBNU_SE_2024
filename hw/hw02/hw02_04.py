###수업중 나온 코드 완성하기
###소수 판별
def sosu(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True    
    
def main():
    aaa = int(input("숫자 입력"))

    if sosu(aaa):
        print(f"{aaa}는 소수입니다.")
    else:
        print(f"{aaa}는 소수가 아닙니다.")

if __name__ == "__main__":
    main()