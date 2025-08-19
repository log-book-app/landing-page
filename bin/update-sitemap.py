#!/usr/bin/env python3

from datetime import date
from lxml import etree

SITEMAP_FILE = "sitemap.xml"
NAME_SPACE = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

def update_lastmod(file_path):
    # Dzisiejsza data w formacie YYYY-MM-DD
    today = date.today().isoformat()

    # Parsowanie XML
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_path, parser)
    root = tree.getroot()

    # Iteracja po wszystkich <url>
    for url in root.findall("sm:url", NAME_SPACE):
        lastmod = url.find("sm:lastmod", NAME_SPACE)
        if lastmod.text != today:
            lastmod.text = today
            print(f"✅ Zaktualizowano <lastmod> dla {url.find("sm:loc", NAME_SPACE).text} na {today}")

    tree.write(
        file_path,
        pretty_print=True,
        doctype='<?xml version="1.0" encoding="UTF-8"?>',
        encoding="UTF-8"
    )


if __name__ == "__main__":
    update_lastmod(SITEMAP_FILE)
