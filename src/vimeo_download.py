'''
    instructinos:
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
output_file = "downloaded_video_2.mp4"

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


    

# import requests
# import vimeo_json
# # set target video url
# # target_video_url = 'https://vimeo.com/712159936'
# # target_video_url= "https://vimeo.com/1105215213/4bf2776f9b"
# target_video_url= "https://vimeo.com/1105215213"

# # remove slash from the end of the url
# if target_video_url[-1] == '/':
#     target_video_url = target_video_url[:-1]

# # get video id from url
# video_id = target_video_url.split('/')[-1]

# # check the result
# print(video_id)

# ## --------
# # set video config url
# video_config_url = 'https://player.vimeo.com/video/' + video_id + '/config'

# # send get request to get video json config
# print('go 1')
# video_config_response = requests.get(video_config_url)
# print('go 2')
# print(f'video_config_response: {video_config_response}')
# # generate obj from json
# # video_config_json = video_config_response.json()
# video_config_json = vimeo_json.video_config_json
# # check the result
# print(video_config_json)

# # exit()

# ##-------
# # make variable for video config
# # video_config = video_config_json['request']['files']['progressive'][0]
# video_config = video_config_json['request']['files']['dash']['streams'][0]

# # get video url
# # video_url = video_config['url']
# # video_url = "https://skyfire.vimeocdn.com/1753768173-0x9d9059dfe9ca1beb473f5cae4165de014d1d8902/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/prot/cXNyPTE/playlist.json?pathsig=8c953e4f~z8oY8GOMIZCYUWT2u2dLIliZTl_OMmc4oxuJis4NX2Y&qsr=1&r=dXM%3D&rh=1cruGi"
# # video_url = "https://vod-adaptive-ak.vimeocdn.com/exp=1753768173~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=eb14ebc54e28a7fe9454f96f07c0b3b2204e1576722a7d1252c65529cf52957d/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/prot/cXNyPTE/playlist.json?pathsig=8c953e4f~z8oY8GOMIZCYUWT2u2dLIliZTl_OMmc4oxuJis4NX2Y&qsr=1&r=dXM%3D&rh=1cruGi"
# # video_url = "https://vod-adaptive-ak.vimeocdn.com/exp=1753768173~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=eb14ebc54e28a7fe9454f96f07c0b3b2204e1576722a7d1252c65529cf52957d/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/prot/cXNyPTE/playlist.json?omit=av1-hevc&pathsig=8c953e4f~z8oY8GOMIZCYUWT2u2dLIliZTl_OMmc4oxuJis4NX2Y&qsr=1&r=dXM%3D&rh=1cruGi"
# # video_url = "https://vod-adaptive-ak.vimeocdn.com/exp=1753768173~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=eb14ebc54e28a7fe9454f96f07c0b3b2204e1576722a7d1252c65529cf52957d/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4"
# video_url = "https://vod-adaptive-ak.vimeocdn.com/exp=1753768173~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=eb14ebc54e28a7fe9454f96f07c0b3b2204e1576722a7d1252c65529cf52957d/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=av1-hevc-opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4"
# # prepare file name for that video
# video_name = video_id + '_' + video_config['quality'] + '.mp4'

# # download video
# video_response = requests.get(video_url)

# # open file and write content there
# video_file = open(video_name, 'wb')
# video_file.write(video_response.content)
# video_file.close()

# # print result
# print('downloaded: ' + video_name)






# import vimeo_dl as vimeo
# # url = "https://vimeo.com/140816903"
# # url = "https://vimeo.com/1105215213/4bf2776f9b"
# url = "https://vimeo.com/1105215213/4bf2776f9b?share=copy"
# video = vimeo.new(url)
# # video.title
# # '[PHP][C++]Root Exploiter - No Back-Connect (Part 2)'

# # video.viewcounts, video.author, video.likes
# # (647, u'Mukarram Khalid', 0)

# # video.author, video.duration
# # ('Mukarram Khalid', '10:00')
# streams = video.streams
# for s in streams:
#     print(s)
# # normal:mp4@1162x720
# # normal:webm@640x398
# streams[0].download(quiet=False)
# # 163,840 Bytes [0.56%] received. Rate: [ 275 KB/s].  ETA: [104 secs]
# # best.download(quiet=False)
# # 212,992 Bytes [2.64%] received. Rate: [ 203 KB/s].  ETA: [38 secs]