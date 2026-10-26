import cv2,numpy as np,vtracer,re
im=cv2.imread('reef-control-freak-coral-teardrop.jpg')
g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ys,xs=np.where(g<170); print(xs.min(),xs.max(),ys.min(),ys.max())
x0,x1,y0,y1=xs.min()-4,xs.max()+5,ys.min()-4,ys.max()+5
S=6
def trace(cx0,cx1,name):
    c=g[y0:y1,cx0:cx1]
    c=cv2.resize(c,None,fx=S,fy=S,interpolation=cv2.INTER_CUBIC)
    c=cv2.GaussianBlur(c,(5,5),0)
    m=np.where(c<165,0,255).astype(np.uint8)
    cv2.imwrite(f'/tmp/{name}.png',m)
    vtracer.convert_image_to_svg_py(f'/tmp/{name}.png',f'/tmp/{name}.svg',colormode='binary',mode='spline',filter_speckle=8,corner_threshold=60,length_threshold=4,splice_threshold=45,path_precision=2)
    s=open(f'/tmp/{name}.svg').read()
    paths=re.findall(r'<path[^>]*/>',s)
    return paths,(cx1-cx0)*S,(y1-y0)*S
# split drop vs wordmark at gap column
cols=(g[y0:y1]<170).sum(0); gap=[x for x in range(260,x1) if cols[x]==0 and x>200][:1]
gx=[x for x in range(200,300) if cols[x]==0]; split=gx[len(gx)//2]; print('split',split)
dp,dw,h=trace(x0,split,'drop'); wp,ww,_=trace(split,x1,'word')
def svg(paths,w,h,fill,extra=''):
    ps=''.join(re.sub(r'fill="[^"]*"','',p).replace('<path',f'<path fill="{fill}"') for p in paths)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{extra}{ps}</svg>'
def g_(paths,dx,fill): return f'<g transform="translate({dx} 0)">'+''.join(re.sub(r'fill="[^"]*"','',p).replace('<path',f'<path fill="{fill}"') for p in paths)+'</g>'
T='#13788D'
for suf,f in [('',T),('-white','#fff'),('-currentColor','currentColor')]:
    open(f'reef-mark-drop{suf}.svg','w').write(svg(dp,dw,h,f))
    W=dw+ww
    open(f'reef-mark-lockup{suf}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}">'+g_(dp,0,f)+g_(wp,dw,f)+'</svg>')
print(len(dp),len(wp))
