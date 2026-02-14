import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventory Management System", layout="centered")

st.title("Inventory Management System")

# =====================================================
# Initialize inventory
# =====================================================
if "inventory" not in st.session_state:
    st.session_state.inventory = pd.DataFrame(
        columns=["Item ID", "Item Name", "Category", "Quantity", "Price"]
    )

# =====================================================
# Sidebar
# =====================================================
menu = st.sidebar.selectbox(
    "Menu",
    ["Add Item", "View Inventory", "Update Quantity", "Delete Item"]
)

# =====================================================
# ADD ITEM
# =====================================================
if menu == "Add Item":
    st.header("Add New Item")

    item_id = st.text_input("Item ID")
    item_name = st.text_input("Item Name")
    category = st.text_input("Category")
    quantity = st.number_input("Quantity", min_value=0)
    price = st.number_input("Price", min_value=0.0)

    if st.button("Add Item"):
        new_item = {
            "Item ID": item_id,
            "Item Name": item_name,
            "Category": category,
            "Quantity": quantity,
            "Price": price
        }

        st.session_state.inventory = pd.concat(
            [st.session_state.inventory, pd.DataFrame([new_item])],
            ignore_index=True
        )

        st.success("Item added successfully!")

# =====================================================
# VIEW
# =====================================================
elif menu == "View Inventory":
    st.header("Inventory List")

    if st.session_state.inventory.empty:
        st.warning("Inventory is empty")
    else:
        st.dataframe(st.session_state.inventory)

# =====================================================
# UPDATE
# =====================================================
elif menu == "Update Quantity":
    st.header("Update Item Quantity")

    item_id = st.text_input("Enter Item ID")
    new_quantity = st.number_input("New Quantity", min_value=0)

    if st.button("Update Quantity"):
        if item_id in st.session_state.inventory["Item ID"].values:
            st.session_state.inventory.loc[
                st.session_state.inventory["Item ID"] == item_id, "Quantity"
            ] = new_quantity
            st.success("Quantity updated successfully!")
        else:
            st.error("Item ID not found")

# =====================================================
# DELETE
# =====================================================
elif menu == "Delete Item":
    st.header("Delete Item")

    item_id = st.text_input("Enter Item ID to delete")

    if st.button("Delete Item"):
        if item_id in st.session_state.inventory["Item ID"].values:
            st.session_state.inventory = st.session_state.inventory[
                st.session_state.inventory["Item ID"] != item_id
            ]
            st.success("Item deleted successfully!")
        else:
            st.error("Item ID not found")
