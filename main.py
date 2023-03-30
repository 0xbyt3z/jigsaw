import drawsvg as draw


width = 500
height = 300

d = draw.Drawing(width, height, origin=(0, 0))


# Draw a rectangle
r = draw.Rectangle(0, 0, width, height, stroke="black", fill="none")
r.append_title("base")  # Add a tooltip
d.append(r)


# Draw an arbitrary path (a triangle in this case)
p = draw.Path(stroke_width=1, stroke="black", fill="black", fill_opacity=0.2)
for i in [[20, 20]]:
    p.M(i[0], i[1])  # Start path at point
    p.C(30, 10, 30, 10, 70, 50)  # Draw a curve to (70, -20)
    d.append(p)


d.set_pixel_scale(2)  # Set number of pixels per geometry unit
# d.set_render_size(400, 200)  # Alternative to set_pixel_scale
d.save_svg("example.svg")
