# IoT_Binoc_Eye
## Server code and Modules
https://drive.google.com/drive/u/1/folders/0ADVj7Fiq9xH7Uk9PVA

## Cloud drive share folder
https://drive.google.com/drive/u/1/folders/0AEuOsGn9NllPUk9PVA

## How to run
To run the client code, make sure you update the path to project folder, your ssh remote login address and your slection of module in the 'run_client' script. To use Rclone, please first get access to the two shared drive above, then you will need to download and configure the tool to connect your local machine to the shared drive. Detail totorials can be found at https://rclone.org/install/.

Sample images can be found in the sample_images folder. Move the images you would like to run to the img_folder before running the client code.

Then simple run

```
./run_client
```

To run the server, find the server script 'server.ipynb' in the Bionic_Eye_IoT_Script folder and execute the script from the beginning.
