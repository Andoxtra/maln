def is_figure_in_start(figure):
    if figure.status == 0:
        return True
    else:
        return False


def is_figure_in_home(figure):
    if figure.status == 2:
        return True
    else:
        return False


def is_figure_on_gamefield(figure):
    if figure.status == 1:
        return True
    else:
        return False
