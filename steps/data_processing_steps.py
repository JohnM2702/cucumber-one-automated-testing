from behave import given, when, then
from data_processing import process_data


@given('the user has some raw data')
def step_impl(context):
    context.raw_data = [{'id': 1, 'name': 'John', 'age': 30},
                        {'id': 2, 'name': 'Jane', 'age': 77}]


@when('the data is processed')
def step_impl(context):
    context.processed_data = process_data(context.raw_data)


@then('the processed data should meet the expected criteria')
def step_impl(context):
    assert len(context.processed_data) == 2
    assert all(item['name'].startswith('J') for item in context.processed_data)
    assert all(0 < item['age'] < 100 for item in context.processed_data)
