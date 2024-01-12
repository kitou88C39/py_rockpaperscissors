//tkinterをimportし、as keyordによりtkという名前をつける:2行目以降にtkが使える
import tkinter as tk

root = tk.Tk()//tkというmoduleが持っているtk classのobjectを作成する
root.geometry("200x200")//geometryというmethodを呼ぶことで、windowの大きさを決める

//frameウイジェットは、ホーム画面上にウィンドウの表示や操作をするための機能
//(master=root)と記述することでrootのウィンドウにフレームを配置するという意味
frame = tk.Frame(master=root)
frame.pack(expand=True, fill="both")

//ウィンドウのフレームにbuttonを配置するという意味
//command=root.destroyはボタンをクリックした時の動作
button = tk.Button(frame, text="Button", command=root.destroy)
//buttonを座標のどこに配置するという意味
button.place(x=80, y=80)

root.mainloop()//mainloopを置くことでイベントが起きたら、それに対応するコマンドを実行する形でアプリを動かす機能