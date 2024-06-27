# Feature

def process_data(raw_data):
    processed_data = []
    for item in raw_data:
        if item['name'].startswith('J') and 0 < item['age'] < 100:
            processed_data.append(item)

    return processed_data
