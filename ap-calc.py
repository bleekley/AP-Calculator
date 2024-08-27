import streamlit as st
import math

# Define the function to calculate APs
def calculate_aps(total_area, floors, attenuation, corp_users, guest_users):
    # Define bandwidth requirements
    corp_bandwidth_per_user = 11  # Corporate user bandwidth (Mbps)
    guest_bandwidth_per_user = 8   # Guest user bandwidth (Mbps)
    
    # Define coverage range based on attenuation
    if attenuation == "Low":
        coverage_range = 2500
    elif attenuation == "Medium":
        coverage_range = 2000
    else:
        coverage_range = 1500
    
    # Calculate APs for coverage
    coverage_ap_count = (total_area * floors) / coverage_range

    # Calculate total bandwidth demand
    total_bandwidth = (corp_users * corp_bandwidth_per_user) + (guest_users * guest_bandwidth_per_user)

    # Assume each AP can handle 100 Mbps of effective throughput
    capacity_ap_count = total_bandwidth / 100

    # Return the higher of the two AP counts, rounded up to the nearest whole number
    return math.ceil(max(coverage_ap_count, capacity_ap_count))

# Streamlit app interface
st.title('Wi-Fi Access Point Calculator')

# Inputs
total_area = st.number_input("Total Square Footage per Floor", value=9000)
floors = st.number_input("Number of Floors", value=6)
attenuation = st.selectbox("Attenuation Level", ["Low", "Medium", "High"], index=1)
corp_users = st.number_input("Number of Corporate Users", value=150)
guest_users = st.number_input("Number of Guest Users", value=100)

# Button to trigger calculation
if st.button('Calculate APs'):
    # Perform calculation
    total_ap_count = calculate_aps(total_area, floors, attenuation, corp_users, guest_users)
    
    # Output result
    st.write(f"Total Recommended AP Count: {total_ap_count}")

    # Provide a note if the AP count is below 2
    if total_ap_count < 2:
        st.write("The tool has calculated only one access point, but we should always design for secondary coverage as a best practice.")
