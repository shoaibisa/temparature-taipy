from taipy.gui import Markdown, Gui


text = "Welcome to home page"
mahi_text = "So how are you"

home_md = Markdown("""
# **Home**
 <|{text}|> <br/>
                   <|{mahi_text}|>

""")
