import time
from datetime import datetime

import flet as ft
import pyotp


def otpnow() -> str:
    totp = pyotp.TOTP("OU2HOYKRKJ4WGQTF")
    return totp.now()


def main(page: ft.Page):
    page.theme_mode = page.theme_mode.LIGHT  # type: ignore
    ft.MainAxisAlignment = ft.MainAxisAlignment.CENTER
    ft.CrossAxisAlignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 700

    # Progress bar
    pr = ft.ProgressRing(width=16, height=16, stroke_width=20)

    def show_snakebar():
        page.snack_bar = ft.SnackBar(
            content=ft.Text("OTP copied to clipboard"),
            duration=2000, )
        page.snack_bar.open = True
        page.update()

    def on_click(e):
        page.set_clipboard(f"{otpnow()}")
        show_snakebar()

    def on_keyboard(e: ft.KeyboardEvent):
        if e.ctrl and e.key == "C":
            on_click(e)

    page.on_keyboard_event = on_keyboard
    text_otp = ft.Text(otpnow(), size=45, text_align=ft.alignment.center)
    ct_content = ft.Row([text_otp, pr])
    ct_content.alignment = ft.MainAxisAlignment.CENTER
    ct = ft.Container(
        content=ct_content,
        ink=True,
        margin=10,
        border_radius=10,
        width=380,
        height=610,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.LIGHT_BLUE_100,
        on_click=on_click,
    )

    page.add(ct)
    page.update()
    while True:
        current_sec = datetime.now().second
        timer = 30 - (current_sec % 30)
        progress = timer / 30.0
        pr.value = progress
        text_otp.value = otpnow()
        time.sleep(1)
        page.update()


ft.app(target=main)
