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
