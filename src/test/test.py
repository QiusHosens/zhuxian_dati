# -*- coding: utf-8 -*-

source = '歌词来源专辑：华语乐队组合/TFBOYS/大梦想家(adsbygoogle=window.adsbygoogle||[]).push({});王俊凯	:,天窗外那树影被拉很长,透射出若隐若现的微光,伸出手嘴角上扬,我就能触及,心中的希望,易烊千玺	:,午后跑道旁弥漫青草香,延伸向名为未来的方向,放学后篮球场上,听信仰疯狂,在血液中流淌,王源:,就算退缩懦弱,也不会有被同情的目光,不如即刻整装,勇敢冲向梦想的彼方,合唱:,我微笑歌唱心底的愿望,很简单只要你坚强,我们挺起胸膛去乘风破浪,让世界东方迸射出光芒,我微笑歌唱心底的梦想,等待它华丽的绽放,记忆在远方不朽的荡漾,我们一起把迷茫的前方都照亮,王源:,看楼外那蒲公英在生长,跟微风轻轻在空中飘荡,易烊千玺	:,即使不能够远航,但也要飞往,最憧憬的地方,王俊凯	:,就算退缩懦弱,也不会有被同情的目光,合唱:,不如即刻整装,勇敢冲向梦想的彼方,合唱:,我微笑歌唱心底的愿望,很简单只要你坚强,我们挺起胸膛,去乘风破浪,让世界东方迸射出光芒,我微笑歌唱心底的梦想,等待它华丽的绽放,记忆在远方不朽的荡漾,我们一起把迷茫的前方都照亮,王俊凯	:我追寻最初的冲动,王源:踏坚定的征程,易烊千玺	:中国的梦,合唱:有最耀眼天空,王俊凯	:,我微笑歌唱心底的愿望,很简单只要你坚强,合唱:,我们挺起胸膛去乘风破浪,让世界东方迸射出光芒,合唱:,我微笑歌唱心底的梦想,等待它华丽的绽放,记忆在远方不朽的荡漾,我们一起把迷茫的前方都照亮'
poss = []
pos = 0
_pos = 0
while pos != -1:
    pos = source.find(',')
    if pos == -1:
        break
    source = source[pos + 1:]
    if len(poss) > 0:
        _pos = poss[len(poss) - 1] + pos + 1
    else:
        _pos = pos
    poss.append(_pos)
    print pos, source

print poss

source = '歌词来源专辑：华语乐队组合/TFBOYS/大梦想家(adsbygoogle=window.adsbygoogle||[]).push({});王俊凯	:,天窗外那树影被拉很长,透射出若隐若现的微光,伸出手嘴角上扬,我就能触及,心中的希望,易烊千玺	:,午后跑道旁弥漫青草香,延伸向名为未来的方向,放学后篮球场上,听信仰疯狂,在血液中流淌,王源:,就算退缩懦弱,也不会有被同情的目光,不如即刻整装,勇敢冲向梦想的彼方,合唱:,我微笑歌唱心底的愿望,很简单只要你坚强,我们挺起胸膛去乘风破浪,让世界东方迸射出光芒,我微笑歌唱心底的梦想,等待它华丽的绽放,记忆在远方不朽的荡漾,我们一起把迷茫的前方都照亮,王源:,看楼外那蒲公英在生长,跟微风轻轻在空中飘荡,易烊千玺	:,即使不能够远航,但也要飞往,最憧憬的地方,王俊凯	:,就算退缩懦弱,也不会有被同情的目光,合唱:,不如即刻整装,勇敢冲向梦想的彼方,合唱:,我微笑歌唱心底的愿望,很简单只要你坚强,我们挺起胸膛,去乘风破浪,让世界东方迸射出光芒,我微笑歌唱心底的梦想,等待它华丽的绽放,记忆在远方不朽的荡漾,我们一起把迷茫的前方都照亮,王俊凯	:我追寻最初的冲动,王源:踏坚定的征程,易烊千玺	:中国的梦,合唱:有最耀眼天空,王俊凯	:,我微笑歌唱心底的愿望,很简单只要你坚强,合唱:,我们挺起胸膛去乘风破浪,让世界东方迸射出光芒,合唱:,我微笑歌唱心底的梦想,等待它华丽的绽放,记忆在远方不朽的荡漾,我们一起把迷茫的前方都照亮'
print source
source = source.replace(',', '')
list = list(source)
for pos in poss:
    list.insert(pos, ',')
print ''.join(list)