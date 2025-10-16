import webview
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
html_path = os.path.join(BASE_DIR,"UI", "layout.html")

class Bridge:
    pass

        
bridge=Bridge()

webview.create_window('C-arc', f"file://{html_path}", width=700, height=500 ,resizable=True, js_api=bridge)

webview.start()