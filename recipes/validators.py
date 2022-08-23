from django.core.exceptions import ValidationError

valid_unit_measurements = ['pounds', 'lbs', 'oz', 'whole', 'half', 'cups']


def validate_unit_of_measure(value):

    if value not in valid_unit_measurements:
        raise ValidationError(f"{value} is not a valid unit of measure")
