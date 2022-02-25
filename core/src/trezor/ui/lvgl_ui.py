import lvgl as lv
from trezor import log

font_siyuan32 = lv.font_load("A:/lvgl_res/ui_font_siyuan32.bin")

class Screen(lv.obj):
    # def __new__(cls, pre_scr=None):
    #     if not hasattr(cls, '_instance'):
    #         log.debug(__name__, "++++++ create screen 0+++++++ ")  
    #         cls._instance = super().__new__(cls)
    #         log.debug(__name__, "++++++ create screen 1+++++++ ")  
    #     return cls._instance

    def __init__(self):
        log.debug(__name__, "++++++ create screen+++++++ ")
        self.root_screen = lv.obj()
        pass

    def __del__(self):
        log.debug(__name__, "++++++ del screen+++++++ ")
        pass

class UiHomescreen(Screen):
    _init = False

    def __init__(self, state: str):
        log.debug(__name__, "++++++ ui home init 0 +++++++ ")
        if self._init:
            return
        else:
            self._init = True
            log.debug(__name__, "++++++ ui home init 1 +++++++ ")
            super().__init__()
            dispp = lv.disp_get_default()
            theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_default())
            dispp.set_theme(theme) 

            ui_home = self.root_screen 
            ui_Image1 = lv.img(ui_home)
            # ui_Image1.set_src(ui_images.ui_img_logo_png)
            ui_Image1.set_src("A:/lvgl_res/logo.png")

            ui_Image1.set_x(0)
            ui_Image1.set_y(0)

            ui_Image1.set_align( lv.ALIGN.CENTER)

            ui_Label1 = lv.label(ui_home)

            ui_Label1.set_long_mode(lv.label.LONG.WRAP)
            ui_Label1.set_text(state)

            ui_Label1.set_width(lv.SIZE.CONTENT)	# 1
            ui_Label1.set_height(lv.SIZE.CONTENT)   # 1

            ui_Label1.set_x(lv.pct(0))
            ui_Label1.set_y(lv.pct(10))

            ui_Label1.set_align( lv.ALIGN.CENTER)

            ui_Label1.set_style_text_font( font_siyuan32, lv.PART.MAIN | lv.STATE.DEFAULT )

            lv.scr_load(ui_home)  


class UiResetDevice(Screen):
    
    def __init__(self, title: str, prompt: str):
        super().__init__()
        self.cancel = False
        self.confirm = False
        self.ui_resetdevice = self.root_screen 

        ui_Label1 = lv.label(self.ui_resetdevice)

        ui_Label1.set_long_mode(lv.label.LONG.WRAP)
        ui_Label1.set_text(title)

        ui_Label1.set_width(lv.SIZE.CONTENT)	# 1
        ui_Label1.set_height(lv.SIZE.CONTENT)   # 1

        ui_Label1.set_x(lv.pct(0))
        ui_Label1.set_y(lv.pct(-30))

        ui_Label1.set_align( lv.ALIGN.CENTER)

        ui_Label1.set_style_text_font( font_siyuan32, lv.PART.MAIN | lv.STATE.DEFAULT )

        ui_Label3 = lv.label(self.ui_resetdevice)

        ui_Label3.set_long_mode(lv.label.LONG.WRAP)
        ui_Label3.set_text(prompt)

        ui_Label3.set_width(lv.pct(80))	# 1
        ui_Label3.set_height(lv.SIZE.CONTENT)   # 1

        ui_Label3.set_x(0)
        ui_Label3.set_y(-180)

        ui_Label3.set_align( lv.ALIGN.CENTER)

        ui_Label3.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)
        ui_Label3.set_scroll_dir(lv.DIR.ALL)         

        ui_BTN_Cancel = lv.btn(self.ui_resetdevice)

        ui_BTN_Cancel.set_width(50)
        ui_BTN_Cancel.set_height(50)

        ui_BTN_Cancel.set_x(0)
        ui_BTN_Cancel.set_y(32)

        ui_BTN_Cancel.set_align( lv.ALIGN.TOP_LEFT)
        ui_BTN_Cancel.add_event_cb(self.ui_BTN_Cancel_eventhandler, lv.EVENT.ALL, None)

        ui_BTN_Cancel.set_style_bg_color( lv.color_hex(0x101418), lv.PART.MAIN | lv.STATE.DEFAULT )
        ui_BTN_Cancel.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

        ui_Image1 = lv.img(ui_BTN_Cancel)
        ui_Image1.set_src("A:/lvgl_res/nav-arrow-left.png")

        ui_Image1.set_width(lv.SIZE.CONTENT)	# 48
        ui_Image1.set_height(lv.SIZE.CONTENT)   # 48

        ui_Image1.set_x(0)
        ui_Image1.set_y(0)

        ui_Image1.set_align( lv.ALIGN.CENTER)

        ui_BTNConfirm = lv.btn(self.ui_resetdevice)

        ui_BTNConfirm.set_width(lv.pct(50))
        ui_BTNConfirm.set_height(lv.SIZE.CONTENT)   # 50

        ui_BTNConfirm.set_x(0)
        ui_BTNConfirm.set_y(242)

        ui_BTNConfirm.set_align( lv.ALIGN.CENTER)

        ui_BTNConfirm.add_event_cb(self.ui_BTNConfirm_eventhandler, lv.EVENT.ALL, None)

        ui_BTNConfirm.set_style_radius( 50, lv.PART.MAIN | lv.STATE.DEFAULT )
        ui_BTNConfirm.set_style_bg_color( lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT )
        ui_BTNConfirm.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

        ui_Label5 = lv.label(ui_BTNConfirm)

        ui_Label5.set_long_mode(lv.label.LONG.WRAP)
        ui_Label5.set_text("Create")

        ui_Label5.set_width(lv.SIZE.CONTENT)	# 1
        ui_Label5.set_height(lv.SIZE.CONTENT)   # 1

        ui_Label5.set_x(0)
        ui_Label5.set_y(0)

        ui_Label5.set_align( lv.ALIGN.CENTER)

        ui_Label5.set_style_text_color( lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT )
        ui_Label5.set_style_text_font( font_siyuan32, lv.PART.MAIN | lv.STATE.DEFAULT )

        lv.scr_load(self.ui_resetdevice)

    def ui_BTN_Cancel_eventhandler(self,evt):
        event = evt.code
        if event == lv.EVENT.CLICKED:
            self.cancel = True
    
    def ui_BTNConfirm_eventhandler(self,evt):
        event = evt.code
        if event == lv.EVENT.CLICKED:
            self.confirm = True


