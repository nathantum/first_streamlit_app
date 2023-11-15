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
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('🍌🥭 ---------Build your own Smoothie---------- 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), ['Avocado', 'Strawberries']) #display the table on the page

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe (fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
import requests 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruity_normalized)


