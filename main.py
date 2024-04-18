import flet as ft
import pyotp


def otpnow() -> str:
    totp = pyotp.TOTP("OU2HOYKRKJ4WGQTF")
    return totp.now()  # => '492039'


def main(page: ft.Page):
    page.theme_mode = page.theme_mode.LIGHT # type: ignore
    ft.MainAxisAlignment = "CENTER"
    page.window_width = 400
    page.window_height = 700
    
    def show_snakebar():
        page.snack_bar = ft.SnackBar(
            content=ft.Text("OTP copied to clipboard"),
            duration=2000,)
        page.snack_bar.open = True
        page.update()
    
    
    def on_click(e):
        page.set_clipboard(f"{otpnow()}")
        show_snakebar()
        
        
    def on_keyboard(e: ft.KeyboardEvent):
        if e.ctrl and e.key == "C":
            on_click()
            print("ctrl C")

    page.on_keyboard_event = on_keyboard

    ct = (
        ft.Container(
            content=ft.Text(f"{otpnow()}", size=45),
            ink=True,
            margin=10,
            border_radius=10,
            width=380,
            height=610,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.LIGHT_BLUE_100,
            on_click=on_click,
            # on_long_press=remove_instance
        )
    )
    page.add(ct)

    page.update()


ft.app(target=main)
