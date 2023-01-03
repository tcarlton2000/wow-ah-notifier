from discord import post_content
from wow import best_price_items

if __name__ == '__main__':
    items = best_price_items()
    post_content(items)
