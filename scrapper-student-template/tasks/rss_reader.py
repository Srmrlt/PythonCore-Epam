# You shouldn't change  name of function or their arguments
# ,but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import json as js
import xml.etree.ElementTree as Et
from html import unescape


class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        # >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link>
        <description>Some RSS Channel</description></channel></rss>'
        # >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        # >>> print("\\n".join(rss_parser(xml)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    # tuples of tags and their readable format
    teg_channel = ('title', 'link', 'lastBuildDate', 'pubDate', 'language',
                   'category', 'managingEditor', 'description')
    line_names_channel = ('Feed', 'Link', 'Last Build Date', 'Publish Date',
                          'Language', 'Categories', 'Editor', 'Description')
    teg_item = ('title', 'author', 'pubDate', 'link', 'category', 'description')
    line_names_item = ('Title', 'Author', 'Published', 'Link', 'Categories', None)

    # converting xml data to work in python
    xml_obj = Et.fromstring(xml)[0]

    # creating a data dictionary for a tag 'channel'
    channel_dict = dict_builder(xml_obj, teg_channel)

    # creation of data dictionaries packed into a list for a tag 'item'
    items_dicts = list()
    items = item_finder(xml_obj, limit)
    for item in items:
        items_dicts.append(dict_builder(item, teg_item))

    if json:
        # creating json data output
        data = channel_dict
        if items_dicts:
            # excludes the display of the 'item' tag in the missing of this data
            data['items'] = items_dicts
        json_data = js.dumps(data, indent=2)
        news_list = json_data.split('\n')
    else:
        # creating str data output
        news_list = list()
        news_list += dict2str(channel_dict, teg_channel, line_names_channel, 'channel')
        for item_dict in items_dicts:
            news_list.append('')
            news_list += dict2str(item_dict, teg_item, line_names_item, 'item')

    return news_list


def item_finder(xml_obj, limit):
    """Forming a list of length 'limit' by tag 'item' from xml data"""
    item_list = [el for el in xml_obj if el.tag == 'item']
    return item_list[:limit]


def dict_builder(xml_obj, teg_names):
    """Creating a dictionary from xml by predefined tags (teg_names), preserving their order"""
    teg_dict = dict()
    category_list = list()
    for teg in teg_names:
        for el in xml_obj:
            if teg == el.tag:
                if el.tag == 'category':
                    # For the "category" tag, we form a list for storing values
                    category_list.append(unescape(el.text))
                    teg_dict[teg] = category_list
                else:
                    teg_dict[teg] = unescape(el.text)
    return teg_dict


def dict2str(teg_dict: dict, teg_s: tuple, names: tuple, mode: str):
    """
    Formation of a list of lines from dict, where each line is the name of the xml tag + the text of the xml tag.
    The name of the xml tag is converted into a readable form. Example: 'lastBuildDate' -> 'Last Build Date'.
    :param teg_dict:
    :param teg_s:  list of tags on which data output is generated
    :param names:  list of readable tag names
    :param mode:   output mode of data "description"
    """
    str_list = list()
    names_dict = dict(zip(teg_s, names))
    for teg in teg_dict:
        if teg == 'category':
            # write category values separated by commas
            category_str = ', '.join(teg_dict[teg])
            str_list.append(f'{names_dict[teg]}: {category_str}')
        elif (teg == 'description') and (mode == 'item'):
            # different implementation of displaying the data of the description teg for channel and item mode
            str_list.append(f'\n{teg_dict[teg]}')
        else:
            str_list.append(f'{names_dict[teg]}: {teg_dict[teg]}')
    return str_list


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
