import turtle


def hilbert(level, edge_len, flip, turtle):
    if level < 1: return

    if flip:
        turtle.left(90)
    else:
        turtle.right(90)

    hilbert(level - 1, edge_len, not flip, turtle)
    turtle.forward(edge_len)

    if flip:
        turtle.right(90)
    else:
        turtle.left(90)

    hilbert(level - 1, edge_len, flip, turtle)
    turtle.forward(edge_len)
    hilbert(level - 1, edge_len, flip, turtle)

    if flip:
        turtle.right(90)
    else:
        turtle.left(90)

    turtle.forward(edge_len)
    hilbert(level - 1, edge_len, not flip, turtle)

    if flip:
        turtle.left(90)
    else:
        turtle.right(90)


if __name__ == '__main__':
  hilbert(3, 20, False, turtle.Turtle())
