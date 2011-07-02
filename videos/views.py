from videos import models

def get_videos():
    return models.Video.fallback.filter(published=True)

