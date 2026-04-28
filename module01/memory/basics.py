import copy

# ============================================================
# id() — memory address of an object
# type() — type of an object
# ============================================================

track = "Bohemian Rhapsody"
plays = 1_200_000
rating = 4.8
is_playing = True
current_track = None

print(type(track))        # <class 'str'>
print(type(plays))        # <class 'int'>
print(type(rating))       # <class 'float'>
print(type(is_playing))   # <class 'bool'>
print(type(current_track))# <class 'NoneType'>

print(id(track))          # memory address, e.g. 4371829872
print(id(plays))          # different address


# ============================================================
# Immutable types — reassignment creates a new object
# ============================================================

# Strings and ints are immutable — you can't change them in place
a = "Imagine"
b = a             # b points to the same object
print(id(a) == id(b))  # True — same object in memory

b = "Black"       # reassignment — b now points to a new object
print(id(a) == id(b))  # False
print(a)          # "Imagine" — unchanged


# ============================================================
# Mutable types — assignment copies the reference, not the value
# ============================================================

playlist = ["Imagine", "Black", "Wonderwall"]
playlist_ref = playlist       # NOT a copy — both point to the same list

playlist_ref.append("Hotel California")
print(playlist)               # ["Imagine", "Black", "Wonderwall", "Hotel California"]
                              # original changed because it's the same object in memory

print(id(playlist) == id(playlist_ref))  # True


# ============================================================
# Shallow copy — new list, but nested objects are still shared
# ============================================================

playlist = ["Imagine", "Black", "Wonderwall"]

shallow = playlist.copy()     # or playlist[:]  or  list(playlist)

shallow.append("Hotel California")
print(playlist)               # ["Imagine", "Black", "Wonderwall"] — not affected
print(shallow)                # ["Imagine", "Black", "Wonderwall", "Hotel California"]
print(id(playlist) == id(shallow))  # False — different objects


# Shallow copy limitation: nested objects are still shared
library = [["Imagine", "Jealous Guy"], ["Black", "Alive"]]
shallow_lib = library.copy()

shallow_lib[0].append("Mind Games")
print(library[0])             # ["Imagine", "Jealous Guy", "Mind Games"] — affected!
                              # inner list is the same object in both copies


# ============================================================
# Deep copy — fully independent clone, including nested objects
# ============================================================

library = [["Imagine", "Jealous Guy"], ["Black", "Alive"]]
deep_lib = copy.deepcopy(library)

deep_lib[0].append("Mind Games")
print(library[0])             # ["Imagine", "Jealous Guy"] — not affected
print(deep_lib[0])            # ["Imagine", "Jealous Guy", "Mind Games"]


# ============================================================
# Same rule applies to dicts
# ============================================================

track_info = {"title": "Imagine", "artist": "John Lennon", "tags": ["rock", "classic"]}

ref = track_info                        # same object
shallow_info = track_info.copy()        # shallow copy
deep_info = copy.deepcopy(track_info)   # deep copy

ref["title"] = "Black"
print(track_info["title"])              # "Black" — ref mutated the original

shallow_info["tags"].append("piano")
print(track_info["tags"])               # ["rock", "classic", "piano"] — nested list shared

deep_info["tags"].append("anthem")
print(track_info["tags"])               # ["rock", "classic", "piano"] — deep copy is isolated
