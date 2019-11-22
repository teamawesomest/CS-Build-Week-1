import random

room_names = [
"Belén", "Bella Vista", "Sanguanzhai", "Campos Novos", "Deranitan", "Tashla", "Santo Amaro da Imperatriz",
"Hegeng", "Babantar", "San Vicente", "Xibër-Murrizë", "Dallas", "Bārkhān", "Lazaro Cardenas", "Hejiaping",
"Changle", "Murree", "Le Mans", "Trmice", "Sierpc", "Glagahan",
"Fujisawa", "Orly", "Shiree", "Labuhansumbawa", "Ciparay", "Hoktember", "Uttar Char Fasson", "Angoulême",
"Lincheng", "Souto", "El Fahs", "Matriz de Camaragibe", "Shangyu", "Teberda", "Picoto", "Radocza", "Banī Zayd", "Siaya", "Italó", "Tha Ruea", "Lagoa", "Banjar Tengah",
"Yŏnmu", "Saratov", "Yotsukaidō", "Gastoúni", "Lysekil", "Valencia", "Georgiyevka", "Lais", "Västerås", "Maslog",
"Luján de Cuyo", "Dado", "Mouhijärvi", "Stockholm", "Kuala Terengganu", "Songgyuan", "Pamoyanan", "Roi Et",
"Cabudare", "Belén de Escobar", "Tando Muhammad Khān",
"Färgelanda", "Kuala Lumpur", "Le Bourget-du-Lac", "Santa Cruz", "Bergen", "Cerrillos", "Rio Formoso", "Almaty",
"Yinchuan", "Ribeira Seca", "Hanyū", "Linköping", "Firovo", "Sacapulas", "Donostia-San Sebastian", "Tambaksari",
"Daoxian", "Paris", "Phanat Nikhom", "Ugbokpo",
"Dijon", "Terter", "Thị Trấn Tà Lùng", "Lamu", "Dykan’ka", "Pridonskoy", "Guadalupe", "Oodweyne", "Khuan Don",
"Ralevka", "Lorient", "Suwałki", "Kakan", "Chimanimani", "Sumbersih", "Tarnawatka"
]

room_descriptions = [
"Realigned fault-tolerant moratorium", "Monitored leading edge process improvement", 
"User-centric web-enabled data-warehouse", "Reverse-engineered context-sensitive function", 
"Devolved dynamic hierarchy", "Progressive impactful focus group", "Open-source logistical  system", 
"Self-enabling even-keeled model", "Assimilated dynamic application", "Balanced systematic capability", 
"Synergized optimal synergy", "Synergized regional workforce", "Innovative discrete projection", 
"De-engineered explicit paradigm", "Operative foreground function", "Total clear-thinking pricing structure", 
"Programmable neutral solution", "Reverse-engineered secondary challenge", 
"Fully-configurable heuristic alliance", "Horizontal multimedia  architecture", 
"Multi-channelled modular  architecture", "Multi-tiered eco-centric hardware", 
"Stand-alone user-facing methodology", "Function-based static synergy", "Decentralized uniform challenge", 
"Exclusive asymmetric concept", "Proactive modular local area network", "Re-contextualized systematic paradigm", 
"Ergonomic intangible architecture", "Total stable standardization", "Robust  generation capacity", 
"Operative background algorithm", "Persistent generation capability", "Programmable systemic portal", 
"Team-oriented contextually-based database", "Profound  generation secured line", "Triple-buffered  conglomeration", 
"Business-focused reciprocal benchmark", "Operative zero tolerance circuit", "Robust zero defect data-warehouse", 
"Intuitive intangible benchmark", "Public-key  generation application", "Upgradable systemic encryption", 
"Configurable transitional forecast", "Organic tangible toolset", "Synergistic scalable superstructure", 
"Profit-focused transitional process improvement", "Digitized regional structure", 
"Grass-roots mission-critical superstructure", "Pre-emptive  knowledge user", "Robust scalable application", 
"Multi-lateral zero administration local area network", "Enterprise-wide foreground structure", 
"Versatile coherent hub", "Devolved systematic alliance", "Innovative homogeneous ability", "Mandatory  policy", 
"User-friendly analyzing collaboration", "Monitored local definition", "Universal bi-directional conglomeration", 
"Right-sized multi-state core", "Innovative modular solution", "Devolved directional benchmark", 
"Re-engineered explicit challenge", "Robust  generation functionalities", "Self-enabling upward-trending encoding", 
"Reactive neutral parallelism", "Up-sized foreground methodology", "Implemented systematic initiative", 
"Universal analyzing superstructure", "Digitized value-added function", "Horizontal zero administration hardware", 
"Persevering value-added contingency", "Advanced actuating access", "Visionary asynchronous orchestration", 
"Re-contextualized secondary hierarchy", "Operative transitional concept", "Focused client-driven superstructure", 
"Adaptive context-sensitive ability", "Centralized national archive", "Multi-tiered optimizing application", 
"User-friendly value-added extranet", "Seamless web-enabled forecast", "Assimilated foreground model", 
"Persevering scalable model", "Right-sized multi-tasking strategy", "Cloned tangible strategy", 
"Switchable static encoding", "Multi-layered homogeneous ability", "Triple-buffered interactive throughput", 
"Proactive regional intranet", "Team-oriented impactful projection", "Decentralized tertiary application", 
"Programmable generation application", "Future-proofed maximized protocol", 
"Programmable bifurcated standardization", "Object-based demand-driven Graphical User Interface", 
"Distributed user-facing leverage", "Operative reciprocal infrastructure", "Secured framework" 
]

def make_rooms():
    room = f'{random.choice(room_names)}'
    # room = [r for r in room_names]
    return room 

def make_descriptions():
    description = f'{random.choice(room_descriptions)}'
    # description = [d for d in room_descriptions]
    return description

# print('room', make_rooms())
# print('description', make_description())
