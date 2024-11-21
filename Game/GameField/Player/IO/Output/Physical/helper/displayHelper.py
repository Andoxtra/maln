from PIL import Image


def setup_img():
    img = Image.new('1', (128, 64), 0)
    return img


def create_static_structure_lines(draw):
    lines = [
        {"x0": 0, "y0": 0, "x1": 127, "y1": 0},
        {"x0": 0, "y0": 63, "x1": 127, "y1": 63},
        {"x0": 0, "y0": 1, "x1": 0, "y1": 62},
        {"x0": 127, "y0": 1, "x1": 127, "y1": 62},
        {"x0": 64, "y0": 1, "x1": 64, "y1": 62},
        {"x0": 1, "y0": 43, "x1": 126, "y1": 43},
        {"x0": 1, "y0": 12, "x1": 63, "y1": 12},
        {"x0": 16, "y0": 13, "x1": 16, "y1": 30},
        {"x0": 32, "y0": 13, "x1": 32, "y1": 30},
        {"x0": 48, "y0": 13, "x1": 48, "y1": 30},
        {"x0": 1, "y0": 31, "x1": 63, "y1": 31},
        {"x0": 16, "y0": 44, "x1": 16, "y1": 62},
        {"x0": 32, "y0": 44, "x1": 32, "y1": 62},
        {"x0": 48, "y0": 44, "x1": 48, "y1": 62},
    ]
    for line in lines:
        draw.line((line["x0"], line["y0"], line["x1"], line["y1"]), fill=1)


def create_static_cube_border(draw):
    lines = [
        {"x0": 82, "y0": 5, "x1": 111, "y1": 5},
        {"x0": 112, "y0": 6, "x1": 112, "y1": 6},
        {"x0": 113, "y0": 7, "x1": 113, "y1": 36},
        {"x0": 112, "y0": 37, "x1": 112, "y1": 37},
        {"x0": 82, "y0": 38, "x1": 111, "y1": 38},
        {"x0": 81, "y0": 37, "x1": 81, "y1": 37},
        {"x0": 80, "y0": 36, "x1": 80, "y1": 7},
        {"x0": 81, "y0": 6, "x1": 81, "y1": 6},
    ]
    for line in lines:
        draw.line((line["x0"], line["y0"], line["x1"], line["y1"]), fill=1)


def create_static_text(draw):
    characters = [
        {"x0": 16, "y0": 8, "char": "S"},
        {"x0": 21, "y0": 8, "char": "P"},
        {"x0": 26, "y0": 8, "char": "I"},
        {"x0": 30, "y0": 8, "char": "E"},
        {"x0": 35, "y0": 8, "char": "L"},
        {"x0": 40, "y0": 8, "char": "E"},
        {"x0": 45, "y0": 8, "char": "R"},

        {"x0": 16, "y0": 39, "char": "F"},
        {"x0": 21, "y0": 39, "char": "I"},
        {"x0": 25, "y0": 39, "char": "G"},
        {"x0": 30, "y0": 39, "char": "U"},
        {"x0": 35, "y0": 39, "char": "R"},
        {"x0": 40, "y0": 39, "char": "E"},
        {"x0": 45, "y0": 39, "char": "N"},

        {"x0": 68, "y0": 49, "char": "1"},
        {"x0": 74, "y0": 49, "char": "."},
        {"x0": 77, "y0": 49, "char": "S"},
        {"x0": 82, "y0": 49, "char": "T"},
        {"x0": 88, "y0": 49, "char": "A"},
        {"x0": 93, "y0": 49, "char": "R"},
        {"x0": 98, "y0": 49, "char": "T"},

        {"x0": 67, "y0": 55, "char": "2"},
        {"x0": 74, "y0": 55, "char": "."},
        {"x0": 77, "y0": 55, "char": "S"},
        {"x0": 82, "y0": 55, "char": "P"},
        {"x0": 87, "y0": 55, "char": "I"},
        {"x0": 91, "y0": 55, "char": "E"},
        {"x0": 96, "y0": 55, "char": "L"},
        {"x0": 101, "y0": 55, "char": "F"},
        {"x0": 106, "y0": 55, "char": "E"},
        {"x0": 111, "y0": 55, "char": "L"},
        {"x0": 116, "y0": 55, "char": "D"},

        {"x0": 66, "y0": 61, "char": "3"},
        {"x0": 74, "y0": 61, "char": "."},
        {"x0": 77, "y0": 61, "char": "H"},
        {"x0": 82, "y0": 61, "char": "A"},
        {"x0": 87, "y0": 61, "char": "U"},
        {"x0": 92, "y0": 61, "char": "S"},

    ]
    for character in characters:
        draw_char(draw, character["char"], character["x0"], character["y0"])


