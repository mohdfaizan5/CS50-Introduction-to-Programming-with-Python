from project import validate, available_reso

def test_validate():
    assert validate("http://www.youtube.com/shorts/ufNgIeS3rg8") == "http://www.youtube.com/shorts/ufNgIeS3rg8"
    assert validate("https://www.youtube.com/shorts/ufNgIeS3rg8") == "https://www.youtube.com/shorts/ufNgIeS3rg8"
    assert validate("www.youtube.com/shorts/ufNgIeS3rg8") == "www.youtube.com/shorts/ufNgIeS3rg8"
    assert validate("youtube.com/shorts/ufNgIeS3rg8") == "youtube.com/shorts/ufNgIeS3rg8"

def test_function_2():
    assert ("http://www.youtube.com/shorts/ufNgIeS3rg8")


def test_available_reso():
    assert available_reso('<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="8fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">') == ['17', '18', '22']