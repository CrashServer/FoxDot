#coding: utf8
#!/usr/bin/env python3

## Crash GUI Server Generator ###
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import pickle
import os
from datetime import date
import pyperclip as clip
from pyfiglet import figlet_format

class ServerConf:
	
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	
	def __init__(self):
		self.crash_gui_dir = os.path.dirname(os.path.realpath(__file__))
		self.window = Tk()
		self.window.title("Crash Server Configurator")
		self.window.geometry("1080x720")
		self.window.minsize(800,600)
		#self.window.iconbitmap("logo.ico")
		self.window.config(background="#e6e7d0")
		self.code_dict = {}
		self.attack_data = {}

		#Initialisationd des composants
		self.title_frame = Frame(self.window, bg='#e6e7d0', pady=3, height=50, relief=RAISED, borderwidth=3)
		self.frame = Frame(self.window, bg='#e6e7d0')
		self.button_frame = Frame(self.window, bg='#e6e7d0', height=100, relief=RAISED, borderwidth=3)
		self.attack_frame = Frame(self.window)
		self.attack =  Frame(self.attack_frame)
		self.part = Frame(self.attack_frame)
		
		#Lecture des données du server actif
		if os.path.isfile('server_data.cs'):
			self.read_data("server_data.cs")

		#Creation des composants
		self.create_widgets()

		#empaquetage
		self.frame.pack(fill=X, expand=True)
		self.button_frame.pack(side=BOTTOM, fill=Y, expand=True)
		self.attack_frame.pack(fill=X, expand=True)
		self.part.pack(side= LEFT, fill=X, expand=True)
		self.attack.pack(side=LEFT, fill=X, expand=True)
		
		#lecture des données du server
		self.load_server_data()

	def create_widgets(self):
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
		
		### BUTTONS
		self.create_up_button()
		self.create_down_button()
		self.create_save_button()
		self.create_open_button()	
		self.create_quit_button()
		self.create_test_button()
		self.create_update_button()
		self.create_delete_button()
		self.create_new_button()
		self.create_add_button()
		#self.create_reset_button()
				
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

		label_part = Label(frame_part, text="Parties :")
		label_part.pack(side=TOP, padx=5, pady=5)

		self.up_down_button_frame = Frame(frame_part)
		self.up_down_button_frame.pack(side=LEFT, fill=Y, padx=5, pady=5)

		self.part_box_frame = Frame(frame_part)
		self.part_box_frame.pack(side=LEFT, fill=Y, padx=5, pady=5)
		self.part_box = Listbox(self.part_box_frame, relief=SUNKEN, selectmode=SINGLE)
		self.part_box.config(height = 30)
		self.part_box.pack(side=LEFT, fill=Y, padx=5)

		self.part_get()
		self.part_box.bind("<<ListboxSelect>>", self.change_part)
		self.part_box.select_set(0, None)
		self.reset_data()
		self.load_attack_data(self.part_box.get(0))
		self.button_part = Frame(self.part_box_frame)
		self.button_part.pack(side=RIGHT)


	def change_part(self, val):
		if val:
			part_name = self.get_name_from_list(val)
			if part_name:
				self.get_attack_data()
				self.reset_data()
				self.load_attack_data(part_name)

			
	def create_nom(self):
		# Nom du server
		frame_nom = Frame(self.attack)
		frame_nom.pack(fill=X)

		label_nom = Label(frame_nom, text="NOM : ", width=20)
		label_nom.pack(side=LEFT, padx=5, pady=5)
		var_nom = StringVar()
		self.nom = Entry(frame_nom, textvariable = var_nom)
		self.nom.pack(side=LEFT, fill=X, padx=5, expand=True)
		

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
		self.dialogue = Text(frame_dialogue, wrap=WORD)
		self.dialogue.config(height=5)
		self.dialogue.pack(side=LEFT, fill=X, padx=5, expand=True)

	def create_code(self):
		frame_code = Frame(self.attack)
		frame_code.pack(expand=True, fill=X)

		label_code = Label(frame_code, text="CODE : ", width=20)
		label_code.pack(side=LEFT, padx=5, pady=5)
		self.code = Text(frame_code, wrap=WORD)
		self.code.pack(side=LEFT, fill=X, padx=5, expand=True)

	### BUTTONS

	def create_up_button(self):
		self.bouton_up = Button(self.up_down_button_frame, text="UP", command=self.up_button)
		self.bouton_up.pack(side=TOP, padx=5, pady=5)

	def create_down_button(self):
		self.bouton_down = Button(self.up_down_button_frame, text="DOWN", command=self.down_button)
		self.bouton_down.pack(side=TOP, padx=5, pady=5)	

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
	def create_test_button(self):
		self.buton_test = Button(self.button_part, text="Test it", command=self.test_button)
		self.buton_test.pack(side=TOP, padx=15, pady=5)

	def create_add_button(self):
		self.bouton_add = Button(self.button_part, text="Add", command=self.add_button)
		self.bouton_add.pack(side=TOP, padx=15, pady=5)

	def create_delete_button(self):
		self.bouton_delete = Button(self.button_part, text="Delete", command=self.delete_button)
		self.bouton_delete.pack(side=TOP, padx=15, pady=5)

	def create_update_button(self):
		self.bouton_update = Button(self.button_part, text="Update", command=self.update)
		self.bouton_update.pack(side=TOP, padx=15, pady=5)

	def create_new_button(self):
		self.bouton_new = Button(self.button_part, text="New", command=self.new_button)
		self.bouton_new.pack(side=TOP, padx=15, pady=5)


	### Functions
	def part_get(self):
		pos = self.part_box.curselection()
		self.part_box.delete(0, 'end')
		self.part_list = []
		self.part_list = [key for (key, value) in sorted(self.attack_data.items(), key= lambda x: x[1][3]) if value is not ""]		
		for i, part in enumerate(self.part_list):
			self.part_box.insert(i, part)		
		if pos is not ():
			self.part_box.selection_set(pos[0])

	def save_button(self):
		self.get_server_data()
		self.get_attack_data()
		self.code_dict["server_data"] = self.server_data
		self.code_dict["attack_data"] = self.attack_data
		self.save()

	def delete_button(self):
		try:
			value = str(self.part_box.get(self.part_box.curselection())) 
		except:
			pass   
		del self.attack_data[value]
		self.update()

	def add_button(self):
		self.part_list.append(self.nom.get())
		self.get_attack_data()
		self.update()

	def update(self):
		for i, part in enumerate(self.part_list):
			if part in self.attack_data.keys():
				self.attack_data[part][3] = i
		self.part_get()		
		self.reset_data()

	def new_button(self):
		self.reset_data()

	def test_button(self):
		blase = self.ascii.get()
		code_txt = self.code.get("0.0", "end")
		clip.copy((figlet_format(blase) if blase is not None else "") + "\n" + (code_txt if code_txt is not None else ""))

	def up_button(self):
		self.part_idx = self.part_box.curselection()
		if self.part_idx is not None:
			for pos in self.part_idx: 
				if pos == 0:
					continue
				text = self.part_box.get(pos)
				self.part_box.delete(pos)
				self.part_box.insert(pos-1, text)
				self.part_list.pop(pos)
				self.part_list.insert(pos-1, text)
				self.part_box.selection_set(pos-1)			
		else: 
			pass
		self.update()

	def down_button(self):
		self.part_idx = self.part_box.curselection()
		if self.part_idx is not None:
			for pos in self.part_idx: 
				if pos == len(self.part_list)-1:
					continue
				text = self.part_box.get(pos)
				self.part_box.delete(pos)
				self.part_box.insert(pos+1, text)
				self.part_list.pop(pos)
				self.part_list.insert(pos+1, text)
				self.part_box.selection_set(pos+1)
		else: 
			pass
		self.update()


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
		# Clear attack data
		self.nom.delete(0, len(self.nom.get()))
		self.ascii.delete(0, len(self.ascii.get()))
		self.dialogue.delete("0.0", "end")
		self.code.delete("0.0", "end")

	def get_attack_data(self):
		# Get the windows data from the attack part
		name = self.nom.get()
		if name:
			self.attack_data[name] = [self.ascii.get(), self.dialogue.get("0.0", "end"), self.code.get("0.0", "end"), self.part_list.index(name)]
			self.reset_data()

	def save(self):		
		if self.var_active.get() == 1:
			file_server = "server_data.cs"
			with open("lostfile.cs", "wb") as lostfile:
				lost_pickler = pickle.Pickler(lostfile)
				lost_pickler.dump(self.part_list)
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
		self.load_server_data()
		self.load_attack_data(self.part_box.get(0))	

		
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
		# Return the name of the selected part in the list
		part_name = None
		if val is not None:
			sender = val.widget
			idx = sender.curselection()
			if idx:
				part_name = str(sender.get(idx))
			else:
				if self.part_box.curselection():
					part_name = str(self.part_box.get(self.part_box.curselection()))
		else:
			if self.part_box.curselection():
				part_name = str(self.part_box.get(self.part_box.curselection()))
		if part_name:
			return part_name


	def load_attack_data(self, part_name=None):
		### ATTACK DATA LOAD
		self.reset_data()
		self.nom.insert(0, part_name)
		self.ascii.insert(0, self.attack_data[part_name][0])
		self.dialogue.insert("0.0", self.attack_data[part_name][1])
		self.code.insert("0.0", self.attack_data[part_name][2])
		

	def reset_index(self):
		i = 0
		for keys in self.attack_data:
			self.attack_data[keys][3] = i
			self.attack_data[keys][4] = 0
			print(keys, self.attack_data[keys][3], self.attack_data[keys][4])	
			i += 1 
		#self.update()

#afficher
server = ServerConf()
server.window.mainloop()