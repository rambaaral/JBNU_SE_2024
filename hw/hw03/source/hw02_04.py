###수업중 나온 코드 완성하기
###소수 판별
import tkinter as tk
def sosu(n):
    for i in range(2,n):
        if n % i == 0:
            return f"{n}은(는) 소수가 아닙니다."
    return f"{n}은(는) 소수입니다." 

def hamsu():
    try:
        n = int(input1.get())
        res = sosu(n)
        input1.delete(0, tk.END)
        output.config(text=res)
    except ValueError:
        pass

def main():
    global input1, output
    window = tk.Tk()
    window.title("과제02_4 - 소수 판별")
    window.resizable(False, False)

    label = tk.Label(window, text="숫자 입력")
    label.grid(row=0, column=0, padx=10, pady=10)

    input1 = tk.Entry(window, width=10)
    input1.grid(row=0, column=1, padx=10, pady=10)

    button = tk.Button(window, text="제출", command=hamsu)
    button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    output = tk.Label(window, text="")
    output.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()