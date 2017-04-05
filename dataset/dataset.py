import random
import os
import yaml

class Dataset(object):

	def __init__(self, dataset_name, dataset_dir="/srv/datasets/"):
		self.dataset_dir = dataset_dir
		self.dataset_name = dataset_name

		self.dataset_fullpath = self.dataset_dir + self.dataset_name

		#split: [item_filepaths]
		self.items_cache = {}

	def get_info(self):
		yaml_fullpath = self.dataset_fullpath + "/" + "info.yaml"
		data = yaml.load(open(yaml_fullpath, "r"))
		return data


	def get_item(self, split, idx=None):
		#if split not in cache, add it
		if not self.items_cache.has_key(split):
			split_fullpath = self.dataset_fullpath + "/" + split + ".txt"
			f = open(split_fullpath, 'r')
			lines = f.readlines()
			items = [None]*len(lines)
			for i, line in enumerate(lines):
				items[i] = line.replace("\n", "").split(", ")

			self.items_cache[split] = items

		items = self.items_cache[split]
		
		#if idx not specified, get a random one
		if not idx:
			idx = random.randrange(0, len(items))

		return items[idx]

	def get_num_items(self, split):
		split_fullpath = self.dataset_fullpath + "/" + split + ".txt"
		f = open(split_fullpath, 'r')
		return len(f.readlines())

	def get_split_names(self):
		txt_files = [x for x in os.listdir(self.dataset_fullpath) if ".txt" in x]

		splits = [x.replace(".txt", "") for x in txt_files]
		return splits
