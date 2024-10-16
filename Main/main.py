import tkinter as tk
from tkinter import messagebox #neshon ddn error o alert
from tkinter import ttk
import matplotlib.pyplot as plt #graph . radar
import numpy as np
from tkinter import * #without .tk
from PIL import Image, ImageTk #photo
from tkinter import PhotoImage
import csv
import webbrowser



normal_values = {
    "WBC": (4000, 11000),
    "RBC": (4.7, 6.1),
    "Hb": (13.8, 17.2),
    "Hct": (40.7, 50.3),
    "MCV": (80, 100),
    "MCHC": (32, 36),
    "PLT": (150000, 450000),
    "Glu": (70, 100),
    "BUN": (7, 20),
    "Cr": (0.7, 1.3),
    "AST": (10, 40),
    "ALP": (44, 147),
    "LDL": (0, 100),
    "HDL": (40, 1000),
    "TG": (0, 150),
    "pH": (7.35, 7.45),
    "SG": (1.005, 1.030),
    "Blood": (0, 0),
    "T3": (80, 180),
    "T4": (4.5, 11.2),
    "FSH": (1.4, 18.1),
    "LH": (1.8, 8.6),
}

recommendations = {
    "WBC": "1. Maintain a healthy diet and stay hydrated.\n2. Regular exercise can boost your immune system.\n3. Avoid smoking and limit alcohol intake.",
    "RBC": "1. Ensure adequate iron intake through foods like red meat, beans, and spinach.\n2. Consider vitamin B12 supplements if needed.\n3. Stay active to promote circulation.",
    "Hb": "1. Eat foods rich in vitamin B12 and folic acid, like eggs and leafy greens.\n2. Avoid excessive caffeine which can inhibit iron absorption.\n3. Consult with a doctor if low levels persist.",
    "Hct": "1. Stay active and maintain hydration levels.\n2. Include iron-rich foods in your diet.\n3. Regular check-ups to monitor your levels.",
    "MCV": "1. Include vitamin B12 and folate-rich foods in your diet, such as citrus fruits and legumes.\n2. Consider iron supplementation if you're low.\n3. Keep track of your dietary habits.",
    "MCHC": "1. Hydrate well and eat iron-rich foods like red meat and lentils.\n2. Regular exercise can help improve overall health.\n3. Consult a doctor for persistent issues.",
    "PLT": "1. Avoid alcohol and maintain a balanced diet rich in fruits and vegetables.\n2. Regular health check-ups are important.\n3. Stay active to support overall health.",
    "Glu": "1. Limit sugar intake and exercise regularly to maintain healthy blood sugar levels.\n2. Consider fiber-rich foods to help regulate glucose.\n3. Monitor your levels regularly.",
    "BUN": "1. Stay hydrated and consume a balanced diet, especially foods high in water content.\n2. Regular exercise helps improve kidney function.\n3. Consult a doctor if levels are abnormal.",
    "Cr": "1. Ensure a balanced diet with adequate hydration, focusing on fruits and vegetables.\n2. Limit processed foods high in salt.\n3. Regular check-ups to monitor kidney health.",
    "AST": "1. Limit alcohol and avoid processed foods high in sugar and unhealthy fats.\n2. Incorporate liver-supportive foods like garlic and green tea.\n3. Regular exercise can help maintain liver health.",
    "ALP": "1. Include calcium-rich foods like dairy and leafy greens in your diet.\n2. Regular exercise helps maintain bone health.\n3. Monitor your levels regularly with a doctor.",
    "LDL": "1. Reduce saturated fats by avoiding fried foods and processed snacks.\n2. Increase fiber intake through whole grains and fruits.\n3. Regular cardiovascular exercise is beneficial.",
    "HDL": "1. Engage in physical activity like walking or cycling to boost HDL levels.\n2. Include healthy fats in your diet, such as avocados and olive oil.\n3. Avoid trans fats and processed foods.",
    "TG": "1. Limit sugar and refined carbohydrates in your diet.\n2. Regular physical activity can help manage triglyceride levels.\n3. Consult with a healthcare provider for personalized advice.",
    "pH": "1. Stay hydrated and eat a balanced diet rich in fruits and vegetables.\n2. Limit intake of acidic foods and drinks.\n3. Regular check-ups to monitor your body's pH levels.",
    "SG": "1. Maintain hydration and consume balanced meals to support kidney function.\n2. Regular exercise promotes overall health.\n3. Consult a healthcare provider for specific concerns.",
    "Blood": "1. Consult a doctor for any concerns or symptoms related to blood health.\n2. Maintain a balanced diet and stay hydrated.\n3. Regular health check-ups are essential.",
    "T3": "1. Maintain a balanced diet with adequate iodine, found in seafood and dairy.\n2. Regular exercise supports hormonal balance.\n3. Consult a healthcare provider for thyroid-related concerns.",
    "T4": "1. Ensure sufficient iodine intake through diet, especially from iodized salt.\n2. Regular health screenings can help monitor levels.\n3. Consult a doctor if experiencing symptoms.",
    "FSH": "1. Consult a healthcare provider for hormonal balance.\n2. Regular check-ups to monitor reproductive health.\n3. Maintain a balanced diet and stay active.",
    "LH": "1. Maintain a balanced diet and consult a doctor if needed.\n2. Regular check-ups to monitor hormonal health.\n3. Consider lifestyle changes to support overall wellness.",
}



