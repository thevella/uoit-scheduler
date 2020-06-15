#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    GUI frontend to create schedules for OnTechU. Pulls info directly from
        their API at 'https://ssbp.mycampus.ca/prod_uoit/bwckschd.p_get_crse_unsec'.
"""

import tkinter as tk

class schedulergui(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()




if __name__ == '__main__':
    app = schedulergui(None)
    app.title('OnTechU Scheduler')
    app.mainloop()
