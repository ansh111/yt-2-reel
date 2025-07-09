import yt_dlp

def download_video(url, output_path="video.mp4") :
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': output_path,
        'sleep_interval': 10,          # 10 seconds between downloads to avoid rate limiting
        'max_sleep_interval': 15,  
        'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]',
        'external_downloader': 'aria2c',
        'external_downloader_args': ['-x', '16', '-k', '1M'],  
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path