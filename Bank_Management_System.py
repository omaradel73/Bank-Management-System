import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, account_number, holder_name, password, location, phone_number, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.password = password
        self.location = location
        self.phone_number = phone_number
        self.balance = balance
        self.transaction_logs = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_logs.append(f"Deposited: ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_logs.append(f"Withdrew: ${amount}")
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name, password, location, phone_number, balance=0):
        if holder_name in [account.holder_name for account in self.accounts.values()]:
            return False  # Reject if name already exists
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, holder_name, password, location, phone_number, balance)
            return True
        return False

    def get_account_by_name(self, holder_name):
        for account in self.accounts.values():
            if account.holder_name == holder_name:
                return account
        return None

    def get_account_by_number(self, account_number):
        return self.accounts.get(account_number)

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return True
        return False

    def display_accounts(self):
        return [f"Account Number: {account.account_number}, Name: {account.holder_name}, Balance: {account.balance}" for account in self.accounts.values()]

class BankUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System")
        self.root.geometry("600x500")  # Set window size
        self.bank = Bank()
        self.logged_in_account = None
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        self.label_title = tk.Label(self.root, text="Welcome to Fleeca Bank", font=("Helvetica", 18, "bold"))
        self.label_title.pack(pady=10)
        tk.Label(self.root, text="Account Holder Name:").pack(pady=5)
        self.entry_holder_name = tk.Entry(self.root)
        self.entry_holder_name.pack(pady=5)
        tk.Label(self.root, text="Password:").pack(pady=5)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)
        self.button_login = tk.Button(self.root, text="Login", command=self.check_login)
        self.button_login.pack(pady=10)

    def check_login(self):
        holder_name = self.entry_holder_name.get()
        password = self.entry_password.get()
        if holder_name == 'admin' and password == 'admin':
            self.logged_in_account = 'teller'
            messagebox.showinfo("Success", "Teller login successful!")
            self.show_teller_menu()
        else:
            account = self.bank.get_account_by_name(holder_name)
            if account and account.password == password:
                self.logged_in_account = account
                messagebox.showinfo("Success", "Login successful!")
                self.show_account_menu(account)
            else:
                messagebox.showwarning("Error", "Account not found or incorrect password!")

    def show_teller_menu(self):
        self.clear_window()
        self.label_teller = tk.Label(self.root, text="Teller Menu")
        self.label_teller.pack(pady=10)
        self.button_create_account = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.button_create_account.pack(pady=5)
        self.button_edit_account = tk.Button(self.root, text="Edit Account", command=self.edit_account)
        self.button_edit_account.pack(pady=5)
        self.button_add_money = tk.Button(self.root, text="Add Money", command=self.add_money)
        self.button_add_money.pack(pady=5)
        self.button_remove_money = tk.Button(self.root, text="Remove Money", command=self.remove_money)
        self.button_remove_money.pack(pady=5)
        self.button_view_logs = tk.Button(self.root, text="View Account Logs", command=self.view_account_logs)
        self.button_view_logs.pack(pady=5)
        self.button_delete_account = tk.Button(self.root, text="Delete Account", command=self.delete_account)
        self.button_delete_account.pack(pady=5)
        self.button_display_accounts = tk.Button(self.root, text="Display All Accounts", command=self.display_accounts)
        self.button_display_accounts.pack(pady=5)
        self.button_search_account = tk.Button(self.root, text="Search Account", command=self.search_account)
        self.button_search_account.pack(pady=5)
        self.button_logout = tk.Button(self.root, text="Logout", command=self.logout)
        self.button_logout.pack(pady=5)

    def show_account_menu(self, account):
        self.clear_window()
        self.label_account = tk.Label(self.root, text=f"Welcome {account.holder_name}", font=("Helvetica", 18, "bold"))
        self.label_account.pack(pady=10)
        tk.Label(self.root, text=f"Account Number: {account.account_number}").pack(pady=5)
        tk.Label(self.root, text=f"Balance: ${account.balance}").pack(pady=5)
        self.button_deposit = tk.Button(self.root, text="Deposit Money", command=self.deposit_money)
        self.button_deposit.pack(pady=5)
        self.button_withdraw = tk.Button(self.root, text="Withdraw Money", command=self.withdraw_money)
        self.button_withdraw.pack(pady=5)
        self.button_view_logs = tk.Button(self.root, text="View Transaction Logs", command=self.view_transaction_logs)
        self.button_view_logs.pack(pady=5)
        self.button_logout = tk.Button(self.root, text="Logout", command=self.logout)
        self.button_logout.pack(pady=5)

    def deposit_money(self):
        self.clear_window()
        tk.Label(self.root, text="Deposit Money").pack(pady=10)
        tk.Label(self.root, text="Amount:").pack()
        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.pack()
        self.button_deposit = tk.Button(self.root, text="Deposit", command=self.process_deposit)
        self.button_deposit.pack(pady=10)
        self.button_back = tk.Button(self.root, text="Back", command=lambda: self.show_account_menu(self.logged_in_account))
        self.button_back.pack(pady=5)

    def process_deposit(self):
        amount = float(self.entry_amount.get())
        if self.logged_in_account.deposit(amount):
            messagebox.showinfo("Success", f"Deposited ${amount} to your account.")
            self.show_account_menu(self.logged_in_account)
        else:
            messagebox.showwarning("Error", "Invalid deposit amount!")

    def withdraw_money(self):
        self.clear_window()
        tk.Label(self.root, text="Withdraw Money").pack(pady=10)
        tk.Label(self.root, text="Amount:").pack()
        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.pack()
        self.button_withdraw = tk.Button(self.root, text="Withdraw", command=self.process_withdraw)
        self.button_withdraw.pack(pady=10)
        self.button_back = tk.Button(self.root, text="Back", command=lambda: self.show_account_menu(self.logged_in_account))
        self.button_back.pack(pady=5)

    def process_withdraw(self):
        amount = float(self.entry_amount.get())
        if self.logged_in_account.withdraw(amount):
            messagebox.showinfo("Success", f"Withdrew ${amount} from your account.")
            self.show_account_menu(self.logged_in_account)
        else:
            messagebox.showwarning("Error", "Invalid withdrawal amount!")

    def view_transaction_logs(self):
        logs = "\n".join(self.logged_in_account.transaction_logs)
        messagebox.showinfo("Transaction Logs", logs if logs else "No transactions found.")
        self.show_account_menu(self.logged_in_account)

    def create_account(self):
        self.clear_window()
        tk.Label(self.root, text="Create Account").pack(pady=10)
        tk.Label(self.root, text="Name:").pack()
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()
        tk.Label(self.root, text="Password:").pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()
        tk.Label(self.root, text="Phone Number:").pack()
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.pack()
        tk.Label(self.root, text="Location:").pack()
        self.entry_location = tk.Entry(self.root)
        self.entry_location.pack()
        tk.Label(self.root, text="Initial Balance:").pack()
        self.entry_balance = tk.Entry(self.root)
        self.entry_balance.pack()
        self.button_create = tk.Button(self.root, text="Create", command=self.process_create_account)
        self.button_create.pack(pady=10)
        self.button_back = tk.Button(self.root, text="Back", command=self.show_teller_menu)
        self.button_back.pack(pady=5)

    def process_create_account(self):
        holder_name = self.entry_name.get()
        password = self.entry_password.get()
        phone_number = self.entry_phone.get()
        location = self.entry_location.get()
        balance = float(self.entry_balance.get())
        account_number = f"{len(self.bank.accounts) + 1}"  

        if self.bank.create_account(account_number, holder_name, password, location, phone_number, balance):
            messagebox.showinfo("Success", "Account created successfully!")
            self.show_teller_menu()
        else:
            messagebox.showwarning("Error", "Account creation failed! Name may already exist.")

    def edit_account(self):
        self.clear_window()
        tk.Label(self.root, text="Edit Account").pack(pady=10)
        tk.Label(self.root, text="Account Number:").pack()
        self.entry_account_number = tk.Entry(self.root)
        self.entry_account_number.pack()
        self.button_edit = tk.Button(self.root, text="Edit", command=self.process_edit_account)
        self.button_edit.pack(pady=10)
        self.button_back = tk.Button(self.root, text="Back", command=self.show_teller_menu)
        self.button_back.pack(pady=5)

    def process_edit_account(self):
        account_number = self.entry_account_number.get()
        account = self.bank.get_account_by_number(account_number)
        if account:
            self.clear_window()
            tk.Label(self.root, text="Edit Account").pack(pady=10)
            tk.Label(self.root, text="Name:").pack()
            self.entry_name = tk.Entry(self.root)
            self.entry_name.insert(0, account.holder_name)
            self.entry_name.pack()
            tk.Label(self.root, text="Password:").pack()
            self.entry_password = tk.Entry(self.root, show="*")
            self.entry_password.insert(0, account.password)
            self.entry_password.pack()
            tk.Label(self.root, text="Phone Number:").pack()
            self.entry_phone = tk.Entry(self.root)
            self.entry_phone.insert(0, account.phone_number)
            self.entry_phone.pack()
            tk.Label(self.root, text="Location:").pack()
            self.entry_location = tk.Entry(self.root)
            self.entry_location.insert(0, account.location)
            self.entry_location.pack()
            self.button_save = tk.Button(self.root, text="Save Changes", command=lambda: self.save_account_changes(account))
            self.button_save.pack(pady=10)
            self.button_back = tk.Button(self.root, text="Back", command=self.show_teller_menu)
            self.button_back.pack(pady=5)
        else:
            messagebox.showwarning("Error", "Account not found!")

    def save_account_changes(self, account):
        new_holder_name = self.entry_name.get()

        # Check for duplicate name
        if new_holder_name != account.holder_name and new_holder_name in [acct.holder_name for acct in self.bank.accounts.values()]:
            messagebox.showwarning("Error", "Account holder name already exists!")
            return
        
        account.holder_name = new_holder_name
        account.password = self.entry_password.get()  
        account.phone_number = self.entry_phone.get()
        account.location = self.entry_location.get()
        messagebox.showinfo("Success", "Account updated successfully!")
        self.show_teller_menu()

    def add_money(self):
        self.clear_window()
        tk.Label(self.root, text="Add Money").pack(pady=10)
        tk.Label(self.root, text="Account Number:").pack()
        self.entry_account_number = tk.Entry(self.root)
        self.entry_account_number.pack()
        tk.Label(self.root, text="Amount:").pack()
        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.pack()
        self.button_add = tk.Button(self.root, text="Add", command=self.process_add_money)
        self.button_add.pack(pady=10)
        self.button_back = tk.Button(self.root, text="Back", command=self.show_teller_menu)
        self.button_back.pack(pady=5)

    def process_add_money(self):
        account_number = self.entry_account_number.get()
        amount = float(self.entry_amount.get())
        account = self.bank.get_account_by_number(account_number)
        if account and account.deposit(amount):
            messagebox.showinfo("Success", f"Added ${amount} to account {account_number}")
        else:
            messagebox.showwarning("Error", "Failed to add money!")

    def remove_money(self):
        self.clear_window()
        tk.Label(self.root, text="Remove Money").pack(pady=10)
        tk.Label(self.root, text="Account Number:").pack()
        self.entry_account_number = tk.Entry(self.root)
        self.entry_account_number.pack()
        tk.Label(self.root, text="Amount:").pack()
        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.pack()
        self.button_remove = tk.Button(self.root, text="Remove", command=self.process_remove_money)
        self.button_remove.pack(pady=10)
        self.button_back = tk.Button(self.root, text="Back", command=self.show_teller_menu)
        self.button_back.pack(pady=5)

    def process_remove_money(self):
        account_number = self.entry_account_number.get()
        amount = float(self.entry_amount.get())
        account = self.bank.get_account_by_number(account_number)
        if account and account.withdraw(amount):
            messagebox.showinfo("Success", f"Removed ${amount} from account {account_number}")
        else:
            messagebox.showwarning("Error", "Failed to remove money!")

    def view_account_logs(self):
        self.clear_window()
        tk.Label(self.root, text="View Account Logs").pack(pady=10)
        tk.Label(self.root, text="Account Number:").pack()
        self.entry_account_number = tk.Entry(self.root)
        self.entry_account_number.pack()
        self.button_view = tk.Button(self.root, text="View Logs", command=self.process_view_logs)
        self.button_view.pack(pady=10)
        self.button_back = tk.Button(self.root, text="Back", command=self.show_teller_menu)
        self.button_back.pack(pady=5)

    def process_view_logs(self):
        account_number = self.entry_account_number.get()
        account = self.bank.get_account_by_number(account_number)
        if account:
            logs = "\n".join(account.transaction_logs)
            messagebox.showinfo("Transaction Logs", logs if logs else "No transactions found.")
        else:
            messagebox.showwarning("Error", "Account not found!")

    def delete_account(self):
        self.clear_window()
        tk.Label(self.root, text="Delete Account").pack(pady=10)
        tk.Label(self.root, text="Account Number:").pack()
        self.entry_account_number = tk.Entry(self.root)
        self.entry_account_number.pack()
        self.button_delete = tk.Button(self.root, text="Delete", command=self.process_delete_account)
        self.button_delete.pack(pady=10)
        self.button_back = tk.Button(self.root, text="Back", command=self.show_teller_menu)
        self.button_back.pack(pady=5)

    def process_delete_account(self):
        account_number = self.entry_account_number.get()
        if self.bank.delete_account(account_number):
            messagebox.showinfo("Success", "Account deleted successfully!")
            self.show_teller_menu()
        else:
            messagebox.showwarning("Error", "Account not found!")

    def display_accounts(self):
        account_info = "\n".join(self.bank.display_accounts())
        messagebox.showinfo("Accounts", account_info if account_info else "No accounts found.")
        self.show_teller_menu()

    def search_account(self):
        self.clear_window()
        tk.Label(self.root, text="Search Account").pack(pady=10)
        tk.Label(self.root, text="Enter Account Number or Holder Name:").pack()
        self.entry_search = tk.Entry(self.root)
        self.entry_search.pack()
        self.button_search = tk.Button(self.root, text="Search", command=self.process_search_account)
        self.button_search.pack(pady=10)
        self.button_back = tk.Button(self.root, text="Back", command=self.show_teller_menu)
        self.button_back.pack(pady=5)

    def process_search_account(self):
        search_term = self.entry_search.get()
        account = self.bank.get_account_by_number(search_term) or self.bank.get_account_by_name(search_term)
        if account:
            messagebox.showinfo("Account Found", f"Account Number: {account.account_number}\nName: {account.holder_name}\nBalance: ${account.balance}")
        else:
            messagebox.showwarning("Error", "Account not found!")


    def logout(self):
        self.logged_in_account = None
        self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


root = tk.Tk()
app = BankUI(root)
root.mainloop()
