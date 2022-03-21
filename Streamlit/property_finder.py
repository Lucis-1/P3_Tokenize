# Cryptocurrency Wallet

################################################################################
# This code will assume the perspective of a Property Finder to lease
# customer in order to do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase
# (which you created earlier in the module).

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total value of an Ethereum transaction, including the gas
# estimate, that pays a property owner for leasing their place.

# * Digitally sign a transaction that pays a property owner, and send
# this transaction to the Ganache blockchain.

# * Review the transaction hash code associated with the validated blockchain transaction.


################################################################################
# Imports
from sqlite3 import DateFromTicks
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
from datetime import datetime, date, time
################################################################################
# Step 1:
# Import Ethereum Transaction Functions into the Property Finder Application

################################################################################
# Step 1 - Part 3:
# Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# @TODO:
# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
# YOUR CODE HERE
from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# Property Finder Information
st.session_state.booked_dates = []

# Database of Property Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
property_database = {
    "Property1": ["Property1", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4 Bed, 2 Bath", .40, "Images/Property1.jpeg", "Images/Map1.jpeg"],
    "Property2": ["Property2", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "3 Bed, 2 Bath", .33, "Images/Property2.jpeg", "Images/Map2.jpeg"],
    "Property3": ["Property3", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "2 Bed, 1 Bath", .20, "Images/Property3.jpeg", "Images/Map3.jpeg"],
    "Property4": ["Property4", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "1 Bed, 1 Bath", .15, "Images/Property4.jpeg", "Images/Map4.jpeg"]

} #Change image

# A list of the properties
properties = ["Property1", "Property2", "Property3", "Property4"]


def get_properties():
    """Display the database of Property information."""
    db_list = list(property_database.values())

    for number in range(len(properties)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("Property Specifications: ", db_list[number][2])
        st.write("Daily Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Property Finder!")
st.markdown("## Rent a Property!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Property Finder
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# @TODO
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
# YOUR CODE HERE
st.sidebar.write("Ethereum Account:", get_balance(w3, account.address))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################

# Cache the contract on load
@st.cache(allow_output_mutation=True)

# Define the load_contract function
def load_contract():

    # Load Art Gallery ABI
    with open(Path('./contracts/compiled/certificate_abi.json')) as f:
        certificate_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=certificate_abi
    )
    # Return the contract from the function
    return contract

# Load the contract
contract = load_contract()

###############################

# Create a select box to choose a Property Hire
property = st.sidebar.selectbox('Select a Property', properties)

# Create a select box to choose date of stay
Book = 'Date of Booking'
datesMemory = st.sidebar.date_input(label=Book)

# Create a input field to record the number of days the candidate worked
days = st.sidebar.number_input("Number of Days", step=1)

st.sidebar.markdown("## Property Location, Rate, and Ethereum Address")

# Identify the property
candidate = property_database[property][0]

# Write the property's name to the sidebar
st.sidebar.write(candidate)

# Identify the property's hourly rate
daily_rate = property_database[property][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(daily_rate)

# Identify the property's Ethereum Address
property_wallet_address = property_database[property][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(property_wallet_address)

# Write the property's name to the sidebar
st.sidebar.markdown("## Total cost to lease in Ether")

################################################################################
# Step 2: Sign and Execute a Payment Transaction

# @TODO
# Calculate total `wage` for the property by multiplying the property's hourly
# rate from the properties database (`property_database[property][3]`) by the
# value of the `days` variable
# YOUR CODE HERE
wage =property_database[property][3] * days

# @TODO
# Write the `wage` calculation to the Streamlit sidebar
# YOUR CODE HERE
st.sidebar.write("Total cost for days booked:",wage)

##########################################
# Step 2 - Part 2:



if st.sidebar.button("Send Transaction"):
    st.sidebar.write("#### Date already taken!")   
    st.sidebar.write(datesMemory)
    st.sidebar.write(type(str(datesMemory)))


    # If loop for dates
    if datesMemory in st.session_state.booked_dates:
        st.warning(f'The date "{datesMemory}" is already booked!')
    else:
        st.session_state.booked_dates.append(datesMemory)

    # @TODO
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `property_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    # YOUR CODE HERE
    transaction_hash = send_transaction(w3, account=account,to=property_wallet_address,wage=wage)
    
    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    #st.balloons()

# The function that starts the Streamlit application
# Writes property locations to the Streamlit page
get_properties()

################################################################################