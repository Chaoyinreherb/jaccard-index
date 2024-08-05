import os
import sys

j_list = []

def read(r, code): #ファイルの内容を取り込む　ファイルパス、文字コード
    if os.path.isfile(r):
        print("ファイルを確認しました。\n")
    else:
        print("ファイルが見つかりません。\n")
        return -1

    f = open(r,"r",encoding=code) #文字コードを指定してファイルを開く

    k = 0
    print("データ一覧:")
    list = f.readline()
    j_list = []

    while list:
        if '\n' in list[0]:
            print("改行")
        else:
            k += 1

            if '\n' in list:
                print("改行あり〼。")
            else:
                print("改行ありません。")
        
            print("list" + str(k) + ":\n",list)
            j_list.insert(0,list.split())
            
        list = f.readline()

    f.close()
    j_list.reverse()
    return j_list

def jaccard_sim_coef(j_list): #jaccard係数を計算
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

            e += 1
        c += 1

def main():
    print("2024/2/1")
    while True:
        code = input("※実行時に'UnicodeDecodeError'が出る場合はここに文字コードを入力し、指定してください。そのまま(utf-8で良い場合はそのままEnterを押してください。)>>") #もしEnterなら\nが入力される
        print("比較するデータが書かれたテキストファイルを選択してください。条件はREADME.mdを参照してください")

        t = input("ファイルのパスを入力してください>>")

        if not code:
            print("文字コード:デフォルト")
            code = "utf-8"
        else:
            print("文字コード:" + code)

        if (j_list := read(t, code)) == -1:
            sys.exit()
        else:
            jaccard_sim_coef(j_list)
    
        t = input("続けて行う場合は'y'、終了する場合は'n'を入力してください。≫")
        if t == "n":
            sys.exit()

main()
