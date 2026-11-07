from PIL import Image, ImageDraw
import imageio
import numpy as np
import math

W, H = 720, 1280
FPS = 12
DURATION = 45

with imageio.get_writer(
    "stickman_video.mp4",
    fps=FPS,
    codec="libx264"
) as video:

    for frame in range(FPS * DURATION):

        img = Image.new("RGB", (W, H), "#87CEEB")
        d = ImageDraw.Draw(img)

        # Background
        d.rectangle((0, 900, W, H), fill="#555555")
        d.rectangle((0, 870, W, 900), fill="green")

        # Clouds
        d.ellipse((80, 120, 220, 180), fill="white")
        d.ellipse((400, 200, 550, 260), fill="white")

        # Moving obstacle
        ox = 650 - (frame * 5) % 850
        d.rectangle((ox, 790, ox + 70, 870),
                    fill="brown")

        # Stickman
        x = 180 + int(25 * math.sin(frame * 0.08))
        jump = abs(math.sin(frame * 0.08)) * 100
        y = int(740 - jump)

        # Head
        d.ellipse((x-35, y-150, x+35, y-80),
                  outline="black", width=8)

        # Body
        d.line((x, y-80, x, y+50),
               fill="black", width=9)

        # Arms
        swing = int(35 * math.sin(frame * 0.3))
        d.line((x, y-40, x-50, y+swing),
               fill="black", width=8)
        d.line((x, y-40, x+50, y-swing),
               fill="black", width=8)

        # Legs
        d.line((x, y+50, x-40, y+120+swing),
               fill="black", width=9)
        d.line((x, y+50, x+40, y+120-swing),
               fill="black", width=9)

        video.append_data(np.array(img))

print("Stickman video created!")
