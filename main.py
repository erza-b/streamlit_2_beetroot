import streamlit as st

st.title('Hello to our wage app:sunglasses:')

hours = st.number_input('Insert hours')
rates = st.number_input('Insert rate')


def calculate_wage(hour, rate):
    return hour*rate


result = calculate_wage(hours, rates)

st.write('The current number is ', result)
