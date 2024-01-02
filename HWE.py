import tkinter as tk
from tkinter import ttk
import json
#from tkinterdnd2 import TkinterDnD, DND_FILES
#import tkinterDnD  # Importing the tkinterDnD moduleD
import os


playerclass_list = ["Cremator", "Ghost", "Heavy", "Survivor", "Berserker", "Demolition", "Medic", "Engineer", "Assault", "Warden"]

class DataEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Horde Item Editor")




        playerclass_list = ["Cremator", "Ghost", "Heavy", "Survivor", "Berserker", "Demolition", "Medic", "Engineer", "Assault", "Warden"]
        self.damage_type_vars = []
        self.damage_type_options = [
            ("Ballistic",2.0),
            ("Slashing",4.0),
            ("Blunt",3.0),
            ("Other Phys", 1.0),
            ("Fire", 5.0),
            ("Cold", 6.0),
            ("Lightning", 7.0),
            ("Poison", 8.0),
            ("Blast", 9.0)
        ]

        self.infusion_vars = []
        self.infusion_options = [
            ("Hemo", 1.0),
            ("Concussive", 2.0),
            ("Septic", 3.0),
            ("Flaming", 4.0),
            ("Arctic", 5.0),
            ("Galvanizing", 6.0),
            ("Quality", 7.0),
            ("Impaling", 8.0),
            ("Rejuv", 9.0),
            ("Quick Silver", 10.0),
            ("Siphoning", 11.0),
            ("Titanium", 12.0),
            ("Chrono", 13.0),
            ("Ruination", 14.0)
        ]


        self.class_entry = tk.Entry(self.root)
        self.price_entry = tk.Entry(self.root)
        self.total_levels_entry = tk.Entry(self.root)
        self.level_entries = []
        self.level_options = ["Cremator", "Ghost", "Heavy", "Survivor", "Berserker", "Demolition", "Medic", "Engineer", "Assault", "Warden"]
        
        self.whitelist_vars = []
        self.whitelist_options = playerclass_list.copy()

        self.starter_class_vars = []
        self.starter_class_options = playerclass_list.copy()
        self.create_widgets()


    def create_widgets(self):
        tk.Label(self.root, text="Model Name:").grid(row=0, column=0, sticky="ne")
        self.model_name_entry = tk.Entry(self.root)
        self.model_name_entry.grid(row=0, column=1, sticky="nw")

         # Set up drag-and-drop for the model_name_entry
        #self.model_name_entry.drop_target_register(DND_FILES)
        #self.model_name_entry.dnd_bind('<<Drop>>', self.handle_drop)

        tk.Label(self.root, text="Weapon Name:").grid(row=1, column=0, sticky="ne")
        self.igname_entry = tk.Entry(self.root)
        self.igname_entry.grid(row=1, column=1, sticky="nw")

        tk.Label(self.root, text="Description:").grid(row=2, column=0, sticky="ne")
        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=2, column=1, sticky="nw")

        tk.Label(self.root, text="Category:").grid(row=3, column=0, sticky="ne")
        self.category_combobox = ttk.Combobox(self.root, values=["Melee", "Pistol", "SMG", "Rifle", "Explosive", "Equipment", "Gadget"])
        self.category_combobox.grid(row=3, column=1, sticky="nw")

        tk.Label(self.root, text="Price:").grid(row=4, column=0, sticky="ne")
        self.ammo_price_entry = tk.Entry(self.root)
        self.ammo_price_entry.grid(row=4, column=1, sticky="nw")

        tk.Label(self.root, text="Ammo Price:").grid(row=5, column=0, sticky="ne")
        self.ammo_price_entry = tk.Entry(self.root)
        self.ammo_price_entry.grid(row=5, column=1, sticky="nw")

        tk.Label(self.root, text="Secondary Ammo Price:").grid(row=6, column=0, sticky="ne")
        self.secondary_ammo_price_entry = tk.Entry(self.root)
        self.secondary_ammo_price_entry.grid(row=6, column=1, sticky="nw")

        tk.Label(self.root, text="Weight:").grid(row=7, column=0, sticky="ne")
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=7, column=1, sticky="nw")


        # Levels

        tk.Label(self.root, text="Levels:").grid(row=0, column=3, rowspan= 1, sticky="w")
        self.levels_frame = ttk.Frame(self.root)
        self.levels_frame.grid(row=1, column=3, columnspan=2, rowspan=4, sticky="nw")
        self.create_levels_entry(self.levels_frame, self.level_options)

        tk.Label(self.root, text="Damage Types:").grid(row=8, column=0, sticky="e")
        self.damage_types_frame = ttk.Frame(self.root)
        self.damage_types_frame.grid(row=8, column=1, sticky="w")
        self.create_checkbuttons(self.damage_types_frame, self.damage_type_options, self.damage_type_vars)

        tk.Label(self.root, text="Infusions:").grid(row=8, column=2, sticky="e")
        self.infusions_frame = ttk.Frame(self.root)
        self.infusions_frame.grid(row=8, column=3, sticky="w")
        self.create_checkbuttons(self.infusions_frame, self.infusion_options,self.infusion_vars)

        tk.Label(self.root, text="Whitelist:").grid(row=11, column=0, sticky="e")
        self.whitelist_frame = ttk.Frame(self.root)
        self.whitelist_frame.grid(row=11, column=1, sticky="w")
        self.create_checkbuttons(self.whitelist_frame, self.whitelist_options, self.whitelist_vars)



        tk.Label(self.root, text="Starter\nClasses:").grid(row=11, column=2, sticky="e")
        self.starter_class_frame = ttk.Frame(self.root)
        self.starter_class_frame.grid(row=11, column=3, sticky="w")
        self.create_checkbuttons(self.starter_class_frame, self.starter_class_options, self.starter_class_vars)
        
        tk.Label(self.root, text="Sub/Custom \nStarter Classes").grid(row=12, column=2, sticky="e")
        self.customclasses_input = ttk.Entry(self.root)
        self.customclasses_input.grid(row=12, column=3, sticky="w", columnspan=3)

        tk.Button(self.root, text="Export JSON", command=self.print_selected_options).grid(row=12, column=1, columnspan=1, pady=10)
        #tk.Button(self.root, text="Import from Clipboard", command=self.import_from_clipboard).grid(row=11, column=1, columnspan=1, pady=10)


    ### Methods ###
        
    def handle_drop(self, event):
        # Get the dropped files
        files = event.data

        # Assuming you want the first file from the dropped list
        if files:
            file_path = files
            # Extract the filename without extension
            filename_without_extension = os.path.splitext(os.path.basename(file_path))[0]

            # Insert the filename into the model_name_entry
            self.model_name_entry.delete(0, tk.END)
            self.model_name_entry.insert(0, filename_without_extension)

            


    def create_levels_entry(self, parent, options):
        for i, option in enumerate(options):
            tk.Label(parent, text=option).grid(row=i // 2, column=i % 2 * 2, sticky="nw")
            entry = tk.Entry(parent, name=str(option).lower())  # Assign a unique identifier (index in self.level_options)
            entry.grid(row=i // 2, column=i % 2 * 2 + 1, sticky="nw")
            self.level_entries.append(entry)
            print(f"Entry created: {entry.winfo_name()}")  # Use winfo_name() to get the name attribute
        print(entry.winfo_name())
        print(self.level_entries)


    def create_checkbuttons(self, frame, options, vars_list, columns=3):
        for i, option in enumerate(options):
            if isinstance(option, tuple) and len(option) == 2:
                text, value = option
            elif isinstance(option, str):
                text, value = option, None
            else:
                continue

            var = tk.IntVar()
            checkbutton = ttk.Checkbutton(frame, text=text, variable=var)
            checkbutton.grid(row=i // columns, column=i % columns, sticky="w")
            vars_list.append((text, var, value))

    def get_selected_options(self, vars_list):
        selected_options = []
        for text, var, value in vars_list:
            if var.get():
                selected_options.append((text, value))
        return selected_options
    
    def print_selected_levels(self):
        selected_levels = self.get_selected_levels()
        sl = []
        print("\nSelected Levels:")
        for level_index, value in selected_levels.items():
            if value:
                sl.append(f'{str(level_index).capitalize()}: {value}')
            else:
                continue
        print(sl)
        return sl
    
    def get_selected_levels(self):
        selected_levels = {}
        for entry in self.level_entries:
            level_index = entry.winfo_name()  # Retrieve the unique identifier (index in self.level_options)
            value = entry.get()
            selected_levels[level_index] = value
        return selected_levels


    def print_selected_whitelist(self):
        selected_whitelist = self.get_selected_options(self.whitelist_vars)
        wl = []
        text = []
        print("\nSelected Whitelist:")
        for player_class in playerclass_list:
            found = False
            for text, value in selected_whitelist:
                if player_class == text:
                    found = True
                    break
            wl.append(f'{player_class}: {found}')
        print(wl)
        return wl
    

    def print_selected_starter_classes(self):
        selected_starter_classes = self.get_selected_options(self.starter_class_vars)
        sc= []
        text=[]
        print("\nSelected Starterlist:")
        for player_class in playerclass_list:           
            for text, value in selected_starter_classes:
                if player_class == text:
                    sc.append(text)   
        ccisplit = str(self.customclasses_input.get())
        custom_classes_list = [custom_class.strip() for custom_class in ccisplit.split(',')]
        sc.extend(custom_classes_list)
        return sc
    
    def display_json_popup(self, json_str):
        popup = tk.Toplevel(self.root)
        popup.title("Exported JSON")

        text_widget = tk.Text(popup, wrap="none")
        text_widget.insert("1.0", json_str)
        text_widget.config(state="disabled")

        scroll_y = ttk.Scrollbar(popup, orient="vertical", command=text_widget.yview)
        scroll_y.pack(side="right", fill="y")
        text_widget.config(yscrollcommand=scroll_y.set)

        text_widget.pack(expand=True, fill="both")
        

    def print_selected_options(self):
        selected_damage_types = self.get_selected_options(self.damage_type_vars)
        selected_infusions = self.get_selected_options(self.infusion_vars)
        dt = [value for _, value in selected_damage_types]
        inf = [value for _, value in selected_infusions]
        sc = self.print_selected_starter_classes()
        wl = self.print_selected_whitelist()


        json_data = {
            "Model Name": self.model_name_entry.get(),
            "Description": self.igname_entry.get(),
            "entity_properties": {"type":1.0},
            "Category": self.category_combobox.get(),
            "Price": self.ammo_price_entry.get(),
            "Ammo Price": self.ammo_price_entry.get(),
            "Secondary Ammo Price": self.secondary_ammo_price_entry.get(),
            "Weight": self.weight_entry.get(),
            "Levels": self.print_selected_levels(),
            "Damage Types": dt,
            "Infusions": inf,
            "Starter Classes": sc,
            "Whitelist": wl
        }

        json_str = json.dumps(json_data, indent=2)

        # Display JSON in a pop-up window
        self.display_json_popup(json_str)





    
root = tk.Tk()
app = DataEditorApp(root)
root.mainloop()
