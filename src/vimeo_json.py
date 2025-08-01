video_config_json ={
    "cdn_url": "https://f.vimeocdn.com",
    "vimeo_api_url": "api.vimeo.com",
    "request": {
        "files": {
            "dash": {
                "cdns": {
                    "akfire_interconnect_quic": {
                        "avc_url": "https://vod-adaptive-ak.vimeocdn.com/exp=1753771665~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=cd16ba62701c23d454225e9a7aaf4ad34b88899414e59d25b8d76b8a5e40be2c/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/prot/cXNyPTE/playlist.json?omit=av1-hevc&pathsig=8c953e4f~z8oY8GOMIZCYUWT2u2dLIliZTl_OMmc4oxuJis4NX2Y&qsr=1&r=dXM%3D&rh=1cruGi",
                        "origin": "gcs",
                        "url": "https://vod-adaptive-ak.vimeocdn.com/exp=1753771665~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=cd16ba62701c23d454225e9a7aaf4ad34b88899414e59d25b8d76b8a5e40be2c/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/prot/cXNyPTE/playlist.json?pathsig=8c953e4f~z8oY8GOMIZCYUWT2u2dLIliZTl_OMmc4oxuJis4NX2Y&qsr=1&r=dXM%3D&rh=1cruGi"
                    },
                    "fastly_skyfire": {
                        "avc_url": "https://skyfire.vimeocdn.com/1753771665-0x2a66d648da37253b4f0e5fc71c0c805ef47e82bd/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/prot/cXNyPTE/playlist.json?omit=av1-hevc&pathsig=8c953e4f~z8oY8GOMIZCYUWT2u2dLIliZTl_OMmc4oxuJis4NX2Y&qsr=1&r=dXM%3D&rh=1cruGi",
                        "origin": "gcs",
                        "url": "https://skyfire.vimeocdn.com/1753771665-0x2a66d648da37253b4f0e5fc71c0c805ef47e82bd/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/prot/cXNyPTE/playlist.json?pathsig=8c953e4f~z8oY8GOMIZCYUWT2u2dLIliZTl_OMmc4oxuJis4NX2Y&qsr=1&r=dXM%3D&rh=1cruGi"
                    }
                },
                "default_cdn": "akfire_interconnect_quic",
                "separate_av": True,
                "streams": [
                    {
                        "profile": "f9e4a5d7-8043-4af3-b231-641ca735a130",
                        "id": "d26706a7-164a-45b8-8eb5-cbd43e7c7d2f",
                        "fps": 30,
                        "quality": "540p"
                    },
                    {
                        "profile": "d0b41bac-2bf2-4310-8113-df764d486192",
                        "id": "eda505d5-98dc-4fcb-993b-a3d46135bca0",
                        "fps": 30,
                        "quality": "240p"
                    },
                    {
                        "profile": "c3347cdf-6c91-4ab3-8d56-737128e7a65f",
                        "id": "5dcfc276-d886-4570-8a7b-3b611f472549",
                        "fps": 30,
                        "quality": "360p"
                    }
                ],
                "streams_avc": [
                    {
                        "profile": "f9e4a5d7-8043-4af3-b231-641ca735a130",
                        "id": "d26706a7-164a-45b8-8eb5-cbd43e7c7d2f",
                        "fps": 30,
                        "quality": "540p"
                    },
                    {
                        "profile": "d0b41bac-2bf2-4310-8113-df764d486192",
                        "id": "eda505d5-98dc-4fcb-993b-a3d46135bca0",
                        "fps": 30,
                        "quality": "240p"
                    },
                    {
                        "profile": "c3347cdf-6c91-4ab3-8d56-737128e7a65f",
                        "id": "5dcfc276-d886-4570-8a7b-3b611f472549",
                        "fps": 30,
                        "quality": "360p"
                    }
                ]
            },
            "hls": {
                "captions": "https://vod-adaptive-ak.vimeocdn.com/exp=1753771665~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=cd16ba62701c23d454225e9a7aaf4ad34b88899414e59d25b8d76b8a5e40be2c/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4",
                "cdns": {
                    "akfire_interconnect_quic": {
                        "avc_url": "https://vod-adaptive-ak.vimeocdn.com/exp=1753771665~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=cd16ba62701c23d454225e9a7aaf4ad34b88899414e59d25b8d76b8a5e40be2c/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=av1-hevc-opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4",
                        "captions": "https://vod-adaptive-ak.vimeocdn.com/exp=1753771665~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=cd16ba62701c23d454225e9a7aaf4ad34b88899414e59d25b8d76b8a5e40be2c/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4",
                        "origin": "gcs",
                        "url": "https://vod-adaptive-ak.vimeocdn.com/exp=1753771665~acl=%2Fac3c5092-4d36-4f58-8403-e9440582a9e4%2F%2A~hmac=cd16ba62701c23d454225e9a7aaf4ad34b88899414e59d25b8d76b8a5e40be2c/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4"
                    },
                    "fastly_skyfire": {
                        "avc_url": "https://skyfire.vimeocdn.com/1753771665-0x2a66d648da37253b4f0e5fc71c0c805ef47e82bd/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=av1-hevc-opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4",
                        "captions": "https://skyfire.vimeocdn.com/1753771665-0x2a66d648da37253b4f0e5fc71c0c805ef47e82bd/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4",
                        "origin": "gcs",
                        "url": "https://skyfire.vimeocdn.com/1753771665-0x2a66d648da37253b4f0e5fc71c0c805ef47e82bd/ac3c5092-4d36-4f58-8403-e9440582a9e4/v2/playlist/av/primary/sub/244698559-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&omit=opus&pathsig=8c953e4f~a-PfXBA655efg5fFKARnnng0Huy3b7Iccy4X0r6S1CI&qsr=1&r=dXM%3D&rh=1cruGi&sf=fmp4"
                    }
                },
                "default_cdn": "akfire_interconnect_quic",
                "separate_av": True
            }
        },
        "file_codecs": {
            "av1": [],
            "avc": [
                "d26706a7-164a-45b8-8eb5-cbd43e7c7d2f",
                "eda505d5-98dc-4fcb-993b-a3d46135bca0",
                "5dcfc276-d886-4570-8a7b-3b611f472549"
            ],
            "hevc": {
                "dvh1": [],
                "hdr": [],
                "sdr": []
            }
        },
        "lang": "en",
        "referrer": "https://vimeo.com/",
        "cookie_domain": ".vimeo.com",
        "signature": "50ce606f41b0bced05781539a9b31af7",
        "timestamp": 1753760385,
        "expires": 11280,
        "text_tracks": [
            {
                "id": 244698559,
                "lang": "en-x-autogen",
                "url": "/texttrack/244698559.vtt?token=68886e91_0xfae2bb89c9762c88c8f20710e4ff1e6b20d142af",
                "kind": "subtitles",
                "label": "English (auto-generated)",
                "provenance": "ai_generated"
            }
        ],
        "thumb_preview": {
            "url": "https://videoapi-sprites.vimeocdn.com/video-sprites/image/5fe6b8bd-61a8-476c-a57b-8bfd0bf5b9f4.0.jpeg?ClientID=sulu&Expires=1753763888&Signature=1d73c99b4bbfc5ad117eb6ada53e344bc6b581d1",
            "height": 2640,
            "width": 4686,
            "frame_height": 240,
            "frame_width": 426,
            "columns": 11,
            "frames": 120
        },
        "currency": "USD",
        "session": "915db15c7179c3198ecfd8ce5d84c776dd62e6a41753760385",
        "cookie": {
            "volume": 1,
            "quality": '',
            "hd": 0,
            "captions": '',
            "transcript": '',
            "captions_styles": {
                "color": '',
                "fontSize": '',
                "fontFamily": '',
                "fontOpacity": '',
                "bgOpacity": '',
                "windowColor": '',
                "windowOpacity": '',
                "bgColor": '',
                "edgeStyle": ''
            },
            "audio_language": '',
            "audio_kind": '',
            "qoe_survey_vote": 0
        },
        "build": {
            "backend": "dae115f",
            "js": "4.41.22"
        },
        "urls": {
            "js": "https://f.vimeocdn.com/p/4.41.22/js/player.js",
            "js_base": "https://f.vimeocdn.com/p/4.41.22/js",
            "js_module": "https://f.vimeocdn.com/p/4.41.22/js/player.module.js",
            "js_vendor_module": "https://f.vimeocdn.com/p/4.41.22/js/vendor.module.js",
            "locales_js": {
                "de-DE": "https://f.vimeocdn.com/p/4.41.22/js/player.de-DE.js",
                "en": "https://f.vimeocdn.com/p/4.41.22/js/player.js",
                "es": "https://f.vimeocdn.com/p/4.41.22/js/player.es.js",
                "fr-FR": "https://f.vimeocdn.com/p/4.41.22/js/player.fr-FR.js",
                "ja-JP": "https://f.vimeocdn.com/p/4.41.22/js/player.ja-JP.js",
                "ko-KR": "https://f.vimeocdn.com/p/4.41.22/js/player.ko-KR.js",
                "pt-BR": "https://f.vimeocdn.com/p/4.41.22/js/player.pt-BR.js",
                "zh-CN": "https://f.vimeocdn.com/p/4.41.22/js/player.zh-CN.js"
            },
            "ambisonics_js": "https://f.vimeocdn.com/p/external/ambisonics.min.js",
            "barebone_js": "https://f.vimeocdn.com/p/4.41.22/js/barebone.js",
            "chromeless_js": "https://f.vimeocdn.com/p/4.41.22/js/chromeless.js",
            "three_js": "https://f.vimeocdn.com/p/external/three.rvimeo.min.js",
            "vuid_js": "https://f.vimeocdn.com/js_opt/modules/utils/vuid.min.js",
            "hive_sdk": "https://f.vimeocdn.com/p/external/hive-sdk.js",
            "hive_interceptor": "https://f.vimeocdn.com/p/external/hive-interceptor.js",
            "proxy": "https://player.vimeo.com/static/proxy.html",
            "css": "https://f.vimeocdn.com/p/4.41.22/css/player.css",
            "chromeless_css": "https://f.vimeocdn.com/p/4.41.22/css/chromeless.css",
            "fresnel": "https://arclight.vimeo.com/add/player-stats",
            "player_telemetry_url": "https://arclight.vimeo.com/player-events",
            "telemetry_base": "https://lensflare.vimeo.com"
        },
        "flags": {
            "plays": 1,
            "dnt": 0,
            "autohide_controls": 0,
            "preload_video": "auto",
            "qoe_survey_forced": 0,
            "ai_widget": 0,
            "ecdn_delta_updates": 0,
            "disable_mms": 0,
            "check_clip_skipping_forward": 0
        },
        "country": "US",
        "client": {
            "ip": "8.19.238.175"
        },
        "ab_tests": {
            "prevent_up_switch_not_visible": {
                "group": "control",
                "track": True,
                "data": ''
            }
        },
        "atid": "282861773.1753760385",
        "ai_widget_signature": "bf94e2f338a58f9a757cdcbe4cccec4d9cf1ad923f04bac20d33bca15e3f6f8f_1753763985",
        "config_refresh_url": "https://player.vimeo.com/video/1105215213/config/request?atid=282861773.1753760385&expires=11280&referrer=https%3A%2F%2Fvimeo.com%2F&session=915db15c7179c3198ecfd8ce5d84c776dd62e6a41753760385&signature=50ce606f41b0bced05781539a9b31af7&time=1753760385&v=1"
    },
    "player_url": "player.vimeo.com",
    "video": {
        "id": 1105215213,
        "title": "2025-07-28 12-24-50",
        "width": 852,
        "height": 480,
        "duration": 2820,
        "url": "",
        "share_url": "https://vimeo.com/1105215213",
        "embed_code": "<iframe title=\"vimeo-player\" src=\"https://player.vimeo.com/video/1105215213?h=4bf2776f9b\" width=\"640\" height=\"360\" frameborder=\"0\" referrerpolicy=\"strict-origin-when-cross-origin\" allow=\"autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share\"   allowfullscreen></iframe>",
        "default_to_hd": 0,
        "privacy": "unlisted",
        "embed_permission": "public",
        "thumbnail_url": "https://i.vimeocdn.com/video/2041674282-e399ffc187e2bf5b98242b4b52b10ee605810d7bb8600afd8d88865bbc3a9a93-d",
        "owner": {
            "id": 86600200,
            "name": "TCoast Studios",
            "img": "https://i.vimeocdn.com/portrait/28281405_60x60?sig=5d726de1ae03f03cfcc47dc053c2335342f36213313d0421e1241af004e35575&v=1&region=us",
            "img_2x": "https://i.vimeocdn.com/portrait/28281405_60x60?sig=5d726de1ae03f03cfcc47dc053c2335342f36213313d0421e1241af004e35575&v=1&region=us",
            "url": "https://vimeo.com/tcoaststudios",
            "account_type": "live_premium"
        },
        "spatial": 0,
        "live_event": '',
        "version": {
            "current": '',
            "available": [
                {
                    "id": 1044828030,
                    "file_id": 3921651395,
                    "is_current": True
                }
            ]
        },
        "unlisted_hash": "4bf2776f9b",
        "rating": {
            "id": 6
        },
        "fps": 30,
        "bypass_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGlwX2lkIjoxMTA1MjE1MjEzLCJleHAiOjE3NTM3NzE2ODB9.wB1WkW3KK3wWSE88ICABS3wFERa4ObhVSdaYK6fQ1lE",
        "channel_layout": "stereo",
        "ai": 0,
        "locale": ""
    },
    "user": {
        "id": 0,
        "team_id": 0,
        "team_origin_user_id": 0,
        "account_type": "none",
        "liked": 0,
        "watch_later": 0,
        "owner": 0,
        "mod": 0,
        "logged_in": 0,
        "private_mode_enabled": 0,
        "vimeo_api_client_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uX2lkIjoiOTE1ZGIxNWM3MTc5YzMxOThlY2ZkOGNlNWQ4NGM3NzZkZDYyZTZhNDE3NTM3NjAzODUiLCJleHAiOjE3NTM3NzE2NjUsImFwcF9pZCI6MTE4MzU5LCJzY29wZXMiOiJwdWJsaWMgc3RhdHMifQ.sYF_xy2AC_GGJbIya2vv0X7OtdpeJ8rj8AuaUpgaLE4"
    },
    "view": 1,
    "vimeo_url": "vimeo.com",
    "embed": {
        "autoplay": 0,
        "autopause": 1,
        "dnt": 0,
        "editor": 0,
        "keyboard": 1,
        "log_plays": 1,
        "loop": 0,
        "muted": 0,
        "on_site": 1,
        "texttrack": "",
        "transparent": 0,
        "outro": "nothing",
        "playsinline": 1,
        "quality": '',
        "player_id": "",
        "api": '',
        "app_id": "",
        "color": "00adef",
        "color_one": "000000",
        "color_two": "00adef",
        "color_three": "ffffff",
        "color_four": "000000",
        "context": "Vimeo\\Controller\\Api\\Resources\\VideoController.",
        "settings": {
            "auto_pip": 1,
            "badge": 0,
            "byline": 0,
            "collections": 0,
            "color": 0,
            "force_color_one": 1,
            "force_color_two": 1,
            "force_color_three": 1,
            "force_color_four": 1,
            "embed": 0,
            "fullscreen": 1,
            "like": 0,
            "logo": 1,
            "playbar": 1,
            "portrait": 0,
            "pip": 1,
            "share": 0,
            "spatial_compass": 0,
            "spatial_label": 0,
            "speed": 1,
            "title": 0,
            "volume": 1,
            "watch_later": 0,
            "watch_full_video": 1,
            "controls": 1,
            "instant_sidedock": 1,
            "airplay": 1,
            "audio_tracks": 1,
            "chapters": 1,
            "chromecast": 1,
            "cc": 1,
            "transcript": 0,
            "quality": 1,
            "play_button_position": 0,
            "ask_ai": 0,
            "skipping_forward": 1,
            "debug_payload_collection_policy": "default"
        },
        "create_interactive": {
            "has_create_interactive": False,
            "viddata_url": ""
        },
        "persistent_logo": 0,
        "min_quality": '',
        "max_quality": '',
        "initial_quality": ''
    }
}