class Config:
    FIELD_NAME_DICT = {
        # Словарь содержит все варианты наименования родственных полей
        'department': ['department',],
        'name': ['name',],
        'hours': ['hours_worked', 'hours'],
        'rate': ['rate', 'hourly_rate', 'salary'],
    }
    PAYOUT_REPORT_FIELDS = {
        'title': 'Отчет по выплатам',
        'existing_fields': [
            'department',
            'name',
            'hours',
        ],
        'calculated_fields': ['payout'],
        # индексация полей сквозная, начиная с нуля. Сначала идут существующие, потом вычисляемые
        # !Группируем только по нулевому полю, сортируем по любому
        'group_by_field_index': 0,
        'order_by_field_index': 1,
    }