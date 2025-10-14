import webview
from pathlib import Path

def initialize(window):
    window.maximize()

window =webview.create_window('C-arc', frameless=True)
webview.start(initialize, window)