def get_crown_pos():
    pos = [
        {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": 0}, {"x": 4, "y": 0}, {"x": 5, "y": 0},
        {"x": 6, "y": 0}, {"x": 7, "y": 0}, {"x": 8, "y": 0}, {"x": 9, "y": 0}, {"x": 10, "y": 0}, {"x": 10, "y": -1},
        {"x": 10, "y": -2}, {"x": 10, "y": -3}, {"x": 9, "y": -3}, {"x": 8, "y": -2}, {"x": 7, "y": -3},
        {"x": 6, "y": -2}, {"x": 5, "y": -3}, {"x": 4, "y": -2}, {"x": 3, "y": -3}, {"x": 2, "y": -2},
        {"x": 1, "y": -3}, {"x": 0, "y": -3}, {"x": 0, "y": -2}, {"x": 0, "y": -1}, {"x": 0, "y": 0},
    ]
    return pos


def get_cube_eyes_pos():
    pos = {
        "cube": {"x0": 1, "y0": -6, "x1": 6, "y1": 0},
        "lines": [
            {"x0": 1, "y0": 0, "x1": 6, "y1": 0}, {"x0": 7, "y0": -1, "x1": 7, "y1": -6},
            {"x0": 6, "y0": -7, "x1": 1, "y1": -7}, {"x0": 0, "y0": -6, "x1": 0, "y1": -1}
        ]
    }
    return pos


def get_figure_head_pos():
    pos = {
        "cube": {"x0": -2, "y0": -14, "x1": 2, "y1": -7},
        "lines": [
            {"x0": -3, "y0": -13, "x1": -3, "y1": -9}, {"x0": 3, "y0": -13, "x1": 3, "y1": -9}
        ]
    }
    return pos


def get_marker_pos():
    marker_pos = [
        {"x0": 4, "y0": 1, "x1": 10, "y1": 1},
        {"x0": 3, "y0": 2, "x1": 11, "y1": 2},
        {"x0": 2, "y0": 3, "x1": 12, "y1": 3},
        {"x0": 1, "y0": 4, "x1": 13, "y1": 4},
        {"x0": 0, "y0": 5, "x1": 14, "y1": 5}
    ]
    return marker_pos


def get_status_dict():
    status_dict = {
        0: "1",
        1: "2",
        2: "3"
    }
    return status_dict


def get_figure_dict():
    figure_dict = {
        0: {"x": 8, "y": 60},
        1: {"x": 24, "y": 60},
        2: {"x": 40, "y": 60},
        3: {"x": 56, "y": 60}
    }
    return figure_dict


def get_player_dict():
    player_dict = {
        0: {"x": 1, "y": 25},
        1: {"x": 17, "y": 25},
        2: {"x": 33, "y": 25},
        3: {"x": 49, "y": 25}
    }
    return player_dict


def draw_rectangle_with_corner_by_line_and_cube(draw, pos, fill, x, y):
    for line in pos["lines"]:
        draw.line((line["x0"] + x, line["y0"] + y, line["x1"] + x, line["y1"] + y), fill=fill)
    cube = pos["cube"]
    draw.rectangle([(cube["x0"] + x, cube["y0"] + y), (cube["x1"] + x, cube["y1"] + y)], fill=fill)


def draw_cube(draw, x, y):
    cube_eyes_pos = get_cube_eyes_pos()
    draw_rectangle_with_corner_by_line_and_cube(draw, cube_eyes_pos, "white", x, y)


def clean_dice(draw):
    draw.rectangle([(83, 8), (110, 35)], fill="black", width=0)


def draw_dice_by_cube_eye(draw, cube_eye):
    cube_pos = {
        1: [{"x": 93, "y": 26}],
        2: [{"x": 83, "y": 35}, {"x": 103, "y": 15}],
        3: [{"x": 83, "y": 35}, {"x": 93, "y": 25}, {"x": 103, "y": 15}],
        4: [{"x": 83, "y": 35}, {"x": 83, "y": 15}, {"x": 103, "y": 15}, {"x": 103, "y": 35}],
        5: [{"x": 83, "y": 35}, {"x": 83, "y": 15}, {"x": 93, "y": 25}, {"x": 103, "y": 15},
            {"x": 103, "y": 35}],
        6: [{"x": 83, "y": 35}, {"x": 83, "y": 25}, {"x": 83, "y": 15}, {"x": 103, "y": 15},
            {"x": 103, "y": 25}, {"x": 103, "y": 35}]
        }
    clean_dice(draw)
    cube_to_draw = cube_pos[cube_eye]
    for single_cube in cube_to_draw:
        draw_cube(draw, single_cube["x"], single_cube["y"])


def get_pos_for_char(character):
    char = {
        "S": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": -1}, {"x": 2, "y": -2},
              {"x": 1, "y": -2}, {"x": 0, "y": -3}, {"x": 1, "y": -4}, {"x": 2, "y": -4}, {"x": 3, "y": -4}],
        "P": [{"x": 0, "y": 0}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4},
              {"x": 1, "y": -4}, {"x": 2, "y": -4}, {"x": 3, "y": -3}, {"x": 2, "y": -2}, {"x": 1, "y": -2}],
        "I": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 1, "y": -1}, {"x": 1, "y": -2},
              {"x": 1, "y": -3}, {"x": 1, "y": -4}, {"x": 0, "y": -4}, {"x": 2, "y": -4}],
        "E": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": 0}, {"x": 0, "y": -1},
              {"x": 0, "y": -2}, {"x": 1, "y": -2}, {"x": 2, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4},
              {"x": 1, "y": -4}, {"x": 2, "y": -4}, {"x": 3, "y": -4}],
        "L": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": 0}, {"x": 0, "y": -1},
              {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4}],
        "R": [{"x": 0, "y": 0}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4},
              {"x": 1, "y": -4}, {"x": 2, "y": -4}, {"x": 3, "y": -3}, {"x": 1, "y": -2}, {"x": 2, "y": -2},
              {"x": 2, "y": -1}, {"x": 3, "y": 0}],
        "F": [{"x": 0, "y": 0}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4},
              {"x": 1, "y": -4}, {"x": 2, "y": -4}, {"x": 3, "y": -4}, {"x": 1, "y": -2}, {"x": 2, "y": -2}],
        "G": [{"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": -1}, {"x": 3, "y": -2}, {"x": 2, "y": -2},
              {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 1, "y": -4}, {"x": 2, "y": -4}],
        "U": [{"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": -1}, {"x": 3, "y": -2}, {"x": 3, "y": -3},
              {"x": 3, "y": -4}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4}],
        "N": [{"x": 0, "y": 0}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4},
              {"x": 1, "y": -3}, {"x": 2, "y": -2}, {"x": 3, "y": -4}, {"x": 3, "y": -3}, {"x": 3, "y": -2},
              {"x": 3, "y": -1}, {"x": 3, "y": 0}],
        "T": [{"x": 2, "y": 0}, {"x": 2, "y": -1}, {"x": 2, "y": -2}, {"x": 2, "y": -3}, {"x": 0, "y": -4},
              {"x": 1, "y": -4}, {"x": 2, "y": -4}, {"x": 3, "y": -4}, {"x": 4, "y": -4}],
        "A": [{"x": 0, "y": 0}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 1, "y": -4},
              {"x": 2, "y": -4}, {"x": 3, "y": -3}, {"x": 3, "y": -2}, {"x": 2, "y": -2}, {"x": 1, "y": -2},
              {"x": 3, "y": -1}, {"x": 3, "y": -0}],
        "D": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": -1}, {"x": 3, "y": -2},
              {"x": 3, "y": -3}, {"x": 2, "y": -4}, {"x": 1, "y": -4}, {"x": 0, "y": -4}, {"x": 0, "y": -3},
              {"x": 0, "y": -2}, {"x": 0, "y": -1}],
        "H": [{"x": 0, "y": 0}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4},
              {"x": 1, "y": -2}, {"x": 2, "y": -2}, {"x": 3, "y": -4}, {"x": 3, "y": -3}, {"x": 3, "y": -2},
              {"x": 3, "y": -1}, {"x": 3, "y": 0}],
        "B": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": -1}, {"x": 2, "y": -2},
              {"x": 1, "y": -2}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4},
              {"x": 1, "y": -4}, {"x": 2, "y": -4}, {"x": 3, "y": -3}],
        ".": [{"x": 0, "y": 0}],
        "1": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 1, "y": -1}, {"x": 1, "y": -2},
              {"x": 1, "y": -3}, {"x": 0, "y": -4}, {"x": 1, "y": -4}, {"x": 2, "y": -4}],
        "2": [
            {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": 0}, {"x": 4, "y": 0},
            {"x": 1, "y": -1}, {"x": 1, "y": -2}, {"x": 1, "y": -3}, {"x": 3, "y": -1}, {"x": 3, "y": -2},
            {"x": 3, "y": -3}, {"x": 0, "y": -4}, {"x": 1, "y": -4}, {"x": 2, "y": -4}, {"x": 3, "y": -4},
            {"x": 4, "y": -4}],
        "3": [
            {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": 0}, {"x": 4, "y": 0},
            {"x": 5, "y": 0}, {"x": 6, "y": 0}, {"x": 0, "y": -4}, {"x": 1, "y": -4}, {"x": 2, "y": -4},
            {"x": 3, "y": -4}, {"x": 4, "y": -4}, {"x": 5, "y": -4}, {"x": 6, "y": -4}, {"x": 1, "y": -1},
            {"x": 1, "y": -2}, {"x": 1, "y": -3}, {"x": 3, "y": -1}, {"x": 3, "y": -2}, {"x": 3, "y": -3},
            {"x": 5, "y": -1}, {"x": 5, "y": -2}, {"x": 5, "y": -3},
        ]
    }
    return char[character]


def draw_char(draw, char, x, y):
    pos_for_char = get_pos_for_char(char)
    for pos in pos_for_char:
        draw.point((x + pos["x"], y + pos["y"]), fill=1)


def get_pos_of_figure_outline():
    pos_of_figure = [
        {"x": 0, "y": 0}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}, {"x": 0, "y": -4},
        {"x": 0, "y": -5}, {"x": 0, "y": -6}, {"x": 1, "y": -7}, {"x": 1, "y": -8}, {"x": 2, "y": -9},
        {"x": 3, "y": -10}, {"x": 2, "y": -11}, {"x": 2, "y": -12}, {"x": 2, "y": -13}, {"x": 2, "y": -14},
        {"x": 2, "y": -15}, {"x": 3, "y": -16}, {"x": 4, "y": -17}, {"x": 5, "y": -17}, {"x": 6, "y": -17},
        {"x": 7, "y": -17}, {"x": 8, "y": -17}, {"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3},
        {"x": 0, "y": -4}, {"x": 0, "y": -5}, {"x": 9, "y": -16}, {"x": 10, "y": -15}, {"x": 10, "y": -14},
        {"x": 10, "y": -13}, {"x": 10, "y": -12}, {"x": 10, "y": -11}, {"x": 9, "y": -10}, {"x": 10, "y": -9},
        {"x": 11, "y": -8}, {"x": 11, "y": -7}, {"x": 12, "y": -6}, {"x": 12, "y": -5}, {"x": 12, "y": -4},
        {"x": 12, "y": -3}, {"x": 12, "y": -2}, {"x": 12, "y": -1}, {"x": 12, "y": 0}
    ]
    return pos_of_figure


def draw_figure_outline(draw, x, y):
    figure_outline = get_pos_of_figure_outline()
    for pixel in figure_outline:
        draw.point((pixel["x"] + x, pixel["y"] + y), fill=1)


def create_all_figures_outline(draw):
    draw_figure_outline(draw, 2, 62)
    draw_figure_outline(draw, 18, 62)
    draw_figure_outline(draw, 34, 62)
    draw_figure_outline(draw, 50, 62)


def draw_figure_status(draw, figure, status):
    figure_dict = get_figure_dict()
    status_dict = get_status_dict()
    clean_figure_status(draw, figure)
    x = figure_dict[figure]["x"] - (status + 1)
    y = figure_dict[figure]["y"]
    draw_char(draw, status_dict[status], x, y)


def clean_figure_status(draw, figure):
    figure_dict = get_figure_dict()
    figure_pos = figure_dict[figure]
    x = figure_pos["x"]
    y = figure_pos["y"]
    draw.rectangle([(x - 3, y - 5), (x + 3, y)], fill="black")


def clean_figures_selected(draw):
    figure_head_pos = get_figure_head_pos()
    figure_dict = get_figure_dict()
    for figure in figure_dict.values():
        draw_rectangle_with_corner_by_line_and_cube(draw, figure_head_pos, "black", figure["x"], figure["y"])


def clear_player_by_color(draw, color):
    player_positions = {
        0: {"x0": 1, "y0": 13, "x1": 15, "y1": 30},
        1: {"x0": 17, "y0": 13, "x1": 31, "y1": 30},
        2: {"x0": 33, "y0": 13, "x1": 47, "y1": 30},
        3: {"x0": 49, "y0": 13, "x1": 63, "y1": 30}
    }
    player_pos = player_positions[color]
    draw.rectangle([(player_pos["x0"], player_pos["y0"]), (player_pos["x1"], player_pos["y1"])], fill="black")


def draw_figure_selected(draw, figure):
    clean_figures_selected(draw)
    figure_head_pos = get_figure_head_pos()
    figure_dict = get_figure_dict()
    draw_rectangle_with_corner_by_line_and_cube(
        draw, figure_head_pos, "white", figure_dict[figure]["x"], figure_dict[figure]["y"])


def draw_half_players(draw):
    clear_player_by_color(draw, 1)
    clear_player_by_color(draw, 3)
    draw_char(draw, "G", 4, 23)
    draw_char(draw, "E", 9, 23)
    draw_char(draw, "R", 36, 23)
    draw_char(draw, "T", 41, 23)


def draw_all_players(draw):
    draw_char(draw, "G", 4, 23)
    draw_char(draw, "E", 9, 23)
    draw_char(draw, "G", 20, 23)
    draw_char(draw, "N", 25, 23)
    draw_char(draw, "R", 36, 23)
    draw_char(draw, "T", 41, 23)
    draw_char(draw, "B", 52, 23)
    draw_char(draw, "L", 57, 23)


def draw_question_mark(draw, x, y):
    pos_of_question_mark = [
        {"x": 1, "y": 0},
        {"x": 2, "y": 0},
        {"x": 0, "y": -1},
        {"x": 3, "y": -1},
        {"x": 0, "y": -2},
        {"x": 3, "y": -2},
        {"x": 1, "y": -3},
        {"x": 2, "y": -3},
        {"x": 1, "y": -6},
        {"x": 2, "y": -6},
        {"x": 0, "y": -7},
        {"x": 3, "y": -7},
        {"x": 0, "y": -8},
        {"x": 3, "y": -8},
        {"x": 0, "y": -9},
        {"x": 4, "y": -9},
        {"x": 0, "y": -9},
        {"x": 5, "y": -9},
        {"x": 0, "y": -10},
        {"x": 6, "y": -10},
        {"x": 1, "y": -11},
        {"x": 7, "y": -11},
        {"x": 2, "y": -12},
        {"x": 8, "y": -12},
        {"x": 3, "y": -13},
        {"x": 8, "y": -13},
        {"x": 4, "y": -14},
        {"x": 8, "y": -14},
        {"x": 4, "y": -15},
        {"x": 8, "y": -15},
        {"x": 4, "y": -16},
        {"x": 8, "y": -16},
        {"x": 4, "y": -17},
        {"x": 8, "y": -17},
        {"x": -3, "y": -18},
        {"x": -4, "y": -18},
        {"x": 4, "y": -18},
        {"x": 8, "y": -18},
        {"x": -5, "y": -19},
        {"x": -2, "y": -19},
        {"x": 4, "y": -19},
        {"x": 8, "y": -19},
        {"x": -5, "y": -20},
        {"x": -2, "y": -20},
        {"x": 4, "y": -20},
        {"x": 8, "y": -20},
        {"x": -5, "y": -21},
        {"x": -1, "y": -21},
        {"x": 0, "y": -21},
        {"x": 1, "y": -21},
        {"x": 2, "y": -21},
        {"x": 3, "y": -21},
        {"x": 4, "y": -21},
        {"x": 8, "y": -21},
        {"x": -4, "y": -22},
        {"x": 7, "y": -22},
        {"x": -3, "y": -23},
        {"x": 6, "y": -23},
        {"x": -2, "y": -24},
        {"x": -1, "y": -24},
        {"x": 0, "y": -24},
        {"x": 1, "y": -24},
        {"x": 2, "y": -24},
        {"x": 3, "y": -24},
        {"x": 4, "y": -24},
        {"x": 5, "y": -24}
    ]
    for pos in pos_of_question_mark:
        draw.point((x + pos["x"], y + pos["y"]), fill=1)


def draw_players(draw, number_of_player):
    if number_of_player == 4:
        draw_all_players(draw)
    elif number_of_player == 2:
        draw_half_players(draw)


def get_player_to_clean_dict():
    player_to_clean_dict = {
        0: [0, 1, 2, 3],
        1: [0, 1, 2, 3],
        2: [0, 1, 2, 3],
        3: [0, 1, 2, 3]
    }
    return player_to_clean_dict


def clear_current_player(draw, current_player):
    player_to_clean_dict = get_player_to_clean_dict()
    player_dict = get_player_dict()
    players_to_clean = player_to_clean_dict[current_player]
    for player in players_to_clean:
        x = player_dict[player]["x"]
        y = player_dict[player]["y"]
        draw.line((x + 0, y + 0, x + 14, y + 0), fill="black")
        draw.line((x + 0, y - 8, x + 14, y - 8), fill="black")


def draw_current_player(draw, current_player):
    clear_current_player(draw, current_player)
    player_dict = get_player_dict()
    x = player_dict[current_player]["x"]
    y = player_dict[current_player]["y"]
    draw.line((x + 0, y + 0, x + 14, y + 0), fill=1)
    draw.line((x + 0, y - 8, x + 14, y - 8), fill=1)


def draw_crown(draw, x, y):
    crown_pos = get_crown_pos()
    for pixel in crown_pos:
        draw.point((pixel["x"] + x, pixel["y"] + y), fill=1)


def create_marker_for_own_player(draw, player):
    marker_pos = get_marker_pos()
    player_dict = get_player_dict()
    x = player_dict[player]["x"]
    y = player_dict[player]["y"]
    for pos in marker_pos:
        draw.line((pos["x0"] + x, pos["y0"] + y, pos["x1"] + x, pos["y1"] + y), fill=1)


def draw_player_won(draw, player_won):
    player_dict = get_player_dict()
    x = player_dict[player_won]["x"] + 2
    y = player_dict[player_won]["y"] - 8
    draw_crown(draw, x, y)


def create_all_static(draw, color_of_own_player):
    create_static_structure_lines(draw)
    create_static_cube_border(draw)
    create_static_text(draw)
    create_all_figures_outline(draw)
    create_marker_for_own_player(draw, color_of_own_player)


def clearDisplay(draw):
    draw.rectangle([(0, 0), (128, 64)], fill="black", width=0)


#img = setup_img()
# draw = ImageDraw.Draw(img)
# create_all_static(draw, 1)
# draw_players(draw, 4)
# draw_current_player(draw, 2)
# draw_current_player(draw, 0)
# draw_dice_by_cube_eye(draw, 6)
# draw_dice_by_cube_eye(draw, 3)
# draw_figure_selected(draw, 3)
# draw_figure_selected(draw, 3)
# draw_figure_status(draw, 3, 2)
# draw_figure_status(draw, 2, 0)
# draw_player_won(draw, 2)
# clear_player_by_color(draw, 0)
# clearDisplay(draw)
# img.save('./simplePixel.png')  # or any image format
