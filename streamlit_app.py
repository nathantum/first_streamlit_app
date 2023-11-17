import streamlit
import requests 
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom's New Healthy Dinner")

streamlit.header('🍌🥭 ---------Breakfast---------- 🥝🍇')
streamlit.text('          <\> Omega 3 & Blueberry Oatmeal')
streamlit.text('          <\> Kale, Spinach & Rocket Smoothie')
streamlit.text('          <\> Hard-Boiled Free-Range Egg')
streamlit.text('          <\> Ugali Mboga and milk')
streamlit.text('          <\> Chicken with Fried Ice')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('🍌🥭 ---------Build your own Smoothie---------- 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), ['Avocado', 'Strawberries']) #display the table on the page

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

# allow the user to add fruits
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add ?')

if streamlit.button('Add a Fruit to the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_fro,_function)

# add button to load data
if streamlit.button("Get Fruit Load List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

# fruits_to_show = my_fruit_list.loc[fruits_selected]
# streamlit.dataframe (fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header('Fruityvice Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like infprmation about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()
    






# let the user choose the fruit 
# get user input
# fruit_choice = streamlit.text_input('What fruit would you like infprmation about?', 'Kiwi')

# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# streamlit.text(fruityvice_response.json())

# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains: ")
streamlit.dataframe(my_data_row)

second_fruit_choice = streamlit.text_input("What fruit would you like to add?")
streamlit.write("Thanks for adding " + second_fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
