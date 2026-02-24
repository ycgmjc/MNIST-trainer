import os
import gzip


train_img_dir = "./dataset/train-images.idx3-ubyte"
train_label_dir = "./dataset/train-labels.idx1-ubyte"
val_img_dir = "./dataset/t10k-images.idx3-ubyte"
val_label_dir = "./dataset/t10k-labels.idx1-ubyte"

def local_dataset_exists():
    counter = 0
    result = False
    counter += os.path.exists(train_img_dir)
    counter += os.path.exists(train_label_dir)
    counter += os.path.exists(val_img_dir)
    counter += os.path.exists(val_label_dir)
    
    if(counter == 4) :
        result = True
        
    return result


if(local_dataset_exists()):
    print("Dataset exists!")
else:
    print("[Error] Missing datasets")