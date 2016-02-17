
import re
for element in condensin.pdb:
	m = re.match("(^ATOM\s.*$)", element)
	if m:
		print(m.groups())
