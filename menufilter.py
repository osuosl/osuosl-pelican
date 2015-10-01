#!/usr/bin/env python
from jinja2 import Environment

def menu_filter(page_dict):
    unsorted_result = []
    top_menu = []

    for page in page_dict:
        if hasattr(page, 'menu'):
            menu_dict = {
                'menu': page.menu
            }
            menu_data = menu_dict['menu'].split(';')

            for item in menu_data:
                menu_loc_data = item.split(',')
                temp_dict = {
                    'parent': menu_loc_data[0].strip(),
                    'name': menu_loc_data[1].strip(),
                    'weight': int(menu_loc_data[2]),
                    'children': [],
                    'link': '/' + page.slug
                }
                unsorted_result.append(temp_dict)

    for item in unsorted_result:
        if item['parent'] == 'top':
            top_menu.append(item.copy())


    sorted_top = sorted(top_menu, key=lambda k: k['weight'])
    result = sorted(unsorted_result, key=lambda k: k['weight'])

    for item in sorted_top:
        for page in result:
            if page['parent'] == item['name']:
                item['children'].append(page.copy())

    for item in sorted_top:
        for child in item['children']:
            for page in result:
                if page['parent'] == child['name']:
                    child['children'].append(page.copy())


    return sorted_top


if __name__ == '__main__':
    """TEST"""
    print 'hello'
