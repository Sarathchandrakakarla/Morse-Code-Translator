import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

Window.clearcolor = (.25,.5,.5,0)

class Content(App):

    def build(self):

        self.icon = r"C:\Users\kakar\Desktop\Icons\preview.png"

        self.var=0

        superBox = BoxLayout(orientation ='vertical')
        
        HB1=BoxLayout(orientation='horizontal')
        HB2=BoxLayout(orientation='horizontal')
        HB3=BoxLayout(orientation='horizontal')
        HB4=BoxLayout(orientation='horizontal')
        HB41=BoxLayout(orientation='horizontal')
        HB5=BoxLayout(orientation='horizontal')

        self.lb1=Label(text='Morse Text:',size_hint=(.15,.09),pos_hint={'x':.6,'y':1})

        self.lb2=Label(text='English Text:',size_hint=(.15,.09),pos_hint={'x':.6,'y':1})

        self.text1="NOTE: 1.Give one space for each letter in Morse Code\n2. Give ' , ' at the starting of next word   \nEx: .... .. ,.... . .-.. .-.. ---    HI HELLO "
        self.text2="NOTE: If ' , ' is there i.e., it is the starting of next word"

        self.lb3=Label(text=self.text1)
        
        self.t1=TextInput(multiline = True,size_hint=(.5,.5),pos_hint={'x':.12,'y':.75})
        self.t2=TextInput(multiline = True,size_hint=(.5,.5),pos_hint={'x':.12,'y':.75})

        btn1=Button(text='Translate',size_hint=(.3,.5),pos_hint={'x':.5,'y':.3},background_color =(.5, 0, 2, 1))
        btn1.bind(on_press = lambda button:self.click(self.t1.text))

        btn2=Button(text='Clear',size_hint=(.3,.5),pos_hint={'x':.5,'y':.3},background_color =(1,1,1,1))
        btn2.bind(on_press=self.clear)

        btn3=Button(text='Quit',size_hint=(.3,.5),pos_hint={'x':.5,'y':.3},background_color =(2, 0, 0, 1))
        btn3.bind(on_press = self.quit)

        self.check1=CheckBox(active=True,group='Lang',size_hint=(.1,.09),pos_hint={'x':2,'y':1})
        self.check1.bind(active=self.morse_to_eng)

        self.check2=CheckBox(active=False,group='Lang',size_hint=(.1,.09),pos_hint={'x':2,'y':1})
        self.check2.bind(active=self.eng_to_morse)
        
        HB1.add_widget(Label(text='MORSE CODE CONVERTER APP',size_hint=(.15,.09),pos_hint={'x':.6,'y':.6}))

        HB2.add_widget(self.lb1)
        HB2.add_widget(self.t1)

        HB3.add_widget(self.lb2)
        HB3.add_widget(self.t2)

        HB4.add_widget(Label(text='Morse to English',center_x=5,size_hint=(.1,.09),pos_hint={'x':.5,'y':1}))
        HB4.add_widget(self.check1)
        self.var=1  #Checking which radio button is active
        HB4.add_widget(Label(text='English to Morse',size_hint=(.1,.09),pos_hint={'x':.5,'y':1}))
        HB4.add_widget(self.check2)

        HB41.add_widget(self.lb3)

        HB5.add_widget(btn1)
        HB5.add_widget(btn2)
        HB5.add_widget(btn3)

        superBox.add_widget(HB1)
        superBox.add_widget(HB2)
        superBox.add_widget(HB3)
        superBox.add_widget(HB4)
        superBox.add_widget(HB41)
        superBox.add_widget(HB5)

        return superBox

    def morse_to_eng(self,checkboxinstance,isActive):
        if not isActive:
            self.lb1.text='English Text:'
            self.lb2.text='Morse Text:'
        else:
            self.lb1.text='Morse Text:'
            self.lb2.text='English Text:'
            self.var=1
            self.lb3.text=self.text1
            

    def eng_to_morse(self,checkboxinstance,isActive):
        if not isActive:
            self.lb1.text='Morse Text:'
            self.lb2.text='Text Text:'
        else:
            self.lb1.text='English Text:'
            self.lb2.text='Morse Text:'
            self.var=2
            self.lb3.text=self.text2

    def click(self,text):
        txt=text.upper()
        self.a=""
        self.t2.text=""

        morse_dict={'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}
        def get_key(val):
            for key, value in morse_dict.items():
                 if val == value:
                     return key

        
        if self.var==1:
            for letter in txt.split(' '):
                    if ',' in letter:
                        self.a+=' '
                        self.a+=str(get_key(letter[1:len(letter)]))
                    
                    else:
                        self.a+=str(get_key(letter))

        elif self.var==2:
            for letter in txt:
                if letter in list(morse_dict.keys()):
                    if letter!=txt[-1]:
                        self.a+=morse_dict.get(letter)
                        self.a+=' '
                    elif letter==txt[-1]:
                        self.a+=morse_dict.get(letter)
                elif letter.isspace()==True:
                    self.a+=','

            
        self.t2.insert_text(self.a)

    def clear(self,instance):
        self.t1.text=""
        self.t2.text=""

    def quit(self,instance):
        App.get_running_app().stop()
        Window.close()

app=Content()
app.run()
       
