import os
import yaml
import time


class DatasetWriter(object):

    """
    This class creates a Dataset Directory in /srv/datasets to be used for training
    This will use the flat files sitting in /srv/data
    """
    def __init__(self, dataset_name, dataset_dir="/srv/datasets/"):
        self.dataset_dir = dataset_dir
        self.dataset_name = dataset_name

        self.dataset_fullpath = self.dataset_dir + self.dataset_name


        if os.path.exists(self.dataset_fullpath):
            raise Exception("Dataset Already Exists")

        os.mkdir(self.dataset_fullpath)
        self.add_info_item("creation_date", time.strftime("y%y_m%m_d%d_h%H_m%M_s%S"))

    """
    This should be the filenames for a training example
    ex:
    [/srv/data/shape_completion_data/grasp_database/lime_poisson_000/pointclouds/_2_3_9_x.pcd,
    /srv/data/shape_completion_data/grasp_database/lime_poisson_000/pointclouds/_2_3_9_y.pcd]
    """
    def add_item(self, split, filename_list):
        split_fullpath = self.dataset_fullpath + "/" + split + ".txt"
        f = open(split_fullpath, 'a')
        line = ", ".join(filename_list) + "\n"
        f.write(line)
        f.close()

    """
    Use this to add key value information to the info.yaml for the dataset
    ex patch_size: 40
    """
    def add_info_item(self, key, value):
        yaml_fullpath = self.dataset_fullpath + "/" + "info.yaml"
        if os.path.exists(yaml_fullpath):
            data = yaml.load(open(yaml_fullpath, "r"))
        else:
            data = {}

        #add the new information to the yaml dict
        data[key] = value

        with open(yaml_fullpath, "w") as outfile:
            yaml.dump(data, outfile, default_flow_style=True)
