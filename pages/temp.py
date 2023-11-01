from taipy.gui import Gui, Markdown


def fahren_to_celcius(fahr):
    return (fahr-32)*5/9


fahr = 100
celcious = fahren_to_celcius(fahr)

temp_page = Markdown("""

# **Home**
Fahrenheit : <|{fahr}|>
                
Converted Celcius : <|{celcious}|>

""")
