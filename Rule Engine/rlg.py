import tkinter as tk
from tkinter import messagebox, Scrollbar, Text
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

class RuleEngineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rule Engine GUI")

        # Setting colors and styles
        self.bg_color = "#F5F5F5"  # A more neutral background color
        self.button_color = "#007BFF"  # A professional blue color
        self.entry_bg_color = "#FFFFFF"  # White entry background
        self.root.configure(bg=self.bg_color)

        # Create Rule Section
        self.create_rule_frame = tk.Frame(root, bg=self.bg_color)
        self.create_rule_frame.pack(pady=10)
        tk.Label(self.create_rule_frame, text="Create Rule", bg=self.bg_color, font=("Arial", 14)).pack()
        self.rule_string_entry = tk.Entry(self.create_rule_frame, width=70, bg=self.entry_bg_color, font=("Arial", 12))  # Increased width and font size
        self.rule_string_entry.pack(pady=5)
        self.create_rule_button = tk.Button(self.create_rule_frame, text="Create Rule", bg=self.button_color, fg="white", command=self.create_rule)
        self.create_rule_button.pack(pady=5)

        # Combine Rules Section
        self.combine_rule_frame = tk.Frame(root, bg=self.bg_color)
        self.combine_rule_frame.pack(pady=10)
        tk.Label(self.combine_rule_frame, text="Combine Rules (comma-separated IDs)", bg=self.bg_color, font=("Arial", 14)).pack()
        self.rule_ids_entry = tk.Entry(self.combine_rule_frame, width=70, bg=self.entry_bg_color, font=("Arial", 12))  # Increased width and font size
        self.rule_ids_entry.pack(pady=5)
        self.combine_rule_button = tk.Button(self.combine_rule_frame, text="Combine Rules", bg=self.button_color, fg="white", command=self.combine_rules)
        self.combine_rule_button.pack(pady=5)

        # Evaluate Rule Section
        self.evaluate_rule_frame = tk.Frame(root, bg=self.bg_color)
        self.evaluate_rule_frame.pack(pady=10)
        tk.Label(self.evaluate_rule_frame, text="Evaluate Rule (Rule ID)", bg=self.bg_color, font=("Arial", 14)).pack()
        self.mega_rule_id_entry = tk.Entry(self.evaluate_rule_frame, width=70, bg=self.entry_bg_color, font=("Arial", 12))  # Increased width and font size
        self.mega_rule_id_entry.pack(pady=5)
        tk.Label(self.evaluate_rule_frame, text="Data (JSON)", bg=self.bg_color, font=("Arial", 14)).pack()
        self.data_entry = tk.Entry(self.evaluate_rule_frame, width=70, bg=self.entry_bg_color, font=("Arial", 12))  # Increased width and font size
        self.data_entry.pack(pady=5)
        self.evaluate_rule_button = tk.Button(self.evaluate_rule_frame, text="Evaluate Rule", bg=self.button_color, fg="white", command=self.evaluate_rule)
        self.evaluate_rule_button.pack(pady=5)

        # Modify Rule Section
        self.modify_rule_frame = tk.Frame(root, bg=self.bg_color)
        self.modify_rule_frame.pack(pady=10)
        tk.Label(self.modify_rule_frame, text="Modify Rule (Rule ID)", bg=self.bg_color, font=("Arial", 14)).pack()
        self.modify_rule_id_entry = tk.Entry(self.modify_rule_frame, width=70, bg=self.entry_bg_color, font=("Arial", 12))  # Increased width and font size
        self.modify_rule_id_entry.pack(pady=5)
        tk.Label(self.modify_rule_frame, text="New Rule String", bg=self.bg_color, font=("Arial", 14)).pack()
        self.new_rule_string_entry = tk.Entry(self.modify_rule_frame, width=70, bg=self.entry_bg_color, font=("Arial", 12))  # Increased width and font size
        self.new_rule_string_entry.pack(pady=5)
        self.modify_rule_button = tk.Button(self.modify_rule_frame, text="Modify Rule", bg=self.button_color, fg="white", command=self.modify_rule)
        self.modify_rule_button.pack(pady=5)

        # Output Section
        self.output_frame = tk.Frame(root, bg=self.bg_color)
        self.output_frame.pack(pady=10)

        self.output_text = Text(self.output_frame, height=10, width=80, bg=self.entry_bg_color, font=("Arial", 12), wrap=tk.WORD)  # Increased font size
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for output text area
        self.scrollbar = Scrollbar(self.output_frame, command=self.output_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text['yscrollcommand'] = self.scrollbar.set

    # Function to create a new rule
    def create_rule(self):
        rule_string = self.rule_string_entry.get()
        try:
            response = requests.post(f"{BASE_URL}/create_rule", json={"rule_string": rule_string})
            response.raise_for_status()
            self.output_text.insert(tk.END, f"Create Rule Response: {response.json()}\n")
        except requests.exceptions.RequestException as e:
            self.output_text.insert(tk.END, f"Error: {e}\n")

    # Function to combine rules
    def combine_rules(self):
        rule_ids = self.rule_ids_entry.get().split(',')
        rule_ids = [id.strip() for id in rule_ids]
        try:
            response = requests.post(f"{BASE_URL}/combine_rules", json={"rule_ids": rule_ids})
            response.raise_for_status()
            self.output_text.insert(tk.END, f"Combine Rules Response: {response.json()}\n")
        except requests.exceptions.RequestException as e:
            self.output_text.insert(tk.END, f"Error: {e}\n")

    # Function to evaluate a rule
    def evaluate_rule(self):
        mega_rule_id = self.mega_rule_id_entry.get()
        data = self.data_entry.get()
        try:
            data_json = json.loads(data)
            response = requests.post(f"{BASE_URL}/evaluate_rule", json={"rule_id": mega_rule_id, "data": data_json})
            response.raise_for_status()
            self.output_text.insert(tk.END, f"Evaluate Rule Response: {response.json()}\n")
        except json.JSONDecodeError as e:
            self.output_text.insert(tk.END, f"JSON Decode Error: {e}\n")
        except requests.exceptions.RequestException as e:
            self.output_text.insert(tk.END, f"Error: {e}\n")

    # Function to modify a rule
    def modify_rule(self):
        rule_id = self.modify_rule_id_entry.get()
        new_rule_string = self.new_rule_string_entry.get()
        try:
            response = requests.post(f"{BASE_URL}/modify_rule", json={"rule_id": rule_id, "new_rule_string": new_rule_string})
            response.raise_for_status()
            self.output_text.insert(tk.END, f"Modify Rule Response: {response.json()}\n")
        except requests.exceptions.RequestException as e:
            self.output_text.insert(tk.END, f"Error: {e}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = RuleEngineApp(root)
    root.mainloop()
