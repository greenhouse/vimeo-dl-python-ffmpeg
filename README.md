# vimeo-dl-python-ffmpeg
download any publically accessible vimeo videos (080125)


## Requirements
- vimeo video url from a video that is publically accessible
    - ex: https://vimeo.com/1105215213
- web browser to retreive video config json
- ffmpeg -> $ brew install ffmpeg

## instructions:
- navigate to the video: https://vimeo.com/1105215213
- right-click -> inspect -> network
- look for 'config' file 
- click 'preview' to view json
- copy json to vimeo_json.py
    - in 'vimeo_json.py' set video_config_json = <copied_json>
- run     ```$ python3.11 vimeo_download.py```

## NOTES:
- vimeo may change their config json format
    - this script curently expects the following format (as of 080125) ... ref: vimeo_download.py

        ```m3u8_url = video_config_json['request']['files']['hls']['cdns']['akfire_interconnect_quic']['avc_url']```
- if this script breaks because vimeo changes their json format, 
    then simply look for the key 'avc_url' in the 'config' json retreived from 'inspect -> network' (above)
    and set that url value to 'm3u8_url' in vimeo_download.py
