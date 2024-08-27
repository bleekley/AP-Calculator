# Wi-Fi Access Point (AP) Calculator

This project is a **Wi-Fi Access Point Calculator** built with **Streamlit**. The calculator helps estimate the number of wireless access points (APs) required for a given environment based on factors such as square footage, number of floors, attenuation levels, and the number of corporate and guest users.

## Features
- **Calculate APs based on coverage and capacity**.
- **Handles different user types**: Corporate users (with a default bandwidth of 11 Mbps per user) and Guest users (with a default bandwidth of 8 Mbps per user).
- **Adjusts for environmental attenuation** with selectable options like Low, Medium, and High.
- **Automatic rounding** of AP count to the nearest whole number.
- **Provides a secondary coverage recommendation** when only one AP is calculated.

## Installation

To get started with this project, you'll need to have **Python** and **Streamlit** installed on your system.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/bleekley/AP-Calculator.git
   
2. **Navigate to the project directory**:

   ```bash
   cd AP-Calculator

4. **Install the required dependencies**:
   ```bash
   pip install streamlit


## Usage
1. **Run the Streamlit app**:

   To launch the calculator, use the following command in your terminal:

   ```bash
   streamlit run ap_calculator.py
   
2. **Interact with the app**:

   Once the app is running you can interact with it in your web browser by entering the following inputs

   - **Total Square Footage per Floor**
   - **Number of Floors**
   - **Attenuation Level (Low, Medium, or High)**
   - **Number of Corporate Users**
   - **Number of Guest Users**

3. **View the results**:

  After clicking the "Calculate APs" button, the app will display the recommended number of Access Points (APs) based on both coverage and capacity.
  
## Example

Here’s an example scenario:

- Total Square Footage per Floor: 9000 sqft
- Number of Floors: 6
- Attenuation Level: Medium
- Number of Corporate Users: 150
- Number of Guest Users: 100

The calculator will estimate the number of access points required based on these parameters.

## Project Structure

   ```bash
   .
   ├── README.md               # Project documentation
   ├── ap_calculator.py        # Streamlit app for AP calculation
   └── .gitignore              # Files to ignore in Git
   ```
## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a Pull Request.