def clear_all():
    for label, entry in entries.items():
        low, high = normal_values[label]
        placeholder_text = f"{low} - {high}" #baze gray
        
        if entry.get() != placeholder_text:  
            entry.delete(0, tk.END) 
            entry.insert(0, placeholder_text)  
            entry.config(fg='grey')  


def continue_action():
    results = []
    notebook.tab(results_tab, state='normal')
    for label, entry in entries.items():
        try:
            value = float(entry.get())
            low, high = normal_values[label]
            if value < low:
                results.append((f"{label} is below normal range ({value} < {low})", "below"))
            elif value > high:
                results.append((f"{label} is above normal range ({value} > {high})", "above"))
            else:
                results.append((f"{label} is within normal range.", "normal"))
        except ValueError:
            results.append((f"{label} has invalid input.", "error"))
    
    display_results(results)
    notebook.select(results_tab)   




def display_results(result_list):
    #delete old widget
    for widget in results_tab.winfo_children():
        widget.destroy()

   
    result_label = tk.Label(results_tab, text="Your Check-up Results:", font=("Arial", 20, "bold"), bg="#f3e5ab")
    result_label.grid(row=0, column=0, columnspan=2, pady=10)

    #invalids
    result_text_box = tk.Text(results_tab, wrap=tk.WORD, font=("Arial", 14), bg="#f3e5ab" ,fg="gray", relief=tk.FLAT)
    result_text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

    #weights(ba tab bozorg mishe)
    results_tab.grid_rowconfigure(1, weight=1)
    results_tab.grid_columnconfigure(0, weight=1)
    results_tab.grid_columnconfigure(1, weight=1)
    
    for result_text, result_type in result_list:
        if result_type == "above" or result_type == "below":
            result_text_box.insert(tk.END, result_text + "\n", "highlight")
          
        else:
            result_text_box.insert(tk.END, result_text + "\n")
            
    #below or above
    result_text_box.tag_configure("highlight", foreground="red", font=("Arial", 14, "bold"))
    
    result_text_box.config(state=tk.DISABLED)

    
    disease_button = tk.Button(results_tab, text=" Possible Diseases", command=lambda : show_diseases(result_list), bg="#004c4c", fg="white", font=("Arial", 14, "bold"), borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2)
    disease_button.grid(row=3,column=0, pady=10 , padx= 10, sticky='ew')

   
    graph_button = tk.Button(results_tab, text="Graph", command=lambda: show_graph(result_list), bg="#004c4c", fg="white", font=("Arial", 14, "bold"), borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2)
    graph_button.grid(row=2, column=1, pady=10, padx=10, sticky='ew')

    radar_button = tk.Button(results_tab, text="Radar", command=lambda: show_radar(result_list), bg="#004c4c", fg="white", font=("Arial", 14, "bold"), borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2)
    radar_button.grid(row=2, column=0, pady=10, padx=10, sticky='ew')
    
    download_button = Button(results_tab, text='Download CSV', command=download_csv, bg="#004c4c", fg="white", font=("Arial", 14, "bold"), borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2)
    download_button.grid(row=3 , column=1, pady=10, padx=10, sticky='ew')
   
    

def show_graph(result_list):
    labels = []
    values = []
    
    for label, entry in entries.items():
        try:
            value = float(entry.get())
            values.append(value)
            labels.append(label)
        except ValueError:
            continue

    
    if not values:
        messagebox.showerror("Error", "No valid values to display in graph.")
        return

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color='#004c4c', alpha=0.7)
    plt.title('Check-up Results')
    plt.xlabel('Parameters')
    plt.ylabel('Values')
    plt.xticks(rotation=45)  
    plt.ylim(0, max(values) + 10)  
    plt.grid(axis='y')  
    plt.show()  


