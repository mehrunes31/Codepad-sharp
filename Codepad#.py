import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, colorchooser
import base64

class CodeEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad#")
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill="both")

        self.languages = {
            "English": {
                "File": "File",
                "New": "New",
                "Open": "Open",
                "Save": "Save",
                "Save As": "Save As",
                "Exit": "Exit",
                "Edit": "Edit",
                "Undo": "Undo",
                "Copy": "Copy",
                "Paste": "Paste",
                "Select All": "Select All",
                "Search": "Search",
                "Find...": "Find...",
                "Languages": "Languages",
                "View": "View",
                "Choose Background Color": "Choose Background Color",
                "Run": "Run",
                "Run File": "Run File",
                "Base64": "Base64",
                "Encode": "Encode",
                "Decode": "Decode",
                "Hexadecimal": "Hexadecimal",
                "Exit Confirmation": "Exit",
                "Exit Message": "Do you really want to exit?",
                "Error": "Error",
                "Invalid Base64": "Invalid Base64 text!",
                "Invalid Hexadecimal": "Invalid Hexadecimal text!",
                "Search Prompt": "Enter text to search:",
                "Find": "Find",
                "Programming Languages": "Programming Languages",
                "Python": "Python",
                "Rust": "Rust",
                "C++": "C++",
                "Java": "Java",
                "JavaScript": "JavaScript",
                "HTML": "HTML",
                "CSS": "CSS",
            },
            "Turkish": {
                "File": "Dosya",
                "New": "Yeni",
                "Open": "Aç",
                "Save": "Kaydet",
                "Save As": "Farklı Kaydet",
                "Exit": "Çıkış",
                "Edit": "Düzen",
                "Undo": "Geri Al",
                "Copy": "Kopyala",
                "Paste": "Yapıştır",
                "Select All": "Hepsini Seç",
                "Search": "Ara",
                "Find...": "Bul...",
                "Languages": "Diller",
                "View": "Görünüm",
                "Choose Background Color": "Arka Plan Rengi Seç",
                "Run": "Çalıştır",
                "Run File": "Dosyayı Çalıştır",
                "Base64": "Base64",
                "Encode": "Encode",
                "Decode": "Decode",
                "Exit Confirmation": "Çıkış",
                "Exit Message": "Gerçekten çıkıcak mısın?",
                "Error": "Hata",
                "Invalid Base64": "Geçersiz Base64 metni!",
                "Search Prompt": "Aranacak kelimeyi girin:",
                "Find": "Bul",
                "Programming Languages": "Programlama Dileri",
                "Python": "Python",
                "Rust": "Rust",
                "C++": "C++",
                "Java": "Java",
                "JavaScript": "JavaScript",
                "HTML": "HTML",
                "CSS": "CSS",
            },
            "German": {
                "File": "Datei",
                "New": "Neu",
                "Open": "Öffnen",
                "Save": "Speichern",
                "Save As": "Speichern unter",
                "Exit": "Beenden",
                "Edit": "Bearbeiten",
                "Undo": "Rückgängig",
                "Copy": "Kopieren",
                "Paste": "Einfügen",
                "Select All": "Alles auswählen",
                "Search": "Suchen",
                "Find...": "Finden...",
                "Languages": "Sprachen",
                "View": "Ansicht",
                "Choose Background Color": "Hintergrundfarbe wählen",
                "Run": "Ausführen",
                "Run File": "Datei ausführen",
                "Base64": "Base64",
                "Encode": "Kodieren",
                "Decode": "Dekodieren",
                "Exit Confirmation": "Beenden",
                "Exit Message": "Möchten Sie wirklich beenden?",
                "Error": "Fehler",
                "Invalid Base64": "Ungültiger Base64-Text!",
                "Search Prompt": "Suchbegriff eingeben:",
                "Find": "Finden",
                "Programming Languages": "Programmiersprachen",
                "Python": "Python",
                "Rust": "Rust",
                "C++": "C++",
                "Java": "Java",
                "JavaScript": "JavaScript",
                "HTML": "HTML",
                "CSS": "CSS",
            },
            "Russian": {
                "File": "Файл",
                "New": "Новый",
                "Open": "Открыть",
                "Save": "Сохранить",
                "Save As": "Сохранить как",
                "Exit": "Выход",
                "Edit": "Правка",
                "Undo": "Отменить",
                "Copy": "Копировать",
                "Paste": "Вставить",
                "Select All": "Выделить все",
                "Search": "Поиск",
                "Find...": "Найти...",
                "Languages": "Языки",
                "View": "Вид",
                "Choose Background Color": "Выбрать цвет фона",
                "Run": "Запуск",
                "Run File": "Запустить файл",
                "Base64": "Base64",
                "Encode": "Кодировать",
                "Decode": "Декодировать",
                "Exit Confirmation": "Выход",
                "Exit Message": "Вы действительно хотите выйти?",
                "Error": "Ошибка",
                "Invalid Base64": "Недопустимый текст Base64!",
                "Search Prompt": "Введите текст для поиска:",
                "Find": "Найти",
                "Programming Languages": "Языки программирования",
                "Python": "Python",
                "Rust": "Rust",
                "C++": "C++",
                "Java": "Java",
                "JavaScript": "JavaScript",
                "HTML": "HTML",
                "CSS": "CSS",
            },
            "French": {
               "File": "Fichier",
               "New": "Nouveau",
               "Open": "Ouvrir",
               "Save": "Enregistrer",
               "Save As": "Enregistrer sous",
               "Exit": "Quitter",
               "Edit": "Éditer",
               "Undo": "Annuler",
               "Copy": "Copier",
               "Paste": "Coller",
               "Select All": "Tout sélectionner",
               "Search": "Rechercher",
               "Find...": "Trouver...",
               "Languages": "Langues",
               "View": "Affichage",
               "Choose Background Color": "Choisir la couleur de fond",
               "Run": "Exécuter",
               "Run File": "Exécuter le fichier",
               "Base64": "Base64",
               "Encode": "Encoder",
               "Decode": "Décoder",
               "Exit Confirmation": "Quitter",
               "Exit Message": "Voulez-vous vraiment quitter ?",
               "Error": "Erreur",
               "Invalid Base64": "Texte Base64 invalide !",
               "Search Prompt": "Entrez le texte à rechercher :",
               "Find": "Trouver",
               "Programming Languages": "Langages de programmation",
                "Python": "Python",
                "Rust": "Rust",
                "C++": "C++",
                "Java": "Java",
                "JavaScript": "JavaScript",
                "HTML": "HTML",
                "CSS": "CSS",
            },
            "Spanish": {
               "File": "Archivo",
               "New": "Nuevo",
               "Open": "Abrir",
               "Save": "Guardar",
               "Save As": "Guardar como",
               "Exit": "Salir",
               "Edit": "Editar",
               "Undo": "Deshacer",
               "Copy": "Copiar",
               "Paste": "Pegar",
               "Select All": "Seleccionar todo",
               "Search": "Buscar",
               "Find...": "Encontrar...",
               "Languages": "Idiomas",
               "View": "Ver",
               "Choose Background Color": "Elegir color de fondo",
               "Run": "Ejecutar",
               "Run File": "Ejecutar archivo",
               "Base64": "Base64",
               "Encode": "Codificar",
               "Decode": "Decodificar",
               "Exit Confirmation": "Salir",
               "Exit Message": "¿Realmente quieres salir?",
               "Error": "Error",
               "Invalid Base64": "¡Texto Base64 inválido!",
               "Search Prompt": "Ingrese el texto a buscar:",
               "Find": "Encontrar",
               "Programming Languages": "Lenguajes de programación",
                "Python": "Python",
                "Rust": "Rust",
                "C++": "C++",
                "Java": "Java",
                "JavaScript": "JavaScript",
                "HTML": "HTML",
                "CSS": "CSS",
            },
            "Italian": {
               "File": "File",
               "New": "Nuovo",
               "Open": "Apri",
               "Save": "Salva",
               "Save As": "Salva come",
               "Exit": "Esci",
               "Edit": "Modifica",
               "Undo": "Annulla",
               "Copy": "Copia",
               "Paste": "Incolla",
               "Select All": "Seleziona tutto",
               "Search": "Cerca",
               "Find...": "Trova...",
               "Languages": "Lingue",
               "View": "Visualizza",
               "Choose Background Color": "Scegli il colore di sfondo",
               "Run": "Esegui",
               "Run File": "Esegui file",
               "Base64": "Base64",
               "Encode": "Codifica",
               "Decode": "Decodifica",
               "Exit Confirmation": "Esci",
               "Exit Message": "Vuoi davvero uscire?",
               "Error": "Errore",
               "Invalid Base64": "Testo Base64 non valido!",
               "Search Prompt": "Inserisci il testo da cercare:",
               "Find": "Trova",
               "Programming Languages": "Linguaggi di programmazione",
                "Python": "Python",
                "Rust": "Rust",
                "C++": "C++",
                "Java": "Java",
                "JavaScript": "JavaScript",
                "HTML": "HTML",
                "CSS": "CSS",
            },
            "Ελληνικά": {
                "File": "Αρχείο",
                "New": "Νέο",
                "Open": "Άνοιγμα",
                "Save": "Αποθήκευση",
                "Save As": "Αποθήκευση ως",
                "Exit": "Έξοδος",
                "Edit": "Επεξεργασία",
                "Undo": "Αναίρεση",
                "Copy": "Αντιγραφή",
                "Paste": "Επικόλληση",
                "Select All": "Επιλογή όλων",
                "Search": "Αναζήτηση",
                "Find...": "Εύρεση...",
                "Languages": "Γλώσσες",
                "View": "Προβολή",
                "Choose Background Color": "Επιλογή χρώματος φόντου",
                "Run": "Εκτέλεση",
                "Run File": "Εκτέλεση αρχείου",
                "Base64": "Base64",
                "Encode": "Κωδικοποίηση",
                "Decode": "Αποκωδικοποίηση",
                "Hexadecimal": "Δεκαεξαδικό",
                "Exit Confirmation": "Επιβεβαίωση εξόδου",
                "Exit Message": "Θέλετε πραγματικά να βγείτε;",
                "Error": "Σφάλμα",
                "Invalid Base64": "Μη έγκυρο κείμενο Base64!",
                "Invalid Hexadecimal": "Μη έγκυρο δεκαεξαδικό κείμενο!",
                "Search Prompt": "Εισάγετε κείμενο για αναζήτηση:",
                "Find": "Εύρεση",
                "Programming Languages": "Γλώσσες προγραμματισμού",
                "Python": "Python",
                "Rust": "Rust",
                "C++": "C++",
                "Java": "Java",
                "JavaScript": "JavaScript",
                "HTML": "HTML",
                "CSS": "CSS"
            },
            "中文": {
                "File": "文件",
                "New": "新建",
                "Open": "打开",
                "Save": "保存",
                "Save As": "另存为",
                "Exit": "退出",
                "Edit": "编辑",
                "Undo": "撤销",
                "Copy": "复制",
                "Paste": "粘贴",
                "Select All": "全选",
                "Search": "搜索",
                "Find...": "查找...",
                "Languages": "语言",
                "View": "视图",
                "Choose Background Color": "选择背景颜色",
                "Run": "运行",
                "Run File": "运行文件",
                "Base64": "Base64",
                "Encode": "编码",
                "Decode": "解码",
                "Hexadecimal": "十六进制",
                "Exit Confirmation": "退出确认",
                "Exit Message": "您真的想退出吗？",
                "Error": "错误",
                "Invalid Base64": "无效的Base64文本！",
                "Invalid Hexadecimal": "无效的十六进制文本！",
                "Search Prompt": "输入要搜索的文本：",
                "Find": "查找",
                "Programming Languages": "编程语言",
                "Python": "Python",
                "Rust": "Rust",
                "C++": "C++",
                "Java": "Java",
                "JavaScript": "JavaScript",
                "HTML": "HTML",
                "CSS": "CSS"
}
        }

        self.current_language = "English"
        self.translations = self.languages[self.current_language]

        self.create_menu()

        # Menü oluşturulduğundan emin olun, sonra dili ayarlayın
        self.set_language(self.current_language)

        self.text_area.bind("<Key>", self.on_keypress)

        # Klavye kısayollarını ayarlayın
        self.root.bind_all("<Control-n>", lambda event: self.new_file())
        self.root.bind_all("<Control-o>", lambda event: self.open_file())
        self.root.bind_all("<Control-s>", lambda event: self.save_file())
        self.root.bind_all("<Control-Shift-S>", lambda event: self.save_as_file())
        self.root.bind_all("<Control-q>", lambda event: self.exit_app())
        self.root.bind_all("<Control-z>", lambda event: self.undo())
        self.root.bind_all("<Control-c>", lambda event: self.copy())
        self.root.bind_all("<Control-v>", lambda event: self.paste())
        self.root.bind_all("<Control-a>", lambda event: self.select_all())
        self.root.bind_all("<Control-f>", lambda event: self.find_text())

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label=self.translations["File"], menu=self.file_menu)
        self.file_menu.add_command(label=self.translations["New"], command=self.new_file)
        self.file_menu.add_command(label=self.translations["Open"], command=self.open_file)
        self.file_menu.add_command(label=self.translations["Save"], command=self.save_file)
        self.file_menu.add_command(label=self.translations["Save As"], command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label=self.translations["Exit"], command=self.exit_app)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label=self.translations["Edit"], menu=self.edit_menu)
        self.edit_menu.add_command(label=self.translations["Undo"], command=self.undo)
        self.edit_menu.add_command(label=self.translations["Copy"], command=self.copy)
        self.edit_menu.add_command(label=self.translations["Paste"], command=self.paste)
        self.edit_menu.add_command(label=self.translations["Select All"], command=self.select_all)

        self.search_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label=self.translations["Search"], menu=self.search_menu)
        self.search_menu.add_command(label=self.translations["Find..."], command=self.find_text)

        self.color_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label=self.translations["View"], menu=self.color_menu)
        self.color_menu.add_command(label=self.translations["Choose Background Color"], command=self.choose_background_color)

        self.run_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label=self.translations["Run"], menu=self.run_menu)
        self.run_menu.add_command(label=self.translations["Run File"], command=self.run_file)

        self.base64_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label=self.translations["Base64"], menu=self.base64_menu)
        self.base64_menu.add_command(label=self.translations["Encode"], command=self.encode_base64)
        self.base64_menu.add_command(label=self.translations["Decode"], command=self.decode_base64)

        self.hexadecimal_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label=self.translations["Hexadecimal"], menu=self.hexadecimal_menu)
        self.hexadecimal_menu.add_command(label=self.translations["Encode"], command=self.encode_hexadecimal)
        self.hexadecimal_menu.add_command(label=self.translations["Decode"], command=self.decode_hexadecimal)

        self.language_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label=self.translations["Languages"], menu=self.language_menu)
        for language in self.languages:
            self.language_menu.add_command(label=language, command=lambda lang=language: self.set_language(lang))

        self.programming_languages_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label=self.translations["Programming Languages"], menu=self.programming_languages_menu)
        self.programming_languages_menu.add_command(label=self.translations["Python"], command=lambda: self.select_language("Python"))
        self.programming_languages_menu.add_command(label=self.translations["Rust"], command=lambda: self.select_language("Rust"))
        self.programming_languages_menu.add_command(label=self.translations["C++"], command=lambda: self.select_language("C++"))
        self.programming_languages_menu.add_command(label=self.translations["Java"], command=lambda: self.select_language("Java"))
        self.programming_languages_menu.add_command(label=self.translations["JavaScript"], command=lambda: self.select_language("JavaScript"))
        self.programming_languages_menu.add_command(label=self.translations["HTML"], command=lambda: self.select_language("HTML"))
        self.programming_languages_menu.add_command(label=self.translations["CSS"], command=lambda: self.select_language("CSS"))

    def set_language(self, language):
        self.current_language = language
        self.translations = self.languages[language]
        self.update_ui_language()

    def update_ui_language(self):
        self.menu_bar.entryconfig(1, label=self.translations["File"])
        self.menu_bar.entryconfig(2, label=self.translations["Edit"])
        self.menu_bar.entryconfig(3, label=self.translations["Search"])
        self.menu_bar.entryconfig(4, label=self.translations["View"])
        self.menu_bar.entryconfig(5, label=self.translations["Run"])
        self.menu_bar.entryconfig(6, label=self.translations["Base64"])
        self.menu_bar.entryconfig(7, label=self.translations["Hexadecimal"])
        self.menu_bar.entryconfig(8, label=self.translations["Languages"])
        self.menu_bar.entryconfig(9, label=self.translations["Programming Languages"])

        self.file_menu.entryconfig(0, label=self.translations["New"])
        self.file_menu.entryconfig(1, label=self.translations["Open"])
        self.file_menu.entryconfig(2, label=self.translations["Save"])
        self.file_menu.entryconfig(3, label=self.translations["Save As"])
        self.file_menu.entryconfig(5, label=self.translations["Exit"])

        self.edit_menu.entryconfig(0, label=self.translations["Undo"])
        self.edit_menu.entryconfig(1, label=self.translations["Copy"])
        self.edit_menu.entryconfig(2, label=self.translations["Paste"])
        self.edit_menu.entryconfig(3, label=self.translations["Select All"])

        self.search_menu.entryconfig(0, label=self.translations["Find..."])

        self.color_menu.entryconfig(0, label=self.translations["Choose Background Color"])

        self.run_menu.entryconfig(0, label=self.translations["Run File"])

        self.base64_menu.entryconfig(0, label=self.translations["Encode"])
        self.base64_menu.entryconfig(1, label=self.translations["Decode"])

        self.hexadecimal_menu.entryconfig(0, label=self.translations["Encode"])
        self.hexadecimal_menu.entryconfig(1, label=self.translations["Decode"])

        for i, language in enumerate(self.languages):
            self.language_menu.entryconfig(i, label=language)

    def new_file(self):
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if hasattr(self, "file_path") and self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def exit_app(self):
        if messagebox.askokcancel(self.translations["Exit Confirmation"], self.translations["Exit Message"]):
            self.root.quit()

    def undo(self):
        self.text_area.edit_undo()

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def select_all(self):
        self.text_area.tag_add("sel", "1.0", "end")

    def find_text(self):
        search_prompt = tk.simpledialog.askstring(self.translations["Find"], self.translations["Search Prompt"])
        if search_prompt:
            self.search_text(search_prompt)

    def search_text(self, search_prompt):
        start_pos = "1.0"
        while True:
            start_pos = self.text_area.search(search_prompt, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_prompt)}c"
            self.text_area.tag_add("highlight", start_pos, end_pos)
            self.text_area.tag_config("highlight", background="yellow")
            start_pos = end_pos

    def choose_background_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(bg=color)

    def run_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            exec(open(file_path).read())

    def encode_base64(self):
        input_text = self.text_area.get("1.0", tk.END).strip()
        try:
            encoded_text = base64.b64encode(input_text.encode()).decode()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, encoded_text)
        except Exception as e:
            messagebox.showerror(self.translations["Error"], self.translations["Invalid Base64"])

    def decode_base64(self):
        input_text = self.text_area.get("1.0", tk.END).strip()
        try:
            decoded_text = base64.b64decode(input_text.encode()).decode()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, decoded_text)
        except Exception as e:
            messagebox.showerror(self.translations["Error"], self.translations["Invalid Base64"])

    def encode_hexadecimal(self):
        input_text = self.text_area.get("1.0", tk.END).strip()
        try:
            encoded_text = input_text.encode().hex()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, encoded_text)
        except Exception as e:
            messagebox.showerror(self.translations["Error"], self.translations["Invalid Hexadecimal"])

    def decode_hexadecimal(self):
        input_text = self.text_area.get("1.0", tk.END).strip()
        try:
            decoded_text = bytes.fromhex(input_text).decode()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, decoded_text)
        except Exception as e:
            messagebox.showerror(self.translations["Error"], self.translations["Invalid Hexadecimal"])

    def on_keypress(self, event):
        self.text_area.edit_modified(True)

    def select_language(self, language):
        messagebox.showinfo("Programming Language Selected", f"You selected {language}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeEditorApp(root)
    root.mainloop()
