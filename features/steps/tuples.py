#pylint: disable=all
from behave import *
    
@given('a <- tuple (4.3, -4.2, 3.1, 1.0)')
def step_impl(context):
    context.a = (4.3, -4.2, 3.1, 1.0)
    
@then('a.x = 4.3')
def step_impl(context):
    assert context.a[0] == 4.3
    
@then('a.y = -4.2')
def step_impl(context):
    assert context.a[1] == -4.2
    
@then('a.z = 3.1')
def step_impl(context):
    assert context.a[2] == 3.1
    
@then('a.w = 1.0')
def step_impl(context):
    assert context.a[3] == 1.0
    
@then('a is a point')
def step_impl(context):
    assert context.a[3] == 1.0
    
@then('a is not a vector')
def step_impl(context):
    assert context.a[3] != 0.0
    
# -----------------------------------------

@given('a <- tuple (4.3, -4.2, 3.1, 0.0)')
def step_impl(context):
    context.a = (4.3, -4.2, 3.1, 0.0)

@then('a.w = 0.0')
def step_impl(context):
    assert context.a[3] == 0.0
    
@then('a is not a point')
def step_impl(context):
    assert context.a[3] != 1.0
    
@then('a is a vector')
def step_impl(context):
    assert context.a[3] != 1.0
    
# -----------------------------------------

@given('p <- point(4, -4, 3)')
def step_impl(context):
    context.p = (4, -4, 3, 1)

@then('p = tuple(4, -4, 3, 1)')
def step_impl(context):
    assert context.p == (4, -4, 3, 1)