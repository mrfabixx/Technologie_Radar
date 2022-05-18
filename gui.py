from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import messagebox
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import Search_sentiment_analysis


class App(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        # Label variables
        self.search_label_var = StringVar()
        self.hover_label_var = StringVar()
        self.data_label_var = StringVar()
        self.diagram_label_var = StringVar()
        self.msg_label_var = StringVar()
        self.question1_var = StringVar()
        self.question2_var = StringVar()

        '''Creating Pages'''
        container = Frame(self, bg="#f6f7fb")
        container.pack(side="right", fill="both", expand=True)

        self.frames = {}
        for F in (Page4, Page3, Page2, Page1):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        button_frame = Frame(self, bg="#0f65af")
        button_frame.pack(side="left", fill="both", expand=False)

        # Icons
        self.radar_btn = PhotoImage(file="icons/wradar.png")
        self.databank_btn = PhotoImage(file="icons/wdatabank.png")
        self.diagram_btn = PhotoImage(file="icons/wdiagram.png")
        self.settings_btn = PhotoImage(file="icons/wsettings.png")

        # Buttons for Pages
        def start():
            self.show_frame('Page1')

        b1 = Button(button_frame, image=self.radar_btn, bg="#0f65af",
                    activebackground="#003055", command=start, relief='raised',
                    borderwidth=0)

        def data():
            self.show_frame('Page2')

        b2 = Button(button_frame, image=self.databank_btn, bg="#0f65af",
                    activebackground="#003055", command=data, relief='raised',
                    borderwidth=0)

        def result():
            self.show_frame('Page3')

        b3 = Button(button_frame, image=self.diagram_btn, bg="#0f65af",
                    activebackground="#003055", command=result, relief='raised',
                    borderwidth=0)

        def settings():
            self.show_frame('Page4')

        b4 = Button(button_frame, image=self.settings_btn, bg="#0f65af",
                    activebackground="#003055", command=settings, relief='raised',
                    borderwidth=0)

        b1.pack(side="top")
        b2.pack(side="top")
        b3.pack(side="top")
        b4.pack(side="bottom")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Page1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')

        # label
        controller.search_label_var.set("Suche")
        label_search = Label(self, textvariable=controller.search_label_var, bg="#f6f7fb")
        label_search.place(x=2, y=2)

        # Keywords
        keywords_entry = ttk.Entry(self)

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
                Search_sentiment_analysis.printTweets(keywords_entry.get())
                Search_sentiment_analysis.result_quantity(number_posts.get())

            else:
                ab = messagebox.askquestion(controller.question1_var.get(), controller.question2_var.get())
                if ab == "yes":
                    start_button.config(text='START')
                    printKeywords('')

        # Icons
        self.facebook_icon = PhotoImage(file="icons/facebook.png")
        self.linkedin_icon = PhotoImage(file="icons/linkedin.png")
        self.twitter_icon = PhotoImage(file="icons/twitter.png")
        self.info_icon = PhotoImage(file="icons/info.png")

        # selected Icons
        self.bleach_facebook_icon = PhotoImage(file="icons/bleach_facebook.png")
        self.bleach_linkedin_icon = PhotoImage(file="icons/bleach_linkedin.png")
        self.bleach_twitter_icon = PhotoImage(file="icons/bleach_twitter.png")

        # Define a callback function for Link
        def callback():
            webbrowser.open_new_tab('https://de.wikipedia.org/wiki/Sentiment_Detection')

        # Button select
        select_smedia = StringVar()
        select_smedia.set("facebook")

        def select():
            selected_media = select_smedia.get()
            print(selected_media)

        # Buttons
        facebook_btn = Radiobutton(self, image=self.bleach_facebook_icon, variable=select_smedia, value=1,
                                   command=select, bg="#f6f7fb", selectimage=self.facebook_icon, selectcolor="#f6f7fb",
                                   indicatoron=0, activebackground="#f6f7fb", borderwidth=0)
        linkedin_btn = Radiobutton(self, image=self.bleach_linkedin_icon, variable=select_smedia, value=2,
                                   command=select, bg="#f6f7fb", selectimage=self.linkedin_icon, selectcolor="#f6f7fb",
                                   indicatoron=0, activebackground="#f6f7fb", borderwidth=0)
        twitter_btn = Radiobutton(self, image=self.bleach_twitter_icon, variable=select_smedia, value=3,
                                  command=select, bg="#f6f7fb", selectimage=self.twitter_icon, selectcolor="#f6f7fb",
                                  indicatoron=0, activebackground="#f6f7fb", borderwidth=0)

        # Info Button and hovertip
        info_btn = Button(self, image=self.info_icon, bg="#f6f7fb", command=callback,
                          activebackground="#f6f7fb", borderwidth=0)

        # Hover-tip
        controller.hover_label_var.set("Was ist eine Sentiment Analyse?")

        hover_label = Label(textvariable=controller.hover_label_var, bg="#ffffff", relief='raised')

        # function to appear , when button on hover
        def changeOnHover(button):
            button.bind("<Enter>", func=lambda e: hover_label.place(relx=0.95, rely=0.01, anchor=NE))

            # forget on leving widget
            button.bind("<Leave>", func=lambda e: hover_label.place_forget())

        changeOnHover(info_btn)

        info_btn.place(relx=1, rely=0, anchor=NE)

        # Start Button
        start_button = Button(self, text="START", font=8, bg="#f9faff", command=start_toggle, activebackground='white',
                              borderwidth=0.5)
        start_button.place(relx=0.3, rely=0.8, relheight=0.1, relwidth=0.3, anchor=NW)

        def select_post_count(selected_quantity):
            Search_sentiment_analysis.result_quantity(count=selected_quantity)

        # Number of posts in Spinbox
        number_posts = ttk.Entry(self, justify=CENTER)
        number_posts.place(relx=0.3, rely=0.6, relwidth=0.3, anchor=NW)

        controller.msg_label_var.set("Anzahl der Posts")
        msg = Label(self, textvariable=controller.msg_label_var, font=("Times", 12), bg="#f6f7fb")
        msg.place(relx=0.3, rely=0.65, relheight=0.1, relwidth=0.3, anchor=NW)

        # Placements
        keywords_entry.place(relx=0.2, rely=0.1, relwidth=0.53, height=30, anchor=NW)
        facebook_btn.place(relx=0.2, rely=0.3, height=100, anchor=NW)
        linkedin_btn.place(relx=0.4, rely=0.3, height=100, anchor=NW)
        twitter_btn.place(relx=0.6, rely=0.3, height=100, anchor=NW)


class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')

        controller.data_label_var.set('Datenbank')
        label = Label(self, textvariable=controller.data_label_var, bg="#f6f7fb")
        label.place(x=2, y=2)

        # dataset = 0
        # dataset_count = Label(self, text=f'Datensätze . . . . . . . . . . . . . . . . . . . .  {dataset}',
        #                       bg="#f6f7fb", anchor=W)
        #
        # dataset_count.place(relx=0.2, rely=0.1, relwidth=0.5, height=30, anchor=NW)


class Page3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')

        # Label diagram
        controller.diagram_label_var.set('Diagramm')
        label = Label(self, textvariable=controller.diagram_label_var, bg="#f6f7fb")
        label.place(x=2, y=2)

        # plot function
        def plot():
            '''example diagram'''

            # x-axis values in a list
            x = [7, 2, 5]

            # y-axis values in a list
            stimmen = ['Positiv', 'Negativ', 'Neutral']

            fig = Figure(figsize=(5, 5), facecolor='#f6f7fb')
            a = fig.add_subplot(111)
            a.pie(x, labels=stimmen)

            # diagram displayed on canvas
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.get_tk_widget().pack()
            canvas.draw()

        # Button for showing diagram
        self.pie_icon = PhotoImage(file="icons/diagram.png")
        pie_icon = Button(self, image=self.pie_icon, bg="#f6f7fb", command=plot,
                          activebackground="#f6f7fb")

        pie_icon.place(relx=0, rely=0, anchor=NW)

        # export function
        def export():
            file = filedialog.asksaveasfile(mode='w', defaultextension=".pdf",
                                            filetypes=(("PDF file", "Technologie-Radar.pdf"), ("All Files", "*.*")))
            if file:
                fig.save()  # saves the image to the input file name.

        self.download_icon = PhotoImage(file="icons/download.png")
        download_icon = Button(self, image=self.download_icon, bg="#f6f7fb", command=export,
                               activebackground="#f6f7fb", borderwidth=0.5)
        download_icon.place(relx=0.95, rely=0.95, anchor=SE)


class Page4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')

        self.controller = controller

        lang_label_var = StringVar()
        lang_label_var.set('Sprache:')
        label_lang = Label(self,
                           textvariable=lang_label_var, bg="#f6f7fb")
        label_lang.place(relx=0.1, rely=0.4)

        # create a combobox
        selected_lang = StringVar()
        selected_lang.set('Deutsch')
        languages = ttk.Combobox(self, textvariable=selected_lang)

        # languages
        languages['values'] = ['Deutsch', 'English', 'Česky']

        # prevent typing a value
        languages['state'] = 'readonly'

        # place the Language-select widget
        languages.place(relx=0.2, rely=0.4)

        # bind the selected value changes
        def language_change(event):
            choice = selected_lang.get()
            '''Languages'''
            if choice == 'Deutsch':

                lang_label_var.set('Sprache:')
                controller.search_label_var.set('Suche')
                controller.hover_label_var.set("Was ist eine Sentiment Analyse?")
                controller.data_label_var.set('Datenbank')
                controller.diagram_label_var.set('Diagramm')
                controller.msg_label_var.set("Anzahl der Posts")
                controller.question1_var.set("Wirklich Abbrechen?")
                controller.question2_var.set("Wollen Sie den Vorgang abbrechen?")

            elif choice == 'English':

                lang_label_var.set('Language:')
                controller.search_label_var.set('Search')
                controller.hover_label_var.set("What is Sentiment Analysis?")
                controller.data_label_var.set('Database')
                controller.diagram_label_var.set('Diagram')
                controller.msg_label_var.set("Number of posts")
                controller.question1_var.set("Warning!")
                controller.question2_var.set("Do you want to abort the process?")

            elif choice == 'Česky':

                lang_label_var.set('Jazyk:')
                controller.search_label_var.set('Vyhledávání')
                controller.hover_label_var.set("Co je to analýza sentimentu?")
                controller.data_label_var.set('Databáze')
                controller.diagram_label_var.set('Diagram')
                controller.msg_label_var.set("Počet příspěvků")
                controller.question1_var.set("Varování!")
                controller.question2_var.set("Chcete proces přerušit?")

        languages.bind('<<ComboboxSelected>>', language_change)

        # Define a callback function for Link
        def callback(url):
            webbrowser.open_new_tab(url)

        self.logo_png = PhotoImage(file="icons/Logo.png")

        # Labels
        link = Label(self, text="Github", bg="#f6f7fb",
                     font=('Helveticabold', 12), fg="blue", cursor="hand2")
        readmelink = Label(self, text="readme", bg="#f6f7fb",
                           font=('Helveticabold', 12), fg="blue", cursor="hand2")
        logo = Label(self, image=self.logo_png, bg="#f6f7fb")
        vt = Label(self, text="Technologie-Radar\nCopyright ⓒ 2022 \nVersion 1.0", bg="#f6f7fb")

        link.bind('<Button-1>', lambda e: callback("https://github.com/mrfabixx/Technologie_Radar"))
        readmelink.bind('<Button-1>', lambda e: callback("README.md"))

        # Placements
        vt.place(relx=0.1, rely=0.2)
        link.place(relx=0.1, rely=.55)
        readmelink.place(relx=0.1, rely=.6)
        logo.place(relx=1, rely=1, anchor=SE)


if __name__ == "__main__":
    root = Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    root.title('Technologie Radar')
    root.iconbitmap('icons/Logo.ico')
    root.wm_geometry('800x600')
    root.minsize(800, 600)
    # root.resizable(width=False, height=False)
    root.mainloop()
