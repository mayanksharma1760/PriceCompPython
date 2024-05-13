from django import template

register = template.Library()

@register.filter
def convert_and_add(value, conversion_rate):
    # Assuming value is in Euro, convert it to Indian Rupee and add 30
    inr_value = value * conversion_rate
    total_inr_value = inr_value + 30
    return total_inr_value
