from taipy.gui import Gui, Markdown
name = "maho"
...
page = """
 ...
 <|{dialog_is_visible}|dialog|
 Enter a name:

 <|{name}|input|>
 |>
 ...
 """
...
pages = {
  "/" : page,
  'page1': Markdown("# My first page"),
  'page2': Markdown("# My second page")
}



Gui(pages=pages).run(title="Mahi App",port=5001 )