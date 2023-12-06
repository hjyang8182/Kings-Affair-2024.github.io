# script to convert image sequence to video using moviepy

import moviepy.editor as mp
import sys
from imageio.plugins.ffmpeg import get_exe

print('ffmpeg binary:', get_exe())

sys.exit()

clip = mp.ImageSequenceClip('assets/bg/images/edited', fps=24)
# as high quality as possible
# clip.write_videofile(
#     'bg.mp4',
#     codec='libx264',
#     audio=False,
#     preset='veryslow',
#     ffmpeg_params=['-crf', '17', '-tune', 'animation', '-pix_fmt', 'yuv420p'])
clip.write_videofile(
    'bg_lossless.webm',
    # codec='libvpx-vp9',
    audio=False,
    preset='veryslow',
    ffmpeg_params=['-crf', '4', '-pix_fmt', 'yuv420p'])
