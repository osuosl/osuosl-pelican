#!/usr/bin/env python
import bs4

def menu_filter(pelican_pages, direct_templates):
    """
    Jinja filter for Pelican page object list

    Structures pages into a three-level menu that can be parsed by Jinja2
    templating. Reads page metadata of the form:
    :menu: <parent>, <name>, <weight>; <parent2>, <name2>, <weight2>; ...
    where the top-level menu items have a parent name 'top'.
    """
    page_list = []
    menu = []

    # Pull menu metadata from Pelican page object list
    for page in pelican_pages:
        if hasattr(page, 'menu'):

            # Split into list of menu locations for each page
            menu_data = page.menu.split(';')

            # Record each menu location per page
            for item in menu_data:
                temp_data = item.split(',')
                temp_dict = {
                    'parent': temp_data[0].strip(),
                    'name': temp_data[1].strip(),
                    'weight': int(temp_data[2]),
                    'link': "/{0}".format(page.slug),
                    'children': [],
                }

                #Add each menu location to a page list
                page_list.append(temp_dict)

    # Add the direct templates before sorting
    for item in direct_templates:
        page_list.append(item.copy())

    # Sort the page list by weight
    page_list = sorted(page_list, key=lambda k: k['weight'])

    # Find top-level menu items and place in menu
    for item in page_list:
        if item['parent'] == 'top':
            menu.append(item.copy())

    # For each top-menu item, find its children
    for parent in menu:
        for page in page_list:
            if page['parent'] == parent['name']:
                parent['children'].append(page.copy())

    # For each second-level menu item, find its children
    for parent in menu:
        for child in parent['children']:
            for page in page_list:
                if page['parent'] == child['name']:
                    child['children'].append(page.copy())

    return menu

def close_html_tags(html_string):
    """Closes any html tags in html_string that have been opened but have not
    been closed.
    """
    soup = bs4.BeautifulSoup(html_string, "html.parser")
    return soup
