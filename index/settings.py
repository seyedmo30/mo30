
deploy = True
if deploy:
    from .dep_settings import *
else:
    from .dev_settings import *
