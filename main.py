#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.10.0')

from core.sendmail import SendMailApp

if __name__ == '__main__':
    SendMailApp().run()
