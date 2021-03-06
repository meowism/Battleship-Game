#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:44:00 2020

@author: jameselijah
"""

'''
Program Name: battleship_game_no_self_import

Description: This file/module contains all the work done from login to ship
placement in a long chain, so as to avoid any problems involved in importing
functions from other python files.

This is really long, so be prepared.
'''

import tkinter as tk 
from tkinter import *


from tkinter import messagebox 

import os 
from random import randint
import random
import time

Player = {'Carrier':[(3, 2, 1), (4, 2, 1), (5, 2, 1), (6, 2, 1)], 'Submarine': [(4, 10, 0), (5, 10, 0), (6, 10, 0)]}
AI_player = {'Carrier':[(12,12,1), (12,13,1), (12,14,1)], 'Submarine': [(0,12,0), (0,13,0), (0,14,0), (0,15,0)]}

color="red"
default_color="white"

def redraw_boards():
    global redraw_gameboard
    global Player
    global AI_player
    global player_underwater_cell
    global player_surface_cell
    global AI_underwater_cell
    global AI_surface_cell
    
    
    print (Player)
    print (AI_player)
    
    Player["Player Surface"] = {}
    Player["Player Underwater"] = {}
    AI_player["AI Surface"] = {}
    AI_player["AI Underwater"] = {}
    
    redraw_gameboard = Tk()
    redraw_gameboard.title("Battleship Game")
    redraw_gameboard.geometry("1080x1240")
    redraw_gameboard.resizable(False, False)
    
    Label(redraw_gameboard, text="Player Underwater", height = 3, width = 40).grid(row=0, column=0, columnspan=10)
    Label(redraw_gameboard, text="Player Surface", height = 3, width = 40).grid(row=0, column=12, columnspan=10)

    # Preparing spacings between the grids
    Label(redraw_gameboard, text="", height = 20, width = 4).grid(row=1, column=10, rowspan=10)
    Label(redraw_gameboard, text="AI Underwater", height = 3, width = 40).grid(row=11, column=0, columnspan=10)
    Label(redraw_gameboard, text="AI Surface", height = 3, width = 40).grid(row=11, column=11, columnspan=10)
    Label(redraw_gameboard, text="", height = 4, width = 1).grid(row=11, column=0, columnspan=10)

    last_clicked = [None]
    
    for i in range(1, 11):
        Player["Player Underwater"][i] = {}
        for j in range(10):
            Player["Player Underwater"][i][j] = {}
            Player["Player Underwater"][i][j]["Presence"] = None
            player_underwater_cell = Button(redraw_gameboard, 
                                            height = 2, 
                                            width = 4, 
                                            command=cannot_shoot)
            player_underwater_cell.grid(row=i, column=j)
            
    for i in range(1, 11):
        Player["Player Surface"][i] = {}
        for j in range(11, 21):
            Player["Player Surface"][i][j] = {}
            Player["Player Surface"][i][j]["Presence"] = None
            player_surface_cell = Button(redraw_gameboard, 
                                         height = 2, 
                                         width = 4, 
                                         command=cannot_shoot)
            player_surface_cell.grid(row=i, column=j) 
            
    for i in range(12, 22):
        AI_player["AI Underwater"][i] = {}
        for j in range(10):
            AI_player["AI Underwater"][i][j] = {}
            AI_player["AI Underwater"][i][j]["Presence"] = None
            AI_underwater_cell = Button(redraw_gameboard, 
                                        height = 2, 
                                        width = 4)
            AI_underwater_cell.grid(row=i, column=j)
            AI_underwater_cell["command"] = lambda AI_underwater_cell = AI_underwater_cell, depth = 1: shoot(AI_underwater_cell, depth, last_clicked)

    
    for i in range(12, 22):
        AI_player["AI Surface"][i] = {}
        for j in range(11, 21):
            AI_player["AI Surface"][i][j] = {}
            AI_player["AI Surface"][i][j]["Presence"] = None
            AI_surface_cell = Button(redraw_gameboard, 
                                     height = 2, 
                                     width = 4)
            AI_surface_cell.grid(row=i, column=j) 
            AI_surface_cell["command"] = lambda AI_surface_cell = AI_surface_cell, depth = 1: shoot(AI_surface_cell, depth, last_clicked)
    

    redraw_gameboard.mainloop()
    #referee()

def cannot_shoot():
    print (messagebox.showinfo("Invalid","Cannot shoot yourself. lol :P"))
def already_shot():
    print (messagebox.showinfo("Invalid","You have already shot here!"))
def hit_shot():
    print (messagebox.showinfo("HIT!", "Nice shot! AI Turn"))
def hit_missed():
    print (messagebox.showinfo("MISSED!", "Better Luck Next time! AI Turn"))
def AI_hit():
    print (messagebox.showinfo("HIT!", "AI managed to hit you! AI Turn"))
def AI_hit_missed():
    print (messagebox.showinfo("MISSED!", "AI did not hit you! your Turn"))
def AI_commandless():
    pass

def draw_new_button_hit(row, column):
    
    global redraw_gameboard
    global Player
    global AI_player
    global player_underwater_cell
    global player_surface_cell
    global AI_underwater_cell
    global AI_surface_cell
    
    new_button = Button(redraw_gameboard, 
                        height = 2, 
                        width = 4, 
                        command= already_shot,
                        bg = '#FF0000')
    
    new_button.grid(row = row, column = column)


def draw_new_button_miss(row, column):
    
    global redraw_gameboard
    global Player
    global AI_player
    global player_underwater_cell
    global player_surface_cell
    global AI_underwater_cell
    global AI_surface_cell
    
    new_button = Button(redraw_gameboard, 
                        height = 2, 
                        width = 4, 
                        command= already_shot,
                        bg = '#000000')
    
    new_button.grid(row = row, column = column)
    
def shoot(button, depth, last_clicked):
    global redraw_gameboard
    global Player
    global AI_player
    global player_underwater_cell
    global player_surface_cell
    global AI_underwater_cell
    global AI_surface_cell
        
    if depth == 1: #means AI_surface
        #while AI_player["AI Surface"]["Presence"] == "HIT":
         #   already_shot()
         #   break
            
        else:
            if (button, 1) == AI_player["Carrier"][0]:
                AI_player["AI Surface"][row][column]["Presence"] = "HIT"
                hit_shot()
                row, column, depth
                last_clicked[0] = button
                
                AI_player_turn()
                
            elif (button,1) == AI_player["Carrier"][1]:
                AI_player["AI Surface"][row][column]["Presence"] = "HIT"
                hit_shot()
                if last_clicked[0]:
                    last_clicked[0]["bg"] = default_color
                    last_clicked[0]["activebackground"] = default_color
                button["bg"] = color
                button["activebackground"] = color
                last_clicked[0] = button
                
                AI_player_turn()
                
            elif (button,1) == AI_player["Carrier"][2]:
                AI_player["AI Surface"][row][column]["Presence"] = "HIT"
                hit_shot()
                
                if last_clicked[0]:
                    last_clicked[0]["bg"] = default_color
                    last_clicked[0]["activebackground"] = default_color
                button["bg"] = color
                button["activebackground"] = color
                last_clicked[0] = button
                
                AI_player_turn()
            
            elif (button,1) == AI_player["Carrier"][2]:
                AI_player["AI Surface"][row][column]["Presence"] = "HIT"
                hit_shot()
                
                if last_clicked[0]:
                    last_clicked[0]["bg"] = default_color
                    last_clicked[0]["activebackground"] = default_color
                button["bg"] = color
                button["activebackground"] = color
                last_clicked[0] = button
                
                AI_player_turn()
                
    
            
            else:
                AI_player["AI Surface"][row][column]["Presence"] = "HIT"
                hit_missed()
                
                if last_clicked[0]:
                    last_clicked[0]["bg"] = default_color
                    last_clicked[0]["activebackground"] = default_color
                button["bg"] = color
                button["activebackground"] = color
                last_clicked[0] = button
                
                AI_player_turn()
                    
    else:
        while AI_player["AI Underwater"][row][column]["Presence"] == "HIT":
            already_shot()
            break
            
        else:
            
            if (row,column,0) == AI_player["Submarine"][0] :
                AI_player["AI Underwater"][row][column]["Presence"] = "HIT"
                hit_shot()
                if last_clicked[0]:
                    last_clicked[0]["bg"] = default_color
                    last_clicked[0]["activebackground"] = default_color
                button["bg"] = color
                button["activebackground"] = color
                last_clicked[0] = button
                
                AI_player_turn()
            
            elif (row,column,0) == AI_player["Submarine"][1]:
                AI_player["AI Underwater"][row][column]["Presence"] = "HIT"
                hit_shot()
                if last_clicked[0]:
                    last_clicked[0]["bg"] = default_color
                    last_clicked[0]["activebackground"] = default_color
                button["bg"] = color
                button["activebackground"] = color
                last_clicked[0] = button
                
                AI_player_turn()
            
            elif (row,column,0) == AI_player["Submarine"][2]:
                AI_player["AI Underwater"][row][column]["Presence"] = "HIT"
                hit_shot()
                if last_clicked[0]:
                    last_clicked[0]["bg"] = default_color
                    last_clicked[0]["activebackground"] = default_color
                button["bg"] = color
                button["activebackground"] = color
                last_clicked[0] = button
                AI_player_turn()
                
                
            else:
                hit_missed()
                AI_player["AI Underwater"][row][column]["Presence"] = "HIT"
                if last_clicked[0]:
                    last_clicked[0]["bg"] = default_color
                    last_clicked[0]["activebackground"] = default_color
                button["bg"] = color
                button["activebackground"] = color
                last_clicked[0] = button
                AI_player_turn()
 

def AI_player_turn():
    global redraw_gameboard
    global Player
    global AI_player
    global player_underwater_cell
    global player_surface_cell
    global AI_underwater_cell
    global AI_surface_cell
    
    random_surface = random.randint(0,1)
    
    if random_surface == 0:
        random_underwater_x = random.randint(1,10)
        random_underwater_y = random.randint(0,9)
        AI_underwater_coordinates = (random_underwater_x,random_underwater_y,0)
        row = random_underwater_x
        column = random_underwater_y

        if Player["Player Underwater"][random_underwater_x][random_underwater_y]["Presence"] == "HIT":
            print ("Bot Thinking...")
            AI_player_turn()
        
        elif AI_underwater_coordinates == Player["Submarine"][0]:
            #referee()
            
            Player["Player Underwater"][random_underwater_x][random_underwater_y]["Presence"] = "HIT"
            draw_new_button_hit(row, column)
            AI_hit()
            
            
            
        elif AI_underwater_coordinates == Player["Submarine"][1]:
            
            AI_hit()
            Player["Player Underwater"][random_underwater_x][random_underwater_y]["Presence"] = "HIT"
            draw_new_button_hit(row, column)
            

        elif AI_underwater_coordinates == Player["Submarine"][2]:
            AI_hit()
            Player["Player Underwater"][random_underwater_x][random_underwater_y]["Presence"] = "HIT"
            draw_new_button_hit(row, column)
            
            
        else:
            AI_hit_missed()
            Player["Player Underwater"][random_underwater_x][random_underwater_y]["Presence"] = "HIT"
            draw_new_button_miss(row, column)
            
    else:
        random_surface_x = random.randint(1,10)
        random_surface_y = random.randint(11,20)
        AI_surface_coordinates = (random_surface_x,random_surface_y,1)
        
        row = random_surface_x
        column = random_surface_y
        
        if Player["Player Surface"][random_surface_x][random_surface_y]["Presence"] == "HIT":
            print ("Bot Thinking...")
            AI_player_turn()
        
        
        elif AI_surface_coordinates == Player["Carrier"][0]:
            AI_hit()
            Player["Player Surface"][random_surface_x][random_surface_y]["Presence"] = "HIT"
            draw_new_button_hit(row, column)
            
        elif AI_surface_coordinates == Player["Carrier"][1]:
            AI_hit()
            Player["Player Surface"][random_surface_x][random_surface_y]["Presence"] = "HIT"
            draw_new_button_hit(row, column)
            
        elif AI_surface_coordinates == Player["Carrier"][2]:
            AI_hit()
            Player["Player Surface"][random_surface_x][random_surface_y]["Presence"] = "HIT"
            draw_new_button_hit(row, column)
            
        elif AI_surface_coordinates == Player["Carrier"][3]:
            AI_hit()
            Player["Player Surface"][random_surface_x][random_surface_y]["Presence"] = "HIT"
            draw_new_button_hit(row, column)
            
        else:
            AI_hit_missed()
            Player["Player Surface"][random_surface_x][random_surface_y]["Presence"] = "HIT"
            Player["Player Surface"][random_surface_x][random_surface_y] = Button(redraw_gameboard,
                  height = 2,
                  width = 4,
                  command = AI_commandless, 
                  bg = 'black')
            draw_new_button_miss(row, column)

redraw_boards()