def show_radar(result_list):
    labels = []
    values = []
    ranges = []
    
    for label, entry in entries.items():
        try:
            value = float(entry.get())
            low, high = normal_values[label]
            values.append(value)
            labels.append(label)
            ranges.append(high)
        except ValueError:
            continue
    
    if not values:
        messagebox.showerror("Error", "No valid values to display in radar chart.")
        return
    

    values += values[:1]  
    ranges += ranges[:1]  
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()  #tedade labelo ba zavie
    angles += angles[:1]  
    
   
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='#004c4c', alpha=0.25)
    ax.plot(angles, values, color='#004c4c', linewidth=2)
    ax.set_yticklabels([])  #barchasb y makhfi
    ax.set_xticks(angles[:-1]) #zavie x
    ax.set_xticklabels(labels, fontsize=10, fontweight="bold")
    
    plt.show()




def show_diseases(result_list):
    disease_window = tk.Toplevel(root)
    disease_window.title("Possible Diseases")
    disease_window.geometry("550x715+{}+{}".format(root.winfo_x(), root.winfo_y()))
    disease_window.configure(bg="#f3e5ab")

    disease_label = tk.Label(disease_window, text="Possible Diseases about Check-up:", font=("Arial", 20, "bold"), bg="#f3e5ab")
    disease_label.pack(pady=10)

    diseases = {
        "WBC": ("Infection, Inflammation", "Immune system disorders"),
        "RBC": ("Anemia, Blood loss", "Polycythemia"),
        "Hb": ("Anemia", "Dehydration"),
        "Hct": ("Anemia", "Dehydration"),
        "MCV": ("Microcytic anemia", "Macrocytic anemia"),
        "MCHC": ("Hypochromic anemia", "Spherocytosis"),
        "PLT": ("Thrombocytopenia", "Thrombocythemia"),
        "Glu": ("Diabetes", "Hypoglycemia"),
        "BUN": ("Kidney disease", "Dehydration"),
        "Cr": ("Kidney disease", "Dehydration"),
        "AST": ("Liver disease", "Muscle damage"),
        "ALP": ("Liver disease", "Bone disease"),
        "LDL": ("Heart disease", "High cholesterol"),
        "HDL": ("Low cholesterol", "Risk of heart disease"),
        "TG": ("Risk of heart disease", "Metabolic syndrome"),
        "pH": ("Acidosis", "Alkalosis"),
        "SG": ("Dehydration", "Kidney problems"),
        "Blood": ("Infection", "Kidney disease"),
        "T3": ("Hyperthyroidism", "Hypothyroidism"),
        "T4": ("Hyperthyroidism", "Hypothyroidism"),
        "FSH": ("Menstrual irregularities", "Menopause"),
        "LH": ("Menstrual irregularities", "Menopause"),
    }

    for label in normal_values.keys():
        disease_text = ""
        if any(f"{label} is above" in text for text, _ in result_list):
            disease_text = f"High {label}: {diseases[label][0]}"
        elif any(f"{label} is below" in text for text, _ in result_list):
            disease_text = f"Low {label}: {diseases[label][1]}"
        
        disease_label = tk.Label(disease_window, text=disease_text, font=("Arial", 14), bg="#f3e5ab")
        disease_label.pack(pady=5)
        
        if disease_text:  
            recommendation_button = tk.Button(disease_window, text=f"Recommendation for {label}", command=lambda l=label: show_recommendation(l), bg="#005757", fg="white", font=("Arial", 12, "bold"), borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2)
            recommendation_button.pack(pady=5)



def show_recommendation(parameter):
    recommend_window = tk.Toplevel(root)
    recommend_window.title(f"Recommendations for {parameter}")

    recommend_window.geometry("400x300+{}+{}".format(root.winfo_x(), root.winfo_y()))
    recommend_window.configure(bg="#f3e5ab")

    recommend_label = tk.Label(recommend_window, text=f"Recommendations for {parameter}:", font=("Arial", 16, "bold"), bg="#f3e5ab")
    recommend_label.pack(pady=10)

    recommend_text_box = tk.Text(recommend_window, wrap=tk.WORD, font=("Arial", 14), bg="#f3e5ab", relief=tk.FLAT)
    recommend_text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    recommend_text_box.insert(tk.END, recommendations[parameter] + "\n")
    recommend_text_box.config(state=tk.DISABLED)
    
    
    

