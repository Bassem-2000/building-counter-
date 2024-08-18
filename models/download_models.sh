#!/bin/bash

wget https://huggingface.co/flkennedy/YOLOv8s-building-segmentation-demo/resolve/main/best.pt -O ./models/flkennedy.pt

wget https://huggingface.co/Bruno64/YOLOv8-building-detect/resolve/main/YOLOv8_20240124_bruno.pt -O ./models/Bruno64.pt

wget https://huggingface.co/odil111/yolov8m-seg-fine-tuned-on-spacenetv2/resolve/main/yolov8m_inst_seg_2024-06-11--15-57-15/weights/best.pt -O ./models/odil111.pt

wget https://huggingface.co/keremberke/yolov8n-building-segmentation/resolve/main/best.pt -O ./models/keremberke-n.pt

wget https://huggingface.co/keremberke/yolov8s-building-segmentation/resolve/main/best.pt -O ./models/keremberke-s.pt

wget https://huggingface.co/keremberke/yolov8m-building-segmentation/resolve/main/best.pt -O ./models/keremberke-m.pt