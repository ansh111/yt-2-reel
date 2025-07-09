import ffmpeg

def cut_clips(input_file, clips):
    output_files = []
    for i, clip in enumerate(clips):
        start = float(clip['start'])
        end = float(clip['end'])
        duration = end - start

        out_path = f"static/clip_{i}.mp4"

        (
            ffmpeg
            .input(input_file, ss=start, t=duration)
            .output(
                out_path,
                vf='scale=720:1280',
                acodec='aac',          # ✅ encode audio
                audio_bitrate='128k',  # optional: set audio quality
                vcodec='libx264',      # optional: re-encode video
                preset='fast',
                movflags='faststart'
            )
            .overwrite_output()
            .run()
        )

        print(f"Generated clip: {out_path}")
        output_files.append(out_path)

    return output_files
