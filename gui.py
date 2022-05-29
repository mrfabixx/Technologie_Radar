from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# ---- Import from other files ----
import Search_sentiment_analysis
import diagram


class App(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        '''The class App is based on the class Frame from Tkinter, but with some behaviors slightly customized. The 
        App class will need to call code from the Frame class. That's what's happening here: when App is instantiate, 
        Frame is initialized as a  first, and then performs the App-specific initialization. Here App explicitly 
        calls its parent class's __init__() method. Because Tkinter uses "old-style classes", you have to do it the 
        old way here. (Usually you could also do this using the super() function it's basically required in 
        multiple-inheritance scenarios.) '''

        # ---- Label variables ----
        self.search_label_var = StringVar()
        self.hover_label_var = StringVar()
        self.data_label_var = StringVar()
        self.diagram_label_var = StringVar()
        self.msg_label_var = StringVar()
        self.question1_var = StringVar()
        self.question2_var = StringVar()
        self.create_var = StringVar()
        self.save_var = StringVar()
        self.stored_var = StringVar()

        # ======--- Creating Pages -----======
        # ---- Container for Pages ----
        container = Frame(self, bg="#f6f7fb")
        container.pack(side="right", fill="both", expand=True)

        self.frames = {}
        for F in (Page4, Page3, Page2, Page1):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # build form bottom up, so that the program starts with Page1
        # If, for what ever reason, want to start with Page3:
        # you can write for F in (Page4, Page2, Page1, Page3):

        # ---- Frame for Buttons ----
        button_frame = Frame(self, bg="#0f65af")
        button_frame.pack(side="left", fill="both", expand=False)

        # ---- Icons ----
        self.radar_btn = PhotoImage(file="icons/wradar.png", master=self)
        self.databank_btn = PhotoImage(file="icons/wdatabank.png", master=self)
        self.diagram_btn = PhotoImage(file="icons/wdiagram.png", master=self)
        self.settings_btn = PhotoImage(file="icons/wsettings.png", master=self)

        # ======--- Buttons for Page Menu -----======
        # ---- Menu-Buttons and Functions to call the Page ----
        def start():
            self.show_frame('Page1')

        b1 = Button(button_frame, image=self.radar_btn, bg="#0f65af",
                    activebackground="#003055", command=start, relief='raised',
                    borderwidth=0)

        # ----------------
        def data():
            self.show_frame('Page2')

        b2 = Button(button_frame, image=self.databank_btn, bg="#0f65af",
                    activebackground="#003055", command=data, relief='raised',
                    borderwidth=0)

        # ----------------
        def result():
            self.show_frame('Page3')

        b3 = Button(button_frame, image=self.diagram_btn, bg="#0f65af",
                    activebackground="#003055", command=result, relief='raised',
                    borderwidth=0)

        # ----------------
        def settings():
            self.show_frame('Page4')

        b4 = Button(button_frame, image=self.settings_btn, bg="#0f65af",
                    activebackground="#003055", command=settings, relief='raised',
                    borderwidth=0)

        # ---- Button Placements ----
        b1.pack(side="top")
        b2.pack(side="top")
        b3.pack(side="top")
        b4.pack(side="bottom")

    # ======--- Page Call function -----======
    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class Page1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')

        # ---- Search Label ----
        controller.search_label_var.set("Suche")
        label_search = Label(self, textvariable=controller.search_label_var, bg="#f6f7fb")
        label_search.pack(pady=10, anchor='nw')
        # ============================================

        # Keywords
        keywords_entry = ttk.Entry(self)
        keywords_entry.place(relx=0.2, rely=0.1, relwidth=0.53, height=30, anchor=NW)

        def printKeywords(take_keywords):
            keywords_label = Label(self, text=f'Keywords: {take_keywords}', pady=1, bg="#f6f7fb", anchor=W)
            keywords_label.place(relx=0.2, rely=0.2, relwidth=0.5, anchor=NW)

        # Start Button toggle and Warning-Message
        controller.question1_var.set("Wirklich Abbrechen?")
        controller.question2_var.set("Wollen Sie den Vorgang abbrechen?")

        def start_toggle():
            if start_button.config('text')[-1] == 'START':
                start_button.config(text='STOP')
                printKeywords(keywords_entry.get())
                Search_sentiment_analysis.printTweets(keywords_entry.get(), number_posts.get(), True)

            else:
                ab = messagebox.askquestion(controller.question1_var.get(), controller.question2_var.get())
                if ab == "yes":
                    start_button.config(text='START')
                Search_sentiment_analysis.printTweets(None, None, run=False)
                # Search_sentiment_analysis.printTweets(None, None)

        # Start Button
        start_button = Button(self, text="START", font=8, bg="#f9faff", command=start_toggle, state=DISABLED,
                              activebackground='white',
                              borderwidth=0.5)
        start_button.place(relx=0.3, rely=0.8, relheight=0.1, relwidth=0.3, anchor=NW)

        # Icons
        self.facebook_icon = PhotoImage(file="icons/facebook.png", master=self)
        self.linkedin_icon = PhotoImage(file="icons/linkedin.png", master=self)
        self.twitter_icon = PhotoImage(file="icons/twitter.png", master=self)
        self.info_icon = PhotoImage(file="icons/info.png", master=self)

        # selected Icons
        self.bleach_facebook_icon = PhotoImage(file="icons/bleach_facebook.png", master=self)
        self.bleach_linkedin_icon = PhotoImage(file="icons/bleach_linkedin.png", master=self)
        self.bleach_twitter_icon = PhotoImage(file="icons/bleach_twitter.png", master=self)

        # Define a callback function for Link
        def callback():
            webbrowser.open_new_tab('https://de.wikipedia.org/wiki/Sentiment_Detection')

        # Button select
        select_smedia = IntVar()

        # select_smedia.set(1)

        def select():
            selected_media = select_smedia.get()
            print(selected_media)
            if selected_media is None:
                start_button['state'] = DISABLED
            else:
                start_button['state'] = NORMAL

        # =====--------- Buttons -----------========
        facebook_btn = Radiobutton(self, image=self.bleach_facebook_icon, variable=select_smedia, value=1,
                                   command=select, bg="#f6f7fb", selectimage=self.facebook_icon, selectcolor="#f6f7fb",
                                   indicatoron=FALSE, activebackground="#f6f7fb", borderwidth=0)
        linkedin_btn = Radiobutton(self, image=self.bleach_linkedin_icon, variable=select_smedia, value=2,
                                   command=select, bg="#f6f7fb", selectimage=self.linkedin_icon, selectcolor="#f6f7fb",
                                   indicatoron=FALSE, activebackground="#f6f7fb", borderwidth=0)
        twitter_btn = Radiobutton(self, image=self.bleach_twitter_icon, variable=select_smedia, value=3,
                                  command=select, bg="#f6f7fb", selectimage=self.twitter_icon, selectcolor="#f6f7fb",
                                  indicatoron=FALSE, activebackground="#f6f7fb", borderwidth=0)

        # --------- Info Button & Hover tip ---------
        info_btn = Button(self, image=self.info_icon, bg="#f6f7fb", command=callback,
                          activebackground="#f6f7fb", borderwidth=0)

        # Hover-tip
        controller.hover_label_var.set("Was ist eine Sentiment Analyse?")
        hover_label = Label(textvariable=controller.hover_label_var, bg="#ffffff", relief='raised')

        # --------- Hovertip function ---------
        def changeOnHover(button):
            button.bind("<Enter>", func=lambda e: hover_label.place(relx=0.95, rely=0.01, anchor=NE))

            # forget on leving widget
            button.bind("<Leave>", func=lambda e: hover_label.place_forget())

        changeOnHover(info_btn)
        info_btn.place(relx=1, rely=0, anchor=NE)

        # ============================================
        # ======--- number entry  -----======
        number_posts = ttk.Entry(self, justify=CENTER)
        number_posts.place(relx=0.3, rely=0.6, relwidth=0.3, anchor=NW)

        # Message Label post count
        controller.msg_label_var.set("Anzahl der Posts")
        msg = Label(self, textvariable=controller.msg_label_var, font=("Times", 12), bg="#f6f7fb")
        msg.place(relx=0.3, rely=0.65, relheight=0.1, relwidth=0.3, anchor=NW)

        # Placements
        facebook_btn.place(relx=0.2, rely=0.3, height=100, anchor=NW)
        linkedin_btn.place(relx=0.4, rely=0.3, height=100, anchor=NW)
        twitter_btn.place(relx=0.6, rely=0.3, height=100, anchor=NW)
        # ============================================


class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')

        # ---- Database Label ----
        controller.data_label_var.set('Datenbank')
        label = Label(self, textvariable=controller.data_label_var, bg="#f6f7fb")
        label.pack(pady=10, anchor='nw')

        # ======--- text field -----======
        text_input = Text(self, height=15, bg="white", font=("arial", 14, 'bold'))
        text_input.pack(anchor=N, expand=True)

        # --------- functions ---------
        def create():
            text_input.delete('1.0', END)
            text_input.insert(END, f'[postgresql]\n')
            text_input.insert(END, f"\nhost=")
            text_input.insert(END, f"\ndatabase=")
            text_input.insert(END, f"\nuser=")
            text_input.insert(END, f"\npassword=")
            text_input.insert(END, f"\nport=")

        # ----------------
        def save():
            text_file = open('dbcon.ini', 'w')
            text_file.write(text_input.get(1.0, END))
            text_file.close()

        # ----------------
        def stored():
            text_input.delete('1.0', END)
            try:
                f = open('dbcon.ini')
                text_input.insert(1.0, f.read())

            except:
                text_input.insert(END, f'No data saved')

        # --------- auto-input ---------
        try:
            stored()

        except:
            create()

        # =====--------- language vars -----------========
        controller.create_var.set('Neu')
        controller.save_var.set('Speichern')
        controller.stored_var.set('Gespeichert')

        # =====--------- Buttons -----------========

        # ---- button frame ----
        button_frame = Frame(self)
        button_frame.pack()
        # ---- buttons ----
        create_button = Button(button_frame, textvariable=controller.create_var, bg="white", height=3,
                               width=10, command=create, bd=0, fg="black", activebackground='#0f65af')
        create_button.grid(row=0, column=2, padx=2)
        # ----------------
        save_button = Button(button_frame, textvariable=controller.save_var, bg="white", height=3,
                             width=10, command=save, bd=0, fg="black", activebackground='#0f65af')
        save_button.grid(row=0, column=0, padx=2)
        # ----------------
        stored_button = Button(button_frame, textvariable=controller.stored_var, bg="white", height=3,
                               width=10, command=stored, bd=0, fg="black", activebackground='#0f65af')
        stored_button.grid(row=0, column=1, padx=2)
        # ============================================


class Page3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')

        # ---- Diagram Label ----
        controller.diagram_label_var.set('Diagramm')
        label = Label(self, textvariable=controller.diagram_label_var, bg="#f6f7fb")
        label.pack(anchor=NW)

        # =====--------- Diagram -----------========

        # ---- Create Canvas and displaying Diagram ----
        def draw_canvas():
            fig = diagram.display_diagram()
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.get_tk_widget().pack(anchor=N)
            canvas.draw()

        # ---- Export Diagram ----
        def export():
            a = asksaveasfilename(filetypes=(("PNG Image", "*.png"), ("All Files", "*.*")),
                                  defaultextension='.png')
            if a:
                fig = diagram.display_diagram()
                fig.savefig(a)

        # =====--------- Buttons -----------========
        # ---- Download Button ----
        self.download_icon = PhotoImage(file="icons/download.png", master=self)
        download_icon = Button(self, image=self.download_icon, bg="#f6f7fb", command=export,
                               bd=0.5, activebackground='#0f65af', activeforeground='white')
        download_icon.pack(anchor=NW)

        # ---- Display Button ----
        self.pie_icon = PhotoImage(file="icons/diagram.png", master=self)
        pie_icon = Button(self, image=self.pie_icon, bg="white", command=draw_canvas,
                          bd=0.5, activebackground='#0f65af', activeforeground='white')

        pie_icon.pack(anchor=NW)
        # ============================================


class Page4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')

        # controller is used to control the StringVars,
        # rather than make a widget responsible for global changes.
        # Same as parent is used for the pages container
        self.controller = controller

        # =====--------- Languages Selection -----------========
        # ---- Language Label ----
        lang_label_var = StringVar()
        lang_label_var.set('Sprache:')
        label_lang = Label(self,
                           textvariable=lang_label_var, bg="#f6f7fb")
        label_lang.place(relx=0.1, rely=0.4)

        # ---- Combobox for selecting Language ----
        selected_lang = StringVar()
        selected_lang.set('Deutsch')
        languages = ttk.Combobox(self, textvariable=selected_lang)

        # ---- Languages ----
        languages['values'] = ['Deutsch', 'English', 'Česky']
        languages['state'] = 'readonly'
        # place the Language-select widget
        languages.place(relx=0.2, rely=0.4)

        # ======--- Language StringVars -----======
        def language_change(choice):
            choice = selected_lang.get()
            # =====--------- Language words -----------========
            if choice == 'Deutsch':

                lang_label_var.set('Sprache:')
                controller.search_label_var.set('Suche')
                controller.hover_label_var.set("Was ist eine Sentiment Analyse?")
                controller.data_label_var.set('Datenbank')
                controller.diagram_label_var.set('Diagramm')
                controller.msg_label_var.set("Anzahl der Posts")
                controller.question1_var.set("Wirklich Abbrechen?")
                controller.question2_var.set("Wollen Sie den Vorgang abbrechen?")
                controller.create_var.set('Neu')
                controller.save_var.set('Speichern')
                controller.stored_var.set('Gespeichert')

            elif choice == 'English':

                lang_label_var.set('Language:')
                controller.search_label_var.set('Search')
                controller.hover_label_var.set("What is Sentiment Analysis?")
                controller.data_label_var.set('Database')
                controller.diagram_label_var.set('Diagram')
                controller.msg_label_var.set("Number of posts")
                controller.question1_var.set("Warning!")
                controller.question2_var.set("Do you want to abort the process?")
                controller.create_var.set('New')
                controller.save_var.set('Save')
                controller.stored_var.set('Stored')

            elif choice == 'Česky':

                lang_label_var.set('Jazyk:')
                controller.search_label_var.set('Vyhledávání')
                controller.hover_label_var.set("Co je analýza sentimentu?")
                controller.data_label_var.set('Databáze')
                controller.diagram_label_var.set('Diagram')
                controller.msg_label_var.set("Počet příspěvků")
                controller.question1_var.set("Varování!")
                controller.question2_var.set("Chcete proces přerušit?")
                controller.create_var.set('Nový')
                controller.save_var.set('Uložit')
                controller.stored_var.set('Uloženo')

        languages.bind('<<ComboboxSelected>>', language_change)

        # --------- Link callback Function ---------
        def callback(url):
            webbrowser.open_new_tab(url)

        self.logo_png = PhotoImage(file="icons/Logo.png", master=self)

        # ---- Link and Name Labels ----
        link = Label(self, text="Github", bg="#f6f7fb",
                     font=('Helveticabold', 12), fg="blue", cursor="hand2")
        readmelink = Label(self, text="readme", bg="#f6f7fb",
                           font=('Helveticabold', 12), fg="blue", cursor="hand2")
        logo = Label(self, image=self.logo_png, bg="#f6f7fb")
        vt = Label(self, text="Technologie-Radar\nCopyright ⓒ 2022 \nVersion 1.0", bg="#f6f7fb")

        link.bind('<Button-1>', lambda e: callback("https://github.com/mrfabixx/Technologie_Radar"))
        readmelink.bind('<Button-1>', lambda e: callback("README.md"))

        # ---- Placements ----
        vt.place(relx=0.1, rely=0.2)
        link.place(relx=0.1, rely=.55)
        readmelink.place(relx=0.1, rely=.6)
        logo.place(relx=1, rely=1, anchor=SE)


if __name__ == "__main__":
    root = Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    root.title('Technologie Radar')
    root.iconbitmap('Logo.ico')
    root.wm_geometry('800x600')
    root.minsize(900, 675)
    # root.resizable(width=False, height=False)
    root.mainloop()
