#coding: utf8
#!/usr/bin/env python3

## Crash GUI Server Generator ###
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import pickle
import os
from datetime import date

class ServerConf:
	
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	
	def __init__(self):
		self.crash_gui_dir = os.path.dirname(os.path.realpath(__file__))
		self.window = Tk()
		self.window.title("Crash Server Configurator")
		self.window.geometry("1080x720")
		self.window.minsize(800,900)
		#self.window.iconbitmap("logo.ico")
		self.window.config(background="#e6e7d0")
		self.code_dict = {}
		self.attack_data = {}

		#Initialisationd des composants
		self.title_frame = Frame(self.window, bg='#e6e7d0', pady=3, height=50, relief=RAISED, borderwidth=3)
		self.frame = Frame(self.window, bg='#e6e7d0')
		self.attack_frame = Frame(self.window)
		self.attack =  Frame(self.attack_frame)
		self.part = Frame(self.attack_frame)
		self.button_frame = Frame(self.window, bg='#e6e7d0', height=50, relief=RAISED, borderwidth=3)

		#Lecture des données du server actif
		if os.path.isfile('server_data.cs'):
			self.read_data("server_data.cs")

		#Creation des composants
		self.create_widgets()

		#empaquetage
		self.title_frame.pack(fill=X, expand=True)
		self.frame.pack(fill=X, expand=True)
		self.attack_frame.pack(fill=X, expand=True)
		self.part.pack(side= LEFT, fill=X, expand=True)
		self.attack.pack(side=LEFT, fill=X, expand=True)
		self.button_frame.pack(fill=Y, expand=True)

		#lecture des données du server
		self.load_server_data()

	def create_widgets(self):
		self.create_title()

		### SERVER CONFIG
		self.create_lieu()
		self.create_tmps()
		self.create_lang()
		self.create_scale_root()
		self.create_video()
		self.create_separator(self.frame)
		
		### ATTACK CONFIG
		self.create_nom()
		self.create_ascii()
		self.create_dialogue()
		self.create_code()
		self.create_part()
		#self.create_separator(self.attack)

		### BUTTONS
		self.create_save_button()
		self.create_open_button()	
		self.create_quit_button()
		self.create_update_button()
		self.create_delete_button()
		self.create_new_button()
		self.create_add_button()
		

	def create_title(self):
		label_title = Label(self.title_frame, text="Configuration du Server", font=("Courrier", 40), bg="#41b770", fg='white')
		label_title.pack(fill=X)
		
	def create_separator(self, sep_frame):
		separator = ttk.Separator(sep_frame, orient="horizontal")
		separator.pack(fill=X, padx=2, pady=2)

	### SERVER CONFIG

	def create_lieu(self):
		### Definit le lieu
		frame_lieu = Frame(self.frame)
		frame_lieu.pack(fill=X)

		label_lieu = Label(frame_lieu, text="Lieu du server : ", width=20)
		label_lieu.pack(side=LEFT, padx=5, pady=5)
		var_lieu = StringVar()
		self.lieu = Entry(frame_lieu, textvariable = var_lieu)
		self.lieu.pack(side=LEFT, padx=5, expand=True)

		# Server actif 
		label_active = Label(frame_lieu, text="Active Server : ", width=20)
		label_active.pack(side=LEFT, padx=5, pady=5)
		self.var_active = IntVar()
		self.active = Checkbutton(frame_lieu, variable=self.var_active)
		self.active.pack(side=LEFT, padx=5, expand=True)

	def create_tmps(self):
		frame_tmps = Frame(self.frame)
		frame_tmps.pack(fill=X)

		### Definit le temps d'intro
		label_tmps = Label(frame_tmps, text="Temps d'intro (beat) : ", width=20)
		label_tmps.pack(side=LEFT, padx=5, pady=5)
		var_tmps = IntVar()
		self.tmps = Entry(frame_tmps, textvariable=var_tmps)
		self.tmps.pack(side=LEFT, padx=5, expand=True)

		### Definit le tempo d'intro
		label_bpm = Label(frame_tmps, text="Bpm d'intro : " ,width=20)
		label_bpm.pack(side=LEFT, padx=5, pady=5)
		var_bpm = IntVar()
		self.bpm = Entry(frame_tmps, textvariable=var_bpm)
		self.bpm.pack(side=LEFT, padx=5, expand=True)

	def create_lang(self):
		### Definit la langue 
		frame_lang = Frame(self.frame)
		frame_lang.pack(fill=X)
		label_lang = Label(frame_lang, text="Langue du server : ", width=20)
		label_lang.pack(side=LEFT, padx=5, pady=5)
		var_lang = ["french", "english"]
		self.lang = ttk.Combobox(frame_lang, values=var_lang)
		self.lang.pack(side=LEFT, padx=5, expand=True)

		### Definit le type de voix
		label_voice = Label(frame_lang, text="Type de voix : ", width=20)
		label_voice.pack(side=LEFT, padx=5, pady=5)
		var_voice = IntVar()
		self.voice = Entry(frame_lang, textvariable=var_voice)
		self.voice.pack(side=LEFT, padx=5, expand=True)

	def create_scale_root(self):
		frame_scale = Frame(self.frame)
		frame_scale.pack(fill=X)

		### Definit le Scale d'intro
		label_scale = Label(frame_scale, text="Scale d'intro : ", width=20)
		label_scale.pack(side=LEFT, padx=5, pady=5)
		var_scale = ['aeolian', 'altered', 'bebopDom', 'bebopDorian', 'bebopMaj', 'bebopMelMin', 'blues', 'chinese', 'chromatic', 'custom', 'default', 'diminished', 'dorian', 'dorian2', 'egyptian', 'freq', 'halfDim', 'halfWhole', 'harmonicMajor', 'harmonicMinor', 'hungarianMinor', 'indian', 'justMajor', 'justMinor', 'locrian', 'locrianMajor', 'lydian', 'lydianAug', 'lydianDom', 'lydianMinor', 'major', 'majorPentatonic', 'melMin5th', 'melodicMajor', 'melodicMinor', 'minMaj', 'minor', 'minorPentatonic', 'mixolydian', 'phrygian', 'prometheus', 'romanianMinor', 'susb9', 'wholeHalf', 'wholeTone', 'yu', 'zhi']
		self.scale = ttk.Combobox(frame_scale, values=var_scale)
		self.scale.pack(side=LEFT, padx=5, expand=True)

		### Definit le Root d'intro
		label_root = Label(frame_scale, text="Root d'intro : " ,width=20)
		label_root.pack(side=LEFT, padx=5, pady=5)
		var_root = ["C", "D", "E", "F", "G", "A", "B"]
		self.root = ttk.Combobox(frame_scale, values=var_root)
		self.root.pack(side=LEFT, padx=5, expand=True)

	def create_video(self):
		frame_video = Frame(self.frame)
		frame_video.pack(fill=X)

		### Activation de la video
		label_video = Label(frame_video, text="Vidéo OSC : ", width=20)
		label_video.pack(side=LEFT, padx=5, pady=5)
		self.var_video = IntVar()
		self.video = Checkbutton(frame_video, variable=self.var_video, command=self.check_video)
		self.video.pack(side=LEFT, padx=5, expand=True)

		### adresse du server video
		label_ip = Label(frame_video, text="IP du server vidéo : " ,width=20)
		label_ip.pack(side=LEFT, padx=5, pady=5)
		var_ip = StringVar()
		self.ip = Entry(frame_video, textvariable=var_ip)
		self.ip.insert(0, "0.0.0.0")
		self.ip.pack(side=LEFT, padx=5, expand=True)

	def check_video(self):
		if self.var_video.get()==0:
			self.ip.config(state=DISABLED)
		else:
			self.ip.config(state=NORMAL)

	### ATTACK CONFIG
	def create_part(self):
		frame_part = Frame(self.part)
		frame_part.pack(side=TOP, fill=X)

		label_part = Label(frame_part, text="Parties principales/secondaires :")
		label_part.pack(side=TOP, padx=5, pady=5)
		self.part_list = Listbox(frame_part, relief=SUNKEN, selectmode=SINGLE)
		self.part_list.config(height = 10)
		self.part_list.pack(side=LEFT, fill=Y, padx=5)

		self.sec_part_list = Listbox(frame_part, relief=SUNKEN, selectmode=SINGLE)
		self.sec_part_list.config(height=20)
		self.sec_part_list.pack(side=LEFT, fill=Y, padx=5)
		self.part_get()
		self.part_list.bind("<<ListboxSelect>>", self.change_part)
		self.sec_part_list.bind("<<ListboxSelect>>", self.change_part)
		self.part_list.select_set(0, None)
		self.reset_data()
		self.load_attack_data(self.part_list.get(0))
		self.button_part = Frame(self.part)
		self.button_part.pack(side=BOTTOM)


	def change_part(self, val):
		#print("avant: ", self.main_part.get(), val)
		if val:
			part_name = self.get_name_from_list(val)
			print(part_name, self.main_part.get())
			if part_name:
				self.get_attack_data()
				self.reset_data()
				self.load_attack_data(part_name)
			#print("après: ", self.main_part.get())

	def create_nom(self):
		# Nom du server
		frame_nom = Frame(self.attack)
		frame_nom.pack(fill=X)

		label_nom = Label(frame_nom, text="NOM : ", width=20)
		label_nom.pack(side=LEFT, padx=5, pady=5)
		var_nom = StringVar()
		self.nom = Entry(frame_nom, textvariable = var_nom)
		self.nom.pack(side=LEFT, fill=X, padx=5, expand=True)
		
		# Main part
		label_main_part = Label(frame_nom, text="Main Part: ", width=12)
		label_main_part.pack(side=LEFT, padx=5, pady=5)
		var_main_part = IntVar()
		self.main_part = Entry(frame_nom, textvariable = var_main_part, width=2)
		self.main_part.pack(side=LEFT, fill=X, padx=5, expand=False)
		
		# Secondary weapons
		label_sec_part = Label(frame_nom, text="Secondary Weapons: ", width=20)
		label_sec_part.pack(side=LEFT, padx=5, pady=5)
		self.var_sec_part = IntVar()
		self.sec_part = Checkbutton(frame_nom, variable = self.var_sec_part, command=self.check_main_part)
		self.sec_part.pack(side=LEFT, fill=X, padx=5, expand=False)
		
	def check_main_part(self):
		# Switch between main and secondary part
		if self.var_sec_part.get() == 1:
			self.main_part.delete(0, len(self.main_part.get()))
			self.main_part.insert(0, 0)
			self.main_part.config(state=DISABLED)
		else:
			self.main_part.config(state=NORMAL)	

	def create_ascii(self):
		frame_ascii = Frame(self.attack)
		frame_ascii.pack(fill=X)

		label_ascii = Label(frame_ascii, text="ASCII : ", width=20)
		label_ascii.pack(side=LEFT, padx=5, pady=5)
		var_ascii = StringVar()
		self.ascii = Entry(frame_ascii, textvariable = var_ascii)
		self.ascii.pack(side=LEFT, fill=X, padx=5, expand=True)

	def create_dialogue(self):
		frame_dialogue = Frame(self.attack)
		frame_dialogue.pack(fill=X)

		label_dialogue = Label(frame_dialogue, text="DIALOGUE : ", width=20)
		label_dialogue.pack(side=LEFT, padx=5, pady=5)
		self.dialogue = Text(frame_dialogue)
		self.dialogue.config(height=5)
		self.dialogue.pack(side=LEFT, fill=X, padx=5, expand=True)

	def create_code(self):
		frame_code = Frame(self.attack)
		frame_code.pack(expand=True, fill=BOTH)

		label_code = Label(frame_code, text="CODE : ", width=20)
		label_code.pack(side=LEFT, padx=5, pady=5)
		self.code = Text(frame_code)
		self.code.pack(side=LEFT, fill=X, padx=5, expand=True)

	### BUTTONS

	def create_save_button(self):
		self.bouton_save = Button(self.button_frame, text="Generate Server", command=self.save_button)
		self.bouton_save.pack(side=LEFT, padx=15, pady=5)

	def init_save_button(self):
		self.bouton_save.config(text="Generate server")

	def create_open_button(self):
		self.buton_open = Button(self.button_frame, text="Load Server", command=self.open)
		self.buton_open.pack(side=LEFT, padx=15, pady=5)	

	def create_quit_button(self):
		bouton_quitter = Button(self.button_frame, text="Quitter", command=self.window.quit)
		bouton_quitter.pack(side=RIGHT, padx=15, pady=5)

	### PART BUTTONS
	def create_add_button(self):
		self.bouton_add = Button(self.button_part, text="Add", command=self.add_button)
		self.bouton_add.pack(side=LEFT, padx=15, pady=5)

	def create_delete_button(self):
		self.bouton_delete = Button(self.button_part, text="Delete", command=self.delete_button)
		self.bouton_delete.pack(side=LEFT, padx=15, pady=5)

	def create_update_button(self):
		self.bouton_update = Button(self.button_part, text="Update", command=self.update_button)
		self.bouton_update.pack(side=LEFT, padx=15, pady=5)

	def create_new_button(self):
		self.bouton_new = Button(self.button_part, text="New", command=self.new_button)
		self.bouton_new.pack(side=LEFT, padx=15, pady=5)


	### Functions
	def part_get(self):
		### load the parts in the listbox
		self.part_list.delete(0, 'end')
		self.sec_part_list.delete(0, 'end')
		i = 1
		for k in self.attack_data.keys():
			try:
				if int(self.attack_data[k][3]) > 0:
					self.part_list.insert(int(self.attack_data[k][3]), str(k))
				else: 
					self.sec_part_list.insert(i, str(k))
					i += 1
			except Exception as e:
				self.sec_part_list.insert(i, str(k))
				i += 1
 
	def save_button(self):
		self.get_server_data()
		self.get_attack_data()
		self.code_dict["server_data"] = self.server_data
		self.code_dict["attack_data"] = self.attack_data
		self.part_get()
		self.save()

	def delete_button(self):
		try:
			value = str(self.part_list.get(self.part_list.curselection())) 
		except:
			value = str(self.sec_part_list.get(self.sec_part_list.curselection()))   
		del self.attack_data[value]
		self.part_get()

	def add_button(self):
		self.get_attack_data()
		self.part_get()

	def update_button(self):
		self.part_get()		

	def new_button(self):
		self.reset_data()	

	def get_server_data(self):
		lieu = self.lieu.get()
		tmps = self.tmps.get()
		lang = self.lang.get()
		voice = self.voice.get()
		bpm_intro = self.bpm.get()
		scale_intro = self.scale.get()
		root_intro = self.root.get()
		video = self.var_video.get()
		ip = self.ip.get()

		self.server_data = {
			"lieu" : lieu,	
			"tmps" : tmps,
			"lang" : lang,
			"voice" : voice,
			"bpm_intro": bpm_intro,
			"scale_intro": scale_intro,
			"root_intro": root_intro,
			"video": video,
			"adresse": ip
			}

	def reset_data(self):
		self.nom.delete(0, len(self.nom.get()))
		self.main_part.delete(0, len(self.main_part.get()))
		self.sec_part.deselect()
		self.ascii.delete(0, len(self.ascii.get()))
		self.dialogue.delete("0.0", "end")
		self.code.delete("0.0", "end")

	def get_attack_data(self):
		self.attack_data[self.nom.get()] = [self.ascii.get(), self.dialogue.get("0.0", "end"), self.code.get("0.0", "end"), self.main_part.get(), self.var_sec_part.get()]
		self.reset_data()

	def save(self):		
		if self.var_active.get() == 1:
			file_server = "server_data.cs"
		else:
			file_server = "server_data_" + self.lieu.get() + "_" + date.today().strftime("%d-%m-%y") + ".cs"	

		with open(file_server, 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(self.code_dict)
		
		self.bouton_save.config(text="Server Saved")
		self.bouton_save.after(3000, self.init_save_button)

	def open(self):
		### open dialog to load a server file
		self.filename = filedialog.askopenfilename(initialdir = self.crash_gui_dir, title="Open a Server file", filetypes =(("crash server files", "*.cs"), ("all files", "*.*")))
		if self.filename is not None:
			self.read_data(self.filename)

		
	def read_data(self, file):
		##### Lecture fichier 
		self.file = file
		with open(self.file, "rb") as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			code_dict = mon_depickler.load()
			self.donnee_server = code_dict["server_data"]
			self.donnee_attack = code_dict["attack_data"]

		self.attack_data = self.donnee_attack

	def load_server_data(self):
		if self.file == "server_data.cs":
			self.active.select()
		else:
			self.active.deselect()	
		
		### SERVER DATA LOAD

		self.lieu.delete(0, len(self.lieu.get()))
		self.lieu.insert(0, self.donnee_server["lieu"])

		self.tmps.delete(0, len(self.tmps.get()))
		self.tmps.insert(0, self.donnee_server["tmps"])

		self.bpm.delete(0, len(self.bpm.get()))
		self.bpm.insert(0, self.donnee_server["bpm_intro"])

		self.lang.set(self.donnee_server["lang"])
		
		self.voice.delete(0, len(self.voice.get()))
		self.voice.insert(0, self.donnee_server["voice"])
		
		self.scale.set(self.donnee_server["scale_intro"])

		self.root.delete(0, len(self.root.get()))
		self.root.insert(0, self.donnee_server["root_intro"])

		self.ip.delete(0, len(self.ip.get()))		
		self.ip.insert(0, self.donnee_server["adresse"])

		if self.donnee_server["video"] == 1:
			self.video.select()
		else:
			self.video.deselect()
			self.ip.config(state=DISABLED)

	def get_name_from_list(self, val=None):
		part_name = None
		if val is not None:
			sender = val.widget
			idx = sender.curselection()
			if idx:
				part_name = str(sender.get(idx))
			else:
				if self.part_list.curselection():
					part_name = str(self.part_list.get(self.part_list.curselection()))
				elif self.sec_part_list.curselection():	
					part_name = str(self.sec_part_list.get(self.sec_part_list.curselection()))
		else:
			if self.part_list.curselection():
				part_name = str(self.part_list.get(self.part_list.curselection()))
			elif self.sec_part_list.curselection():	
				part_name = str(self.sec_part_list.get(self.sec_part_list.curselection()))
		if part_name:
			return part_name


	def load_attack_data(self, part_name=None):
		### ATTACK DATA LOAD
		self.nom.insert(0, part_name)
		self.main_part.insert(0, self.attack_data[part_name][3])
		# except:
		# 	self.main_part.insert(0,0)

		try:
			if self.attack_data[part_name][4] == 1:
				self.sec_part.select()
				self.main_part.config(state=DISABLED)
			else:
				self.sec_part.deselect()
				self.main_part.config(state=NORMAL)
		except:
			self.sec_part.deselect()
			self.main_part.config(state=NORMAL)

		self.ascii.insert(0, self.attack_data[part_name][0])
		self.dialogue.insert("0.0", self.attack_data[part_name][1])
		self.code.insert("0.0", self.attack_data[part_name][2])

#afficher
server = ServerConf()
server.window.mainloop()