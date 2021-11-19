import os, os.path
import shutil
import sys

class Device:
    # Thhihs class simulate the bionic eye device
    def __init__(self, img_path, src_path, dst_path, delay):
        self.img_path = img_path
        self.src_path = src_path
        self.dst_path = dst_path
        self.processor = Processor()
        self.camera = Camera(img_path, src_path)
        self.network = Network(self.src_path, self.dst_path, delay = 0.0)
    
    def take_imgs(self):
        self.camera.take_imgs()
    
    def send_imgs(self):
        self.network.send()
    
class Processor:
    # This class simulate the processing
    def __init__(self):
        return

class Camera:
    # This class simulate the camera that takes photos
    # Phase 1: read image from a destination

    def __init__(self, img_path, src_path):
        self.img_path = img_path
        self.src_path = src_path
        
    def take_imgs(self):
        # move images from img_path to src_path
        valid_ext = ['.jpeg', '.jpg','.gif','.png','.tga']
        for f in os.listdir(img_path):
            ext = os.path.splitext(f)[1]
            if ext.lower() not in valid_ext:
                continue
            shutil.copy(img_path + '/' + f, src_path)

class Network:
    cmd = 'rclone copy'
    flags = ''

    # This class simulate the network with linux util rsync
    def __init__(self, src_path, dst_path, delay = 0.0):
        self.src_path = src_path
        self.dst_path = dst_path
        self.delay = delay
        
    # Send all imgs from src_path to dst_path
    def send(self):
        exe_cmd = self.cmd + ' ' + self.flags + ' ' + self.src_path + ' ' + \
                  self.dst_path
        print(exe_cmd)
        os.system(exe_cmd)
    
    # Recv imgs in dst_path
    def recv(self):
        return 'STUB'

if __name__ == '__main__':
    img_path = '/Users/zihaozhang/Desktop/IoT_Binoc_Eye/img_folder'
    src_path = '/Users/zihaozhang/Desktop/IoT_Binoc_Eye/src_folder'
    dst_path_remote = 'Bionic_Eye_IoT_Server:'
    # dst_path_remote = sys.argv[1]
    # print(dst_path_remote)
    
    device = Device(img_path, src_path, dst_path_remote, 0.0)
    device.take_imgs()
    device.send_imgs()



    