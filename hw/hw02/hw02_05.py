###수업중 나온 코드 완성하기
###소수 구하기
def sosu(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def main():
    aaa = int(input("숫자 입력"))

    res = [i for i in range(1,aaa+1) if sosu(i)]

    print(res)
if __name__ == "__main__":
    main()