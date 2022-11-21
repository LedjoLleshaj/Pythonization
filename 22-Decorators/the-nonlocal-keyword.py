def outer():
    bubble_tea_flavor = "mango"

    def inner():
        nonlocal bubble_tea_flavor  # same as global, but for non-global variables
        bubble_tea_flavor = "strawberry"

    inner()

    return bubble_tea_flavor

print(outer())