import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def app():
    st.title('This is a demo')

    st.markdown("""I will show you a couple of things!""")
    st.markdown("""
    * thing 1
    * thing 2""")
    
    st.sidebar.markdown("This is a sidebar!")
    
    N = int(st.text_input("How many points?", '5'))
    
    fig, ax = plt.subplots()
    x = np.random.random(N)*10
    y = np.random.random(N)*10
    plt.scatter(x, y, s=20)

    st.pyplot(fig)
    
    df = pd.DataFrame({'a':[2,3,4], 'b': [3,1,5]})
    st.write(df)
    
if __name__ == '__main__':
    app()