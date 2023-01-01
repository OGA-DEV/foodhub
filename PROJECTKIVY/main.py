from kivy.uix.screenmanager import ScreenManager, NoTransition,Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.image  import Image
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
import sqlite3
import os, sys
import kivy
# from login import Login
import configparser

kivy.require('1.0.8')

Window.size = (350,580) 


class MubsApp(MDApp):
    
    def build(self):
        
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager = ScreenManager(transition =NoTransition())
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("menu.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("fingerprint.kv"))
        screen_manager.add_widget(Builder.load_file("card.kv"))
        con = sqlite3.connect("login_db.db")
        c = con.cursor()
        
        c.execute("""CREATE TABLE if not exists users(
            email text,
            password text
        )
                
                  """)
        con.commit()
        
        con.close()
        
        return screen_manager
    
    
    
    def on_start(self):
        Clock.schedule_once(self.login,10)
        
    def login(self,*args):
        screen_manager.current = "login"
        
    def signup(self,*args):
        screen_manager.current = "signup"
        
    def menu(self,*args):
        screen_manager.current = "menu"
        
    def touch_id(self,*args):
        screen_manager.current = "touch_id"
            
    def card(self,*args):
        screen_manager.current = "card"
        
    def submit(self):
        con = sqlite3.connect("login_db.db")
        c = con.cursor()
        
        c.execute("INSERT INTO users VALUES (:first)",{
            'first':self.root.ids.input_email.text,
        })
        
        self.root.ids.input_email.text = f'{self.root.ids.input_email.text} Added'
        con.commit()
        
        con.close()
        


        
    

if __name__== '__main__':
    MubsApp().run()