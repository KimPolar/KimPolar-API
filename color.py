def compcolor(RGB):
  R, G, B = RGB[0:2], RGB[2:4], RGB[4:6]
  R, G, B = int(R,16), int(G,16), int(B,16)
  R, G, B = 255-R, 255-G, 255-B
  R, G, B = str(hex(R)), str(hex(G)), str(hex(B))
  R, G, B = R.replace("0x",""), G.replace("0x",""), B.replace("0x","")
  return (R+G+B).upper()
