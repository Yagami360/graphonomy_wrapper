# graphonomy_wrapper
Graphonomy の推論スクリプト [`inference.py`](https://github.com/Yagami360/Test_Repository/tree/master/graphonomy-pallarel/graphonomy/Graphonomy/exp/inference) のラッパーモジュール。<br>
単一の画像ではなく、指定したフォルダ内の全人物画像に対して、人物パース画像を生成するように修正しています。

## ■ 動作環境
- Pytorch = 0.4.0 or Pytorch = 1.1.x
    - オリジナルの Graphonomy は Pytorch = 0.4.0 での動作環境になっているが、推論スクリプトは 1.x 系でも動作することを確認済み
- tqdm

## ■ 使い方
1. 学習済みモデルをダウンロードして、checkpoints 以下のフォルダに保管
    1. Universal trained model : [Dowload](https://drive.google.com/file/d/1sWJ54lCBFnzCNz5RTCGQmkVovkY9x8_D/view)<br>
    ※ 詳細は、オリジナルの [Graphonomy](https://github.com/Yagami360/Test_Repository/tree/master/graphonomy-pallarel/graphonomy/Graphonomy) の `README.md` を参照

1. 推論スクリプトを実行
    ```sh
    $ sh inference_all.sh 
    ```
