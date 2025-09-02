import tkinter as tk
from tkinter import ttk, messagebox
import random
import os # For setting the icon (optional)


class NameMatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Name Matcher & Message Generator")
        self.root.geometry("500x500") # Set initial window size
        self.root.resizable(False, False) # Make window non-resizable

        # Optional: Set a small icon if you have one (e.g., 'icon.ico' or 'icon.png')
        if os.path.exists('icon.ico'):
            self.root.iconbitmap('icon.ico')
        elif os.path.exists('icon.png'):
            # For .png, you might need ImageTk from Pillow: pip install Pillow
            # from PIL import ImageTk, Image
            # icon_image = Image.open('icon.png')
            # self.root.iconphoto(True, ImageTk.PhotoImage(icon_image))
            pass

        # Styling for a modern look
        self.style = ttk.Style()
        self.style.theme_use('clam') # 'clam', 'alt', 'default', 'classic'

        self.style.configure('TFrame', background="#54F6D0")
        self.style.configure('TLabel', background='#e0f7fa', font=('Arial', 12))
        self.style.configure('TEntry', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12, 'bold'), padding=8)
        self.style.map('TButton', background=[('active', "#0D7FDD")])

        self._create_widgets()

    def _create_widgets(self):
        # Main Frame for padding and background
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        ttk.Label(main_frame, text="LoveTest Calculater❤️", font=('Arial', 20, 'bold'), foreground="#EF0E0E").pack(pady=19)

      
        # First Name Entry (Love theme design)
        ttk.Label(main_frame, text="Enter Your Name:").pack(pady=5, anchor='w')
        self.name1_entry = tk.Entry(main_frame, width=32, font=('Arial', 13, 'bold'),
                                   bg='#ffe4ec', fg='#d32f2f', relief='flat', highlightthickness=2,
                                   highlightbackground='#d32f2f', highlightcolor='#d32f2f', insertbackground='#d32f2f')
        self.name1_entry.pack(pady=5, ipady=6)
        self.name1_entry.focus_set()

        # Second Name Entry (Love theme design)
        ttk.Label(main_frame, text="Enter Your Partner Name:").pack(pady=5, anchor='w')
        self.name2_entry = tk.Entry(main_frame, width=32, font=('Arial', 13, 'bold'),
                                   bg='#ffe4ec', fg='#d32f2f', relief='flat', highlightthickness=2,
                                   highlightbackground='#d32f2f', highlightcolor='#d32f2f', insertbackground='#d32f2f')
        self.name2_entry.pack(pady=5, ipady=6)

        ttk.Button(main_frame, text="Generate Message", command=self.process_names).pack(pady=20)

        ttk.Label(main_frame, text="Matched Letters:", font=('Arial', 12, 'bold')).pack(pady=5, anchor='w')
        self.match_result_label = ttk.Label(main_frame, text="--", font=('Arial', 14), foreground='#d32f2f')
        self.match_result_label.pack(pady=5, anchor='w')
 
        ttk.Label(main_frame, text="Your Message:", font=('Arial', 12, 'bold')).pack(pady=5, anchor='w')
        self.message_label = ttk.Label(main_frame, text="Enter names and click the button!", font=('Arial', 12, 'italic'), wraplength=450)
        self.message_label.pack(pady=5, anchor='w')

    def calculate_name_match(self, name1, name2):
        """
        Calculates the number of common letters between two names (case-insensitive).
        """
        name1_lower = name1.lower()
        name2_lower = name2.lower()

        freq1 = {}
        for char in name1_lower:
            if 'a' <= char <= 'z':
                freq1[char] = freq1.get(char, 0) + 1

        freq2 = {}
        for char in name2_lower:
            if 'a' <= char <= 'z':
                freq2[char] = freq2.get(char, 0) + 1

        matched_letters_count = 0
        for char, count1 in freq1.items():
            if char in freq2:
                matched_letters_count += min(count1, freq2[char])

        return matched_letters_count

    def generate_positive_message(self, match_score):
        """
        Generates a positive or encouraging message based on the match score.
        Shows the message in a messagebox instead of the label.
        """
        messages = [
            "💖 आपके नामों में 1 अक्षर का मेल है! प्यार की शुरुआत हमेशा छोटी होती है।",
            "💕 आपके नामों में 2 अक्षर का मेल है! यह प्यार की मीठी शुरुआत है।",
            "💞 आपके नामों में 3 अक्षर का मेल है! दिलों की दूरी कम हो रही है।",
            "❤️ आपके नामों में 4 अक्षर का मेल है! यह सच्चे प्यार का संकेत है।",
            "😍 आपके नामों में 5 अक्षर का मेल है! आपके बीच की केमिस्ट्री कमाल की है।",
            "😘 आपके नामों में 6 अक्षर का मेल है! प्यार की खुशबू हर तरफ है।",
            "💑 आपके नामों में 7 अक्षर का मेल है! आप दोनों एक-दूसरे के लिए बने हैं।",
            "🌹 आपके नामों में 8 अक्षर का मेल है! रोमांस की हवा बह रही है।",
            "💓 आपके नामों में 9 अक्षर का मेल है! दिलों का मिलन हो रहा है।",
            "💘 आपके नामों में 10 अक्षर का मेल है! यह प्यार की गहराई दर्शाता है।",
            "💝 आपके नामों में 11 अक्षर का मेल है! आपके रिश्ते में मिठास है।",
            "💖 आपके नामों में 12 अक्षर का मेल है! प्यार की चमक आपके नामों में है।",
            "💕 आपके नामों में 13 अक्षर का मेल है! दिल से दिल का कनेक्शन मजबूत है।",
            "💞 आपके नामों में 14 अक्षर का मेल है! रोमांटिक वाइब्स हर जगह हैं।",
            "❤️ आपके नामों में 15 अक्षर का मेल है! यह सच्चे प्यार की पहचान है।",
            "😍 आपके नामों में 16 अक्षर का मेल है! आपके रिश्ते में जादू है।",
            "😘 आपके नामों में 17 अक्षर का मेल है! प्यार की मिठास बढ़ रही है।",
            "💑 आपके नामों में 18 अक्षर का मेल है! आप दोनों एक-दूसरे के लिए खास हैं।",
            "🌹 आपके नामों में 19 अक्षर का मेल है! रोमांस की खुशबू हर तरफ है।",
            "💓 आपके नामों में 20 अक्षर का मेल है! दिलों का मिलन और भी गहरा हो रहा है।",
            "💘 आपके नामों में 21 अक्षर का मेल है! प्यार की लहरें आपके बीच बह रही हैं।",
            "💝 आपके नामों में 22 अक्षर का मेल है! आपके रिश्ते में मिठास और प्यार है।",
            "💖 आपके नामों में 23 अक्षर का मेल है! प्यार की चमक आपके नामों में झलकती है।",
            "💕 आपके नामों में 24 अक्षर का मेल है! दिल से दिल का कनेक्शन और मजबूत हुआ।",
            "💞 आपके नामों में 25 अक्षर का मेल है! रोमांटिक वाइब्स हर जगह महसूस हो रही हैं।",
            "❤️ आपके नामों में 26 अक्षर का मेल है! यह सच्चे प्यार की गहराई है।",
            "😍 आपके नामों में 27 अक्षर का मेल है! आपके रिश्ते में जादू और रोमांस है।",
            "😘 आपके नामों में 28 अक्षर का मेल है! प्यार की मिठास हर तरफ फैल रही है।",
            "💑 आपके नामों में 29 अक्षर का मेल है! आप दोनों एक-दूसरे के लिए बने हैं।",
            "🌹 आपके नामों में 30 अक्षर का मेल है! रोमांस की खुशबू हर तरफ है।",
            "💓 आपके नामों में 31 अक्षर का मेल है! दिलों का मिलन और भी गहरा हो गया है।",
            "💘 आपके नामों में 32 अक्षर का मेल है! प्यार की लहरें आपके बीच बह रही हैं।",
            "💝 आपके नामों में 33 अक्षर का मेल है! आपके रिश्ते में मिठास और प्यार है।",
            "💖 आपके नामों में 34 अक्षर का मेल है! प्यार की चमक आपके नामों में झलकती है।",
            "💕 आपके नामों में 35 अक्षर का मेल है! दिल से दिल का कनेक्शन और मजबूत हुआ।",
            "💞 आपके नामों में 36 अक्षर का मेल है! रोमांटिक वाइब्स हर जगह महसूस हो रही हैं।",
            "❤️ आपके नामों में 37 अक्षर का मेल है! यह सच्चे प्यार की गहराई है।",
            "😍 आपके नामों में 38 अक्षर का मेल है! आपके रिश्ते में जादू और रोमांस है।",
            "😘 आपके नामों में 39 अक्षर का मेल है! प्यार की मिठास हर तरफ फैल रही है।",
            "💑 आपके नामों में 40 अक्षर का मेल है! आप दोनों एक-दूसरे के लिए बने हैं।",
            "🌹 आपके नामों में 41 अक्षर का मेल है! रोमांस की खुशबू हर तरफ है।",
            "💓 आपके नामों में 42 अक्षर का मेल है! दिलों का मिलन और भी गहरा हो गया है।",
            "💘 आपके नामों में 43 अक्षर का मेल है! प्यार की लहरें आपके बीच बह रही हैं।",
            "💝 आपके नामों में 44 अक्षर का मेल है! आपके रिश्ते में मिठास और प्यार है।",
            "💖 आपके नामों में 45 अक्षर का मेल है! प्यार की चमक आपके नामों में झलकती है।",
            "💕 आपके नामों में 46 अक्षर का मेल है! दिल से दिल का कनेक्शन और मजबूत हुआ।",
            "💞 आपके नामों में 47 अक्षर का मेल है! रोमांटिक वाइब्स हर जगह महसूस हो रही हैं।",
            "❤️ आपके नामों में 48 अक्षर का मेल है! यह सच्चे प्यार की गहराई है।",
            "😍 आपके नामों में 49 अक्षर का मेल है! आपके रिश्ते में जादू और रोमांस है।",
            "😘 आपके नामों में 50 अक्षर का मेल है! प्यार की मिठास हर तरफ फैल रही है।",
            "💑 आपके नामों में 51 अक्षर का मेल है! आप दोनों एक-दूसरे के लिए बने हैं।",
            "🌹 आपके नामों में 52 अक्षर का मेल है! रोमांस की खुशबू हर तरफ है।",
            "💓 आपके नामों में 53 अक्षर का मेल है! दिलों का मिलन और भी गहरा हो गया है।",
            "💘 आपके नामों में 54 अक्षर का मेल है! प्यार की लहरें आपके बीच बह रही हैं।",
            "💝 आपके नामों में 55 अक्षर का मेल है! आपके रिश्ते में मिठास और प्यार है।",
            "💖 आपके नामों में 56 अक्षर का मेल है! प्यार की चमक आपके नामों में झलकती है।",
            "💕 आपके नामों में 57 अक्षर का मेल है! दिल से दिल का कनेक्शन और मजबूत हुआ।",
            "💞 आपके नामों में 58 अक्षर का मेल है! रोमांटिक वाइब्स हर जगह महसूस हो रही हैं।",
            "❤️ आपके नामों में 59 अक्षर का मेल है! यह सच्चे प्यार की गहराई है।",
            "😍 आपके नामों में 60 अक्षर का मेल है! आपके रिश्ते में जादू और रोमांस है।",
            "😘 आपके नामों में 61 अक्षर का मेल है! प्यार की मिठास हर तरफ फैल रही है।",
            "💑 आपके नामों में 62 अक्षर का मेल है! आप दोनों एक-दूसरे के लिए बने हैं।",
            "🌹 आपके नामों में 63 अक्षर का मेल है! रोमांस की खुशबू हर तरफ है।",
            "💓 आपके नामों में 64 अक्षर का मेल है! दिलों का मिलन और भी गहरा हो गया है।",
            "💘 आपके नामों में 65 अक्षर का मेल है! प्यार की लहरें आपके बीच बह रही हैं।",
            "💝 आपके नामों में 66 अक्षर का मेल है! आपके रिश्ते में मिठास और प्यार है।",
            "💖 आपके नामों में 67 अक्षर का मेल है! प्यार की चमक आपके नामों में झलकती है।",
            "💕 आपके नामों में 68 अक्षर का मेल है! दिल से दिल का कनेक्शन और मजबूत हुआ।",
            "💞 आपके नामों में 69 अक्षर का मेल है! रोमांटिक वाइब्स हर जगह महसूस हो रही हैं।",
            "❤️ आपके नामों में 70 अक्षर का मेल है! यह सच्चे प्यार की गहराई है।",
            "😍 आपके नामों में 71 अक्षर का मेल है! आपके रिश्ते में जादू और रोमांस है।",
            "😘 आपके नामों में 72 अक्षर का मेल है! प्यार की मिठास हर तरफ फैल रही है।",
            "💑 आपके नामों में 73 अक्षर का मेल है! आप दोनों एक-दूसरे के लिए बने हैं।",
            "🌹 आपके नामों में 74 अक्षर का मेल है! रोमांस की खुशबू हर तरफ है।",
            "💓 आपके नामों में 75 अक्षर का मेल है! दिलों का मिलन और भी गहरा हो गया है।",
            "💘 आपके नामों में 76 अक्षर का मेल है! प्यार की लहरें आपके बीच बह रही हैं।",
            "💝 आपके नामों में 77 अक्षर का मेल है! आपके रिश्ते में मिठास और प्यार है।",
            "💖 आपके नामों में 78 अक्षर का मेल है! प्यार की चमक आपके नामों में झलकती है।",
            "💕 आपके नामों में 79 अक्षर का मेल है! दिल से दिल का कनेक्शन और मजबूत हुआ।",
            "💞 आपके नामों में 80 अक्षर का मेल है! रोमांटिक वाइब्स हर जगह महसूस हो रही हैं।",
            "❤️ आपके नामों में 81 अक्षर का मेल है! यह सच्चे प्यार की गहराई है।",
            "😍 आपके नामों में 82 अक्षर का मेल है! आपके रिश्ते में जादू और रोमांस है।",
            "😘 आपके नामों में 83 अक्षर का मेल है! प्यार की मिठास हर तरफ फैल रही है।",
            "💑 आपके नामों में 84 अक्षर का मेल है! आप दोनों एक-दूसरे के लिए बने हैं।",
            "🌹 आपके नामों में 85 अक्षर का मेल है! रोमांस की खुशबू हर तरफ है।",
            "💓 आपके नामों में 86 अक्षर का मेल है! दिलों का मिलन और भी गहरा हो गया है।",
            "💘 आपके नामों में 87 अक्षर का मेल है! प्यार की लहरें आपके बीच बह रही हैं।",
            "💝 आपके नामों में 88 अक्षर का मेल है! आपके रिश्ते में मिठास और प्यार है।",
            "💖 आपके नामों में 89 अक्षर का मेल है! प्यार की चमक आपके नामों में झलकती है।",
            "💕 आपके नामों में 90 अक्षर का मेल है! दिल से दिल का कनेक्शन और मजबूत हुआ।",
            "💞 आपके नामों में 91 अक्षर का मेल है! रोमांटिक वाइब्स हर जगह महसूस हो रही हैं।",
            "❤️ आपके नामों में 92 अक्षर का मेल है! यह सच्चे प्यार की गहराई है।",
            "😍 आपके नामों में 93 अक्षर का मेल है! आपके रिश्ते में जादू और रोमांस है।",
            "😘 आपके नामों में 94 अक्षर का मेल है! प्यार की मिठास हर तरफ फैल रही है।",
            "💑 आपके नामों में 95 अक्षर का मेल है! आप दोनों एक-दूसरे के लिए बने हैं।",
            "🌹 आपके नामों में 96 अक्षर का मेल है! रोमांस की खुशबू हर तरफ है।",
            "💓 आपके नामों में 97 अक्षर का मेल है! दिलों का मिलन और भी गहरा हो गया है।",
            "💘 आपके नामों में 98 अक्षर का मेल है! प्यार की लहरें आपके बीच बह रही हैं।",
            "💝 आपके नामों में 99 अक्षर का मेल है! आपके रिश्ते में मिठास और प्यार है।",
            "💖 आपके नामों में 100 अक्षर का मेल है! यह सच्चे प्यार का सबसे बड़ा संकेत है! आप दोनों का प्यार अमर है।"
        ]
        index = max(1, min(match_score, 100)) - 1
        message = messages[index]
        #messagebox.showinfo("Match Message", message)
        #return message
               # Custom love-themed messagebox
        love_box = tk.Toplevel(self.root)
        love_box.title("💖 Love Match Message 💖")
        love_box.geometry("400x220")
        love_box.configure(bg="#ffe4ec")
        love_box.resizable(False, False)

        # Heart icon (emoji) at top
        heart_label = tk.Label(love_box, text="💖", font=("Arial", 36), bg="#ffe4ec", fg="#d32f2f")
        heart_label.pack(pady=(15, 0))
        
        
        # Message text
        msg_label = tk.Label(love_box, text=message, font=("Arial", 13), bg="#ffe4ec", fg="#d32f2f", wraplength=380, justify="center")
        msg_label.pack(pady=(10, 10))

        # OK button to close the messagebox
        ok_btn = tk.Button(love_box, text="OK", font=("Arial", 12, "bold"), bg="#d32f2f", fg="white", command=love_box.destroy)
        ok_btn.pack(pady=(5, 15))

        # Also return the message for label update
        return message
    # Animation: Fade-in effect (optional, simple)
        love_box.attributes('-alpha', 0.0)
        self.fade_in(love_box)

        return message

    def fade_in(self, window, step=0.05):
        alpha = window.attributes('-alpha')
        if alpha < 1.0:
            alpha += step
            window.attributes('-alpha', alpha)
            window.after(20, lambda: self.fade_in(window, step))



    def process_names(self):
        """
        Retrieves names from entry fields, calculates match, and updates GUI.
        """
        name1 = self.name1_entry.get().strip()
        name2 = self.name2_entry.get().strip()

        if not name1 or not name2:
            messagebox.showerror("Input Error", "Please enter both names.")
            self.match_result_label.config(text="--")
            self.message_label.config(text="Enter names and click the button!")
            return

        match_score = self.calculate_name_match(name1, name2)
        message = self.generate_positive_message(match_score)

        self.match_result_label.config(text=f"{match_score} Letters")
        self.message_label.config(text=message)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = NameMatcherApp(root)
    root.mainloop()
