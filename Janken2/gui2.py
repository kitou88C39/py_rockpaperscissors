import tkinter as tk

//Applicationのクラスを作り、tk.Frameを継承する
class Application(tk.Frame):
//クラスの初期化のメソッド
//__init__() メソッドは、インスタンスの作成時に呼び出され、self.name と self.age という属性を初期化する
    def __init__(self, master=None):
//コンストラクタの中で、スーパー親クラスのコンストラクタを選んで、そのままマスターという引数を渡す
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill="both")
        self.create_widgets()
//create_widgetsの中で、ボタンを作成する
    def create_widgets(self):
        self.quit = tk.Button(self,text="Button", command=self.master.destroy)
        self.quit.place(x=80, y=80)

    root = tk.Tk()//rootのインスタンスを作成
    root.geometry("200x200")//rootのインスタンスの大きさを決める
    app = Application(master=root)
    root.mainloop()