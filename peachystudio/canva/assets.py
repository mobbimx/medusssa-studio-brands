# -*- coding: utf-8 -*-
import os
D = "/tmp/claude-0/-home-user-medusssa-studio-brands/90a2d321-d4a3-5e05-b44d-ed19898dbd53/scratchpad/asrc/"
os.makedirs(D, exist_ok=True)
FILT = """<svg width="0" height="0" style="position:absolute"><defs>
<filter id="o" x="-20%" y="-20%" width="140%" height="140%">
<feTurbulence type="fractalNoise" baseFrequency="0.0045 0.0085" numOctaves="2" seed="9" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="78" xChannelSelector="R" yChannelSelector="G"/>
</filter></defs></svg>"""

def bg(name, css):
    open(D+name+".html","w").write(
      "<!doctype html><meta charset='utf-8'><style>*{margin:0;padding:0}html,body{width:1080px;height:1920px;overflow:hidden;position:relative}"
      ".b{position:absolute;left:-150px;top:-150px;width:1380px;height:2220px;%s}</style>%s<div class='b'></div>" % (css, FILT))

bg("bg-checker", "background:repeating-conic-gradient(#f7daff 0% 25%,#fff7fb 0% 50%) 0 0/168px 168px")
bg("bg-checker-wave", "background:repeating-conic-gradient(#f7daff 0% 25%,#fff7fb 0% 50%) 0 0/168px 168px;filter:url(#o)")
bg("bg-swirl-rosa", "background:repeating-conic-gradient(from 8deg at 50% 42%,#ffb7f0 0deg 11deg,#ffe6f8 11deg 22deg);filter:url(#o)")

def sticker(name, w, h, inner, extra=""):
    open(D+name+".html","w").write(
      "<!doctype html><meta charset='utf-8'><style>*{margin:0;padding:0}svg{display:block}html,body{width:%dpx;height:%dpx;background:transparent;overflow:hidden}%s</style>%s"
      % (w, h, extra, inner))

sticker("deco-smiley",240,240,
 '<svg width="240" height="240" viewBox="0 0 100 100"><circle cx="50" cy="50" r="47" fill="#fec900" stroke="#fff" stroke-width="5"/>'
 '<ellipse cx="35" cy="40" rx="6" ry="9" fill="#5e17eb"/><ellipse cx="65" cy="40" rx="6" ry="9" fill="#5e17eb"/>'
 '<path d="M30 60 Q50 80 70 60" stroke="#5e17eb" stroke-width="7" fill="none" stroke-linecap="round"/></svg>')
pets = "".join('<ellipse cx="50" cy="18" rx="12" ry="20" fill="#fff" stroke="#fe42a2" stroke-width="2.5" transform="rotate(%d 50 50)"/>' % a for a in range(0,360,45))
sticker("deco-daisy",260,260,'<svg width="260" height="260" viewBox="0 0 100 100">%s<circle cx="50" cy="50" r="15" fill="#fec900"/></svg>' % pets)
sticker("deco-heart",220,200,
 '<svg width="220" height="200" viewBox="0 0 100 90"><path d="M50 86 L12 48C-2 33 6 10 26 10c11 0 19 7 24 15 5-8 13-15 24-15 20 0 28 23 14 38z" fill="#fe42a2" stroke="#fff" stroke-width="4"/></svg>')
sticker("deco-spark",220,220,
 '<svg width="220" height="220" viewBox="0 0 100 100"><path d="M50 0c4 33 13 42 46 50-33 8-42 17-46 50-4-33-13-42-46-50 33-8 42-17 46-50z" fill="#fec900"/></svg>')

WMCSS = """@font-face{font-family:BF;src:url('file:///root/.fonts/hYkPPucsQOr5dy02WmQr5Zkd4Blsug.ttf')}
@font-face{font-family:YT;src:url('file:///root/.fonts/OZpGg_pnoDtINPfRIlLohlvHxA.ttf')}
.wm{font-family:BF;font-size:150px;line-height:.86;transform:rotate(-2deg);text-align:center;padding:26px 40px}
.wm i{font-style:normal;display:block}
.wm .p{color:#fe42a2;-webkit-text-stroke:.13em #fec900;paint-order:stroke fill;letter-spacing:-.02em}
.wm .s{color:#fff;-webkit-text-stroke:.13em #fec900;paint-order:stroke fill;margin-top:-.22em;letter-spacing:-.02em;text-shadow:0 .05em 0 #f7daff}
.wm .n{font-family:YT;color:#fe42a2;font-size:.36em;margin-top:-.30em;margin-left:2.4em;-webkit-text-stroke:0}"""
sticker("logo-wordmark",760,420,'<div class="wm"><i class="p">Peachy</i><i class="s">Studio</i><i class="n">nails</i></div>', WMCSS)
print("fuentes html listas")
