# Bank Management System

## Overview

This project is a simple Bank Management System implemented in Python using the `tkinter` library for the graphical user interface (GUI). The system allows users to create and manage bank accounts, perform transactions (deposit and withdraw), view transaction logs, and manage accounts as a teller.

## Features

- **Account Management**:
  - Create new bank accounts.
  - Edit existing account details (name, password, phone number, location).
  - Delete accounts.
  - Search for accounts by account number or holder name.
  - Display all accounts.

- **Transactions**:
  - Deposit money into an account.
  - Withdraw money from an account.
  - View transaction logs for an account.

- **Teller Functionality**:
  - Teller login with admin credentials.
  - Add or remove money from any account.
  - View and manage all accounts.

## Requirements

- Python 3.x
- `tkinter` library (usually comes pre-installed with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/omaradel73/bank-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd bank-management-system
   ```
3. Run the Python script:
   ```bash
   python Bank_Management_System.py
   ```

## Usage

1. **Login**:
   - Use the default teller login credentials:
     - **Username**: `admin`
     - **Password**: `admin`
   - Or login as a regular account holder using the account holder name and password.

2. **Teller Menu**:
   - **Create Account**: Create a new bank account.
   - **Edit Account**: Edit details of an existing account.
   - **Add Money**: Add money to any account.
   - **Remove Money**: Remove money from any account.
   - **View Account Logs**: View transaction logs of any account.
   - **Delete Account**: Delete an existing account.
   - **Display All Accounts**: Display details of all accounts.
   - **Search Account**: Search for an account by account number or holder name.

3. **Account Holder Menu**:
   - **Deposit Money**: Deposit money into your account.
   - **Withdraw Money**: Withdraw money from your account.
   - **View Transaction Logs**: View your transaction history.
   - **Logout**: Log out of your account.

## Code Structure

- **Account Class**: Represents a bank account with attributes like account number, holder name, password, location, phone number, balance, and transaction logs. It also includes methods for depositing and withdrawing money.

- **Bank Class**: Manages a collection of accounts. It includes methods for creating, deleting, and retrieving accounts, as well as displaying all accounts.

- **BankUI Class**: Handles the GUI and user interactions. It includes methods for logging in, displaying menus, and processing user inputs.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was created as a simple example of a bank management system using Python and `tkinter`.

---

Feel free to customize this README file to better fit your project and add any additional information you think is necessary.
