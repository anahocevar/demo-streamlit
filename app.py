import streamlit as st
import pandas as pd
from vega_datasets import data
import altair as alt
import numpy as np

def app():
    st.title('This is a demo')
    
    st.markdown(""" ## This is some section
    What else:
    * this
    * and this
    
    """)
    
    st.sidebar.markdown('''Here is the sidebar text''')
    
    df_cars = data.cars()
    st.write(df_cars.head())
    
    brush = alt.selection_interval(encodings=['x', 'y'])
    repeat_chart = alt.Chart(df_cars).mark_point().encode(
    alt.X(alt.repeat('column'), type='quantitative'),
    alt.Y('Miles_per_Gallon:Q'),
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray')),
    opacity=alt.condition(brush, alt.value(0.7), alt.value(0.1))
       ).properties(
       width=150,
       height=150
       ).add_selection(
           brush
       ).repeat(
       column=['Weight_in_lbs', 'Acceleration', 'Horsepower']
        )
    
    st.write(repeat_chart)
    
    st.markdown('## User Input Demo')
    
    n = int(st.text_input('How many points do you want:', '50'))
    
    x = np.random.random(n) * 10
    y = np.random.random(n) * 10
    s = np.random.random(n)
    
    df = pd.DataFrame({'x':x, 'y':y, 'size': s})
    
    chart = alt.Chart(df, width=400,
                      height=400).mark_point().encode(
                  x='x',
                  y='y',
                  size=alt.Size('size', legend=None),
                  tooltip=['size']
                  ).interactive()
    
    st.write(chart)
    
if __name__ == '__main__':
    app()