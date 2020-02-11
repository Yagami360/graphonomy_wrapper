#!/bin/sh
set -eu

python test.py \
    --in_image_dir sample_n5 \
    --results_dir results \
    --load_checkpoints_path Graphonomy/model/0/model.pth \
    --debug
