#Using JSON files, the code creates a simple version control system. Versions and deltas are first stored
# in an empty dictionary upon initialization. Version saving is handled by two methods: save_delta for deltas
# and save_base_version for base versions. Get_version makes it easier to retrieve particular versions by applying
# all deltas up to the version that is needed. The delta is concatenated to the content using the apply_delta function.
# Potential areas for development include optimization for huge files and error handling. All things considered, the code
# lays the groundwork for version control capability, despite its simplicity.


import json


class Vrscontrol:
    def __init__(self):
        self.file = {}  # Dictionary to store versions and deltas

    def save_base_version(self, name, content):
        self.file[1] = {'content': content}  # Base version
        with open(name, 'w') as f:
            json.dump(self.file, f)

    def save_delta(self, name, vrs_num, delta):
        self.file[vrs_num] = delta
        with open(name, 'w') as f:
            json_obj=json.dump(self.file, f)
            print(json_obj)

    def get_version(self, name, vrs_num):
        with open(name, 'r') as f:
            self.file = json.load(f)
        if vrs_num not in self.file:
            return "Version not found"

        content = self.file[vrs_num]['content']
        for v in range(2, vrs_num + 1):
            delta = self.file[v]
            content = self.apply_delta(content, delta)

        return content

    def apply_delta(self, content, delta):
        return content + delta

vc = Vrscontrol()
vc.save_base_version("versions.txt", "This is the base content.")
vc.save_delta("versions.txt", 2, " Added some text.")
vc.save_delta("versions.txt", 3, " Removed unnecessary text.")
print(vc.file)
