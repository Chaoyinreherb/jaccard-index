## 単語によるjaccard係数を求めるpythonコード

条件に沿ったテキストファイルを読み込んで、リストとリストのjaccard係数を求めるかんたんなプログラムです。
ファイルのパスは絶対パス、相対パスのどちらでも良いです。

### 係数を求めるためのファイルの条件:
* 1つ1つの単語が半角スペースで区切られている
* 1つ1つの単語のリスト同士の間が一行空いている
<br>
例:

>
> int main ( int argc , char \*argv[] )
>
> int main ( void )
>
> public static void main ( String[] args )
>

### 参考文献:
* https://mieruca-ai.com/ai/jaccar\_dice\_simpson/
