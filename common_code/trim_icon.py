#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Objective: This is for downloading app icons and trim them into round-cornered shape
Date: 2022/11/22

'''

from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
import requests
import json
import datetime
import os
import argparse


def get_url_dataframe_from_file(input_file):



# parameters
# im: Image object
# rad: radius of the musk
def add_corners(im, rad):
	circle = Image.new('L', (rad * 2, rad * 2), 0)
	draw = ImageDraw.Draw(circle)
	draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
	alpha = Image.new('L', im.size, 255)
	w, h = im.size
	alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
	alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
	alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
	alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
	im.putalpha(alpha)
	return im


def api_download_icons(url_dataframe, export_path):
	


# examples
im = Image.open('tiger.jpg')
im = add_corners(im, 100)
im.save('tiger.png')
