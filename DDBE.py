import tkinter as tk
import customtkinter as ctk

# Dimensions and appearance of the window
appWidth, appHeight = 1300, 600
theme = "Light"  # Default theme

# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("DDB-Editer v0.1")
        self.geometry(f"{appWidth}x{appHeight}")

        # Left Frame for Console and Input
        self.leftFrame = ctk.CTkFrame(self)
        self.leftFrame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        # Database Console
        self.consoleLabel = ctk.CTkLabel(self.leftFrame, text="Database Console")
        self.consoleLabel.pack(pady=10)

        self.console = ctk.CTkTextbox(
            self.leftFrame,
            width=int(appWidth * 0.4),
            height=int(appHeight * 0.5)
        )
        self.console.pack()

        # Command Input Field
        self.commandLabel = ctk.CTkLabel(self.leftFrame, text="Enter Command")
        self.commandLabel.pack(pady=10)

        self.commandEntry = ctk.CTkEntry(self.leftFrame, width=int(appWidth * 0.4))
        self.commandEntry.pack()

        # Right Frame for Buttons
        self.rightFrame = ctk.CTkFrame(self)
        self.rightFrame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        # Connect to Database Button
        self.connectButton = ctk.CTkButton(
            self.rightFrame, text="Connect to Database", command=self.connect_to_db
        )
        self.connectButton.pack(pady=10)

        # Refresh Content Button
        self.refreshButton = ctk.CTkButton(
            self.rightFrame, text="Refresh Content", command=self.refresh_content
        )
        self.refreshButton.pack(pady=10)

        # Save Button
        self.saveButton = ctk.CTkButton(
            self.rightFrame, text="Save", command=self.save_changes
        )
        self.saveButton.pack(pady=10)

        # Change Parameter Button
        self.changeButton = ctk.CTkButton(
            self.rightFrame, text="Change Parameter", command=self.change_param
        )
        self.changeButton.pack(pady=10)

        # Theme Switch
        self.themeSwitch = ctk.CTkSwitch(
            self.rightFrame, text="Theme Switch", command=self.switch_theme
        )
        self.themeSwitch.pack(side="bottom")

        # Apply grid layout to adjust elements dynamically with window resize
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def connect_to_db(self):
        # TODO: Connect to database and display content in console
        self.console.insert(tk.END, "Connected to database!\n")

    def refresh_content(self):
        # TODO: Refresh content from database and display in console
        self.console.insert(tk.END, "Content Refreshed!\n")

    def save_changes(self):
        # TODO: Save changes to database
        self.console.insert(tk.END, "Changes Saved!\n")

    def change_param(self):
        # TODO: Change parameter in database based on user input
        command = self.commandEntry.get()
        self.console.insert(tk.END, f"Changing parameter: {command}\n")
        self.commandEntry.delete(0, tk.END)

    def switch_theme(self):
        global theme
        theme = "Dark" if theme == "Light" else "Light"
        ctk.set_appearance_mode(theme)
        self.console.insert(tk.END, f"Theme switched to {theme}\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()
