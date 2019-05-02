# -*- coding: utf-8 -*-

# @author:  ln_company
# @license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
# @software: PyCharm
# @file:  tutorial.py
# @time: 2019/3/18 11:41
# @Software: PyCharm
# @Site    : 
# @desc:
from behave import *

use_step_matcher('re')


@given('we have behave installed')
def step_register(context):
    print("step_impl 1")
    pass


@When('I no da')
def step_register(context):
    pass


@then('I ni ye')
def step_register(context):
    pass


@then('nu error')
def step_register(context):
    assert 'qwe' in '1', 'no trur %s' % 'error'


@given('we have behave installed error')
def step_impl(context):
    for row in context.table:
        try:
            assert row['name'] == 'name', '%s--%s' % (row['name'], row['department'])
        except Exception as a:
            pass
    pass


@when('we implement a test')
def step_impll(context):
    print("step_impl 2")
    assert True is not False


@then('behave will test it for us!')
def step_implll(context):
    print("step_impl 3")
    assert context.failed is False, context.failed
