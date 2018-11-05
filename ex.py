#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:17:28 2018

@author: computervision
"""
import tkinter as tk
import time

class A:
    def __init__(self, master):
        self.label=tk.Label(master)
        self.label.grid(row=0, column=0)
        self.label.configure(text='nothing')
        self.count = 0
        self.update_label()

    def update_label(self):
        
        self.label.configure(text = 'count: {}'.format(self.count))
        self.label.after(100, self.update_label) # call this method again in 1,000 milliseconds
        self.count += 1
        print(self.count)

root = tk.Tk()
A(root)
root.mainloop()