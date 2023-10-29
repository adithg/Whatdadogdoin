import reflex as rx
from typing import List

class State(rx.State):
    data: List = [
        ['Admiration', 'Adoration','Aesthetic Appreciation','Amusement','Anger','Anxiety','Awe','Awkwardness', 'Boredom','Calmness','Concentration','Confusion','Contemplation','Contempt','Contentment','Craving', 'Desire','Determination','Disappointment','Disgust','Distress','Doubt','Ecstasy','Embarrassment', 'Empathic Pain','Entrancement','Envy','Excitement','Fear','Guilt','Horror','Interest', 'Joy','Love','Nostalgia','Pain','Pride','Realization','Relief','Romance', 'Sadness','Satisfaction','Shame','Surprise (negative)','Surprise (positive)','Sympathy','Tiredness','Triumph']
    ]
    columns: List[str] = [f'Column {i}' for i in range(1, 50)]

def humetable():
    return rx.data_table(
        data=State.data,
        columns=State.columns,
    )
