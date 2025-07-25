from PyQt6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc
from PyQt6.QtGui import QSurfaceFormat, QOpenGLContext, QOffscreenSurface

from common import resource_path
from common.render import RenderWidget
import re


VERSION = "x.x.x"
version_pattern = re.compile(r'\[(\d+\.\d+\.\d+)\]')
with open(resource_path("CHANGELOG.md", None)) as f:
    for line in f:
        match = version_pattern.search(line)
        if match:
            VERSION = match.group(1)


try:
    import pyi_splash
    pyi_splash.update_text("Done extracting, starting program...")
except:
    pass  # This is only used when compiling to .exe


class Redliner(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(f"Redliner v{VERSION}")
        self.resize(800, 600)
        self.setWindowIcon(qtg.QIcon(resource_path('icon.png')))

        r = RenderWidget()

        self.setCentralWidget(r)
        self.setAcceptDrops(True)
        self.show()

if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)

    _redliner = Redliner()
    try:
        pyi_splash.close()
    except:
        pass
    app.exec()