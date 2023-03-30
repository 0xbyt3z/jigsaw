import drawsvg as draw


width = 100
height = 100

arr = [
    {"cx1": 0, "cy1": 0, "cx2": 35, "cy2": 15, "ex": 37, "ey": 5},
    {"cx1": 37, "cy1": 5, "cx2": 40, "cy2": 0, "ex": 38, "ey": -5},
    {"cx1": 38, "cy1": -5, "cx2": 20, "cy2": -20, "ex": 50, "ey": -20},
    {"cx1": 50, "cy1": -20, "cx2": 80, "cy2": -20, "ex": 62, "ey": -5},
    {"cx1": 62, "cy1": -10, "cx2": 60, "cy2": 0, "ex": 63, "ey": 5},
    {"cx1": 63, "cy1": 5, "cx2": 65, "cy2": 15, "ex": 100, "ey": 0},
]

d = draw.Drawing(width, height, origin=(0, 0))


# Draw an arbitrary path (a triangle in this case)
p = draw.Path(stroke_width=1, stroke="black", fill="none")

p.M(0, 50)
p.C(
    arr[0]["cx1"],
    arr[0]["cy1"] + 50,
    arr[0]["cx2"],
    arr[0]["cy2"] + 50,
    arr[0]["ex"],
    arr[0]["ey"] + 50,
)
for i in arr[1:]:
    # p.C(0, 0, 35, 15, 37, 5)
    p.S(i["cx2"], i["cy2"] + 50, i["ex"], i["ey"] + 50)
    d.append(p)


d.set_pixel_scale(2)  # Set number of pixels per geometry unit
# d.set_render_size(400, 200)  # Alternative to set_pixel_scale
d.save_svg("example.svg")
