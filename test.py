import flet as ft
from datetime import datetime
import time

def main(page: ft.Page):
    def update_otps_and_timers():
        current_sec = datetime.now().second
        countdown = 30 - (current_sec % 30)
        progress = countdown / 30.0
        return progress
    
    
    pr = ft.ProgressRing(width=16, height=16, stroke_width = 20)
    countdown = ft.Text()
    page.add(
        ft.Row([pr, countdown]),
    )
    while True:
        pr.value = update_otps_and_timers()/2        
        time.sleep(1)
        
        current_sec = datetime.now().second
        timer = 30 - (current_sec % 30)
        countdown.value = str(timer)
        page.update()


        



ft.app(target=main)
