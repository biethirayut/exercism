def slices(series, length):
    if length <= len(series) and length > 0:
        series_list = [int(i) for i in series]
        start = 0
        results = []
        while length <= len(series):
            results.append(series_list[start:length])
            start += 1
            length += 1
        return results
    else:
        raise ValueError

