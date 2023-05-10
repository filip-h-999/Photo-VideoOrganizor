import os
import shutil
from datetime import datetime
import exifread


input_dir = r'pass in your director'


def get_date_taken(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f, stop_tag='EXIF DateTimeOriginal')
        date_taken = tags['EXIF DateTimeOriginal']
        return datetime.strptime(str(date_taken), '%Y:%m')
    

def organize(input_dir, extension, output_dir):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(tuple(extension)):
            file_path = os.path.join(input_dir, filename)

            try:
                create_time = get_date_taken(file_path)
                
            except Exception:
                create_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                year, month = create_time.strftime('%Y-%m').split('-')
                output_path = os.path.join(output_dir, year, month)
                os.makedirs(output_path, exist_ok=True)

            shutil.move(file_path, os.path.join(output_path, filename))


def image():
    output_dir = f'{input_dir}\\photos'

    image_extensions  = [".jpg", ".png", ".gif", ".jpeg", ".svg"]
    organize(input_dir, image_extensions, output_dir)


def video():
    output_dir = f'{input_dir}\\videos'

    video_extentions = [".mp4", ".avi", ".mov", ".wmv", ".mkv"]
    organize(input_dir, video_extentions, output_dir)


image()
video()