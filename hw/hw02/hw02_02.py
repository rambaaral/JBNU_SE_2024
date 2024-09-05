###수업중 나온 코드 완성하기
###1부터 100까지 중 짝수의 합

def main():

    print(f"1부터 100까지의 합은 {sum([i if i % 2 == 0 else 0 for i in range(101)])}입니다.")

if __name__ == "__main__":
    main()