# 把原文件中的问题解决

f = open('input/mnemo_raw.txt', encoding = 'utf-8', mode = 'r')
l1 = f.readlines()
f.close()

l1 = l1[:946] + [l1[946].strip('\n') + ' ' + l1[948],] + l1[949:]
l1 = l1[:1016] + [l1[1016].strip('\n') + ' ' + l1[1018],] + l1[1019:]
l1 = l1[:1248] + [l1[1248].strip('\n') + ' ' + l1[1250],] + l1[1251:]


l1[2176] = '**7.vad, vag, ced**\n'
l1[3056] = '**3.verg, volv, shift**\n'
l1[3234] = '【小结】' + l1[3234][2:]
l1 = l1[:3256] + ['**4.scru**\n', '\n'] + l1[3256:]
l1 = l1[:3394] + l1[3412:]
l1[3720] = '【根】头\[cip\]在前面\[pre-\],（1）一个人匆忙地向前跑的状态（2）头在\[身体\]前面，就容易“fall down\[落下\]”→a.匆忙的；非常陡峭的\n'
l1[3724] = '【根】头\[cip\]在前面\[pre-\], 头在\[身体\]前面，就容易“fall down\[落下\]”→n.悬崖峭壁\n'

l1[4260] = '【小结】' + l1[4260][2:]
l1[4940] = '**2.brav**\n'
l1[5248] = '**3.tum**\n'
l1[5278] = '【小结】' + l1[5278][2:]
l1[5448] = '**2.jo**\n'
l1[5454] = '【参】' + l1[5454]
l1[5458] = '【参】' + l1[5458]
l1[5462] = '【参】' + l1[5462]
l1[5466] = '【参】' + l1[5466]
l1 = l1[:5468] + l1[5470:]
l1 = l1[:5478] + [l1[5478].strip('\n') + ' ' + l1[5480],] + l1[5481:]
l1 = l1[:5748] + [l1[5748].strip('\n') + ' ' + l1[5758],] + l1[5749:5758] + l1[5760:]
l1 = l1[:6680] + [l1[6680].strip('\n') + ' ' + l1[6682],] + l1[6683:]

l1 = l1[:9318]

# 拆分词根

def div2(start, end, r1, r2, l1):
    l1[start] = '**' + r1 + '**\n'
    l1[start+2] = l1[start+2][3:]
    l1[start+4] = l1[start+4][3:]
    l1 = l1[:start+4] + l1[start+6:end] + \
         ['**' + r2 + '**\n', '\n'] + l1[start+4:start+6] + l1[end:]
    return l1

l1 = div2(1128, 1144, '2.vow', '8.claim', l1)
l1 = div2(1176, 1196, '3.mand', '7.ord', l1)
l1 = div2(2048, 2066, '3.amb', '8.err', l1)
l1 = div2(4284, 4302, '3.brev', '4.long', l1)

def div3(start, mid, end, r1, r2, r3, l1):
    l1[start] = '**' + r1 + '**\n'
    l1[start+2] = l1[start+2][3:]
    l1[start+4] = l1[start+4][3:]
    l1[start+6] = l1[start+6][3:]
    l1 = l1[:start+4] + l1[start+8:mid] + \
         ['**' + r2 + '**\n', '\n'] + l1[start+4:start+6] + l1[mid:end] + \
         ['**' + r3 + '**\n', '\n'] + l1[start+6:start+8] + l1[end:]
    return l1

l1[3362] = '**2.duc \(t)**\n'
l1[3392] = '**3.fac \(t), fect, feit**\n'
l1[3318] = '**1.ag, act**\n'

l1 = l1[:1092] + l1[1094:]
l1 = div3(1084, 1104, 1114, '1.son', '1.ton', '1.phon', l1)
l1 = div3(3064, 3080, 3092, '3.verg', '3.volv', '3.shift', l1)
l1 = div3(2526, 2542, 2552, '1.cis', '1.tom', '1.sect', l1)
l1 = l1[:5766] + ['（1）词根surg表示rise\[升起\], surge\[n.＆v.汹涌\]指“升起的波涛”，可以与surf\[冲浪\]一起进行联想（冲浪时伴随着升起的波涛）。 \n',
                  '\n',
                  '（2）词根cit表示“（向上）引, 唤起\[arouse\]”, cite\[引用\]就来自该词根。excite\[v.激起，使兴奋\]指“引\[cit\]出\[ex-\]（一个人的兴致）”。\n'
                  ] + l1[5767:]
l1 = div2(5764, 5778, '5.surg', '5.cit', l1)
l1 = div3(2184, 2202, 2210, '7.vad, vas', '7.vag', '7.ced, cess', l1)
l1[5472] = '很多由“jo”开始的词根与“快乐\[joy\]（地开玩笑\[joke\]）”有关。\n'
l1[3278] = '可以将scru按照读音联想成“四顾”，表示“（顾虑地）看”。\n'
l1 = div2(4236, 4266, '1.lev', '1.loft', l1)
l1 = div2(1918, 1928, '4.post', '4.pond', l1)
l1 = l1[:1614] + [l1[1614].strip('\n') + l1[1616][3:]] + l1[1617:]
l1 = div2(1612, 1664, '2.tend, tens, tent', '2.tenu', l1)
f = open('input/mnemo.txt', encoding = 'utf-8', mode = 'w')
f.write(''.join(l1))
f.close()
