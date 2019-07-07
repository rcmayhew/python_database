import sys
sys.path.append("..")
import builder as br

test = br.Builder()


data = [1, 3, 5]
test.create_table("list2", data)
