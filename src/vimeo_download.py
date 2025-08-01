'''
    instructions:
        - navigate to video: https://vimeo.com/1105215213/4bf2776f9b?share=copy
        - right-click -> inspect -> network
        - look for 'config' file 
        - click 'preview' to view json
        - from json set m3u8_url = video_config_json['request']['files']['hls']['cdns']['akfire_interconnect_quic']['avc_url']
'''
import subprocess
import requests
import vimeo_json

# Your .m3u8 URL
# m3u8_url = "https://vod-adaptive-ak.vimeocdn.com/exp=1753768173~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=eb14ebc54e28a7fe9454f96f07c0b3b2204e1576722a7d1252c65529cf52957d/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=av1-hevc-opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4"
m3u8_url = vimeo_json.video_config_json['request']['files']['hls']['cdns']['akfire_interconnect_quic']['avc_url']

# Output file path
output_file = "downloaded_video_0.mp4"

# Optional: Add headers or cookies for authentication (if the video is private)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    # Add cookies if needed, e.g., "Cookie": "vuid=abc123; ..."
}

try:
    # Test if the URL is accessible
    response = requests.head(m3u8_url, headers=headers)
    if response.status_code != 200:
        print(f"Error: URL returned status code {response.status_code}. Check authentication or URL validity.")
        exit(1)

    # Run ffmpeg to download and convert the stream to MP4
    ffmpeg_command = [
        "ffmpeg",
        "-i", m3u8_url,
        "-c", "copy",  # Copy streams without re-encoding
        "-bsf:a", "aac_adtstoasc",  # Fix audio stream if needed
        output_file
    ]

    # If headers/cookies are needed, add them to ffmpeg (requires ffmpeg-python or custom handling)
    subprocess.run(ffmpeg_command, check=True)
    print(f"Video downloaded successfully to {output_file}")

except subprocess.CalledProcessError as e:
    print(f"ffmpeg error: {e}")
except requests.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")