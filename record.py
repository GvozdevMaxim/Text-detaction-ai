class PreparedRecords:
    def __init__(self):
        self.all_records = []

    def add_record(self, id, image_text):
        self.all_records.append((id, image_text))

    def clear_records_data(self):
        self.all_records.clear()
