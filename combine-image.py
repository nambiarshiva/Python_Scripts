import os
for i in range(1,5):
    s = 'convert ./%d_comb.png ./%d.png -fx "((255*u)|(255*v))/255" ./%d_comb.png' % (i, i+1, i+1);
    os.system(s)
