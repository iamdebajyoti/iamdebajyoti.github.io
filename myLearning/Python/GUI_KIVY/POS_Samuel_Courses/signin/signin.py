from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        login_msg = self.ids.login_info

        u_name = user.text
        passw = pwd.text

        if u_name == "" or passw == "":
            # print("Username and/or Password is missing !!!")
            login_msg.text = "[color=#FF0000]Username and/or Password is missing !!![/color]"
        elif u_name == "admin" and passw == "admin":
            # print("Login successful")
            login_msg.text = "[color=#00FF00]Login successful[/color]"
        else:
            # print("Invalid Username and/or Password !!!")
            login_msg.text = "[color=#FF0000]Invalid Username and/or Password !!![/color]"
            



class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()
