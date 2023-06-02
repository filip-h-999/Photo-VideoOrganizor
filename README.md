# Image and Video Organizor

The Image and Video Organizor is a Python script that helps you organize your photos and videos by sorting them into subdirectories based on their creation dates. The script takes an input directory containing image and video files and moves them to an output directory, organizing them by year and month.

![image](https://user-images.githubusercontent.com/93609912/236556817-d74d8100-38c2-4cb0-9036-4a085e6639f9.png)

![image](https://user-images.githubusercontent.com/93609912/236556846-9b56c2c4-d991-4278-936e-19108fc69104.png)

![image](https://user-images.githubusercontent.com/93609912/236557730-407f96a4-1b02-4531-bdef-fee4c2e5962c.png)

![image](https://user-images.githubusercontent.com/93609912/236556896-cba4c935-6336-4c90-85ea-e6f1227a1712.png)

#### Example:

For sorting all camera typs use the following command:
> python Photo-VideoOrganizor.py C:\Users\Downloads\test C:\Users\Downloads\test

For sorting specific camera maker pictures and videos use the following command:
> python Photo-VideoOrganizor.py C:\Users\Downloads\test C:\Users\Downloads\test --camera_maker samsung

You can also use multiple camera maker:  
> --camera_maker samsung apple

Arguments:

1. argument is the intup directory
2. argument is the output directory
3. argument is the camera maker