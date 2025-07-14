from file_types import Video, Image, Text, Audio
from storage_types import OtusAbstractFileStorage, FtpStorage, S3Storage, LocalStorage

videoFile = Video()
videoFile.name = "sample_video.mp4"
videoFile.path = "/path/to/video"
videoFile.storage = OtusAbstractFileStorage.get_default_storage()
print(f"\n{videoFile.__dict__}")
videoFile.save()

imageFile = Image()
imageFile.name = "sample_image.jpg"
imageFile.path = "/path/to/image"
imageFile.content = "This is a sample image content."
imageFile.storage = OtusAbstractFileStorage.get_default_storage()
print(f"\n{imageFile.__dict__}")
imageFile.save()

imageFile = Text()
imageFile.name = "text.txt"
imageFile.path = "/path/to/text"
imageFile.content = "This is a sample text content."
imageFile.storage = S3Storage()
print(f"\n{imageFile.__dict__}")
imageFile.save()

