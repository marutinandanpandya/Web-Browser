#!/usr/bin/env python

import pygtk, webkit
import os, sys, gtk
import ctypes, gobject

UI_FILE = "1.glade"
##libgobject = ctypes.CDLL('/usr/lib/i386-linux-gnu/libgobject-2.0.so.0')
##libwebkit = ctypes.CDLL('/usr/lib/libsoup-2.4.so.1')
##libsoup = ctypes.CDLL('/usr/lib/libsoup-2.4.so.1')
##libwebkit = ctypes.CDLL('/usr/lib/libwebkitgtk-1.0.so.0')
##session = libwebkit.webkit_get_default_session()

##cookiejar = libsoup.soup_cookie_jar_text_new('/path/to/your/cookies.txt',False)
##libsoup.soup_session_add_feature(session, cookiejar)

class Browser:
	def __init__(self):
		self.builder = gtk.Builder()
        	self.builder.add_from_file(UI_FILE)
	        self.builder.connect_signals(self)
	
        	self.back = self.builder.get_object("back")
        	self.back.connect("clicked", self.go_back)
        	self.forward = self.builder.get_object("next")
        	self.forward.connect("clicked", self.go_forward)
        	self.url = self.builder.get_object("url")
        	self.surl = self.builder.get_object("surl")
     	
        	self.webview = webkit.WebView()
        	self.browser_settings = self.webview.get_settings()
        	print "Previous enable-plugins:", self.browser_settings.get_property('enable-plugins')
        	self.browser_settings.set_property('user-agent', 'Mozilla/15.0 AppleWebKit')
##        	self.browser_settings.set_property("enable-smooth-scrolling", True)
        	self.browser_settings.set_property("enable-scripts", True)
        	self.browser_settings.set_property("enable-plugins", True)
        	self.browser_settings.set_property("enable-page-cache", True)
##self.browser_settings.set_property("enable-plugins", True)
##        	self.browser_settings.set_property("enable-javascript", True)
        	self.webview.set_settings(self.browser_settings)
##        	self.webview.get_settings().setPluginsEnabled(true);
        	scrolled_window = self.builder.get_object("scrolledwindow")
        	scrolled_window.add(self.webview)
        	self.webview.connect("load_committed", self.update_buttons)
        	self.__go("http://www.youtube.com/?gl=IN&tab=wy")

        	self.event = gtk.gdk.Event(gtk.gdk.KEY_PRESS)
        	self.event.keyval = gtk.keysyms.Return
        	##browser.emit('key-press-event', event)
        	##self.webview.connect("titulo-cambiado", self.on_title_changed)
        	##self.webview.connect("icono-cambiado", self.on_icon_loaded)
        	##self.webview.connect("carga-finalizada", self.on_load_finished)

        	self.window = self.builder.get_object("window")
        	self.window.connect('destroy', lambda w: gtk.main_quit())
        	self.window.show_all()

	def update_buttons(self, widget, data=None):
		'''Gets the current url entry and puts that into the url bar.
           It then checks to see if we can go back, if we can it makes the
           back button clickable.  Then it does the same for the foward
           button.'''
		self.url.set_text( widget.get_main_frame().get_uri() )
		self.back.set_sensitive(self.webview.can_go_back())
		self.forward.set_sensitive(self.webview.can_go_forward())
		

	def go_back(self, widget, data=None):
		'''Webkit will remember the links and this will allow us to go backwards.'''
		self.webview.go_back()
		
	def go_forward(self, widget, data=None):
		'''Webkit will remember the links and this will allow us to go forward.'''
		self.webview.go_forward()
		
	def go_refresh(self, widget, data=None):
		'''Webkit will remember the links and this will allow us to reload webview object'''
		self.webview.reload()


	def on_direccion_activate(self, widget):
		url = widget.get_text()
		if not "http://www." in url:
			url = "http://www." + url
		if not "http://" in url:
			url = "http://" + url
		self.url.set_text(url)
		self.__go(url)

	def on_go_clicked(self, widget):
		url = self.url.get_text()
		self.__go(url)

	def on_home_clicked(self, widget):
		self.url.set_text("http://www.facebook.com")
		self.__go("http://www.facebook.com")

	def on_sdireccion_activate(self, widget):
		surl = widget.get_text()
		surl = "https://www.google.co.in/search?ie=utf-8&oe=utf-8&q=" + surl
		self.url.set_text(surl)
		self.__go(surl)

	def destroy(self, window):
		gtk.main_quit()

	def about_browser(self, widget):
		about = gtk.AboutDialog()
		about.set_program_name("My First Python Web-Browser")
		about.set_version("0.1")
		about.run()
		about.destroy()

	def update_browser(self, widget):
		about = gtk.AboutDialog()
		about.set_program_name("Do you want to update Browser")
		about.set_version("0.16")
		about.run()
		about.destroy()

	def on_url_activate(self,*args):
		#catch url to open page
		url = "http://" + self.enlace.get_text()
		self.__go(url)


	def __go(self,url):
		self.webview.open(url)
        

def main():
    app = Browser()
    gtk.main()

if __name__ == "__main__":
    main()
