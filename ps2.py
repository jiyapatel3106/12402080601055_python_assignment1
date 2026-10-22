import re
class TrieNode: def  init (self):
self.children = {}
self.is_end = False
class Trie:
def  init (self):
self.root = TrieNode() def insert(self, word):
node = self.root
for char in word.lower():
if char not in node.children: node.children[char] = TrieNode()
node = node.children[char] node.is_end = True
def contains_banned_word(self, password): password = password.lower()
for start in range(len(password)): node = self.root
for end in range(start, len(password)): char = password[end]
if char not in node.children: break
node = node.children[char] if node.is_end:
 
return Truereturn False

def has_required_characters(password): has_lower = False
has_upper = False has_digit = False has_special = False
for char in password: if char.islower():
has_lower = True elif char.isupper():
has_upper = True elif char.isdigit():
has_digit = True elif char in "$#@":
has_special = True

return has_lower and has_upper and has_digit and has_special def has_repeated_character(password):
if not password: return False

consecutive_count = 1

for i in range(1, len(password)):
if password[i] == password[i - 1]: consecutive_count += 1
if consecutive_count > 3: return True
else:
consecutive_count = 1
return False
def classify_password(password, banned_trie): if len(password) < 6 or len(password) > 12:
return "WEAK_LENGTH"

if not has_required_characters(password): return "WEAK_PATTERN"
 
if has_repeated_character(password): return "WEAK_PATTERN"
if banned_trie.contains_banned_word(password): return "COMPROMISED"
return "STRONG" def
main():
b = int(input().strip())
if not (1 <= b <= 10000):
raise ValueError("Number of banned words must be between 1 and 10000.") banned_trie = Trie()

for _ in range(b):
word = input().strip() if word:
banned_trie.insert(word) n = int(input().strip())
if not (1 <= n <= 100000):
raise ValueError("Number of passwords must be between 1 and 100000.")

for index in range(1, n + 1): password = input().rstrip("\n")
result = classify_password(password, banned_trie) print(f"{index}: {result}")

if  name	== " main ": main()
