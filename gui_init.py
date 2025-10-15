import webview
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
html_path = os.path.join(BASE_DIR,"UI", "layout.html")

class Bridge:
    def close(self):
        webview.windows[0].destroy()
    def restore(self):
        webview.windows[0].resize(700,500)
    def maximize(self):
        webview.windows[0].maximize()
    def minimize(self):
        webview.windows[0].minimize()
        
bridge=Bridge()

webview.create_window('C-arc', f"file://{html_path}", frameless=True, width=700, height=500 ,resizable=True, js_api=bridge)

webview.start()