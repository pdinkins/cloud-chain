# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.terminalclient.main"
__version__ = "0.1.3"

# TERMINAL CLIENT CONFIG 
displaylogo = True
displaytitle = True

# IMPORTS # 
# python library imports
import platform
import os
import shutil
import datetime
from multiprocessing import Process, Queue

import pygame
from pygame.locals import DOUBLEBUF


import pangolin
import OpenGL.GL as gl
import numpy as np

cclogo = """
                                   /#################\..
                               ,########################\..
                            /###############################\.
                          ####################################\.
                        (#######################################)
                      ############################################.
                   .*###############################################.
             /#######################################################)
         /############################################################.
      #################################################################\..
    ########################################################################,
   ########################.            ,#####..           .###################,
  ,#######################               .###               *####################
  ########################   .########    ###   ,########   *#####################*
  ########################   .###########################   ,######################*
  ########################   .#####                 #####    ####################### 
  /#######################   .###########################    #######################/
   #######################   .########    ###   #########    #######################/
   /######################               .###                #######################*
    /#####################               /###.              (#######################
     ,#############################################################################
       (##########################################################################
           ,##################################################################*
               ,(#########################################################(
"""
cctitle = """
                      _                 _             _           _       
                     | |               | |           | |         (_)      
                  ___| | ___  _   _  __| | ____   ___| |__   __ _ _ _ __  
                 / __| |/ _ \| | | |/ _` | |__|  / __| '_ \ / _` | | '_ \ 
                | (__| | (_) | |_| | (_| |      | (__| | | | (_| | | | | |
                 \___|_|\___/ \__,_|\__,_|       \___|_| |_|\__,_|_|_| |_|                                                                                                                                                                                       
"""

class CORE_INTERFACE:
    """
    Terminal Interface
    # TODO: dynamic titles 
    """
    def __init__(self, menudict, menutitle, lus=0):
        self.__menudict = menudict
        self.__menutitle = menutitle
        self.__operating_system = platform.system()
        self.__localuserstate = lus
        self.__userstate = self.checkuserstate()
        
    
    # Horizontal Title Bar
    def __title_bar(self):
        print("=" * shutil.get_terminal_size().columns)

    # Title Bar Information
    def __title(self):
        if displaylogo: 
            print(cclogo)
        if displaytitle:
            print(cctitle)
        self.__title_bar()
        print('\t\t____________________', datetime.datetime.now())
        print('\t\t[_____ADMIN_____]')
        print("\t\t\t\t[__", platform.platform())
        print("\t\t\t\t[__","Python Version:",platform.python_version())
        self.__title_bar()

    # Determine the system and clear the terminal screen
    def __clear(self):
        if self.__operating_system == 'Darwin':
            os.system('clear')
        elif self.__operating_system == 'Windows':
            os.system('cls')

    def __menu(self):
        initialize_menu(self.__menudict, self.__menutitle)

    def checkuserstate(self):
        if self.__localuserstate == 0:
            return False
        elif self.__localuserstate == 1:
            return True
        else:
            return None

    # Clears the screen then displays the title bar
    def display(self):
        self.__clear()
        self.__title()
        self.__menu()


def initialize_menu(menu_dictionary, menutitle):
    menulist = list(menu_dictionary.keys())
    j = 1
    print('\n\t\t[ ' + menutitle, ']\n')
    for i in range(0,len(menulist)):
        print('\t\t\t','[',j,']','-', menulist[i])
        j += 1 
    choose_from_menu(menulist, menu_dictionary)

def choose_from_menu(menulist, menu_dictionary):
    try:
        try:
            menuchoice = int(input('\n\t\t[ Menu Choice ]:  '))
        except EOFError:
            return
        menuchoice -= 1
        # MENU FUNCTIONS GET EXECUTED RIGHT HERE
        menu_dictionary[menulist[menuchoice]]()
    except (IndexError, ValueError):
        print('***invalid choice***')

# R&D 
# Copyright (c) 2018, George Hotz

class Display2D(object):
  def __init__(self, W, H):
    pygame.init()
    self.screen = pygame.display.set_mode((W, H), DOUBLEBUF)
    self.surface = pygame.Surface(self.screen.get_size()).convert()

  def paint(self, img):
    # junk
    for event in pygame.event.get():
      pass

    # draw
    #pygame.surfarray.blit_array(self.surface, img.swapaxes(0,1)[:, :, [2,1,0]])

    # RGB, not BGR (might have to switch in twitchslam)
    pygame.surfarray.blit_array(self.surface, img.swapaxes(0,1)[:, :, [0,1,2]])
    self.screen.blit(self.surface, (0,0))

    # blit
    pygame.display.flip()


class Display3D(object):
  def __init__(self):
    self.state = None
    self.q = Queue()
    self.vp = Process(target=self.viewer_thread, args=(self.q,))
    self.vp.daemon = True
    self.vp.start()

  def viewer_thread(self, q):
    self.viewer_init(1024, 768)
    while 1:
      self.viewer_refresh(q)

  def viewer_init(self, w, h):
    pangolin.CreateWindowAndBind('Map Viewer', w, h)
    gl.glEnable(gl.GL_DEPTH_TEST)

    self.scam = pangolin.OpenGlRenderState(
      pangolin.ProjectionMatrix(w, h, 420, 420, w//2, h//2, 0.2, 10000),
      pangolin.ModelViewLookAt(0, -10, -8,
                               0, 0, 0,
                               0, -1, 0))
    self.handler = pangolin.Handler3D(self.scam)

    # Create Interactive View in window
    self.dcam = pangolin.CreateDisplay()
    self.dcam.SetBounds(0.0, 1.0, 0.0, 1.0, w/h)
    self.dcam.SetHandler(self.handler)
    # hack to avoid small Pangolin, no idea why it's *2
    self.dcam.Resize(pangolin.Viewport(0,0,w*2,h*2))
    self.dcam.Activate()


  def viewer_refresh(self, q):
    while not q.empty():
      self.state = q.get()

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    self.dcam.Activate(self.scam)

    if self.state is not None:
      if self.state[0].shape[0] >= 2:
        # draw poses
        gl.glColor3f(0.0, 1.0, 0.0)
        pangolin.DrawCameras(self.state[0][:-1])

      if self.state[0].shape[0] >= 1:
        # draw current pose as yellow
        gl.glColor3f(1.0, 1.0, 0.0)
        pangolin.DrawCameras(self.state[0][-1:])

      if self.state[1].shape[0] != 0:
        # draw keypoints
        gl.glPointSize(5)
        gl.glColor3f(1.0, 0.0, 0.0)
        pangolin.DrawPoints(self.state[1], self.state[2])

    pangolin.FinishFrame()

  def paint(self, mapp):
    if self.q is None:
      return

    poses, pts, colors = [], [], []
    for f in mapp.frames:
      # invert pose for display only
      poses.append(np.linalg.inv(f.pose))
    for p in mapp.points:
      pts.append(p.pt)
      colors.append(p.color)
    self.q.put((np.array(poses), np.array(pts), np.array(colors)/256.0))


