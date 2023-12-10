def process_data(raw_data: str, data_headers: list[str]):
    data_map = {}
    for index, line in enumerate(raw_data.split('\n')):
        data_map[data_headers[index]] = []
        for token in line.split(','):
            if token != '':
                data_map[data_headers[index]].append(token)
    return data_map
