import pyautogui as Py, time, cv2, easyocr, numpy as np
if __name__ == '__main__':
    def ActivateBypassBotForSamsung(appX,appY,dashX,dashY,adX,adY,butX,butY,subbutX,subbutY): 
        while True:
                
            if (Py.pixel(appX,appY)[2] == 2):#check app color and open app
                Py.click(1010,630)
                
            if (Py.pixel(dashX,dashY)[1] == 255) and (Py.pixel(954,244)[1] == 52):#check dashboard and click drawer icon
                Py.click(1160,120)
                time.sleep(1)
                Py.click(900,760)
                
            if (Py.pixel(adX,adY)[1] == 21):#check on advertisement and click on it
                time.sleep(1)
                Py.click(900,760)
                
            if (Py.pixel(butX,butY)[1] == 61):#check button appearace and enter captcha code for large banner ads,loop
                image = Py.screenshot(region = (830,612,260,48))
                image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                cv2.imwrite("screenshot.png", image)
                Py.click(970,640)#click on captcha entering box
                reader = easyocr.Reader(['en'],gpu = False)
                result = reader.readtext('screenshot.png',detail = 0)
                Py.write(result)
                time.sleep(1)
                Py.click(subbutX,subbutY)#click on submit button
                time.sleep(3)
                
ActivateBypassBotForSamsung(appX=1050,dashX=1050,adX=1040,butX=960,subbutX=950,appY=910,dashY=100,adY=128,butY=810,subbutY=730)