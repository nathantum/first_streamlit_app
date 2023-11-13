import streamlit

streamlit.title("My Mom's New Healthy Dinner")

streamlit.header('🍌🥭 ---------Breakfast---------- 🥝🍇')
streamlit.text('          <\> Omega 3 & Blueberry Oatmeal')
streamlit.text('          <\> Kale, Spinach & Rocket Smoothie')
streamlit.text('          <\> Hard-Boiled Free-Range Egg')
streamlit.text('          <\> Ugali Mboga and milk')
streamlit.text('          <\> Chicken with Fried Ice')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list (my_fruit_list.values)) #display the table on the page

streamlit.dataframe (my_fruit_list)
