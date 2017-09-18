# -*- coding: utf-8 -*-
import os
import sys
import shutil
import subprocess
import json


def getLength(filename):
    command = ["ffprobe.exe", "-loglevel", "quiet", "-print_format", "json", "-show_format", "-show_streams", "-i",
               filename]
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = result.stdout.read()
    # print(str(out))
    temp = str(out.decode('utf-8'))
    try:
        data = json.loads(temp)['streams'][1]['width']
    except:
        data = json.loads(temp)['streams'][0]['width']
    return data


def getLenTime(filename):
    command = ["ffprobe.exe", "-loglevel", "quiet", "-print_format", "json", "-show_format", "-show_streams", "-i",
               filename]
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = result.stdout.read()
    # print(str(out))
    temp = str(out.decode('utf-8'))
    data = json.loads(temp)["format"]['duration']
    return data
