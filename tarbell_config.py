# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

from flask import Blueprint, g, render_template
import ftfy
import jinja2
# import xlrd
# from markupsafe import Markup
# import json
# import datetime

# For calculating median of demographic data
from numpy import median

blueprint = Blueprint('amazon-hq2-finalists', __name__)




@blueprint.app_template_filter('get_summary_stats')
def get_summary_stats(data, k, zero_out):
	# k is for the desired key
	print data

	retval={}
	data_list = []
	for area in data:
		data_list.append(area[k])

	retval['median'] = median(data_list)
	retval['max'] = max(data_list) 
	retval['min'] = 0 if zero_out else min(data_list)
	retval['median_percentage'] = (retval['median'] - retval['min']) / (retval['max'] - retval['min']) * 100

	return retval

@blueprint.app_template_filter('format_number')
def get_stats(num, format_string):
    if format_string == "int":
        return "{:,}".format(num)
    if format_string == "float":    
        return "{:.1f}".format(num)
    if format_string == "float":    
        return "{.1f%}".format(num)
    return num

# Google spreadsheet key
SPREADSHEET_KEY = "1qnQOBzwubAedCpuAvLFpEZGYZV2k9v8Pk3wvbYJJ9bU"

# Exclude these files from publication
EXCLUDES = ['*.md', 'requirements.txt', 'node_modules', 'sass', 'js/src', 'package.json', 'Gruntfile.js']

# Spreadsheet cache lifetime in seconds. (Default: 4)
# SPREADSHEET_CACHE_TTL = 4

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# Get context from a local file or URL. This file can be a CSV or Excel
# spreadsheet file. Relative, absolute, and remote (http/https) paths can be 
# used.
# CONTEXT_SOURCE_FILE = ""

# EXPERIMENTAL: Path to a credentials file to authenticate with Google Drive.
# This is useful for for automated deployment. This option may be replaced by
# command line flag or environment variable. Take care not to commit or publish
# your credentials file.
# CREDENTIALS_PATH = ""

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    
    "production": "graphics.chicagotribune.com/amazon-hq2-finalists",
    "staging": "apps.beta.tribapps.com/amazon-hq2-finalists",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'amazon-hq2-finalists',
    'title': 'Amazon HQ2 locations handicapped'
}