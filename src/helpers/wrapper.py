from rich.table import Table
from rich import box
from rich.style import Style
from rich.text import Text


class Wrapper:
    @staticmethod
    def create_table(data_rows, num_days, symbol):
        table = Table(
            show_header=True,
            header_style="bold green",
            box=box.ASCII,
            show_lines=True,
            title="",
            border_style="bright_black",
        )

        table.add_column("Rank", justify="right", style="dim")
        table.add_column("Name")
        table.add_column("Symbol")
        table.add_column("{} days change (%)".format(num_days), justify="right", max_width=13)
        table.add_column("{} days highest price ({})".format(num_days, symbol), justify="right", max_width=15)
        table.add_column("{} days lowest price ({})".format(num_days, symbol), justify="right", max_width=14)
        table.add_column("Mean closing price ({})".format(symbol), justify="right", max_width=14)
        table.add_column("90th percentile ({})".format(symbol), justify="right", max_width=14)
        table.add_column(
            "Standard deviation of high prices", justify="right", max_width=20
        )
        table.add_column("Minimum volume", justify="right", max_width=13)
        table.add_column("Maximum market cap", justify="right", max_width=17)
        table.add_column("On Watchlist", justify="right", max_width=11)

        for row in data_rows:
            price_change = str(row['price_change'])

            if price_change == '0.00%':
                row_style = Style()
            else:
                row_style = Style(color="red") if "-" in price_change else Style(color="green")

            hp = str(row['highest_price_last_n_days'])

            table.add_row(
                row['rank'],
                row['name'],
                row['symbol'],
                Text(price_change, style=row_style),
                Text(hp, style=row_style),
                row['lowest_price_last_n_days'],
                row['mean_closing_price'],
                row['high_percentile'],
                row['standard_deviation_high_prices'],
                row['minimum_volume'],
                row['maximum_market_cap'],
                row['watchlist']
            )

        return table
