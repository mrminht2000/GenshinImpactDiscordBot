from datetime import datetime

class Domain(object):
    def __init__(self):
        self.talent = {
            0: {
                "Freedom": ("Aloy", "Amber", "Barbara", "Diona", "Klee", "Sucrose", "Childe", "Main Phong"),
                "Prosperity": ("Keqing", "Ningguang", "Qiqi", "Main Nham", "Xiao"),
                "Transience": ("Main Lôi", "Yoimiya")
            },
            1: {
                "Resistance": ("Bennett", "Dilluc", "Eula", "Jean", "Mona", "Noelle", "Razor"),
                "Diligence": ("Chongyun", "Ganyu", "Hu Tao", "Kazuha", "Xiangling"),
                "Elegance": ("Ayaka", "Sara")
            },
            2: {
                "Ballad": ("Albedo", "Fischl", "Kaeya", "Lisa", "Rosaria", "Venti"),
                "Gold": ("Beidou", "Xingqiu", "Xinyan", "Yanfei", "Zhongli"),
                "Light": ("Raiden Shogun", "Sajuu")
            }
        }
        self.talent[3], self.talent[4], self.talent[5] = self.talent[0], self.talent[1], self.talent[2]
        
        self.weapon = {
            0: {
                "Decarabian": ("Aquila Favonia", "Royal Longsword", "The Viridescent Hunt", "Snow-Tombed Starsilver", "The Alley Flash", "Favonious Sword", "The Stringless", "Favoinus Codex", "Royal Grimoire", "The Bell"),
                "Guyun": ("Primordial Jave Winged-Spear", "Summit Shaper", "Lion\'s Roar", "Blackcliff Longsword", "Cresent Pike", "Blackcliff Warbow", "Lithic Blade", "Whileblind", "Rust", "Blackcliff Agate", "Solar Pearl"),
                "Distant Sea": ("Mistsplitter Reforged", "Amenoma Kageuchi", "Hakushin Ring")
            },
            1: {
                "Boreal Wolf": ("Skyward Harp", "Skyward Blade", "Skyward Pride", "Skyward Atlas", "The Flute", "The Black Sword", " Sacrificial Greatsword", "Sword of Descension", "Deathmatch", "Wine and Song", "The Widsith", "Sacrificial Bow", "Dragonspine Spear"),
                "Mist Veiled Elixir": ("The Unforged", "Eye of Perception", "Prototype Rancour", "Prototype Crescent", "Dragon's Bane", "Blackcliff Pole", "Royal Spear", "Blackcliff Slasher", "Prototype Amber", "Rainslasher"),
                "Narukami": ("Thundering Pulse", "Hamayumi", "Katsuragikiri Nagamasa")
            },
            2: {
                "Dandelion Glaidator": (""),
                "Aerosiderite": ("Memory of Dush", "Vortex Vanquisher", "Iron Sting", "Serpent Spine", "Lithic Spear", "Prototype Starglitter", "Compound Bow", "Mappa Mare", "Prototype Archaic"),
                "Mask": ("Kitain Cross Spear", "Engulfing Lighting", "The Catch")
            }
        }
        self.weapon[3], self.weapon[4], self.weapon[5] = self.weapon[0], self.weapon[1], self.weapon[2]

    def get_output(self, type):
        weekDays = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ Nhật"]
        day = datetime.now().weekday()
        if day == 6:
            return ["Nhà lữ hành, hôm nay là cuối tuần rồi! Vào Chủ Nhật bạn có thể farm mọi loại tài nguyên!"]
        else:
            messages = ["Hôm nay là " + weekDays[day] + " rồi nhà lữ hành, bạn có thể kiếm các loại tài nguyên sau:"]
            if type in ["talent", "book", "all"]:
                for key, value in self.talent[day].items():
                    messages.append("Sách **" + key + "**: " + ", ".join(value))
            if type in ["weapon", "all"]:
                for key, value in self.weapon[day].items():
                    messages.append("Nguyên liệu **" + key + "**: " + ", ".join(value))
            return messages

