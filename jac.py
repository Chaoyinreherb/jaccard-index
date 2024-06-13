import os
import sys
import tkinter.filedialog

j_list = []

def read(r): #ファイルの内容を取り込む
    if os.path.isfile(r):
        print("ファイルを確認しました。\n")
    else:
        print("ファイルが見つかりません。\n")
        return -1

    f = open(r,"r",encoding=code) #文字コードを指定してファイルを開く

    k = 0
    print("データ一覧:")
    list = f.readline()

    while list:
        if '\n' in list[0]:
            print("改行")
        else:
            k = k + 1

            if '\n' in list:
                print("改行あり〼。")
            else:
                print("改行ありません。")
        
            print("list" + str(k) + ":\n",list)
            j_list.insert(0,list.split())
            
        list = f.readline()

    f.close()
    j_list.reverse()

def jaccard_sim_coef(): #jaccard係数を計算
    datas = len(j_list) - 1
    c = 0
    print("\n")

    while c <= datas:
        la = "list" + str(c+1)
        e = c + 1
        
        while e <= datas:
            lb = "list" + str(e+1)
            set_inter = set.intersection(set(j_list[c]),set(j_list[e]))
            num_inter = len(set_inter)
            print(set_inter, num_inter)

            set_union = set.union(set(j_list[c]),set(j_list[e]))
            num_union = len(set_union)
            print(set_union, num_union)

            try:
                print(la + "と" + lb + "のjaccard係数は" , float(num_inter)/num_union, "です。\n")
            except ZeroDivisionError:
                print(la + "と" + lb + "のjaccard係数は" , 1.0 , "です。\n")

            e = e + 1
        c = c + 1

print("2024/2/1")
while True:
    print("※実行時に'UnicodeDecodeError'が出る場合はここに文字コードを入力し、指定してください。")
    code = input("※実行時に'UnicodeDecodeError'が出る場合はここに文字コードを入力し、指定してください。そのまま(utf-8で良い場合はそのままEnterを押してください。)") #もしEnterなら\nが入力される
    print("条件: 1 一つひとつの単語のデータは半角スペース(全角でもおそらく問題ない)で区切られている")
    print("　　　2 データ列の区切りで一行開けている")
    print("比較するデータが書かれた、上の条件にあうテキストファイルを選択してください。")

    t = tkinter.filedialog.askopenfilename(filetypes=[("txt file", "*.txt")]) #エクスプローラーを開く

    if not code:
        print("文字コード:デフォルト")
        code = "utf-8"
    else:
        print("文字コード:" + code)

    if read(t) == -1:
        sys.exit()
    jaccard_sim_coef()
    
    t = input("続けて行う場合は'y'、この画面を閉じる場合は'n'を入力してください。≫")
    if t == "n":
        sys.exit()

    j_list.clear()
