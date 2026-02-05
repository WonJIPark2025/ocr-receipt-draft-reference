from abc import ABC, abstractmethod

class OCREngine(ABC):

    @abstractmethod
    def run(self, image_path: str) -> dict:
        """
        Execute OCR on the given image.
        Must NOT return persisted or validated results.
        """
        raise NotImplementedError
