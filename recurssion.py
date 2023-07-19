# Recursion
# This is when a function calls itself

# Example 1 Psuedo code

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()

    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")


# Example 2 Psuedo code

def look_for_key(box):
    for item in box:
        if item.is_a_box(): # Recursive Case
            look_for_key(item) # <--- Recursion
        elif item.is_a_key(): # Base Case
            print("found the key!")