import os, os.path
import shutil

class Device:
    # Thhihs class simulate the bionic eye device
    def __init__(self, img_path, src_path, dst_path, delay):
        self.processor = Processor()
        self.camera = Camera(img_path, src_path)
        self.network = Network(delay)
    
    def take_imgs(self):
        self.camera.take_imgs()
    
    def send_imgs(self):
        self.network.send(src_path, dst_path)
    
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
    cmd = 'rsync'
    flags = ''

    # This class simulate the network with linux util rsync
    def __init__(self, delay = 0.0):
        self.delay = delay
        
    # Send all imgs from src_path to dst_path
    def send(self, src_path, dst_path):
        os.system(cmd + flags + src_path + dst_path)
    
    # Recv imgs from dst_path and store at src_path
    def recv(self):
        return 'STUB'

if __name__ == '__main__':
    img_path = './img_folder'
    src_path = './src_folder'
    dst_path = './dst_folder'
    device = Device(img_path, src_path, dst_path, 0.0)
    
    device.take_imgs()
    # device.send_imgs()



    