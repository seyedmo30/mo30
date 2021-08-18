from pathlib import Path
from django.conf import settings
from .procedure import AvgMusic
Path(str(settings.MEDIA_ROOT) + "img/albums/webp/").mkdir(parents=True, exist_ok=True)
AvgMusic().createProcedure()

