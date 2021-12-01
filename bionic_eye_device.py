import os, os.path
import shutil
import sys

class Device:
    # This class simulate the bionic eye device
    def __init__(self, img_path, src_path, dst_path, delay, address, module):
        self.img_path = img_path
        self.src_path = src_path
        self.dst_path = dst_path
        self.address = address
        self.module = module
        self.processor = Processor()
        self.camera = Camera(img_path, src_path)
        self.network = Network(self.src_path, self.dst_path, delay = 0.0)
    
    def take_imgs(self):
        # Take imgs and store them in the src_folder
        self.camera.take_imgs()
    
    def send_imgs(self):
        # Send imgs in the src_folder over the network to server
        self.network.send()

    def load_info(self):
        # Write address and module into client_info.txt in the src_folder
        f = open('src_folder/client_info.txt', 'w')
        f.write(self.address + '\n')
        f.write(self.module + '\n')
        f.close()
    
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
    repo_path = sys.argv[1]
    img_path = repo_path + '/img_folder'
    src_path = repo_path + '/src_folder'
    res_path = repo_path + '/res_folder'
    dst_path_remote = 'Bionic_Eye_IoT_Server:Input'

    cmd = 'mkdir ' + src_path + ' ; ' + 'mkdir ' + res_path
    os.system(cmd)

    client_address = sys.argv[2]
    module_selected = sys.argv[3]
    
    device = Device(img_path, src_path, dst_path_remote,
                    0.0, client_address, module_selected)
    device.load_info()
    device.take_imgs()
    device.send_imgs()



    