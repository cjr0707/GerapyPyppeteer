import logging

# pyppeteer logging level
GERAPY_PYPPETEER_LOGGING_LEVEL = logging.WARNING

# pyppeteer timeout
GERAPY_PYPPETEER_DOWNLOAD_TIMEOUT = 30

# pyppeteer browser window
GERAPY_PYPPETEER_WINDOW_WIDTH = 1400
GERAPY_PYPPETEER_WINDOW_HEIGHT = 700

# pyppeteer settings
GERAPY_PYPPETEER_HEADLESS = True
GERAPY_PYPPETEER_EXECUTABLE_PATH = None
GERAPY_PYPPETEER_IGNORE_HTTPS_ERRORS = False
GERAPY_PYPPETEER_SLOW_MO = None
GERAPY_PYPPETEER_IGNORE_DEFAULT_ARGS = False
GERAPY_PYPPETEER_HANDLE_SIGINT = True
GERAPY_PYPPETEER_HANDLE_SIGTERM = True
GERAPY_PYPPETEER_HANDLE_SIGHUP = True
GERAPY_PYPPETEER_DUMPIO = False
GERAPY_PYPPETEER_DEVTOOLS = False
GERAPY_PYPPETEER_AUTO_CLOSE = True
GERAPY_PYPPETEER_PRETEND = True
# pyppeteer args
GERAPY_PYPPETEER_DISABLE_EXTENSIONS = True
GERAPY_PYPPETEER_HIDE_SCROLLBARS = True
GERAPY_PYPPETEER_MUTE_AUDIO = True
GERAPY_PYPPETEER_NO_SANDBOX = True
GERAPY_PYPPETEER_DISABLE_SETUID_SANDBOX = True
GERAPY_PYPPETEER_DISABLE_GPU = True

# ignore resource types, ResourceType will be one of the following: ``document``,
# ``stylesheet``, ``image``, ``media``, ``font``, ``script``,
#  ``texttrack``, ``xhr``, ``fetch``, ``eventsource``, ``websocket``,
#  ``manifest``, ``other``.
GERAPY_PYPPETEER_IGNORE_RESOURCE_TYPES = []
GERAPY_PYPPETEER_SCREENSHOT = None
GERAPY_PYPPETEER_SLEEP = 1
GERAPY_ENABLE_REQUEST_INTERCEPTION = True


