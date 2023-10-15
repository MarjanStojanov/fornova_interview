import re
from helpers import parse_csv


class HotelService:
    def browse(self, page=1, limit=10):
        formatted_data = parse_csv("test_data.csv")
        return self._paginate_results(formatted_data, page=page, limit=limit)

    def search(self, keyword, page=1, limit=10):
        results = []

        formatted_data = parse_csv("test_data.csv")

        pattern = re.compile(keyword, re.IGNORECASE)

        for row in formatted_data:
            if any(
                [
                    re.search(pattern, row["name"]),
                    re.search(pattern, row["city"]),
                    re.search(pattern, row["country"]),
                ]
            ):
                results.append(row)

        return self._paginate_results(results, page=page, limit=limit)

    def _paginate_results(self, results, page, limit):
        starting_index = (page - 1) * limit
        end_index = starting_index + limit

        return results[starting_index:end_index]
