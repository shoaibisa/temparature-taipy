from taipy import Config
from taipy import Core, Gui
from taipy.gui import Markdown
import taipy as tp
from pages.home import home_md
from pages.temp import temp_page


def build_message(name: str):
    return f"Hello! {name}"


input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task(
    "buil_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario(
    "scenariod", task_configs=[build_msg_task_cfg])

# making GUI

input_name = "M ahi"
message = None


def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit()
    state.message = scenario.message.read()


love = "sazia"
page = """
Name: <|{input_name}|input|>
<|submit|button|on_action=submit_scenario|>
Message: <|{message}|text|>
Kima : <|All world are need to safe|text|>
"""


pages = {
    "/": home_md,
    "temp": temp_page,
}


if __name__ == "__main__":
    Core().run()

#     mange scenarios and data
    scenario = tp.create_scenario(scenario_cfg)

#     instance of run gui
    Gui(pages=pages).run(title="Mahi Template", port=5000,
                         favicon="https://www.youtube.com/s/gaming/emoji/7ff574f2/emoji_u1f602.png", )
