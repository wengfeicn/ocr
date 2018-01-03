def run(img):
    import model
    from glob import glob
    import numpy as np
    from PIL import Image
    import time
    im = Image.open(img)
    img = np.array(im.convert('RGB'))
    t = time.time()
    result,img = model.model(img,model='crnn')
    Image.fromarray(img).save('tmp.jpg')
    #for key in result:
    #    print result[key][1]
    print result
    return result
