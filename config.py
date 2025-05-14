class Config:
    FIELD_NAME_DICT = {
        'department': ['department',],
        'name': ['name',],
        'hours': ['hours_worked', 'hours'],
        'rate': ['rate', 'hourly_rate', 'salary'],
    }
    PAYOUT_REPORT_FIELDS = {
        'existing_fields': [
            'department',
            'name',
            'hours',
        ],
        'calculated_fields': ['payout'],
        # индексация полей сквозная, начиная с нуля. Сначала идут существующие, потом вычисляемые
        'group_by_field_index': 0,
        'order_by_field_index': 1,
    }