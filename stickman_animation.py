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

        t = frame / FPS
        img = Image.new("RGB", (W, H), "#17243b")
        d = ImageDraw.Draw(img)

        # Background
        d.rectangle((0, 900, W, H), fill="#303c35")

        # Scene 1: Forest
        if t < 15:
            d.text((230, 100), "THE ADVENTURE", fill="white")
            for x in range(50, 700, 180):
                d.rectangle((x, 500, x+25, 900), fill="#68452e")
                d.ellipse((x-70, 400, x+100, 620), fill="#23733e")

        # Scene 2: Obstacles
        elif t < 30:
            d.text((260, 100), "THE CHALLENGE", fill="white")
            d.rectangle((400, 800, 490, 900), fill="orange")

        # Scene 3: Treasure
        else:
            d.text((260, 100), "THE TREASURE", fill="white")
            d.rectangle((450, 750, 590, 850), fill="gold")
            d.text((480, 780), "$$$", fill="black")

        # Stickman
        x = 180 + int(100 * math.sin(t))
        y = 700 - int(70 * abs(math.sin(t * 3)))

        d.ellipse((x-30, y-150, x+30, y-90),
                  outline="white", width=7)
        d.line((x, y-90, x, y+30),
               fill="white", width=8)
        d.line((x, y-60, x-55, y-20),
               fill="white", width=7)
        d.line((x, y-60, x+55, y-20),
               fill="white", width=7)
        d.line((x, y+30, x-40, y+100),
               fill="white", width=8)
        d.line((x, y+30, x+40, y+100),
               fill="white", width=8)

        video.append_data(np.array(img))

print("Adventure video created!")
