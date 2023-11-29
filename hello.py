
import numpy as np
import streamlit as st
import pandas as pd


st.header('ini contoh header')

st.title('ini contoh titlle')

st.write(
    """
    # My first app
    ## Ini teks kedua saya
    Hello, para calon praktisi data masa depan!
    """
)

st.caption('Copyright (c) 2023')
 
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

 
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

 
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)
