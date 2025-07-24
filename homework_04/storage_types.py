from abc import abstractmethod
from typing import Self
from file_types import AbstractFileType

class SomeConfig:
    def get(self, key: str) -> str:
        """Mock method to simulate getting a configuration value."""

        # In a real implementation, this would fetch from a config file or environment variable
        config = {
            "default_storage": LocalStorage,
            "s3_bucket": {
                'class': S3Storage,
                'access_key': 'your_access_key',
                'secret_key': 'your_secret_key',
            },
            "ftp_server": {
                'class': FtpStorage,
                'host': 'ftp.example.com',
                'username': 'user',
                'password': 'pass',
            },
            "local_storage": {
                'class': LocalStorage,
                'path': '/path/to/local/storage',
            }
        }
        return config.get(key, "")

class OtusAbstractFileStorage:
    @abstractmethod
    def save(self, path: str, content: str) -> bool:
        """Save a file to the storage."""
        print(f"Saving to {path} with content: {content}")
        pass

    def save_file(self, file: AbstractFileType) -> bool:
        """Save a file object to the storage."""
        return self.save(file.path, file.content)

    @abstractmethod
    def load(self, path: str) -> str:
        """Load a file from the storage."""
        pass

    @abstractmethod
    def delete(self, path: str) -> bool:
        """Delete a file from the storage."""
        pass

    @classmethod
    def get_default_storage(cls) -> Self:
        """Get the default storage type."""
        config = SomeConfig()
        defaultStorage = config.get("default_storage")
        return defaultStorage()

class FtpStorage(OtusAbstractFileStorage):
    def __init__(self, configKey: str = None):
        config = SomeConfig().get(configKey or "ftp_server")
        self.host = config.get("host")
        self.username = config.get("username")
        self.password = config.get("password")

class S3Storage(OtusAbstractFileStorage):
    def __init__(self, configKey: str = None):
        config = SomeConfig().get(configKey or "s3_bucket")
        self.access_key = config.get("access_key")
        self.secret_key = config.get("secret_key")

class LocalStorage(OtusAbstractFileStorage):
    def __init__(self, configKey: str = None):
        config = SomeConfig().get(configKey or "local_storage")
        self.path = config.get("path")

    def save(self, file_name: str, content: str) -> bool:
        super().save(file_name, content)
        # Implement saving logic here
        return True

    def load(self, file_name: str) -> dict:
        # Implement loading logic here
        return {"content": "sample content"}

    def delete(self, file_name: str) -> bool:
        # Implement deletion logic here
        return True

# etc. for other storage types...