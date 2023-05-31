import os
import shutil
from datetime import datetime
import sys
import exifread
import argparse


def main():
    parser = argparse.ArgumentParser(description='Move specific camara maker photos from source to destination folder.')
    parser.add_argument('input_dir', type=str, help='Path to the source folder')
    parser.add_argument('output_dir', type=str, help='Path to the destination folder')
    parser.add_argument('--camera_maker', type=str, nargs='*', help='Choose a camera maker such samsung or apple')
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    camera_makers = [maker.lower() for maker in args.camera_maker] if args.camera_maker else []

    def get_date_taken(file_path):
        global camera_maker
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f, stop_tag='EXIF DateTimeOriginal')
            camera_maker = str(tags.get('Image Make', '')).lower() if tags.get('Image Make') is not None else None
            date_taken = tags['EXIF DateTimeOriginal']
            return datetime.strptime(str(date_taken), '%Y:%m'), camera_maker


    def organize(input_dir, extension, output_dir):
        for filename in os.listdir(input_dir):
            if filename.lower().endswith(tuple(extension)):
                file_path = os.path.join(input_dir, filename)

                try:
                    create_time = get_date_taken(file_path)
                    
                except Exception:
                    create_time = datetime.fromtimestamp(os.path.getmtime(file_path))

                year, month = create_time.strftime('%Y-%m').split('-')
                output_path = os.path.join(output_dir, year, f'{year}-{month}')
                os.makedirs(output_path, exist_ok=True)
                
                destination_path = os.path.join(output_path, filename)

                if camera_makers == []:
                    shutil.move(file_path, destination_path)
                elif not os.path.exists(destination_path) and camera_maker in camera_makers:
                    shutil.move(file_path, destination_path)
                else:
                    print(f"A file with the name '{filename}' already exists.")


    def image():
        image_extensions  = [".jpg", ".png", ".gif", ".jpeg", ".svg"]
        organize(input_dir, image_extensions, f'{output_dir}\\photos')


    def video():
        video_extentions = [".mp4", ".avi", ".mov", ".wmv", ".mkv"]
        organize(input_dir, video_extentions, f'{output_dir}\\videos')


    image()
    video()


if __name__ == '__main__':
    main()
