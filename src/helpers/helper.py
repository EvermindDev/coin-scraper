import re


class Helper:

    @staticmethod
    def tuple_list(entries):
        item_list = []
        for key in entries:
            item_list.append((
                entries[key]['name'],
                entries[key]['symbol'],
                entries[key]['rank'],
                entries[key]['watchlist'],
                entries[key]['logo'],
                entries[key]['entry_datetime'],
            ))
        return item_list

    @staticmethod
    def slugify(value):
        value = value.lower().strip()
        value = re.sub(r'[^\w\s-]', '', value)
        value = re.sub(r'[\s_-]+', '-', value)
        value = re.sub(r'^-+|-+$', '', value)
        return value

    @staticmethod
    def normalize_price(value):
        value.replace('$', '').replace(',', '')
        return value
