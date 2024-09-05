###수업중 나온 코드 완성하기
###단위환산 F to C

def main():
    tf = int(input("화씨 입력"))
    tc = (tf - 32) * 5 / 9

    print(f"{tf}F => {tc:.2f}C")

if __name__ == "__main__":
    main()