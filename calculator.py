import streamlit as st

#this will create an app with a title calculator
st.title("calculator :computer:")

#input 1
num1 = st.number_input(label="Enter the first number:",step=1, value=0)
#input 2
num2 = st.number_input(label="Enter second number:",step=1, value=0)


#add
operation=st.radio("Select an operation to perform",
            ( ":heavy_plus_sign:",
            ":heavy_minus_sign:",
            ":heavy_multiplication_x:",
            ":heavy_division_sign:"))

def calculate(num1,num2,operation):
    if operation== ":heavy_plus_sign:":
       total=num1+num2
    elif operation== ":heavy_minus_sign:":
       total=num1-num2
    elif operation== ":heavy_multiplication_x:":
       total=num1*num2
    elif operation== ":heavy_division_sign:" and num2 != 0:
       total=num1/num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        total = "Not defined"

    if operation == ":heavy_division_sign:" and num2 == 0:
        pass
    else:
        st.success(f"The total is {total}")


if st.button("Calculate", help= f"Click here to {operation} two numbers"):
    calculate(num1, num2, operation)









#for f in operation_option:
    #if operation_option == f:
       # st.write(f"num1{f}num2")