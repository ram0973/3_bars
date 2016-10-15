# -*- coding: utf-8 -*-
import json
import sys


def load_win_unicode_console():
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def get_pretty_printed_json(json_data):
    return json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False)
