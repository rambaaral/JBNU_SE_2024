###수업중 나온 코드 완성하기
###단위환산 F to C

import tkinter as tk
def hamsu():
    try:
        n = float(input1.get())
        res = f"화씨 {n}도는 섭씨 {((n - 32) * 5 / 9):.2f}도 입니다."
        input1.delete(0, tk.END)
        output.config(text=res)
    except ValueError:
        pass

def main():
    global input1, output
    window = tk.Tk()
    window.title("과제02_3 - 화씨 -> 섭씨 변환")
    window.resizable(False, False)

    label = tk.Label(window, text="화씨온도 입력")
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