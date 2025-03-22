# pip install freetype-py
import freetype
face = freetype.Face("/usr/share/fonts/truetype/nanum/NanumGothic.ttf")
face.set_char_size( 48*64 )
face.load_char('S')
bitmap = face.glyph.bitmap
print(bitmap.buffer)