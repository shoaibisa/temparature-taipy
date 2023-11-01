
from taipy.gui import Gui, Markdown

input_pid = None
navigation = [("/add_product", "Add Prodcut"), "/", "Home"]
page = """
# Admin Panel
## Add Product

def submit_button(state):
    state.

<|{input_pid}|input|>
<|submit|button|on_action = submit_button>
"""


page1 = """
 ii 
"""

Gui(page=page+page1).run(title="Go To Mall | Admin Panel", port=4000)
