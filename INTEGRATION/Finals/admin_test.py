from tkinter import Frame
import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector

side_panel_bg = "#3f3f3f"
side_panel_font = "Montserrat, 15"
admin_panel_item_font= "Montserrat, 25"

mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')

mycursor = mydb.cursor(buffered=True)



#################  KEYBOARD SHORTCUTS   ######################



##############################################################

# BUTTON FUNCTION
def admin_panel():
    root = tk.Tk()
    root.title("Admin")
    root.geometry("1920x1080")
    # root.iconbitmap("DBMS-Project/work files/Noyal/Q.ico")
    root.iconbitmap("Q.ico")

    def exit_window(e): root.destroy() # to exit window



    def dashboard():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
            widget.destroy()

        admin_panel_label = tk.Label(content_frame, text="Admin Panel", font="Montserrat, 45", bg="white")
        admin_panel_label.pack(pady=30)

        admin_panel_items_frame = tk.Label(content_frame, bg="white")
        admin_panel_items_frame.pack()

        mycursor.execute("SELECT COUNT(DISTINCT(EMAIL)) FROM PLAYERS")
        tot_users = mycursor.fetchall()[0][0] # selecting req value from output: [(5,)]
        mycursor.execute('SELECT COUNT(DISTINCT(CATEGORY_NAME)) FROM CATEGORIES')
        tot_cate = mycursor.fetchall()[0][0]
        mycursor.execute('SELECT COUNT(DISTINCT(Q_NO)) FROM QUESTIONS')
        tot_qns = mycursor.fetchall()[0][0]

        total_user_label = tk.Label(admin_panel_items_frame, text=f"Total Users\n\n{tot_users}", font=admin_panel_item_font, bg="#9747FF", padx=30, pady=20)
        total_user_label.grid(row=0, column=0, padx=50, pady=100)

        total_categories_label = tk.Label(admin_panel_items_frame, text=f"Total Categories\n\n{tot_cate}", font=admin_panel_item_font, bg="#60F93E", padx=30, pady=20)
        total_categories_label.grid(row=0, column=1, padx=50)

        total_question_label = tk.Label(admin_panel_items_frame, text=f"Total Questions\n\n{tot_qns}", font=admin_panel_item_font, bg="#6BFFFF", padx=30, pady=20)
        total_question_label.grid(row=0, column=2, padx=50)

        # Notification Frame
        notification_frame = tk.LabelFrame(admin_panel_items_frame, bg="#F0F0F0")#,width=100, height=250)
        notification_frame.grid(row=1, column=2)

        notification_label = tk.Label(notification_frame, text="Notifications", padx=10, font="Montserrat, 25",width=10, height=3)
        notification_label.pack()

        # notif = mycursor.execute('select * from report') # enable after table creation
        notification_label = tk.Label(notification_frame, text="No new reports", padx=30, font="Montserrat, 25")
        notification_label.pack(pady=20)

        mycursor.execute("SELECT * FROM players")
        results = mycursor.fetchall() # Retrieve the query results
        column_names = [column[0] for column in mycursor.description] # Get the column names

        frame = Frame(admin_panel_items_frame, bg='white')
        frame.place(x=350, y=460, anchor="center") # to change position of table

        # Create a label for each column and place it in the frame
        labels = []
        for i, column_name in enumerate(column_names):
            label = tk.Label(frame, text=column_name,font=('Montserrat', 15), bg='white')
            label.grid(row=0, column=i)
            labels.append(label)

        # Create a label for each row and place it in the frame
        for i, row in enumerate(results):
            for j, col in enumerate(row):
                label = tk.Label(frame, text=col,font=('Montserrat', 12), bg='white')
                label.grid(row=i+1, column=j)
                labels.append(label)



    def question_controls():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
            widget.destroy()

        question_controls_label = tk.Label(content_frame, bg="white", text="Question Controls", font="Montserrat, 55")
        question_controls_label.pack(pady=30)

        question_controls_frame = tk.Frame(content_frame, bg="white")
        question_controls_frame.pack()

        add_question_button = tk.Button(question_controls_frame, bg="#F0F0F0", text="Add Question", padx=10, pady=5, font="motserrat, 25", command=add_question)
        add_question_button.grid(row=0, column=0)

        update_question_button = tk.Button(question_controls_frame, bg="#F0F0F0", text="Update Question", padx=10, pady=5, font="motserrat, 25", command=update_question)
        update_question_button.grid(row=0, column=1, padx=200, pady=50)

        delete_question_button = tk.Button(question_controls_frame, bg="#F0F0F0", text="Delete Question", padx=10, pady=5, font="motserrat, 25", command=delete_question)
        delete_question_button.grid(row=0, column=2)



    def user_controls():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
            widget.destroy()

        user_controls_label = tk.Label(content_frame, bg="white", text="User Controls", font="Montserrat, 55")
        user_controls_label.pack(pady=30)

        user_controls_frame = tk.Frame(content_frame, bg="white")
        user_controls_frame.pack()

        add_user_button = tk.Button(user_controls_frame, bg="#F0F0F0", text="Add User", padx=10, pady=5, font="motserrat, 25")
        add_user_button.grid(row=0, column=0)

        update_user_button = tk.Button(user_controls_frame, bg="#F0F0F0", text="Update User", padx=10, pady=5, font="motserrat, 25")
        update_user_button.grid(row=0, column=1, padx=200, pady=50)

        delete_user_button = tk.Button(user_controls_frame, bg="#F0F0F0", text="Delete User", padx=10, pady=5, font="motserrat, 25")
        delete_user_button.grid(row=0, column=2)


    """

    # TO BE COMPLETED IF WE GET TIME

    def statistics():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
            widget.destroy()

    def user_reports():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
            widget.destroy()
    """



    # SUB BUTTON FUNCTION


    def add_question():

        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
            widget.destroy()

        question_controls()

        add_question_frame = tk.LabelFrame(content_frame, text="Add Question", font=admin_panel_item_font)
        add_question_frame.pack()


        question_title_label = tk.Label(add_question_frame, text="Enter question title", font=side_panel_font, justify="left")
        question_title_label.grid(row=0, column=0, sticky="w", padx=60)

        entry_question_title = tk.Entry(add_question_frame, borderwidth=5, width=160)
        entry_question_title.grid(row=1, column=0, columnspan=3, padx=60)


        option_1_label = tk.Label(add_question_frame, text="Option 1", font=side_panel_font)
        option_1_label.grid(row=2, column=0, sticky="w", pady=15, padx=60)
        option_1_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        option_1_entry.grid(row=3, column=0, sticky="w", padx=60)


        option_3_label = tk.Label(add_question_frame, text="Option 3", font=side_panel_font)
        option_3_label.grid(row=4, column=0, sticky="w", padx=60)
        option_3_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        option_3_entry.grid(row=5, column=0, sticky="w", pady=15, padx=60)

        correct_answer_label = tk.Label(add_question_frame, text="Correct Answer", font=side_panel_font)
        correct_answer_label.grid(row=6, column=0, sticky="w", padx=60)
        correct_answer_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        correct_answer_entry.grid(row=7, column=0, sticky="w", pady=15, padx=60)

        option_2_label = tk.Label(add_question_frame, text="Option 2", font=side_panel_font)
        option_2_label.grid(row=2, column=2, sticky="w", padx=60)
        option_2_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        option_2_entry.grid(row=3, column=2, sticky="w", pady=15, padx=60)


        option_4_label = tk.Label(add_question_frame, text="Option 4", font=side_panel_font)
        option_4_label.grid(row=4, column=2, sticky="w", padx=60)
        option_4_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        option_4_entry.grid(row=5, column=2, sticky="w", padx=60)

        Question_Category_label = tk.Label(add_question_frame, text="Question Category", font=side_panel_font)
        Question_Category_label.grid(row=6, column=2, sticky="w", padx=60)
        Question_Category_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        Question_Category_entry.grid(row=7, column=2, sticky="w", padx=60)

        add_question_button = tk.Button(add_question_frame, text="Add Question", font="motserrat, 25")
        add_question_button.grid(column=1, pady=30)


    def update_question():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
            widget.destroy()

        question_controls()
        add_question_frame = tk.LabelFrame(content_frame, text="Update Question", font=admin_panel_item_font)
        add_question_frame.pack()

        question_title_label = tk.Label(add_question_frame, text="Question title", font=side_panel_font, justify="left")
        question_title_label.grid(row=0, column=0, sticky="w", padx=60)

        entry_question_title = tk.Entry(add_question_frame, borderwidth=5, width=160)
        entry_question_title.grid(row=1, column=0, columnspan=3, padx=60)


        option_1_label = tk.Label(add_question_frame, text="Option 1", font=side_panel_font)
        option_1_label.grid(row=2, column=0, sticky="w", pady=15, padx=60)
        option_1_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        option_1_entry.grid(row=3, column=0, sticky="w", padx=60)


        option_3_label = tk.Label(add_question_frame, text="Option 3", font=side_panel_font)
        option_3_label.grid(row=4, column=0, sticky="w", padx=60)
        option_3_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        option_3_entry.grid(row=5, column=0, sticky="w", pady=15, padx=60)

        correct_answer_label = tk.Label(add_question_frame, text="Correct Answer", font=side_panel_font)
        correct_answer_label.grid(row=6, column=0, sticky="w", padx=60)
        correct_answer_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        correct_answer_entry.grid(row=7, column=0, sticky="w", pady=15, padx=60)

        option_2_label = tk.Label(add_question_frame, text="Option 2", font=side_panel_font)
        option_2_label.grid(row=2, column=2, sticky="w", padx=60)
        option_2_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        option_2_entry.grid(row=3, column=2, sticky="w", pady=15, padx=60)


        option_4_label = tk.Label(add_question_frame, text="Option 4", font=side_panel_font)
        option_4_label.grid(row=4, column=2, sticky="w", padx=60)
        option_4_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        option_4_entry.grid(row=5, column=2, sticky="w", padx=60)

        Question_Category_label = tk.Label(add_question_frame, text="Question Category", font=side_panel_font)
        Question_Category_label.grid(row=6, column=2, sticky="w", padx=60)
        Question_Category_entry = tk.Entry(add_question_frame, borderwidth=5, width=50)
        Question_Category_entry.grid(row=7, column=2, sticky="w", padx=60)

        add_question_button = tk.Button(add_question_frame, text="Add Question", font="motserrat, 25")
        add_question_button.grid(column=1, pady=30)


    def delete_question():
        pass





    # Admin image, used in side panel.
    # admin_img = ImageTk.PhotoImage(Image.open("DBMS-Project/work files/Noyal/admin_white.png"))
    admin_img = ImageTk.PhotoImage(Image.open("admin_white.png"))




    # Side Pannel
    side_panel = tk.Frame(root, bg=side_panel_bg,)
    side_panel.pack(side="left", fill="y")



    # Admin main icon label
    admin_icon_label = tk.Label(side_panel, image=admin_img, bg=side_panel_bg)
    admin_icon_label.pack(pady=35)

    admin_dashboard_button = tk.Button(side_panel, text="Admin Dashboard", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=dashboard)
    admin_dashboard_button.pack(padx=50)

    question_controls_button = tk.Button(side_panel, text="Question Controls", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=question_controls)
    question_controls_button.pack(padx=50, pady=20)

    user_controls_button = tk.Button(side_panel, text="User Controls", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=user_controls)
    user_controls_button.pack(padx=50)

    user_reports_button = tk.Button(side_panel, text="User Reports", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg) # , command=user_reports)
    user_reports_button.pack(padx=50, pady=20)

    statistics_button = tk.Button(side_panel, text="Statistics", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg)# , command=statistics)
    statistics_button.pack(padx=50, pady=20)


    # Content Frame
    content_frame = tk.Frame(root, bg="white")
    content_frame.pack(fill="both", expand="true")

    dashboard()

    root.bind('<Escape>', exit_window)
# root.mainloop()