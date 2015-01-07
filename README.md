fix_id3_kr_encoding
===================

updates ID3 tags that includes EUC-KR or CP949 encoded tags to UTF-8 encoding.

needs mutagen library.
$ sudo easy_install mutagen

$ cd directory_with_mp3_files
$ python fix_kr_id3.py



EUC-KR / CP949 인코딩된 ID3 태그를 UTF-8 인코딩으로 업데이트 해줍니다.
 
mutagen 라이브러리를 먼저 설치해야합니다.
$ sudo easy_install mutagen
 
원하시는 디렉토리에서 실행하면 현재 디렉토리에 있는 mp3 파일을 업데이트합니다.
$ cd directory_with_mp3_files
$ python fix_kr_id3.py

