#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN  = int(environ.get("BOT_TOKEN", ""))
    API_ID  = int(environ.get("API_ID", ""))
    API_HASH  = int(environ.get("API_HASH", ""))
    AUTH_USERS  = int(environ.get("AUTH_USERS", ""))
    
