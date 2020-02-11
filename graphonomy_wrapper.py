# -*- coding:utf-8 -*-
import os
import sys
import numpy as np
from PIL import Image

sys.path.append(os.path.join(os.getcwd(), 'Graphonomy'))
from networks import deeplab_xception_transfer, graph       # Graphonomy のネットワーク
from utils import save_checkpoint, load_checkpoint

class GraphonomyWrapper(object):
    """
    Graphonomy のラッパークラス
    """
    def __init__(self, load_checkpoints_path ):
        self.load_checkpoints_path = load_checkpoints_path
        self.model = None
        self.load_checkpoint()
        return

    def load_checkpoints(self):
        self.model = deeplab_xception_transfer.deeplab_xception_transfer_projection_savemem(
            n_classes=20,
            hidden_layers=128,
            source_classes=7, 
        )

        if not self.load_checkpoints_path == '' and os.path.exists(self.load_checkpoints_path):
            load_checkpoint( model_gmm, device, args.load_checkpoints_path )
        return

    def predict(self):
        """
        Graphonomy の推論を実行する。
        """
        return
