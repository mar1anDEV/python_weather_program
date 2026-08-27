from farbenConfig import f_farbe
def custom_display(text:str,f_text:str=None,s_text:str=None,showCustom:bool=False,units:int = 50,c_color = 'cyan'):
    if showCustom:
        print(f_farbe("="*units,c_color))
        print(f_farbe(f_text,c_color))
        print(f_farbe(s_text,c_color))
        print(f_farbe(text,'green'))
        print(f_farbe("="*units,c_color))
    else:
        print(f_farbe("="*units,c_color))
        print(f_farbe(text,'green'))
        print(f_farbe("="*units,c_color))




    