def is_list_empty(list_to_check):
    if list_to_check is None or len(list_to_check) == 0:
        return True
    else:
        return False


def get_index_of_highest_number_in_list(list_to_check):
    temp_list = [0, 0]
    for index, number in enumerate(list_to_check):
        if number > temp_list[0]:
            temp_list[0] = number
            temp_list[1] = index

    return temp_list[1]


def get_rgb_color_from_hex_to_int(color_in_hex):
    hex_string = color_in_hex.lstrip('#')
    r = int(hex_string[0:2], 16)
    g = int(hex_string[2:4], 16)
    b = int(hex_string[4:6], 16)

    return r, g, b


def get_color_in_hex_from_color_code(color_code):
    color_map = get_color_map()
    color_in_hex = color_map[color_code]
    return color_in_hex


def get_color_code_in_int(color_code):
    colorInHex = get_color_in_hex_from_color_code(color_code)
    return get_rgb_color_from_hex_to_int(colorInHex)


def get_color_code_in_hex(color_code):
    return get_color_in_hex_from_color_code(color_code)


def get_color_map():
    color_map = {
        0: "#ffff00",
        1: "#00ff00",
        2: "#ff0000",
        3: "#0000ff",

        4: "#7f7f00",
        5: "#007f00",
        6: "#7f0000",
        7: "#00007f",

        8: "#7f7f7f",
        9: "#ffffff",
        10: "#000000",

        11: "#ffff00",
        12: "#00ff00",
        13: "#ff0000",
        14: "#0000ff",
    }
    return color_map


def get_start_field_by_color(color):
    return color * 10 + 32
