from csv import reader
from fastapi.exceptions import HTTPException


def parse_csv(filename: str) -> list[dict]:
    formatted_data = []
    try:
        with open(filename, newline="") as csv_file:
            file_reader = reader(csv_file, delimiter=",")
            next(file_reader)  # skip headers

            for row in file_reader:
                formatted_data.append(
                    {
                        "id": row[0],
                        "name": row[1],
                        "city": row[2],
                        "country": row[3],
                    }
                )
    except Exception:
        raise HTTPException(
            status_code=400, detail=f"Missing or malformed CSV file: {filename}"
        )

    return formatted_data
