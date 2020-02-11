# -*- coding:utf-8 -*-
import os
import argparse
from datetime import datetime
import numpy as np
from tqdm import tqdm
from PIL import Image
import random

# PyTorch
import torch

# 自作クラス
from graphonomy_wrapper import GraphonomyWrapper


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', choices=['cpu', 'gpu'], default="gpu", help="使用デバイス (CPU or GPU)")
    parser.add_argument('--in_image_dir', type=str, default="images", help="入力画像のディレクトリ" )
    parser.add_argument('--results_dir', type=str, default="results", help="生成画像の出力ディレクトリ")
    parser.add_argument('--load_checkpoints_path', type=str, default="Graphonomy/model/0/model.pth", help="モデルのチェックポイントパス")
    parser.add_argument('--batch_size', type=int, default=1, help="バッチサイズ")
    parser.add_argument("--seed", type=int, default=8, help="乱数シード値")
    parser.add_argument('--debug', action='store_true', help="デバッグモード有効化")
    args = parser.parse_args()

    # 実行条件の出力
    print( "----------------------------------------------" )
    print( "実行条件" )
    print( "----------------------------------------------" )
    print( "開始時間：", datetime.now() )
    print( "PyTorch version :", torch.__version__ )
    for key, value in vars(args).items():
        print('%s: %s' % (str(key), str(value)))

    # 実行 Device の設定
    if( args.device == "gpu" ):
        use_cuda = torch.cuda.is_available()
        if( use_cuda == True ):
            device = torch.device( "cuda" )
            #torch.cuda.set_device(args.gpu_ids[0])
            print( "実行デバイス :", device)
            print( "GPU名 :", torch.cuda.get_device_name(device))
            print("torch.cuda.current_device() =", torch.cuda.current_device())
        else:
            print( "can't using gpu." )
            device = torch.device( "cpu" )
            print( "実行デバイス :", device)
    else:
        device = torch.device( "cpu" )
        print( "実行デバイス :", device)

    print('-------------- End ----------------------------')

    # 各種出力ディレクトリ
    if not( os.path.exists(args.results_dir) ):
        os.mkdir(args.results_dir)

    # seed 値の固定
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    #-------------------------------
    # Graphonomy
    #-------------------------------
    model = GraphonomyWrapper( args.load_checkpoints_path )
    image_names = sorted( [f for f in os.listdir(args.in_image_dir) if f.endswith(('.jpg','.jpeg','.png','.bmp'))] )
    for image_name in tqdm(image_names):
        img = Image.open( os.path.join(args.in_image_dir, image_name ) )
        parse_img = model.predict(img)
