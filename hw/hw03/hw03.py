#gui 활용
#hw02의 과제들을 gui를 사용하여 완성형으로 만들기
from source import hw02_01
from source import hw02_02
from source import hw02_03
from source import hw02_04
from source import hw02_05
import tkinter as tk

def main():
    window = tk.Tk()
    window.title("과제3 - gui")
    window.resizable(False, False)

    hw02_01_label = tk.Label(window, text="과제02_1")
    hw02_02_label = tk.Label(window, text="과제02_2")
    hw02_03_label = tk.Label(window, text="과제02_3")
    hw02_04_label = tk.Label(window, text="과제02_4")
    hw02_05_label = tk.Label(window, text="과제02_5")

    hw02_01_label.grid(row=0, column=0, padx=10, pady=10)
    hw02_02_label.grid(row=1, column=0, padx=10, pady=10)
    hw02_03_label.grid(row=2, column=0, padx=10, pady=10)
    hw02_04_label.grid(row=3, column=0, padx=10, pady=10)
    hw02_05_label.grid(row=4, column=0, padx=10, pady=10)

    hw02_01_button = tk.Button(window, text="홀수, 짝수 구분하기", width=20, command=hw02_01.main)
    hw02_02_button = tk.Button(window, text="1부터 n까지 중 짝수의 합", width=20, command=hw02_02.main)
    hw02_03_button = tk.Button(window, text="화씨 -> 섭씨 변환", width=20, command=hw02_03.main)
    hw02_04_button = tk.Button(window, text="소수 판별", width=20, command=hw02_04.main)
    hw02_05_button = tk.Button(window, text="1부터 n까지 중 소수", width=20, command=hw02_05.main)

    hw02_01_button.grid(row=0, column=1, pady=10)
    hw02_02_button.grid(row=1, column=1, pady=10)
    hw02_03_button.grid(row=2, column=1, pady=10)
    hw02_04_button.grid(row=3, column=1, pady=10)
    hw02_05_button.grid(row=4, column=1, pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
