def print_table(data: dict, title: str = "", grouped: bool = True):
    if title:
        print(title)
    if not data:
        print("No data")
    if not grouped:
        headers = list(list(data.values())[0].keys())
        table_data = [list(rec.values()) for rec in list(data.values())]
        col_widths = [
            max([len(str(row[i])) for row in [headers] + table_data])
            for i in range(len(headers))
        ]
        print(col_widths)
        header_row = " | ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
        print("-" * len(header_row))
        print(header_row)
        print("-" * len(header_row))
        for row in table_data:
            print(" | ".join(f"{str(cell):<{w}}" for cell, w in zip(row, col_widths)))
            print("-" * len(header_row))
    else:
        headers = list(list(data.values())[0][0].keys())
        col_widths = []
        col_widths.append(
            max(len(item) for item in [headers[0], *list(data.keys())]) + 1
        )
        col_widths.extend(
            [
                max(
                    [
                        len(str(row[i]))
                        for row in [headers]
                        + [
                            list(item.values())
                            for sublist in data.values()
                            for item in sublist
                        ]
                    ]
                )
                for i in range(1, len(headers))
            ]
        )
        header_row = " | ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
        print("-" * len(header_row))
        print(header_row)
        print("-" * len(header_row))
        for key, value in data.items():
            print(key)
            for item in value:
                row = list(item.values())
                print(
                    " | ".join(f"{str(cell):<{w}}" for cell, w in zip(row, col_widths))
                )
                print("-" * len(header_row))
