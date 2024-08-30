low = [
    {
        "host": "www.youtube.com",
        "answers": [{"type": "CNAME", "answer": "restrict.youtube.com"}],
    },
    {
        "host": "youtube.com",
        "answers": [{"type": "CNAME", "answer": "restrict.youtube.com"}],
    },
    {
        "host": "m.youtube.com",
        "answers": [{"type": "CNAME", "answer": "restrict.youtube.com"}],
    },
    {
        "host": "youtubei.googleapis.com",
        "answers": [{"type": "CNAME", "answer": "restrict.youtube.com"}],
    },
    {
        "host": "youtube.googleapis.com",
        "answers": [{"type": "CNAME", "answer": "restrict.youtube.com"}],
    },
    {
        "host": "www.youtube-nocookie.com",
        "answers": [{"type": "CNAME", "answer": "restrict.youtube.com"}],
    },
    {
        # bing
        "host": "bing.com",
        "answers": [{"type": "CNAME", "answer": "strict.bing.com"}],
    },
    {
        "host": "www.bing.com",
        "answers": [{"type": "CNAME", "answer": "strict.bing.com"}],
    },
    {
        "host": "forcesafesearch.google.com",
        "answers": [
            {
                "type": "A",
                "answer": "216.239.38.120",
            },
            {
                "type": "AAAA",
                "answer": "2a00:1450:4006:811::2004",
            },
        ],
    },
    {
        "host": "restrict.youtube.com",
        "answers": [
            {
                "type": "A",
                "answer": "216.239.38.120",
            },
            {
                "type": "AAAA",
                "answer": "2a00:1450:4006:811::2004",
            },
        ],
    },
    {
        # duckduckgo
        "host": "duckduckgo.com",
        "answers": [{"type": "CNAME", "answer": "safe.duckduckgo.com"}],
    },
]


high = []
