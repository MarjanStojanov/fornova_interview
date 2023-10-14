from csv import reader


def parse_csv(filename: str) -> list[dict]:
    # TODO: add error handling

    formatted_data = []
    with open(filename, newline="") as csv_file:
        file_reader = reader(csv_file, delimiter=",")
        next(file_reader)  # skip headers

        for row in file_reader:
            formatted_data.append({
                "id": row[0],
                "name": row[1],
                "city": row[2],
                "country": row[3],
                }
            )

    return formatted_data
