import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🍛 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')
streamlit.header('Build your own fruit smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 


streamlit.multiselect("Pick some fruits:", List(my_fruit_list.index), ['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)