class UiBackUp(Screen):
    
    def __init__(self, title: str, prompt: str):
        super().__init__()
        self.cancel = False
        self.confirm = False
        self.ui_backup = self.root_screen 

        ui_Label1 = lv.label(self.ui_backup)

        ui_Label1.set_long_mode(lv.label.LONG.WRAP)
        ui_Label1.set_text(title)

        ui_Label1.set_width(lv.SIZE.CONTENT)	# 1
        ui_Label1.set_height(lv.SIZE.CONTENT)   # 1

        ui_Label1.set_x(lv.pct(0))
        ui_Label1.set_y(lv.pct(-30))

        ui_Label1.set_align( lv.ALIGN.CENTER)

        ui_Label1.set_style_text_font( font_siyuan32, lv.PART.MAIN | lv.STATE.DEFAULT )

        ui_Label3 = lv.label(self.ui_backup)

        ui_Label3.set_long_mode(lv.label.LONG.WRAP)
        ui_Label3.set_text(prompt)

        ui_Label3.set_width(lv.pct(80))	# 1
        ui_Label3.set_height(lv.SIZE.CONTENT)   # 1

        ui_Label3.set_x(0)
        ui_Label3.set_y(-180)

        ui_Label3.set_align( lv.ALIGN.CENTER)

        ui_Label3.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)
        ui_Label3.set_scroll_dir(lv.DIR.ALL)        

        ui_BTN_Cancel = lv.btn(self.ui_backup)

        ui_BTN_Cancel.set_width(50)
        ui_BTN_Cancel.set_height(50)

        ui_BTN_Cancel.set_x(0)
        ui_BTN_Cancel.set_y(32)

        ui_BTN_Cancel.set_align( lv.ALIGN.TOP_LEFT)
        ui_BTN_Cancel.add_event_cb(self.ui_BTN_Cancel_eventhandler, lv.EVENT.ALL, None)

        ui_BTN_Cancel.set_style_bg_color( lv.color_hex(0x101418), lv.PART.MAIN | lv.STATE.DEFAULT )
        ui_BTN_Cancel.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

        ui_Image1 = lv.img(ui_BTN_Cancel)
        ui_Image1.set_src("A:/lvgl_res/nav-arrow-left.png")

        ui_Image1.set_width(lv.SIZE.CONTENT)	# 48
        ui_Image1.set_height(lv.SIZE.CONTENT)   # 48

        ui_Image1.set_x(0)
        ui_Image1.set_y(0)

        ui_Image1.set_align( lv.ALIGN.CENTER)

        ui_BTNConfirm = lv.btn(self.ui_backup)

        ui_BTNConfirm.set_width(lv.pct(50))
        ui_BTNConfirm.set_height(lv.SIZE.CONTENT)   # 50

        ui_BTNConfirm.set_x(0)
        ui_BTNConfirm.set_y(242)

        ui_BTNConfirm.set_align( lv.ALIGN.CENTER)

        ui_BTNConfirm.add_event_cb(self.ui_BTNConfirm_eventhandler, lv.EVENT.ALL, None)

        ui_BTNConfirm.set_style_radius( 50, lv.PART.MAIN | lv.STATE.DEFAULT )
        ui_BTNConfirm.set_style_bg_color( lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT )
        ui_BTNConfirm.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

        ui_Label5 = lv.label(ui_BTNConfirm)

        ui_Label5.set_long_mode(lv.label.LONG.WRAP)
        ui_Label5.set_text("Back Up")

        ui_Label5.set_width(lv.SIZE.CONTENT)	# 1
        ui_Label5.set_height(lv.SIZE.CONTENT)   # 1

        ui_Label5.set_x(0)
        ui_Label5.set_y(0)

        ui_Label5.set_align( lv.ALIGN.CENTER)

        ui_Label5.set_style_text_color( lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT )
        ui_Label5.set_style_text_font( font_siyuan32, lv.PART.MAIN | lv.STATE.DEFAULT )

        lv.scr_load(self.ui_backup) 

    def ui_BTN_Cancel_eventhandler(self,evt):
        event = evt.code
        if event == lv.EVENT.CLICKED:
            self.cancel = True
    
    def ui_BTNConfirm_eventhandler(self,evt):
        event = evt.code
        if event == lv.EVENT.CLICKED:
            self.confirm = True