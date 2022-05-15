from tkinter import *
import webbrowser
from tkinter import messagebox
from matplotlib import pyplot as plt
from idlelib.tooltip import Hovertip


import Search_sentiment_analysis


class App(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.controller = 'Page1'
        container = Frame(self, bg="#f6f7fb")
        container.pack(side="right", fill="both", expand=True)

        self.frames = {}
        for F in (Page1, Page2, Page3, Page4):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.show_frame("Page1")

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
        self.controller = controller

        label = Label(self, text="Radar", bg="#f6f7fb")
        label.place(x=2, y=2)

        # Keywords
        keywords_entry = Entry(self)

        def printKeywords(take_keywords):
            keywords_label = Label(self, text=f'Keywords: {take_keywords}', pady=1, bg="#f6f7fb", anchor=W)
            keywords_label.place(relx=0.2, rely=0.2, relwidth=0.5, anchor=NW)

        # Start Button toggle and Warning-Message
        def start_toggle():
            if start_button.config('text')[-1] == 'START':
                start_button.config(text='STOP')
                printKeywords(keywords_entry.get())
                Search_sentiment_analysis.printTweets(keywords_entry.get())

            else:
                ab = messagebox.askquestion("Wirklich Abbrechen?", "Wollen Sie den Vorgang abbrechen?")
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
        info_btn = Button(self, image=self.info_icon, bg="#f6f7fb", command=callback,
                          activebackground="#f6f7fb", borderwidth=0)

        # Hovertips
        Hovertip(info_btn, 'Was ist eine Sentiment Analyse?')

        # Enter Keywords Button
        # enter_button = Button(self, text="Enter", padx=10, pady=5, command=printKeywords, borderwidth=1)

        # Start Button
        start_button = Button(self, text="START", font=8, bg="#f9faff", command=start_toggle, activebackground='white',
                              borderwidth=0.5)

        # Number of posts in Spinbox
        number_posts = Spinbox(self, from_=0, to=999999999, justify=CENTER)
        number_posts.place(relx=0.3, rely=0.6, relwidth=0.3, anchor=NW)

        msg = Label(self, text="Anzahl der Posts", font=("Times", 12), bg="#f6f7fb")
        msg.place(relx=0.3, rely=0.65, relheight=0.1, relwidth=0.3, anchor=NW)

        # Placements
        keywords_entry.place(relx=0.2, rely=0.1, relwidth=0.53, height=30, anchor=NW)
        # enter_button.place(relx=0.75, rely=0.1, anchor=N)
        facebook_btn.place(relx=0.2, rely=0.3, height=100, anchor=NW)
        linkedin_btn.place(relx=0.4, rely=0.3, height=100, anchor=NW)
        twitter_btn.place(relx=0.6, rely=0.3, height=100, anchor=NW)
        start_button.place(relx=0.3, rely=0.8, relheight=0.1, relwidth=0.3, anchor=NW)
        info_btn.place(relx=1, rely=0, anchor=NE)


class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')
        self.controller = controller

        label = Label(self, text="Databank", bg="#f6f7fb")

        dataset = 0
        dataset_count = Label(self, text=f'Datensätze . . . . . . . . . . . . . . . . . . . .  {dataset}',
                              bg="#f6f7fb", anchor=W)

        dataset_count.place(relx=0.2, rely=0.1, relwidth=0.5, height=30, anchor=NW)
        label.place(x=2, y=2)


class Page3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')
        self.controller = controller

        label = Label(self, text="Diagram", bg="#f6f7fb")

        # x-axis values in a list
        x = [7, 2, 5]

        # y-axis values in a list
        stimmen = ['Positiv', 'Negativ', 'Neutral']

        self.pie_icon = PhotoImage(file="icons/diagram.png")
        pie_icon = Button(self, image=self.pie_icon, bg="#f6f7fb", command=lambda: plt.show(),
                          activebackground="#f6f7fb")

        def export():
            plt.pie(x, labels=stimmen)
            plt.savefig('Technologie-Radar.pdf')

        self.download_icon = PhotoImage(file="icons/download.png")
        download_icon = Button(self, image=self.download_icon, bg="#f6f7fb", command=export,
                               activebackground="#f6f7fb", borderwidth=0.5)

        label.place(x=2, y=2)
        download_icon.place(relx=0.95, rely=0.95, anchor=SE)
        pie_icon.place(relx=0.2, rely=0.3, anchor=NW)


class Page4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#f6f7fb')
        self.controller = controller

        # Language Settings
        def display_selected(choice):
            choice = variable.get()
            if choice == "Deutsch":
                print("Hallo!")
            else:
                print("hello")

        # Define a callback function for Link
        def callback(url):
            webbrowser.open_new_tab(url)

        # Dropdown Menu for Languages
        languages = ['Deutsch', 'English']
        variable = StringVar()
        variable.set(languages[0])
        dropdown = OptionMenu(self, variable, *languages, command=display_selected)

        self.logo_png = PhotoImage(file="icons/Logo.png")

        # Labels
        link = Label(self, text="Github", bg="#f6f7fb",
                     font=('Helveticabold', 12), fg="blue", cursor="hand2")
        readmelink = Label(self, text="readme", bg="#f6f7fb",
                           font=('Helveticabold', 12), fg="blue", cursor="hand2")
        logo = Label(self, image=self.logo_png, bg="#f6f7fb")
        ll = Label(self, text="Sprache:", bg="#f6f7fb")
        vt = Label(self, text="Technologie-Radar\nCopyright ⓒ 2022 \nVersion 1.0", bg="#f6f7fb")

        link.bind('<Button-1>', lambda e: callback("https://github.com/mrfabixx/Technologie_Radar"))
        readmelink.bind('<Button-1>', lambda e: callback("README.md"))

        # Placements
        vt.place(relx=0.1, rely=0.2)
        dropdown.place(relx=0.2, rely=0.4)
        ll.place(relx=0.1, rely=0.4)
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
