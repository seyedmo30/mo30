from pathlib import Path
from django.conf import settings
Path(str(settings.MEDIA_ROOT) + "img/albums/webp/").mkdir(parents=True, exist_ok=True)