root = tk.Tk()
root.title("Health Check-up app")


root.geometry("550x715")
root.configure(bg="#f3e5ab")


style = ttk.Style()
style.theme_use("default")
style.configure("TFrame", background="#f3e5ab")
style.configure("TNotebook", background="#f3e5ab")
style.configure("TNotebook.Tab", background="#f3e5ab", font=("Arial", 14, "bold"))


notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)


welcome_tab = ttk.Frame(notebook)
notebook.add(welcome_tab, text="Welcome")


welcome_label = tk.Label(welcome_tab, text="Welcome to the Health Check-up App", font=("Arial", 22, "bold"), bg="#f3e5ab")
welcome_label.pack(pady=20)


full_checkup_button = tk.Button(welcome_tab, text="Full Check-up", command=lambda: notebook.select(checkup_tab), bg="#004c4c", fg="white", font=("Arial", 16, "bold"), borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2)
full_checkup_button.pack(pady=20)



first_name_label = tk.Label(welcome_tab, text="First Name:" , font=("Arial", 14, "bold") , bg="#f3e5ab")
first_name_label.pack(pady=10)
first_name_entry = tk.Entry(welcome_tab)
first_name_entry.pack(pady=10)

last_name_label = tk.Label(welcome_tab, text="Last Name:" , font=("Arial", 14, "bold"), bg="#f3e5ab")
last_name_label.pack(pady=10)
last_name_entry = tk.Entry(welcome_tab)
last_name_entry.pack(pady=10)


user_profile = None


def check_name_entries(*args):
    if first_name_entry.get() and last_name_entry.get():
        
        create_profile_button.config(state=tk.NORMAL)
        notebook.tab(checkup_tab, state='disabled')  
    else:
        full_checkup_button.config(state=tk.DISABLED)
        create_profile_button.config(state=tk.DISABLED)
        notebook.tab(checkup_tab, state='disabled')  

full_checkup_button.config(state=tk.NORMAL)





def create_profile():
    global user_profile
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    
    if user_profile is None:  
       
        user_profile = {
            'first_name': first_name,
            'last_name': last_name
        }
        messagebox.showinfo("Profile Created", f"Profile created for {first_name} {last_name}!")
    else:
        messagebox.showinfo("Welcome Back", f"Welcome back, {user_profile['first_name']}!")

    full_checkup_button.config(state=tk.NORMAL) 
    notebook.tab(checkup_tab, state='normal')

    


create_profile_button = tk.Button(welcome_tab, text="Create Profile", command=create_profile , borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2 )
create_profile_button.pack(pady=25)


full_checkup_button.config(state=tk.DISABLED)  
create_profile_button.config(state=tk.DISABLED)  


first_name_entry.bind("<KeyRelease>", check_name_entries) #bind callback function
last_name_entry.bind("<KeyRelease>", check_name_entries) #keyrelease baraye ejraye button



checkup_tab = ttk.Frame(notebook)
notebook.add(checkup_tab, text="Check-up")
notebook.tab(checkup_tab, state='disabled')  


title_label = tk.Label(checkup_tab, text="Enter the data from your check up:", bg="#f3e5ab", font=("Arial", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=4, pady=20)



labels = [
    "WBC", "RBC", "Hb", "Hct", "MCV", "MCHC", "PLT", "Glu",
    "BUN", "Cr", "AST", "ALP", "LDL", "HDL", "TG", "pH",
    "SG", "Blood", "T3", "T4", "FSH", "LH"
]


entries = {}


for i, label in enumerate(labels): #hamzaman i o label too labels dashte bashim
    lbl = tk.Label(checkup_tab, text=f"{label} :", bg="#f3e5ab", font=("Arial", 14, "bold")) #labels
    lbl.grid(row=(i % 11) + 1, column=(i // 11) * 2, padx=10, pady=10, sticky=tk.W)
    
    entry = tk.Entry(checkup_tab, width=15) #fields
    entry.grid(row=(i % 11) + 1, column=(i // 11) * 2 + 1, padx=10, pady=10)
    
    entries[label] = entry



def create_entry_with_placeholder(parent, label, row, column):
   
    entry = tk.Entry(parent, width=15)
    entry.grid(row=row, column=column, padx=10, pady=10)

  
    low, high = normal_values[label]  #matn pishfarz
    placeholder_text = f"{low} - {high}"

    
    entry.insert(0, placeholder_text)
    entry.config(fg='grey')  

   
    def on_focus_in(event):   #vaghti roo field click mishe
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)  
            entry.config(fg='black')  

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder_text)  
            entry.config(fg='grey')  

   
    entry.bind("<FocusIn>", on_focus_in)     #farakhani
    entry.bind("<FocusOut>", on_focus_out)

    return entry



for i, label in enumerate(labels):   #hamzaman i o label too labels dashte bashim
    lbl = tk.Label(checkup_tab, text=f"{label} :", bg="#f3e5ab", font=("Arial", 14, "bold"))  #labels
    lbl.grid(row=(i % 11) + 1, column=(i // 11) * 2, padx=10, pady=10, sticky=tk.W)
    
    
    entry = create_entry_with_placeholder(checkup_tab, label, (i % 11) + 1, (i // 11) * 2 + 1)
    
    entries[label] = entry



clear_button = tk.Button(checkup_tab, text="Clear All", command=clear_all, bg="red", fg="white", font=("Arial", 14, "bold"), borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2)
clear_button.grid(row=12, column=0, pady=20, padx=20, sticky=tk.W)


results_tab = ttk.Frame(notebook)
notebook.add(results_tab, text="Results")
notebook.tab(results_tab, state='disabled')  



continue_button = tk.Button(checkup_tab, text="Continue", command=continue_action, bg="#004c4c", fg="white", font=("Arial", 14, "bold") , borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2)
continue_button.grid(row=12, column=3, pady=20, padx=70, sticky=tk.E)


def download_csv():
    global user_profile
    first_name = user_profile.get('first_name', 'Unknown')   #age nabod unknown
    last_name = user_profile.get('last_name', 'Unknown')

    
    param_names = labels  
    param_values = []

    
    for label in param_names:
        entry_widget = entries[label]  
        value = entry_widget.get().strip()  #strip brye hazf fazaye ezafi vorodi
        param_values.append(value if value else "invalid input")  

    
    with open('results.csv', mode='w', newline='') as file:  #w = mohtava ghabli file delete
        writer = csv.writer(file)

        
        writer.writerow(['Parameter', 'Value'])  
        writer.writerow(['First Name', first_name])  
        writer.writerow(['Last Name', last_name])  
        writer.writerow([]) #fasele

        
        for param_name, param_value in zip(param_names, param_values):   #zip = jof kardan value o name
            writer.writerow([param_name, param_value])  

    messagebox.showinfo("Success", "CSV file downloaded successfully.")







icon = Image.open("logo.png")
icon = icon.resize((32, 32), Image.LANCZOS)  
icon = ImageTk.PhotoImage(icon)  
root.iconphoto(True, icon)



about_tab = ttk.Frame(notebook)
notebook.add(about_tab, text="About Us")

about_label = tk.Label(about_tab, text="About Us", font=("Arial", 22, "bold"), bg="#f3e5ab" )
about_label.pack(pady=20)

about_text = tk.Text(about_tab, wrap=tk.WORD, font=("Arial", 15 , "bold"), bg="#f3e5ab",fg="#004c4c" ,  relief=tk.FLAT)
about_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)



about_description = (
    "This Health Check-up App is designed by arman hooman to provide users with a comprehensive\n"
    "overview of their health check-up results. By entering basic health metrics,\n"
    "users can receive valuable insights, recommendations, and possible diseases\n"
    "to be aware of. Our goal is to promote health awareness and encourage regular\n"
    "check-ups for a healthier life.\n\n"
    "Developed by a dedicated team focused on health education and wellness,\n"
    "this app aims to empower users with the information they need to make\n"
    "informed decisions about their health."


    
)

about_text.insert(tk.END, about_description)


about_email="\n\n\n contact us : armanhooman2525@gmail.com" 





about_text.insert(tk.END, about_email)
about_text.tag_add("email", "end-2l", "end")
about_text.tag_config("email", foreground="#8E44AD", font=("Arial", 15, "italic"))
about_text.insert(tk.END, "\n\n")


about_text.config(state=tk.DISABLED)  


github_button = tk.Button(
    about_tab, 
    text="visit GitHub", 
    font=("Arial", 15, "bold"), 
    bg="#004c4c", 
    fg="white", 
    borderwidth=2, relief="solid", highlightbackground="black", highlightthickness=2 ,
    command=lambda: webbrowser.open("https://github.com/armanhn1010")
)
github_button.pack(pady=10)
about_text.window_create(tk.END, window=github_button)



root.mainloop()
